#!/usr/bin/python

# Author: Maximilian Noppel
# July 2020
#


import logging
from collections import deque
from graphviz import Digraph
import sys
import numpy


def getImplications(implicationsfile,notions):
	edges = []
	nonEdges = []
	seenNotions = []

	with open(implicationsfile) as f:
		lines = f.readlines()
		linNum = 1
		for l in lines:
			l = l.strip()

			if l == "":
				pass
				
			elif l[0] == "#":
				pass
			
			elif l[0] == ":":
				seenNotions.append(l[1:])
				logger.info(f"Added notion {l[1:]}")
				
			elif "<=>" in l:
				splt = l.split("<=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()


				if splt[0] not in seenNotions:
					seenNotions.append(splt[0])
				if splt[1] not in seenNotions:
					seenNotions.append(splt[1])
				edges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
				edges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))

			elif "=|=>" in l:
				splt = l.split("=|=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with =|=> yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()
				
				if splt[0] not in seenNotions:
					seenNotions.append(splt[0])
				if splt[1] not in seenNotions:
					seenNotions.append(splt[1])
				nonEdges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))
				
			elif "<=|=" in l:
				splt = l.split("<=|=")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <=|= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()
					
				if splt[0] not in seenNotions:
					seenNotions.append(splt[0])
				if splt[1] not in seenNotions:
					seenNotions.append(splt[1])
				nonEdges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
				
			elif "=>" in l:
				splt = l.split("=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with => yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()

				if splt[0] not in seenNotions:
					seenNotions.append(splt[0])
				if splt[1] not in seenNotions:
					seenNotions.append(splt[1])
				edges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))
				
			elif "<=" in l:
				splt = l.split("<=")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()

				if splt[0] not in seenNotions:
					seenNotions.append(splt[0])
				if splt[1] not in seenNotions:
					seenNotions.append(splt[1])
				edges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
					
			else:
				raise Exception("Line %d is neither valid inputline nor comment" % linNum)
			linNum = linNum + 1

	return (edges, nonEdges, seenNotions)


def checkDisprovedImplications(edges,nonEdges,notions):
	adjList = [[] for _ in range(len(notions))]

	for (src, dest) in edges:
		adjList[src].append(dest)

	for (src, dest) in nonEdges:
		res = recursiveCheckForTransitivityFailure(adjList,src,src,dest,notions)
		if res != True:
			for p in res:
				print(p)
	return True

def recursiveCheckForTransitivityFailure(adjList,osrc,src,dest,notions):
	for i in adjList[src]:
		if i == dest:
			#logger.info("Found loop for %s =|> %s. Last src was %s" % (notions[osrc],notions[src],notions[dest]))
			l = []
			l.append(notions[dest])
			l.append(notions[src])
			return l
		res = recursiveCheckForTransitivityFailure(adjList,osrc,i,dest,notions)
		if res != True:
			res.append(notions[src])
			return res
	return True

def transitivity(adjMatrix,notions,reflexive=True):
	for osrc in range(0,len(notions)):
		if reflexive:
			adjMatrix[osrc][osrc] = True
		for src in range(0,len(notions)):
			if adjMatrix[osrc][src] == True:
				for dest in range(0,len(notions)):
					if adjMatrix[src][dest] == True:
						adjMatrix[osrc][dest] = True
	return adjMatrix


def printWay(originalMatrix,notions,s,d,l,seen):
	#logger.info("printWay %s %s" % (notions[s],notions[d]))
	if s in seen:
		#Loop
		return False
	seen.append(s)
	for i in range(0,len(notions)):
		if originalMatrix[s][i] == True:
			if i == d:
				l.append((notions[s],notions[d]))
				return l
			lst = printWay(originalMatrix,notions,i,d,copyListe(l),copyListe(seen))
			if lst != False:
				lst.append((notions[s],notions[i]))
				return lst

	return False

# TODO: This can be done by numpy!
def transpose(ain):
	aout = [[ False for _ in range(len(ain)) ] for _ in range(len(ain))]
	for x in range(len(ain)):
		for y in range(len(ain)):
			aout[y][x] = ain[x][y]
	return aout

def antiTransitivity(adjMatrix,adjMatrixNon,notions):
	adjMatrixTrans = transpose(adjMatrix)
	for i in range(0,len(notions)):
		for osrc in range(0,len(notions)):
			for src in range(0,len(notions)):
				if adjMatrixNon[osrc][src] == True:
					for dest in range(0,len(notions)):
						if adjMatrixTrans[src][dest] == True:
							adjMatrixNon[osrc][dest] = True
	for i in range(0,len(notions)):
		for osrc in range(0,len(notions)):
			for src in range(0,len(notions)):
				if adjMatrix[osrc][src] == True:
					for dest in range(0,len(notions)):
						if adjMatrixNon[osrc][dest] == True:
							adjMatrixNon[src][dest] = True
	return adjMatrixNon

# TODO: This can be done by numpy!
def copyListe(liste):
	l = []
	for i in liste:
		l.append(i)
	return l


# TODO: This can be done by numpy!
def copyMatrix(matrix):
	m = [[ False for _ in range(len(matrix)) ] for _ in range(len(matrix))]
	for x in range(len(matrix)):
		for y in range(len(matrix)):
			m[x][y] = matrix[x][y]
	return m

def matrixEqual(m0,m1):
	for x in range(len(m0)):
		for y in range(len(m0)):
			if m0[x][y] != m1[x][y]:
				return False
	return True

def transitivityLoop(adjMatrix,notions):
	while True:
		adjMatrixOld = copyMatrix(adjMatrix)
		adjMatrix = transitivity(adjMatrix,notions)
		if matrixEqual(adjMatrix, adjMatrixOld):
			break
	return adjMatrix

def antitransitivityLoop(adjMatrix,adjMatrixNon,notions):
	while True:
		adjMatrixNonOld = copyMatrix(adjMatrixNon)
		adjMatrixNon = antiTransitivity(adjMatrix,adjMatrixNon,notions)
		if matrixEqual(adjMatrixNon, adjMatrixNonOld):
			break
	return adjMatrixNon

if __name__ == '__main__':
	
	FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
	logging.basicConfig(format=FORMAT, level=logging.INFO)
	logger = logging.getLogger("main")
	logger.info("Starting run!")


	if len(sys.argv) != 2:
		logger.error("Usage: (python) main.py <inputfile>")
		exit(-1)


	f = sys.argv[1]

	notions = []
	edges,nonEdges,notions = getImplications(f,notions)

	N = len(notions)


	originalMatrix = [[ False for _ in range(len(notions)) ] for _ in range(len(notions))]
	for (src, dest) in edges:
		originalMatrix[src][dest] = True
	

	adjMatrix = copyMatrix(originalMatrix)

	adjMatrix = transitivityLoop(adjMatrix,notions)


	originalMatrixNon = [[ False for _ in range(len(notions)) ] for _ in range(len(notions))]
	for (src, dest) in nonEdges:
		originalMatrixNon[src][dest] = True

	adjMatrixNon = copyMatrix(originalMatrixNon)

	adjMatrixNon = antitransitivityLoop(adjMatrix,adjMatrixNon,notions)

	inconsistencies = 0
	incompletenesses = 0

	

	for x in range(0,len(notions)):
		for y in range(0,len(notions)):
			if adjMatrix[x][y] == True and  adjMatrixNon[x][y] == True:
				logger.error("INCONSISTENT! %s => %s and %s =|=> %s" % (notions[x],notions[y],notions[x],notions[y]))
				l = []
				l = printWay(originalMatrix,notions,x,y,l,[])
				logger.warning("Path for =>")
				if l != False:
					for (s,d) in l[::-1]:
						logger.warning("%s => %s" % (s,d))
				else:
					logger.warning("No path found! for =>")
				l = []
				l = printWay(adjMatrixNon,notions,x,y,l,[])
				logger.warning("Path for =|=>")
				if l != False:
					for (s,d) in l[::-1]:
						logger.warning("%s =|=> %s" % (s,d))
				else:
					logger.warning("No path found! for =|=>")

				exit(0)


				inconsistencies += 1
			if adjMatrix[x][y] == False and  adjMatrixNon[x][y] == False:
				logger.warning("Incomplete! %s =?=> %s" % (notions[x],notions[y]))
				incompletenesses += 1


	numpy.save("adjMatrix", adjMatrix)

	logger.info("Number of notions:          %5d" % len(notions))
	logger.info("Number of inconsistencies:  %5d" % inconsistencies)
	logger.info("Number of incompletenesses: %5d" % incompletenesses)

	dot = Digraph(comment='Overview')
	for i in range(0,len(notions)):
		c = "white"
		dot.node(notions[i], notions[i], style='filled',fillcolor=c)

	for dest in range(0,len(notions)):
		for src in range(0,len(notions)):
			if adjMatrix[dest][src] == True:
				dot.edge(notions[dest],notions[src])



	#dot.render('test-output/overview.gv', view=True)
	logger.info("Finished")


	#print(adjMatrix)





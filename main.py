#!/usr/bin/python

# Author: Maximilian Noppel
# July 2020
#
# Credits to: https://www.techiedelight.com/kahn-topological-sort-algorithm/
# The implementation of Kahn Alg. is from this website.
#

import logging
from collections import deque
from graphviz import Digraph
import sys
import numpy

FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger("main")
logger.info("Starting run!")


USE_OPAQUENESS = False
USE_SEEN_NOTIONS = False
USE_TEST = False

if sys.argv[1] == "normal":
	USE_OPAQUENESS = False
	USE_TEST = False
elif sys.argv[1] == "test":
	USE_OPAQUENESS = False
	USE_TEST = True
elif sys.argv[1] == "opa":
	USE_OPAQUENESS = True
	USE_TEST = False

if USE_TEST:
	latexEncoding = {
		"achievedInGeneral": "achieved in general",
		"unachievable": "unachievable",
		"N-OPA": "\\N-OPA",
		"a": "a",
		"b": "b",
		"c": "c",
		"d": "d",
		"e": "e",
		"f": "f",
	}

	pages = [
		{
			"family": "Test",
			"page": 100,
			"notions": [
				"achievedInGeneral",
				"unachievable",
				"N-OPA",
				"a",
				"b",
				"c",
				"d",
				"e",
				"f",

			]
		}
	]
elif USE_OPAQUENESS:
	latexEncoding = {
		"achievedInGeneral": "achieved in general",
		"unachievable": "unachievable",
		"N-OPA": "\\N-OPA",
		"wUA-OCA": "\\widetilde{U}_A-OCA",
		"wUV0-OCA": "\\widetilde{U}_{U_{v_0}}-OCA",
	}

	pages = [
		{
			"family": "opaqueness notions",
			"page": 20,
			"notions": [
				"achievedInGeneral",
				"unachievable",
				"N-OPA",
				"wUA-OCA",
				"wUV0-OCA",
				
			]
		}
	]
else:
	latexEncoding = {
		"achievedInGeneral": "achieved in general",
		"unachievable": "unachievable",
		"N-OPA": "\\N-OPA",

		"CU-OPA": "|U|-OPA",
		"UorH-OPA": "U \\lor H-OPA",
		"UorP-OPA": "U \\lor P-OPA",
		"H-OPA": "H-OPA",
		"Q-OPA": "Q-OPA",
		"P-OPA": "P-OPA",
		"U-OPA": "U-OPA",
		"UandH-OPA": "U \\land H-OPA",
		"QandP-OPA": "Q \\land P-OPA",
		"UandP-OPA": "U \\land P-OPA",
		"QorP-OPA": "Q \\lor P-OPA",

		"nDandES-OPA": "\\nDiamond \\land E_S-OPA",
		"nDandESandCU-OPA": "\\nDiamond \\land E_S \\land |U|-OPA",
		"nDandESandUorH-OPA": "\\nDiamond \\land E_S \\land (U \\lor H)-OPA",
		"nDandESandUorP-OPA": "\\nDiamond \\land E_S \\land (U \\lor P)-OPA",
		"nDandESandH-OPA": "\\nDiamond \\land E_S \\land H-OPA",
		"nDandESandQ-OPA": "\\nDiamond \\land E_S \\land Q-OPA",
		"nDandESandP-OPA": "\\nDiamond \\land E_S \\land P-OPA",
		"nDandESandU-OPA": "\\nDiamond \\land E_S \\land U-OPA",
		"nDandESandUandH-OPA": "\\nDiamond \\land E_S \\land (U \\land H)-OPA",
		"nDandESandQandP-OPA": "\\nDiamond \\land E_S \\land (Q \\land P)-OPA",
		"nDandESandUandP-OPA": "\\nDiamond \\land E_S \\land (U \\land P)-OPA",
		"nDandESandQorP-OPA": "\\nDiamond \\land E_S \\land (Q \\lor P)-OPA",

		"CU-OCA": "|U|-OCA",
		"UorH-OCA": "U \\lor H-OCA",
		"UorP-OCA": "U \\lor P-OCA",
		"H-OCA": "H-OCA",
		"Q-OCA": "Q-OCA",
		"P-OCA": "P-OCA",
		"U-OCA": "U-OCA",
		"UandH-OCA": "U \\land H-OCA",
		"QandP-OCA": "Q \\land P-OCA",
		"UandP-OCA": "U \\land P-OCA",
		"QorP-OCA": "Q \\lor P-OCA",

		"nDandES-OCA": "\\nDiamond \\land E_S-OCA",
		"nDandESandCU-OCA": "\\nDiamond \\land E_S \\land |U|-OCA",
		"nDandESandUorH-OCA": "\\nDiamond \\land E_S \\land (U \\lor H)-OCA",
		"nDandESandUorP-OCA": "\\nDiamond \\land E_S \\land (U \\lor P)-OCA",
		"nDandESandH-OCA": "\\nDiamond \\land E_S \\land H-OCA",
		"nDandESandQ-OCA": "\\nDiamond \\land E_S \\land Q-OCA",
		"nDandESandP-OCA": "\\nDiamond \\land E_S \\land P-OCA",
		"nDandESandU-OCA": "\\nDiamond \\land E_S \\land U-OCA",
		"nDandESandUandH-OCA": "\\nDiamond \\land E_S \\land (U \\land H)-OCA",
		"nDandESandQandP-OCA": "\\nDiamond \\land E_S \\land (Q \\land P)-OCA",
		"nDandESandUandP-OCA": "\\nDiamond \\land E_S \\land (U \\land P)-OCA",
		"nDandESandQorP-OCA": "\\nDiamond \\land E_S \\land (Q \\lor P)-OCA",

		"nCU-OPA": "\\overline{|U|}-OPA",
		"nUornH-OPA": "\\overline{U} \\lor \\overline{H}-OPA",
		"nUornP-OPA": "\\overline{U} \\lor \\overline{P}-OPA",
		"nH-OPA": "\\overline{H}-OPA",
		"nQ-OPA": "\\overline{Q}-OPA",
		"nP-OPA": "\\overline{P}-OPA",
		"nU-OPA": "\\overline{U}-OPA",
		"nUandnH-OPA": "\\overline{U} \\land \\overline{H}-OPA",
		"nQandnP-OPA": "\\overline{Q} \\land \\overline{P}-OPA",
		"nUandnP-OPA": "\\overline{U} \\land \\overline{P}-OPA",
		"nQornP-OPA": "\\overline{Q} \\lor \\overline{P}-OPA",

		"nDandES-OPA2": "\\nDiamond \\land E_S-OPA",
		"nDandESandnCU-OPA": "\\nDiamond \\land E_S \\land \\overline{|U|}-OPA",
		"nDandESandnUornH-OPA": "\\nDiamond \\land E_S \\land (\\overline{U} \\lor \\overline{H})-OPA",
		"nDandESandnUornP-OPA": "\\nDiamond \\land E_S \\land (\\overline{U} \\lor \\overline{P})-OPA",
		"nDandESandnH-OPA": "\\nDiamond \\land E_S \\land \\overline{H}-OPA",
		"nDandESandnQ-OPA": "\\nDiamond \\land E_S \\land \\overline{Q}-OPA",
		"nDandESandnP-OPA": "\\nDiamond \\land E_S \\land \\overline{P}-OPA",
		"nDandESandnU-OPA": "\\nDiamond \\land E_S \\land \\overline{U}-OPA",
		"nDandESandnUandnH-OPA": "\\nDiamond \\land E_S \\land (\\overline{U} \\land \\overline{H})-OPA",
		"nDandESandnQandnP-OPA": "\\nDiamond \\land E_S \\land (\\overline{Q} \\land \\overline{P})-OPA",
		"nDandESandnUandnP-OPA": "\\nDiamond \\land E_S \\land (\\overline{U} \\land \\overline{P})-OPA",
		"nDandESandnQornP-OPA": "\\nDiamond \\land E_S \\land (\\overline{Q} \\lor \\overline{P})-OPA",


		"nCU-OCA": "\\overline{|U|}-OCA",
		"nUornH-OCA": "\\overline{U} \\lor \\overline{H}-OCA",
		"nUornP-OCA": "\\overline{U} \\lor \\overline{P}-OCA",
		"nH-OCA": "\\overline{H}-OCA",
		"nQ-OCA": "\\overline{Q}-OCA",
		"nP-OCA": "\\overline{P}-OCA",
		"nU-OCA": "\\overline{U}-OCA",
		"nUandnH-OCA": "\\overline{U} \\land \\overline{H}-OCA",
		"nQandnP-OCA": "\\overline{Q} \\land \\overline{P}-OCA",
		"nUandnP-OCA": "\\overline{U} \\land \\overline{P}-OCA",
		"nQornP-OCA": "\\overline{Q} \\lor \\overline{P}-OCA",

		"nDandES-OCA2": "\\nDiamond \\land E_S-OCA",
		"nDandESandnCU-OCA": "\\nDiamond \\land E_S \\land \\overline{|U|}-OCA",
		"nDandESandnUornH-OCA": "\\nDiamond \\land E_S \\land (\\overline{U} \\lor \\overline{H})-OCA",
		"nDandESandnUornP-OCA": "\\nDiamond \\land E_S \\land (\\overline{U} \\lor \\overline{P})-OCA",
		"nDandESandnH-OCA": "\\nDiamond \\land E_S \\land \\overline{H}-OCA",
		"nDandESandnQ-OCA": "\\nDiamond \\land E_S \\land \\overline{Q}-OCA",
		"nDandESandnP-OCA": "\\nDiamond \\land E_S \\land \\overline{P}-OCA",
		"nDandESandnU-OCA": "\\nDiamond \\land E_S \\land \\overline{U}-OCA",
		"nDandESandnUandnH-OCA": "\\nDiamond \\land E_S \\land (\\overline{U} \\land \\overline{H})-OCA",
		"nDandESandnQandnP-OCA": "\\nDiamond \\land E_S \\land (\\overline{Q} \\land \\overline{P})-OCA",
		"nDandESandnUandnP-OCA": "\\nDiamond \\land E_S \\land (\\overline{U} \\land \\overline{P})-OCA",
		"nDandESandnQornP-OCA": "\\nDiamond \\land E_S \\land (\\overline{Q} \\lor \\overline{P})-OCA",
	}

	pages = [ 
		{
		"family": "\\mathbb{S}-OPA",
		"page": 0,
		"notions":[
			"CU-OPA",
			"UorH-OPA",
			"UorP-OPA",
			"H-OPA",
			"Q-OPA",
			"P-OPA",
			"U-OPA",
			"UandH-OPA",
			"QandP-OPA",
			"UandP-OPA",
			"QorP-OPA"
		]},
		{
		"family": "\\nDiamond \\land E_S \\land \\mathbb{S}-OPA",
		"page": 1,
		"notions":[
			"nDandES-OPA",
			"nDandESandCU-OPA",
			"nDandESandUorH-OPA",
			"nDandESandUorP-OPA",
			"nDandESandH-OPA",
			"nDandESandQ-OPA",
			"nDandESandP-OPA",
			"nDandESandU-OPA",
			"nDandESandUandH-OPA",
			"nDandESandQandP-OPA",
			"nDandESandUandP-OPA",
			"nDandESandQorP-OPA"
		]},
		{
		"family": "\\mathbb{S}-OCA",
		"page": 2,
		"notions":[
			"CU-OCA",
			"UorH-OCA",
			"UorP-OCA",
			"H-OCA",
			"Q-OCA",
			"P-OCA",
			"U-OCA",
			"UandH-OCA",
			"QandP-OCA",
			"UandP-OCA",
			"QorP-OCA"
		]},
		{
		"family": "\\nDiamond \\land E_S \\land \\mathbb{S}-OCA",
		"page": 3,
		"notions":[
			"nDandES-OCA",
			"nDandESandCU-OCA",
			"nDandESandUorH-OCA",
			"nDandESandUorP-OCA",
			"nDandESandH-OCA",
			"nDandESandQ-OCA",
			"nDandESandP-OCA",
			"nDandESandU-OCA",
			"nDandESandUandH-OCA",
			"nDandESandQandP-OCA",
			"nDandESandUandP-OCA",
			"nDandESandQorP-OCA"
		]},
		{
		"family": "\\overline{\\mathbb{S}}-OPA",
		"page": 4,
		"notions":[
			"nCU-OPA",
			"nUornH-OPA",
			"nUornP-OPA",
			"nH-OPA",
			"nQ-OPA",
			"nP-OPA",
			"nU-OPA",
			"nUandnH-OPA",
			"nQandnP-OPA",
			"nUandnP-OPA",
			"nQornP-OPA"
		]},
		{
		"family": "\\nDiamond \\land E_S \\land \\overline{\\mathbb{S}}-OPA",
		"page": 5,
		"notions":[
			"nDandES-OPA2",
			"nDandESandnCU-OPA",
			"nDandESandnUornH-OPA",
			"nDandESandnUornP-OPA",
			"nDandESandnH-OPA",
			"nDandESandnQ-OPA",
			"nDandESandnP-OPA",
			"nDandESandnU-OPA",
			"nDandESandnUandnH-OPA",
			"nDandESandnQandnP-OPA",
			"nDandESandnUandnP-OPA",
			"nDandESandnQornP-OPA"
		]},
		{
		"family": "\\overline{\\mathbb{S}}-OCA",
		"page": 6,
		"notions":[
			"nCU-OCA",
			"nUornH-OCA",
			"nUornP-OCA",
			"nH-OCA",
			"nQ-OCA",
			"nP-OCA",
			"nU-OCA",
			"nUandnH-OCA",
			"nQandnP-OCA",
			"nUandnP-OCA",
			"nQornP-OCA"
		]},
		{
		"family": "\\nDiamond \\land E_S \\land \\overline{\\mathbb{S}}-OCA",
		"page": 7,
		"notions": [
			"nDandES-OCA2",
			"nDandESandnCU-OCA",
			"nDandESandnUornH-OCA",
			"nDandESandnUornP-OCA",
			"nDandESandnH-OCA",
			"nDandESandnQ-OCA",
			"nDandESandnP-OCA",
			"nDandESandnU-OCA",
			"nDandESandnUandnH-OCA",
			"nDandESandnQandnP-OCA",
			"nDandESandnUandnP-OCA",
			"nDandESandnQornP-OCA"
		]},
		{
		"family": "\\text{Special Notions}",
		"page": 8,
		"notions": [
			"achievedInGeneral",
			"unachievable",
			"N-OPA"
		]} ]





# class to represent a graph object:
class Graph:

	# stores indegree of a vertex
	indegree = None

	# Constructor
	def __init__(self, edges, N):
		# A List of Lists to represent an adjacency list
		self.adjList = [[] for _ in range(N)]
		# initialize indegree of each vertex by 0
		self.indegree = [0] * N
		# add edges to the undirected graph
		for (src, dest) in edges:
			# add an edge from source to destination
			self.adjList[src].append(dest)
			# increment in-degree of destination vertex by 1
			self.indegree[dest] = self.indegree[dest] + 1


# performs Topological Sort on a given DAG
def doTopologicalSort(graph, N):

	# list to store the sorted elements
	L = []

	# get in-degree information of the graph
	indegree = graph.indegree

	# Set of all nodes with no incoming edges
	S = deque([i for i in range(N) if indegree[i] == 0])

	while S:
		# remove a node n from S
		n = S.pop()
		# add n to tail of L
		L.append(n)
		for m in graph.adjList[n]:
			# remove edge from n to m from the graph
			indegree[m] = indegree[m] - 1
			# if m has no other incoming edges then
			# insert m into S
			if indegree[m] == 0:
				S.append(m)

	# if graph has edges then graph has at least one cycle
	for i in range(N):
		if indegree[i]:
			return None

	return L


def substituteNames(name):
	pass



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
			elif "<=>" in l:
				splt = l.split("<=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()

				if USE_SEEN_NOTIONS:
					if splt[0] not in seenNotions:
						seenNotions.append(splt[0])
					if splt[1] not in seenNotions:
						seenNotions.append(splt[1])
					edges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
					edges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))
				else:
					if splt[0] not in notions:
						raise Exception("Unknown notions %s" % splt[0])
					if splt[1] not in notions:
						raise Exception("Unknown notions %s" % splt[1])
					edges.append(( notions.index(splt[1]), notions.index(splt[0]) ))
					edges.append(( notions.index(splt[0]), notions.index(splt[1]) ))
			elif "=|=>" in l:
				splt = l.split("=|=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with =|=> yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()
				
				if USE_SEEN_NOTIONS:
					if splt[0] not in seenNotions:
						seenNotions.append(splt[0])
					if splt[1] not in seenNotions:
						seenNotions.append(splt[1])
					nonEdges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))
				else:
					if splt[0] not in notions:
						raise Exception("Unknown notions %s" % splt[0])
					if splt[1] not in notions:
						raise Exception("Unknown notions %s" % splt[1])
					nonEdges.append(( notions.index(splt[0]), notions.index(splt[1]) ))
			elif "<=|=" in l:
				splt = l.split("<=|=")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <=|= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()
					
				if USE_SEEN_NOTIONS:
					if splt[0] not in seenNotions:
						seenNotions.append(splt[0])
					if splt[1] not in seenNotions:
						seenNotions.append(splt[1])
					nonEdges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
				else:
					if splt[0] not in notions:
						raise Exception("Unknown notions %s" % splt[0])
					if splt[1] not in notions:
						raise Exception("Unknown notions %s" % splt[1])
					nonEdges.append(( notions.index(splt[1]), notions.index(splt[0]) ))
			elif "=>" in l:
				splt = l.split("=>")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with => yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()

				if USE_SEEN_NOTIONS:
					if splt[0] not in seenNotions:
						seenNotions.append(splt[0])
					if splt[1] not in seenNotions:
						seenNotions.append(splt[1])
					edges.append(( seenNotions.index(splt[0]), seenNotions.index(splt[1]) ))
				else:
					if splt[0] not in notions:
						raise Exception("Unknown notions %s" % splt[0])
					if splt[1] not in notions:
						raise Exception("Unknown notions %s" % splt[1])

					edges.append(( notions.index(splt[0]), notions.index(splt[1]) ))
			elif "<=" in l:
				splt = l.split("<=")
				if len(splt) != 2:
					raise Exception("Parsing Error! Split with <= yields array of length > 2")
				splt[0] = splt[0].strip()
				splt[1] = splt[1].strip()

				if USE_SEEN_NOTIONS:
					if splt[0] not in seenNotions:
						seenNotions.append(splt[0])
					if splt[1] not in seenNotions:
						seenNotions.append(splt[1])
					edges.append(( seenNotions.index(splt[1]), seenNotions.index(splt[0]) ))
				else:
					if splt[0] not in notions:
						raise Exception("Unknown notions %s" % splt[0])
					if splt[1] not in notions:
						raise Exception("Unknown notions %s" % splt[1])
					edges.append(( notions.index(splt[1]), notions.index(splt[0]) ))
			
			else:

				raise Exception("Line %d is neither valid inputline nor comment" % linNum)
			linNum = linNum + 1
	if USE_SEEN_NOTIONS:
		return (edges, nonEdges, seenNotions)
	else:
		return (edges, nonEdges, notions)

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

def latexExport(adjMatrix,adjMatrixNon,outfilename,notions,page):

	outfile = open(outfilename+"Page"+str(page["page"])+".tex","w")
	outfile.write('\\begin{longtable}{|r|')
	for j in range(len(page["notions"])):
		outfile.write("c|")
	outfile.write("}\n")
	outfile.write("\\hline")
	for dest in page["notions"]:
		outfile.write("&\\rothead{$%s$}" % (latexEncoding[dest]))
	outfile.write("\\\\\n")
	for src in range(0,len(notions)):
		outfile.write("\\hline\n")
		outfile.write("$%s$" % (latexEncoding[notions[src]]))
		for dest in page["notions"]:
			outfile.write("&")
			destIdx = notions.index(dest)
			if src == destIdx:
				outfile.write("$=$")
			elif adjMatrix[src][destIdx] == True and adjMatrix[destIdx][src] == True:
				outfile.write("$\\iff$")
			elif adjMatrix[src][destIdx] == True:
				outfile.write("$\\Rightarrow$")
					#exit(0)
			elif adjMatrixNon[src][destIdx] == True:
				outfile.write("$\\cancel{\\Rightarrow}$")
			else:
				outfile.write("")
		outfile.write("\\\\\n")
	outfile.write("\\hline")
	outfile.write('\\caption{Completeness $%s$ family}\n' % (page["family"]))
	outfile.write('\\end{longtable}\n')
	outfile.close()

def copyListe(liste):
	l = []
	for i in liste:
		l.append(i)
	return l

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

	if USE_TEST:
		f = "implicationsTest.im"
	elif USE_OPAQUENESS:
		f = "implicationsOpaqueness.im"
	else:
		f = "implications.im"

	notions = []
	for page in pages:
		notions.extend(page["notions"])

	edges,nonEdges,notions = getImplications(f,notions)

	N = len(notions)

	graph = Graph(edges, N)
	L = doTopologicalSort(graph, N)

	if L:
		#for i in L:
		#	print(notions[i])
		pass
	else:
		#logger.info("Graph has at least one cycle. Topological sorting is not possible.")
		#exit(0)
		pass

	# No cycles so far!
	# Checking the disproved implications
	#if checkDisprovedImplications(edges,nonEdges,notions) == False:
	#	logger.info("Conflicts with disproved implications")
		#exit(0)


	
	originalMatrix = [[ False for _ in range(len(notions)) ] for _ in range(len(notions))]
	for (src, dest) in edges:
		originalMatrix[src][dest] = True


	

	adjMatrix = copyMatrix(originalMatrix)

	for dest in range(0,len(notions)):
		if USE_TEST == False:
			# achieved in general implies every notion
			adjMatrix[notions.index("achievedInGeneral")][dest] = True
			# unachievable implies every notion
			adjMatrix[notions.index("unachievable")][dest] = True;
			pass

	adjMatrix = transitivityLoop(adjMatrix,notions)

	for dest in range(0,len(notions)):
		if USE_TEST == False:
			if adjMatrix[dest][notions.index("unachievable")] == False:
				adjMatrix[notions.index("N-OPA")][dest] = True;
				pass

	adjMatrix = transitivityLoop(adjMatrix,notions)


	originalMatrixNon = [[ False for _ in range(len(notions)) ] for _ in range(len(notions))]
	for (src, dest) in nonEdges:
		originalMatrixNon[src][dest] = True

	adjMatrixNon = copyMatrix(originalMatrixNon)

	for dest in range(0,len(notions)):
		if USE_TEST == False:
			if adjMatrix[dest][notions.index("unachievable")] == False:
				adjMatrixNon[dest][notions.index("unachievable")] = True;
				if adjMatrix[dest][notions.index("achievedInGeneral")] == False and dest != notions.index("N-OPA") and adjMatrix[dest][notions.index("N-OPA")] == False:
					adjMatrixNon[dest][notions.index("N-OPA")] = True;
				pass

	adjMatrixNon = antitransitivityLoop(adjMatrix,adjMatrixNon,notions)

	inconsistencies = 0
	incompletenesses = 0

	

	for x in range(0,len(notions)):
		for y in range(0,len(notions)):
			if adjMatrix[x][y] == True and  adjMatrixNon[x][y] == True:
				logger.error("INCONSISTENT! %s => %s and %s =|=> %s" % (notions[x],notions[y],notions[x],notions[y]))
				l = []
				l = printWay(originalMatrix,notions,x,y,l,[])
				logger.warn("Path for =>")
				if l != False:
					for (s,d) in l[::-1]:
						logger.warn("%s => %s" % (s,d))
				else:
					logger.warn("No path found! for =>")
				l = []
				l = printWay(adjMatrixNon,notions,x,y,l,[])
				logger.warn("Path for =|=>")
				if l != False:
					for (s,d) in l[::-1]:
						logger.warn("%s =|=> %s" % (s,d))
				else:
					logger.warn("No path found! for =|=>")

				exit(0)


				inconsistencies += 1
			if adjMatrix[x][y] == False and  adjMatrixNon[x][y] == False:
				logger.warn("Incomplete! %s =?=> %s" % (notions[x],notions[y]))
				incompletenesses += 1


	numpy.save("adjMatrix", adjMatrix)
	for page in pages:
		latexExport(adjMatrix,adjMatrixNon,"../Thesis/Maindocument/outAdjMatrix",notions,page)
		latexExport(adjMatrix,adjMatrixNon,"outAdjMatrix",notions,page)

	logger.info("Number of notions:          %5d" % len(notions))
	logger.info("Number of inconsistencies:  %5d" % inconsistencies)
	logger.info("Number of incompletenesses: %5d" % incompletenesses)

	dot = Digraph(comment='Overview')
	n = 0
	for i in notions:
		c = "white"
		dot.node(str(n), i, style='filled',fillcolor=c)
		n = n+1

	for e in edges:
		dot.edge(str(e[0]),str(e[1]))



	#dot.render('test-output/overview.gv', view=True)
	logger.info("Finished")


	#print(adjMatrix)





import csv


encoding = {
	"nCU": "|U|",
	"nUornH": "\\overline{U} \\lor \\overline{H^\\dagger}",
	"nUornP": "\\overline{U} \\lor \\overline{P^\\dagger}",
	"nH": "\\overline{H^\\dagger}",
	"nQ": "\\overline{Q^\\dagger}",
	"nP": "\\overline{P^\\dagger}",
	"nU": "\\overline{U}",
	"nUandnH": "\\overline{U} \\land \\overline{H^\\dagger}",
	"nQandnP": "\\overline{Q^\\dagger} \\land \\overline{P^\\dagger}",
	"nUandnP": "\\overline{U} \\land \\overline{P^\\dagger}",
	"nQornP": "\\overline{Q^\\dagger} \\lor \\overline{P^\\dagger}",
}

game = "-OCA"
outfile = open("../Thesis/Maindocument/outAdditionalProofsFornSOCA.tex","w")

with open('counterexamplesnS.csv') as csvfile:
	rdr = csv.reader(csvfile, delimiter=',')
	for row in rdr:
		n1 = row[0].strip()
		n2 = row[1].strip()
		s1 = row[2].strip()
		s2 = row[3].strip()

		outfile.write("$%s%s$&$\\cancel{\\Rightarrow}$&$%s%s$ & $\\begin{array}{rcl}eqcls_0 &:=& \\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}\\ \\cup\\  \\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}\\\\ eqcls_1 &:=& V\\ \\setminus eqcls_0\\\\\\end{array}$\\\\\n\\hline\n" % (encoding[n1],game,encoding[n2],game,s1[0],s1[1],s1[2],s1[3],s2[0],s2[1],s2[2],s2[3]) )

outfile.close()


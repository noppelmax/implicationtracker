import csv


encoding = {
	"CU": "|U|",
	"UorH": "(U \\lor H^\\dagger)",
	"UorP": "(U \\lor P^\\dagger)",
	"H": "H^\\dagger",
	"Q": "Q^\\dagger",
	"P": "P^\\dagger",
	"U": "U",
	"UandH": "(U \\land H^\\dagger)",
	"QandP": "(Q^\\dagger \\land P^\\dagger)",
	"UandP": "(U \\land P^\\dagger)",
	"QorP": "(Q^\\dagger \\lor P^\\dagger)",
}

game = "-OPA"

notionheader = [ "" , "\\nDiamond \\land E_S \\land "]

outfile = open("../Thesis/Maindocument/outAdditionalProofsForSOPA.tex","w")

for h1 in notionheader:
	for h2 in notionheader:
		with open('counterexamples.csv') as csvfile:
			rdr = csv.reader(csvfile, delimiter=',')
			for row in rdr:
				n1 = row[0].strip()
				n2 = row[1].strip()
				s1 = row[2].strip()
				s2 = row[3].strip()

				outfile.write("$%s%s%s$&$\\cancel{\\Rightarrow}$&$%s%s%s$ & $\\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}\\ %s%s\\  \\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}$ but $\\cancel{%s%s}$\\\\\n\\hline\n" % (h1,encoding[n1],game,h2,encoding[n2],game,s1[0],s1[1],s1[2],s1[3],h1,encoding[n1],s2[0],s2[1],s2[2],s2[3],h2,encoding[n2]) )

outfile.close()


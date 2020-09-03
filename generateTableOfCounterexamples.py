import csv


encoding = {
	"CU": "|U|",
	"UorH": "(U \\lor H)",
	"UorP": "(U \\lor P)",
	"H": "H",
	"Q": "Q",
	"P": "P",
	"U": "U",
	"UandH": "(U \\land H)",
	"QandP": "(Q \\land P)",
	"UandP": "(U \\land P)",
	"QorP": "(Q \\lor P)",
}

game = "-OPA"

notionheader = [ "" , "\\nDiamond \\land E_S \\land "]

for h1 in notionheader:
	for h2 in notionheader:
		with open('counterexamples.csv') as csvfile:
			rdr = csv.reader(csvfile, delimiter=',')
			for row in rdr:
				n1 = row[0].strip()
				n2 = row[1].strip()
				s1 = row[2].strip()
				s2 = row[3].strip()

				print("$%s%s%s$&$\\cancel{\\Rightarrow}$&$%s%s%s$ & $\\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}\\ %s%s\\  \\begin{bsmallmatrix}%s&%s&%s&%s\\end{bsmallmatrix}$ but $\\cancel{%s%s}$\\\\\n\\hline\n" % (h1,encoding[n1],game,h2,encoding[n2],game,s1[0],s1[1],s1[2],s1[3],h1,encoding[n1],s2[0],s2[1],s2[2],s2[3],h2,encoding[n2]) )



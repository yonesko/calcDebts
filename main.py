import json

kurs = 33
totalContribution = {}

for line in open("baki.csv", "r"):
    who = line.split(";")[2]
    amount = -float(line.split(";")[4].replace(",", "."))
    totalContribution[who] = totalContribution.get(who, 0) + amount

print(totalContribution)

debts = {}

for fr in totalContribution:
    for to in totalContribution:
        if fr != to:
            debt = totalContribution[to] / 4
            contribution = totalContribution[fr] / 4
            if fr not in debts:
                debts[fr] = {}
            debts[fr][to] = debts[fr].get(to, 0) + debt - contribution
            debts[fr][to] = round(debts[fr][to], 2)

##Ad-hoc debts
debts["Gleb"]["Udak"] += 6
debts["Kiril"]["Udak"] += 3

##To show
toShow = {}

for fr in debts:
    for to in debts[fr]:
        if debts[fr][to] > 0:
            if fr not in toShow:
                toShow[fr] = {}
            toShow[fr][to] = round(debts[fr][to] * kurs, 2)

print(json.dumps(toShow, indent=4))

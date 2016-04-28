#!/usr/bin/env python

import sys, os, random, time


rules = """Zasady sa proste, dostajesz zadanie i je wykonujesz!
Zostanie ci podany warunek logiczny a ty masz odpowiedziec jaki jest jego wynik.\n
Wiec do rzeczy! Gramy?  (Odpowiedz tak/nie)\n"""
badAnswer = """Widze ze odpowiedz na proste pytanie sprawia ci trudnosc
wiec zmierzenie sie z wyzwaniem jakim jest ta gra
moze cie przerosnac... ostatnia szansa!\nGRASZ ?! (Odpowiedz tak/nie)"""
badAnswer2 = """Ponownie odpowiedziales zle, konczymy zabawe\nDziekuje dobranoc"""
availableOptions = ("--not","--and","--impl","--or")
mandatoryFilesName = ("not.txt","and.txt","impl.txt","or.txt")
files = {}
numberOfLanes = {}
symbols = {
    "--not": "~",
    "--or": "v",
    "--and": "&",
    "--impl": "=>"
}
allVars = set()
clearScreen = lambda: os.system('cls' if os.name=='nt' else 'clear')

points = 0

def inpOption(key,value):
    assert (key in availableOptions),"Nie istnieje taka opcja: "+key
    assert (value in mandatoryFilesName), "Niedozwolona nazwa pliku, mozliwe nazwy to: and.txt not.txt impl.txt or.txt"
    files[key]=value
    numberOfLanes[key]=0
    return
def getLineFromFile(fileType,nr):
    fileName = files[fileType]
    with open(fileName) as f:
        i = 1
        for lane in f:
            if nr == i :
                return lane
            i += 1
def getLineFromFileWithValue(fileType,arg1):
    fileName = files[fileType]
    with open(fileName) as f:
        for lane in f:
            if lane[0] == str(arg1):
                return lane
def getLineFromFileWithValues(fileType,arg1,arg2):
    fileName = files[fileType]
    with open(fileName) as f:
        for lane in f:
            if lane[0] == str(arg1) and lane[2] == str(arg2):
                return lane
def countLanesInFiles():
    for key in files.keys():  # Count number of lanes in files
        with open(files[key]) as f:
            for line in f:
                numberOfLanes[key] += 1
    return
def getPassedArguments():
    assert (len(sys.argv) % 2 == 1), "Zle podane argumenty, podaj opcje a nastepnie nazwe pliku"
    assert (len(sys.argv) > 4), "Za malo argumentow aby gra miala sens"
    for index in range(1, len(sys.argv), 2):
        inpOption(sys.argv[index], sys.argv[index + 1])
    countLanesInFiles()
    global allVars
    allVars = getAllVars()
    return
def getRandomLane(fileType):
    n = random.randint(1,numberOfLanes[fileType])
    return getLineFromFile(fileType,n)
def getRandomSymbol():            # Random symbol of function but without negation
    types = files.keys()
    types.remove("--not")
    n = random.randint(0,len(types)-1)
    return symbols[types[n]]
def getRandomVar():
    var = str(random.sample(allVars,1))
    return var[2]
def getRawTask(N=1):
    brackets = 1
    inBrackets = 0
    result = "( "
    bracked = True
    n = N
    while n>0 :
        if N/2 < n and brackets < n and random.randint(1,2) == 1:
            result += "( "
            brackets += 1
            bracked =True
        if files.has_key("--not") and random.randint(1,2) == 1:
            result += symbols["--not"]
        if N/2 < n and brackets < n and random.randint(1, 2) == 1:
            result += "( "
            brackets += 1
            bracked = True
        if bracked:
            result += getRandomVar() + " " + getRandomSymbol() + " "
            bracked = False
        else:
            result += getRandomVar() + " ) "
            bracked = True
            brackets -= 1
            while brackets > 0:
                result += ") "
                brackets -= 1

            result += getRandomSymbol() + " "
            i = n
            if i != 1:
                result += "( "
                inBrackets += 1

            while i > 1:
                result += "( "
                brackets += 1
                i -= 1

        if n == 1:
            result += getRandomVar() + " "
            brackets += inBrackets
            while brackets >0:
                result += ") "
                brackets -= 1
        n -= 1
    return result
def sugarRawTask(task):
    newTask = task
    found = True
    beg = task.find("( (")
    while found:            # Delete brackets outside functions
        found = False
        if beg >= 0 and not found:
            while task.find("( (",beg+2,beg+5) >= 0:
                beg = beg+2
            end = beg + 3
            bracked = True
            while (task[end] != ")" or task[end+2] != ")") and bracked :
                if task[end] == ")":
                    bracked = False
                end += 1
            if bracked:
                newTask = task[:beg+1] + task[beg+3:end+1] + task[end+3:]
                task = newTask
                found = True
        if beg >= 0 and not found:
            if task.find("( (",beg+2) >= 0:
                beg = task.find("( (",beg+2)
                found = True
        elif found:
            beg = task.find("( (")
    return newTask
def solveNegation(task,ind):
    relation = getLineFromFileWithValue("--not",task[ind+len(symbols["--not"])])
    newTask = task.replace(task[ind:ind+1+len(symbols["--not"])],relation[2])
    return newTask
def solveFunction(task, ind):
    i = 4
    val = ""
    while task[ind + i] != " ":
        val += task[ind + i]
        i += 1
    functionType = [k for k, v in symbols.iteritems() if v == val]
    relation = getLineFromFileWithValues(functionType[0], task[ind + 2], task[ind + 5 + len(val)])
    task = task.replace(task[ind:ind + 8 +len(val)], relation[4])
    return task
def solveTask(task):
    found = True
    while found:
        found = False
        beg = task.find(")")
        if beg >= 0 :
            found = True
            while task[beg] != "(":
                if task[beg:beg+len(symbols["--not"])] == symbols["--not"]:
                    task = solveNegation(task,beg);
                beg -= 1
            end = task.find(")",beg)
            if end - beg == 4 :
                task = task.replace(task[beg:beg+5],task[beg+2:beg+3])
            else:
                task = solveFunction(task,beg)

    if len(task) == 2:
        return task[0:1]
    else:
        task = "( " + task + ")"
        return solveFunction(task,0)
def getTask(n=1):
    task = getRawTask(n)
    task = sugarRawTask(task)
    return task
def getAllVars():
    vars = set()
    fileType = random.choice(files.keys())
    for i in range(1,numberOfLanes[fileType]+1):
        lane = getLineFromFile(fileType,i)
        vars.add(lane[0])
    return vars
def playLevels(a,b):
    for i in range(a, b+1):
        clearScreen()
        if points >= 0:
            task = getTask(i)
            solvedTask = solveTask(task)
            print "Twoj wynik to:",points,"  Twoje zadanie:",task, "Odpowiedz :", ', '.join(allVars)
            answer = raw_input()
            if answer in allVars:
                if answer == solvedTask:
                    print "Dobrze !"
                    time.sleep(1)
                    global points
                    points += 1
                else:
                    print "Zle !"
                    time.sleep(1)
                    return False
            else:
                print "Nie mozesz tak odpowiedziec !"
                print "Niestety ta gra nie wybacza takich bledow... -5 pkt !"
                time.sleep(3)
                points -= 5
            clearScreen()
        else:
            return False
    clearScreen()
    if points <= 0:
        return False
    else:
        return True
def endGame(won):
    if won:
        print "Wygrales ! uzyskales",points,"pkt !"
    else:
        print "Przegrales ! uzyskales",points,"pkt !"
    return
def playGame():
    print "Zaczniemy od czego latwego !"
    time.sleep(1)
    clearScreen()
    won = playLevels(1,3)

    if won:
        print "Widze ze dajesz rade, co powiesz teraz !"
        time.sleep(2)
        won = playLevels(4,5)
    if won:
        print "Latwo sie nie poddajesz !"
        time.sleep(2)
        won = playLevels(5,8)
    if won:
        print "Ej bo koncza mi sie pomysly !"
        time.sleep(2)
        won = playLevels(9, 11)
    if won:
        print "Ostateczne starcie ! Traktuj to jak walke z bosem !"
        time.sleep(3)
        won = playLevels(15,18)

    endGame(won)
    return

# ================= MAIN PROGRAM =====================
getPassedArguments()
countLanesInFiles()
clearScreen()
print rules
answer = raw_input()
if answer == "tak":
    clearScreen()
    playGame()
elif answer != "nie":
    clearScreen()
    print badAnswer
    answer = raw_input()
    if answer == "tak":
        clearScreen()
        playGame()
    elif answer != "nie":
        clearScreen()
        print badAnswer2



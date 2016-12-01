import networkx as nx
import sys, random
import partyCalcs as pc
#socialGraph = nx.Graph()
#parser output contains Graph, partyCount, hostCount
#parserOutput = []
f = open(sys.argv[1])
socialGraphFile = f.readlines()
f.close()
DEBUG = True

parserOutput = []
def parseFileLines(fileLines):
	socialGraph = nx.Graph()
	splitLine = []
	testCaseCount = 0
	curTestCase = 0
	peopleCount = 0 #N
	linkCount = 0 #F
	partyCount = 0 #M
	partyHostCount = 0 #A
	partyHostIDs = []
	LP = 1 #Line Pointer skip first line

	testCaseCount = int(fileLines[0])
	if DEBUG:
		print "Processing", testCaseCount, "test cases..."
	while LP < len(fileLines):
		curLine = fileLines[LP]
		splitLine = curLine.split()
		if len(splitLine) == 4: #N, F, M, A
			peopleCount = int(splitLine[0])
			linkCount = int(splitLine[1])
			partyCount = int(splitLine[2])
			partyHostCount = int(splitLine[3])
			partyHostIDs = []
			socialGraph = nx.Graph()
			LP += 1
			if DEBUG:
				print "Test case:",curTestCase + 1
				print " People:", peopleCount
				print " Friendships:", linkCount
				print " Parties:", partyCount
				print " Hosts:", partyHostCount

		for lineNum in range(LP, linkCount+LP):
			curLine = fileLines[LP]
			splitLine = curLine.split()
			socialGraph.add_edge(int(splitLine[0]),int(splitLine[1]))
			#print LP+1,"adding edge", splitLine[0],"and",splitLine[1]
			LP += 1	
		curTestArray = [socialGraph,partyCount,partyHostIDs]
		parserOutput.append(curTestArray)
		curTestCase += 1

parseFileLines(socialGraphFile)	
#print "parser output:",parserOutput

#iterate over all the test cases now that they are processed into networkx graphs
for counter, test in enumerate(parserOutput):
	#test = [graph, partyCount, hosts]
	#					0					1					2
	curGraph = test[0]
	partyCount = 1 #test[1] PA3 EDIT
	hosts = test[2]
	people = nx.nodes(curGraph)
	peopleCount = len(people)
	print "\nTest Case",counter+1
	print "-------------------------------"
	avg = 9999 #PA3 EDIT
	chosenHosts = [] #PA3 EDIT	
	while avg > 1:
		chosenHosts = pc.mostPopularT4(curGraph,people,partyCount)
		awkVals = pc.bestAwkVals(curGraph,people,chosenHosts)
		avg = pc.calcAvgAwk(awkVals,chosenHosts)
		partyCount += 1

	print "My Heuristic hosts are", chosenHosts
	print "Average social awkwardness =", avg
	
		

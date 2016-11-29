import networkx as nx
import sys, random
#import partyCalcs as pc
#socialGraph = nx.Graph()
#parser output contains Graph, partyCount, hostCount
#parserOutput = []
f = open(sys.argv[1])
socialGraphFile = f.readlines()
f.close()
DEBUG = False

parserOutput = []
def parseFileLines(fileLines):
	socialGraph = None
	splitLine = []
	testCaseCount = 0
	curTestCase = 0
	curEdgeCount = 0
	curVertexCount = 0
	LP = 1 #Line Pointer skip first line

	testCaseCount = int(fileLines[0])
	if DEBUG:
		print "Processing", testCaseCount, "test cases..."
	for i in range (0,testCaseCount):
		socialGraph = nx.Graph() 
		curLine = fileLines[LP]
		splitLine = curLine.split()
		curVertexCount = int(splitLine[0])
		curEdgeCount = int(splitLine[1])
		LP += 1
		while curEdgeCount > 0:
			curLine = fileLines[LP]
			splitLine = curLine.split()
			socialGraph.add_edge(int(splitLine[0]),int(splitLine[1]))
			curEdgeCount -= 1
			LP += 1
		
		parserOutput.append(socialGraph)
		curTestCase += 1

parseFileLines(socialGraphFile)	
print "parser output:",parserOutput

#part 1
#generate transformation graph accoridng to dominating set reduction.
part1_output = []
for counter, curGraph in enumerate(parserOutput):
	nodes = nx.nodes(curGraph)
	nodeCount = len(nodes)
	newGraph = curGraph
	for edge in curGraph.edges():
		src = int(edge[0])
		trg = int(edge[1])
		newID = 1000 * src + trg
		newGraph.add_edge(src,newID)
		newGraph.add_edge(newID,trg)
	part1_output.append(newGraph)
	

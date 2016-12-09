import networkx as nx
import  sys
#verifyVertexCover
#takes in an original graph, a vertex cover array
#returns true if the givien vertex cover is valid
#false if not 

f1 = open(sys.argv[1])
part1File = f1.readlines()
f2 = open(sys.argv[2])
part3File = f2.readlines()
f1.close()
f2.close()
originalEdges = []
def parseP1(fileLines):
	graph = None
	splitLine = []
	testCaseCount = 0
	curTestCase = 0
	curEdgeCount = 0
	curVertexCount = 0
	LP = 1
	output = []
	testCaseCount = int(fileLines[0])
	for i in range(0, testCaseCount):
		graph = nx.Graph()
		curLine = fileLines[LP]
		splitLine = curLine.split()
		curVertexCount = int(splitLine[0])
		curEdgeCount = int(splitLine[1])
		LP += 1 
		while curEdgeCount > 0:
			curLine = fileLines[LP]
			splitLine = curLine.split()
			graph.add_edge(int(splitLine[0]), int(splitLine[1]))
			curEdgeCount -= 1
			LP += 1 
			
		output.append(graph)
		curTestCase += 1
	return output

def parseP3(fileLines):
	curTestCase = 0
	covers = []
	curNodeCount = 0
	LP = 1
	testCaseCount = int(fileLines[0])
	for i in range(0, testCaseCount):
		curCover = []
		curNodeCount = int(fileLines[LP])
		LP += 1
		while curNodeCount > 0:
			curCover.append(int(fileLines[LP]))
			LP += 1
			curNodeCount -= 1
		covers.append(curCover)
	return covers

def verifyVertexCovers(graphs,covers):	
	result = True
	for counter, graph in enumerate(graphs):
		result = True
		edges = graph.edges()
		print "edges",edges
		cover = covers[counter]
		print "cover",cover
		for edge in edges:
			if not (edge[0] in cover) and not (edge[1] in cover):
				result = False
		print "isCover:",result

	return result


graphs = parseP1(part1File)
covers = parseP3(part3File)
verifyVertexCovers(graphs, covers)

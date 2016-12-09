>python file2nxPart1.py examples/all_in.txt
	will write output to parserOutput.txt

>python file2nxPart2.py parserOutput.txt
	will print hosts found to get awkwardness = 1.0
	will also write the sanitized vertexCovers to vertexCoverOutput.txt

>python verifyVCover.py examples/all_in.txt vertexCoverOutput.txt
	will verify the given vertexCovers are correct for the original example
	first argument must be the same file used for file2nxPart1
	second argument is the file written by file2nxPart2.py



__author__ = "Michael Snider, Kevin Chan"


from PIL import Image
import subprocess


def connect(img):
	""" Connect image to finalize the TSP art after stippling
	"""

	# generate list of all stippled points
	stippledPoints = []

	for x in range(img.size[0]):
		for y in range(img.size[1]):
			if img.getpixel((x, y)) == 0:
				stippledPoints.append((x, y))

	print ""
	print len(stippledPoints), "stipples were generated."

	# how to connect a line: ex. (0, 0) to center of image
	# img = connectLine(img, (0, 0), (img.size[0]//2, img.size[1]//2))

	# generate tsp file for concorde
	with open("tspArtData.tsp", "w") as tspWrite:
		tspWrite.write("NAME : tsp-art\n")
		tspWrite.write("COMMENT : tsp-art-problem (Snider, Chan)\nTYPE : TSP\n")
		tspWrite.write("DIMENSION: %d\n" % len(stippledPoints))
		tspWrite.write("EDGE_WEIGHT_TYPE : EUC_2D\nNODE_COORD_SECTION\n")
	
		for i, stippledPoint in enumerate(stippledPoints):
			tspWrite.write("%d %d %d\n" % (i + 1, stippledPoint[0], stippledPoint[1]))
	
		tspWrite.write("EOF\n")



	subprocess.call(["./concorde", "-x", "-B", "tspArtData.tsp"])



	# collect tour
	tspTour = []
	with open("tspArtData.sol", "r") as tspRead:
		
		for i, currentLine in enumerate(tspRead):
			if i != 0 and currentLine != "" and currentLine != "\n":
				tspTour += [int(x) for x in currentLine.strip().split()]

	#print tspTour

	# connect lines
	for i in range(0, len(tspTour)):

		if i < len(tspTour) - 1:
			# print "Connect points (%d, %d) and (%d, %d)" % (stippledPoints[tspTour[i]][0], stippledPoints[tspTour[i]][1], stippledPoints[tspTour[i + 1]][0], stippledPoints[tspTour[i + 1]][1])
			img = connectLine(img, stippledPoints[tspTour[i]], stippledPoints[tspTour[i + 1]])
		else:
			# print "Connect points (%d, %d) and (%d, %d)" % (stippledPoints[tspTour[i]][0], stippledPoints[tspTour[i]][1], stippledPoints[tspTour[0]][0], stippledPoints[tspTour[0]][1])
			img = connectLine(img, stippledPoints[tspTour[i]], stippledPoints[tspTour[0]])


	
	return img

def connectLine(img, point1, point2):
	""" Given two points, (x, y) tuples, connects the lines along image
		pixels
	"""
	diffX = point2[0] - point1[0]
	diffY = point2[1] - point1[1]
	iterateRows = abs(diffX) >= abs(diffY)

	if iterateRows:

		if diffX < 0:
			xInit = point2[0]
			yInit = point2[1]
			xRange = range(point2[0], point1[0])
		else:
			xInit = point1[0]
			yInit = point1[1]
			xRange = range(point1[0], point2[0])

		#print "xrange", xRange

		for x in xRange:
			yCurrent = yInit + ((x - xInit) * diffY)//diffX
			if yCurrent < 0:
				print yCurrent
			img.putpixel((x, yCurrent), 0)

	else:

		if diffY < 0:
			xInit = point2[0]
			yInit = point2[1]
			yRange = range(point2[1], point1[1])
		else:
			xInit = point1[0]
			yInit = point1[1]
			yRange = range(point1[1], point2[1])

		#print "yrange", yRange

		for y in yRange:
			xCurrent = xInit + ((y - yInit) * diffX)//diffY
			if xCurrent < 0:
				print xCurrent
			img.putpixel((xCurrent, y), 0)

	return img

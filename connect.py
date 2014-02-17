__author__ = "Michael Snider, Kevin Chan"


from PIL import Image


def connect(img):
	""" Connect image to finalize the TSP art after stippling
	"""
	originalImg= []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(img.getpixel((x, y)))
		originalImg.append(colValues)


	#test that connects all lines to center of image

	#for x in range(img.size[0]):
	#	for y in range(img.size[1]):
	#		if originalImg[x][y] == 0:
	#			img = connectLine(img, (x, y), (img.size[0]//2, img.size[1]//2))

	
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
			yCurrent = yInit + ((x - xInit) * diffY)//abs(diffX)
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
			xCurrent = xInit + ((y - yInit) * diffX)//abs(diffY)
			img.putpixel((xCurrent, y), 0)

	return img

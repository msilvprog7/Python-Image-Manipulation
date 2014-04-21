__author__ = "Michael Snider, Kevin Chan"


from random import randint

def stipple(img):
	""" Pass Pillow Image in to allow for a pixel by pixel search and
		remove considerably whiter pixels based on our algorithm for stippling
	"""

	img = threshold(img, 25)

	return img

def threshold(img, value):
	""" Threshold image based on the following rule,
		First go through each column, checking for value differences in pixels.
		Then go through each row, checking for value differences in pixels.
		>= value differences gets assigned a 0 in pixel value
	"""
	pixelValues = []
	for x in range(img.size[0]):
		colValues = []
		for y in range(img.size[1]):
			colValues.append(255)
		pixelValues.append(colValues)


	# column search
	for x in range(img.size[0]):
		for y in range(img.size[1]):

			if y == 0:
				prevYPixel = img.getpixel((x, y))
				continue

			difference = abs(img.getpixel((x, y)) - prevYPixel)
			prevYPixel = img.getpixel((x, y))

			if difference >= value:
				pixelValues[x][y] = 0

	# row search
	for y in range(img.size[1]):
		for x in range(img.size[0]):

			if x == 0:
				prevXPixel = img.getpixel((x, y))
				continue

			difference = abs(img.getpixel((x, y)) - prevXPixel)
			prevXPixel = img.getpixel((x, y))

			if difference >= value:
				pixelValues[x][y] = 0

	length = 2
	total = length*length*255

	# Remove points based on surrounding area

	for x in range(length, img.size[0] - length):
		for y in range(length, img.size[1] - length):
			if pixelValues[x][y] == 0:
				random = randint(1, 10)
				pixeltotal = 0
				for a in range(x - length, x + length):
					for b in range(y - length, y + length):
						pixeltotal += pixelValues[a][b]
				# More surrounding black points means greater probability of removal of that point
				if pixeltotal > total & random > 8:
					pixelValues[x][y] = 255
				elif pixeltotal > total*3/4 & random > 6:
					pixelValues[x][y] = 255
				elif pixeltotal > total/2 & random > 4:
					pixelValues[x][y] = 255
				elif pixeltotal > total/4 & random > 2:
					pixelValues[x][y] = 255
				elif pixeltotal >= 0 & random > 1:
					pixelValues[x][y] = 255



	for x in range(img.size[0]):
		for y in range(img.size[1]):
			img.putpixel((x, y), pixelValues[x][y])

	return img

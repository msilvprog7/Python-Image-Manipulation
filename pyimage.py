__author__ = "Michael Snider, Kevin Chan"


import prompt, stipple
import sys
from PIL import Image



filePath = prompt.getSingleString("Enter path to image")

try:
	fileTmp = open(filePath, "r")
	fileTmp.close()

except IOError:
	print "File not found..."
	sys.exit()


image = Image.open(filePath).convert("L")
print "Image converted to bw..."
print "\t", image.format, image.size, image.mode


# change image here ****


image = stipple.stipple(image)





# **********************


print "Saving image..."

separatedFilePath = filePath.rsplit(".", 1)
newFilePath = separatedFilePath[0] + "-stipple" + "." + separatedFilePath[1]
try:
	fileTmp = open(newFilePath, "r")
	fileTmp.close()

	if not prompt.yes_no_choice("\tWould you like to overwrite file " + newFilePath):
		print "\tImage was not saved."
		sys.exit()

except IOError:
	pass

image.save(newFilePath)
print "\t", "Saved successfully to", newFilePath

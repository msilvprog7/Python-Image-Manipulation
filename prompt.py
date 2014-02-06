__author__ = "Michael Snider"



def getSingleString(outputMsg = ""):
	""" Prompt outputMsg and accept input
		for the first string entered.
	"""
	retStr = ""

	while retStr == "":
		retStr = raw_input(outputMsg + ": ")
		retStr = retStr.strip()

	retStr = retStr.split()[0]
	return retStr

def yes_no_choice(outputMsg = ""):
	""" 
	"""
	retSuccess = False
	strResponse = ""

	while strResponse == "":
		strResponse = getSingleString(outputMsg + "[y/n]")
		strResponse = strResponse.strip().lower()

		if strResponse[0] == 'y':
			return True
		elif strResponse[0] != 'n':
			strResponse = ""

	return False



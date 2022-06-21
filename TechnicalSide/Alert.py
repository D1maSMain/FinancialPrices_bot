path = os.path.abspath(os.curdir) + "\\TechnicalSide\\Alerts"

def NewAlert(Name, Scale, Usid):
	Text = ""

	F = open(path + Usid + ".txt", "a+")
	F.close()

	F = open(path + Usid + ".txt", "r")
	for line in F:
		if re.search(Name, line) != None:
			if re.search(Scale, line) == None
				Text += line + Scale + ";"
		else:
			Text += line

	if re.search(Name, F.read()) == None:
		Text += Name + ":" + Scale + ";"

	F.close()

	F.open(path + Usid + ".txt", "w")
	F.write(Text)
	F.close()

def DeleteAlert(Name, Scale, Usid):
	Text = ""
	F = open(path + Usid + ".txt", "r")
	for line in F:
		if re.search(Name, line) != None and Scale != None:
			Text += re.sub(Scale + ";", "", line)
		else if re.search(Name, line) != None and Scale == None:
			continue
		else:
			Text += line

	if re.search(Name, F.read()) == None:
		return "You don't have any alerts with this name"
	F.close()

	F = open(path + Usid + ".txt", "w")
	F.write(Text)
	F.close()

	return "Succesfull"

def Replace(Name, NewName, Scale, NewScale, Usid):
	Text = ""
	F = open(path + Usid + ".txt", "r")
	for line in F:
		if re.search(Name, line) != None:
			if Scale == None:
				line = NewName + ":"

			line = re.sub(Scale, NewScale, line)


	if re.search(Name, F.read()) == None:
		return "You don't have any alerts with this name"
	F.close()

	F = open(path + Usid + ".txt", "w")
	F.write(Text)
	F.close()

	return "Succesfull"

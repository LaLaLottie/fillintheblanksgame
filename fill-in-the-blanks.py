# IPND Stage 2 Final Project

####################
# Global Variables #
####################

blanks = ["___1___", "___2___", "___3___", "___4___"]

easy_paragraph = '''___1___ is a widely used high-level, general-purpose, interpreted, dynamic ___2___ language.[22][23] Its design philosophy emphasizes code readability, and its ___3___ allows programmers to express concepts in ___4___ lines of code than would be possible in languages such as C++ or Java.[24][25] The language provides constructs intended to enable clear programs on both a small and large scale.[26] Source: Wikipedia''' 
medium_paragraph = '''Python supports multiple programming ___1___, including object-oriented, imperative and ___2___ programming or procedural styles. It features a dynamic type system and automatic ___3___ management and has a large and comprehensive standard ___4___.[27] Source: Wikipedia''' 
hard_paragraph = '''Python interpreters are available for installation on many operating systems, allowing Python code execution on a wide variety of systems. Using third-party tools, such as ___1___ or ___2___,[28] Python code can be ___3___ into stand-alone executable programs for some of the most popular operating systems, allowing the distribution of Python-based software for use on those environments without requiring the installation of a Python interpreter. ___4___, the reference implementation of Python, is free and open-source software and has a community-based development model, as do nearly all of its alternative implementations. Source: Wikipedia'''

easy_answers = ["python", "programming", "syntax", "fewer"]
medium_answers = ["paradigms", "functional", "memory", "library"]
hard_answers = ["py2exe", "pyinstaller", "packaged", "cpython"]	

####################
# Helper Functions #
####################

def greeting(player_name):
	"""To display initial player and game information. 
	Inputs: Inputted name of player.  
	Outputs: Introduction to game greeting."""
		
	print "\nGreat! Welcome, " + player_name + ". The purpose of this game is to fill in the blanks for all the sentences provided. Now, please pick a level by entering in the appropriate number: "


def get_setup(level):
	"""To group all the paragraphs and answers together.  
	Inputs: Current level.  
	Outputs: The specific paragraph and its answers associated with that level."""

	if level == "1":
		print "\nYou chose level 1 - Easy.\n"
		return easy_paragraph, easy_answers

	elif level == "2":
		print "\nYou chose level 2 - Medium.\n"
		return medium_paragraph, medium_answers

	else: # For level 3.
		print "\nYou chose level 3 - Hard.\n"
		return hard_paragraph, hard_answers


def word_in_blanks(word, blanks):
	"""To single out every blank. 
	Inputs: 'word' is the each blank in the 'blanks' list. 'blanks' is the list. 
	Outputs: Returns 'word' if that matches up with the current word in the paragraph."""

	for blank in blanks: # For every blank in the blanks array.
		if blank in word: # If blank is in answer.
			return blank
	return None


def replace_the_blank(word, replaced, blanks, user_answer, index): 
	"""To replace each blank with its correct answer. Part 2.
	Inputs: 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
	the 'user_answer' for that blank, the index number of that 'user_answer' to correctly match that with the right blank to fill in. 
	Outputs: The correctly replaced paragraph."""

	if word_in_blanks(word, blanks) == None:
		if word not in replaced:
			replaced.append(word)
	else:
		replacement = word_in_blanks(word, blanks)
		word = word.replace(replacement, user_answer.upper())

		if replacement == blanks[index]:
			if replacement not in replaced:
				replaced.append(word)
			else:
				position = replaced.index(replacement)
				replaced[position] = word
		else:
			replaced.append(replacement)

	return replaced


def fill_in_answers(paragraph, blanks, replaced, user_answer, index): 
	"""To replace each blank with its correct answer. Part 1.
	Inputs: Paragraph from level, 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
	the 'user_answer' for that blank, the index number of that 'user_answer' to correctly match that with the right blank to fill in. 
	Outputs: The correctly replaced paragraph."""

	split_paragraph = paragraph.split()

	if type(replaced) == str:
		replaced = replaced.split()		

	for word in split_paragraph:
		replace_the_blank(word, replaced, blanks, user_answer, index)
		
	replaced = " ".join(replaced)
	head, sep, tail = replaced.partition("Wikipedia") # To get rid of the extra 'replacements' that tacked on to the end of every paragraph. Inputs: The replaced paragraph.  Outputs: Cleaned replaced paragraph.
	replaced = head + sep
	return replaced


def collect_answers(level, paragraph, answers):
	"""To collect the user's answers. 
	Inputs: The current level, its paragraph, and its answers. 
	Outputs: The updated replaced paragraph, the index of each answer."""
	
	replaced = []
	user_answer = ""

	index = 0
	for blank in blanks:
		# Where the questions and answers gets stated.
		question = "\nWhat is your answer for " + blank + "?"
		print question
		user_answer = raw_input("Type here: ")
		user_answer = user_answer.lower()

		while user_answer != answers[index]:
			print "\nYour answer was wrong. Please try again.\n"
			user_answer = raw_input("Type it here again: ")
			user_answer = user_answer.lower()

		print "\nAwesome, that's correct!\n"	
									
		replaced = fill_in_answers(paragraph, blanks, replaced, user_answer, index)
		print replaced			

		index += 1
	
	return replaced, index

###########################################
# Starting to actually play the 'game'... #
###########################################

def play_game():
	"""To execute the main program/game. Inputs: None.  Outputs: Whole program."""

	player_name = raw_input("What is the name of the current player? ")
	greeting(player_name)

	level = raw_input("\nEasy - 1 | Medium - 2 | Hard - 3 | ")

	if level == "1" or level == "2" or level == "3":
		paragraph, answers = get_setup(level)     
		print paragraph 

		replaced = collect_answers(level, paragraph, answers)

		print "\nYAY, " + player_name + ", YOU WON THE GAME!\n"	
	
	else:		
		print "\nWRONG! Please pick an actual level, " + player_name + ". Game will now restart.\n"
		play_game()

play_game() 

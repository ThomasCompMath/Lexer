##########################################################################
#------------------------------------------------------------------------#

# This plan will create a class for each verb (eventually for each verb phrase. What will the attributes and methods be?
# I think the attributes should be grammatical/usage rules.
# I think the nouns and direct/indirect objects should be methods.

#------------------------------------------------------------------------#
##########################################################################

# Clear the screen:

import os
os.system('cls')




# In the last section, I could correctly identify parts of speech.
# In this section, I want to fill in my object with those parts of speech.

# In 3_2, I am tracing out the idea of having a verb class for analysis.

# In this, I will predefine a 'verb' class and have everything revolve around creating instances of this.

#I want to give it a predefined sentence.
#Eventually, I want to take sentence syntax into consideration, but for now I will choose an intentionally simple sentence.
#Parse it into tokens first. Use the tokens to build the sentences.


###############################################
#	DICTIONARIES
###############################################

parsing_dictionary = {
                     'flies' : 'fly',
                     'walks' : 'walk'
}
part_of_speech = {
                 'fly' : 'verb',
                 'bird' : 'noun',
                 'walk' : 'verb'
}
# Eventually, I want this to be imported from somewhere. For now, I'll hard-code in some words.
# For now I'll use a dictionary, though I would eventually like to associate "flies" with "noun" and "fly"


###############################################
#	ERRORS
###############################################

#For now, I will ignore this error catching portion, since I don't fully understand how it works.
class Error:
	def __init__(self, error_name, details):
		self.error_name = error_name
		self.details = details
		
	def as_string(self):
		result = f'{self.error_name}: {self.details}'
		return result
		
class IllegalCharError(Error):
	def __init__(self, details):
		super().__init__('Illegal Character', details)





###############################################
# CREATE CLASSES TO CONCEPTIONALLY REPRESENT MY CLAUSES
###############################################

    
class Clause:
    def __init__(self, verbRoot, subject, dirObj, indirObj):
        self.verbRoot = verbRoot
        self.takesSubject = subject
        self.takesObject = dirObj
        self.takesIndirObj = indirObj

###############################################
# MY SAMPLE SENTENCE SHOULD BE: THE BIRD FLIES
# IGNORE WORDS NOT IN MY LIST, SUCH AS: 'THE'
# THE SECOND STEP COULD BE TO HAVE IT PARSE: 'THE CARDINAL FLIES' TO BE EQUAL TO 'THE RED BIRD FLIES'
###############################################

# Parse the text into tokens. It needs to create a token for 'bird' and a token for 'flies'
# The tokens can call the 'flies' method on the 'bird' object.
# In future tutorials, he will go over how to parse strings. For now, I will just do whatever I can come up with.
# Long-term goal -> design this in a game engine. The computer can create a model of what the words describe, much as the brain does.
# True end goal -> the computer can draw insights and make predictions from the model, and use these insights and predictions to update it's objects and methods

# An object is an instance of a class


class Token:
    def __init__(self, type_, value_ = None):
        self.type = type_
        self.value = value_
        
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
        
##############################################
#	LEXER
##############################################

# stringVariableName.split(' ') will split every string into words by spaces



class Lexer:    # From this I create tokens to be used to fill in my clauses
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.listOfStrings = self.text.split(' ')
        
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

# For starters, I will deal with simple sentences without punctuation.
# Eventually, I'll initially want to split by periods/exclamations/question marks first, then by commas second, and then by words
# In this way, I can create a dependancy tree


# This will presuppose that the text has been split into clauses.        
    def make_tokens(self):
        tokens = []
        i = 0
        self.advance()
        
        for i in self.listOfStrings:
            if i in parsing_dictionary.keys():
                j = parsing_dictionary[i]
                tokens.append([j, part_of_speech[j]])
            elif i in part_of_speech.keys():
                tokens.append([i, part_of_speech[i]])

        for i in tokens:            # Here I'll make the clause.
            if i[1] == 'verb':
                os.system('type nul> verb.py')
                f = open('verb.py', 'w+')
                f.writelines([  'class enterTheName:' + '\n', 
                                '\t' + 'def __inti__(self):' + '\n', 
                                '\t\t' + 'self.firstAtt = attribute1' + '\n',
                                '\t\t' + 'self.secondAtt = attribute2' + '\n\n',
                                '\t' + 'def method1(self):' + '\n',
                                '\t\t' + 'print(\'first method\')'])
                f.close()
        return tokens, None # I am going to want to pass 'tokens' into the object that I create.






######################################
# RUN
######################################

def run1(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    
    return tokens, error


# I could create many empty classes. More than the number of words I plan to have in the text, and then fill in the classes from the words.
# A subject could create a class.
# A verb could create a method tied to the subject.
# The predicate could define attributes of the method?
# Actually, I think I want the verb to be the class, since in language, the verb is the primary piece of the sentence.
# Perhaps the attributes could be the subjects that the verb takes, relationships with other words, and key grammatical points.
# The methods could be the subject performing the verb on the a predicate
# Currently, I can lay this out in the following:
#   Have the script import some kind of dictionary that lists the parts of speech of various words.
#   Have the script mark each word with a token if it is a noun or verb.
#   Use an empty class. Have the script create objects from the empty class based on the verbs.
#   Fill in the objects with the subjects.
#   Fill in the objects with the remaining nouns. (for advanced sentences it will have to break it into noun phrases and use these instead of nouns.)
#   Eventually, I want it to build an environment from this information, then it can perform a series of tests, "analysing" this information in some predefined ways or through machine learning.
#   I want it to use the environment created to draw conclusions and update definitions.
#   I do not need an empty class. I can just use a class called 'verb' and then fill in a verb object with the details.

















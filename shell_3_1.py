#Make your own programming language - EP1 - Lexer by CodePulse on Youtube
#A version of Basic

import basic_3_4

kill_command = False

while kill_command != True:
    text = input('input > ')
    result, error = basic_3_4.run1(text)
    
    if error: print(error.as_string())
    else: 
        print(result)
        import verb
        f = verb.enterTheName()
        f.method1()
    
    if text == 'kill':
        kill_command = False
    
# Just like I want to learn Hungarian with a narrow focus, try to
# create a general intelligence that still has a narrow focus.
# So, it could have a general understanding about a battlefield, warehouse, kitchen, etc.
# If I avoid living things, that would cut out a great deal of understanding required.

# The key for me will be to create an environment. I could try a kitchen or a city.
# There needs to be a lot of understanding about the objects and about how their attributes relate to reality.
# For the initial project, choosing a good environment is key.
# Why not choose a military environment?
# Actually intelligence predicts actions before acting. It evaluates the results and tweaks its next attempt based on the result.
# If regular machine learning could fish texts for new information to make its model of reality closer to reality, then that would be great.

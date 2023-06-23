#establishes initial resources
choices = []
import random 

#input any genre of food
while True:
     options = input ("what food option would you like: ")
     choices.append(options)
     
#randomly select one of the foods,repeatable
     if options == "choose":
          choices.remove("choose")
          rng_list = random.randint(0,len(choices)-1)
          print (choices[rng_list])
          
#in-case you forget what you've typed
     if options == "list":
          choices.remove("list")
          print (choices)
          
#ends the loop
     if options == "end":
          break
     
#in-case you forget what to type
     if options == "help":
          choices.remove ("help")
          print ("list: lists all items submitted")
          print ("end: stops the loop")
          print ("choose: selects random item from list")
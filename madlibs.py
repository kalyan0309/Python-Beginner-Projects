#strings concatenation (aka hwot o put string together)
#To create a string that says "subscribe to _____"
youtuber = "Kalyan Chittajallu"

#few ways to do this 
#print("Subscribe to "+youtuber)
#print("Subscribe to {}".fo+rmat(youtuber))
#print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("verb:")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"
print(madlib)

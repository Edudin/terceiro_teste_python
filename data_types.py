#string data type

#literal assignment

first = 'Edu'
last = 'Moraes'

#print(type(first))
#print(type(first) == str)
#print(isinstance(first, str))

#constructor function   

#pizza = str("Pepperoni")
#print(type(pizza))
#print(type(pizza) == str)
#print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
#decade = str(1980)
#print(type(decade))
#print(decade)

#statement = "i like rock music from the " + decade + "s."
#print(statement)

#multiple lines
#multiline = '''
#Hey, how are you?                                                     

#I was just checking in.   
#                            All good?

#'''
#print(multiline)

#sentence = 'I\'m back at work'
#print(sentence)

#escaping special characters 
sentence2 = "I\'m back at work \tHey! \n\nWhere\'s this at\\located?" 
print(sentence2)

print(first.lower())
print(first.upper())
print(first)

idade = "19"
print(idade)
def madlib(name, subject):
   
    the_madlib = "Your name is %s and your favorite subject is %s." % (name, subject)
    return the_madlib


name = input("Enter a name: ")
subject = input("Enter a subject: ")

print(madlib(name, subject))

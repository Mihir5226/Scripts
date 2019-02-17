import time
start_time =time.time()
print('what is your name?')
myName = input()
while myname != 'MP':
    if myName == 'your name':
    print("Haha, very funny.seriously, what is your name")
    myname =input()
    else:    
    print("this is not your name PLease type real name")
    myName(input())
print('Hello, ' + myname + '. That is a good name. How old are you?')
myAge = input()


if myAge <13:
    print("You're a minor?")
elif myAge == 13:
    print("you're a teenager now... that's cool, I guess")
elif myAge > 13 and myAge <30:
    print("you're young and dumb")
elif myAge >= 30 and myAge <65:
    print("You're adulting.")

else:
    print("... and you're not dead yet?")
programAge =int(time.time()- start_time)
print("%s? Thats funny, Im only %s old." %(myAge,programAge))
print("I wish I was %s years old" %(myAge*2)

time.sleep(3)
print("I am tired. I want to sleep right now")
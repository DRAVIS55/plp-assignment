#Here are some fun and beginner-friendly project ideas you can try at this stage:

#Random Joke Generator 🤣
#Build a program that stores a list of jokes and randomly selects one
#to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random
index=random.randint(0,4)
jokes=['smart you','pranked','simple logics','exciting','hacked']
print(jokes[index])

#1. Personalized Greeting App 👋
#Create a program that asks for the user’s name and favorite color, then prints 
#a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
name=input('enter your name')
color=input('favourite colour')
print(f'Hello {name}')
print(f'your favourite color {color} is awesome')

#2. Simple Quiz Game 🎮
#Create a multiple-choice quiz with questions about Python, 
#movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆
print('1. which one is false')
print('     A. i am a medics')
print('     B. i am a software engineer')
print('     C. i am a webdeveloper')
print('     D. i am a ethical hacker')
answ1=input('enter the correct answer').capitalize()
if answ1==('A'):
    result1=10
    print(f'Correct got  {result1} marks')
else:
    print('wrong the correct answer is A ')

print('1. which one is false')
print('     A. i am a medics')
print('     B. i am a software engineer')
print('     C. i am a webdeveloper')
print('     D. i am a ethical hacker')
answ2=input('enter the correct answer').capitalize()

if answ2==('A'):
    result1=10
    print(f'Correct got  {result1} marks')
else:
    print('wrong the correct answer is A ')

#Random Joke Generator 🤣
#Build a program that stores a list of jokes and randomly selects one
#to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random
index=random.randint(0,4)
jokes=['smart you','pranked','simple logics','exciting','hacked']
print(jokes[index])
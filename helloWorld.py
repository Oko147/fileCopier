# first_name = "Piotr"
# last_name = "Krzyżanowski"
# full_name = first_name +" "+ last_name
# print(type(first_name))
# print("Hello " +full_name)

# age = 31
# age+=1
#
# print("Your age is: " +str(age))

# float_number = 3.14155465464565464564
# print(float_number)

# human = True
#
# name = "Piotr"
# print(name*8)
#
# x = 1
# y = 2.0
# z = "3"
#
# x = float(x)
#
# print(x)
# print(int(y))
# print(z)

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("What is your height (in centimeters)?: "))
#
# print("You are "+name + ", you are "+str(age)+ " years old, and your height is " +str(height) +"cm")

# name = input("Imię: ")
# surname = input("Nazwisko: ")
# age = int(input("Wiek: "))
#
# if age >= 18:
#     print("Dzień dobry, dorosły człowieku")
#
# else:
#     print("Do domu gówniaku!!")




# temp = int(input("What is temp outside?: "))
#
# if temp >= 0 and temp <=30:
#     print("The temperature is awesome. Go outside!")
# elif temp < 0:
#     print("Don't go outside! It's freaking cold! Brrr....")
# elif temp > 30 and temp <= 50:
#     print("You're gonna melt. Let's swim in our pool, shall we?")
# else:
#     print("Don't....go....please. You're gonna die, brah")

# name = None
#
#
# while not name:
#     name = input("What is your name?: ")
#
# print("Hi, "+name)

# import time
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New York!")


# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

#
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

#food = ["pizza", "sushi", "penaut butter", "fries"]

#food.pop()
#food.insert(0, "lasagne")
#for x in food:
#    print(x)




# 2D lists

# drinks = ["coffee", "tea","soda"]
# dinner = ["pizza", "hamburger", "hotdog"]
# desserts = ["icecream","apple"]
#
# food = [drinks,dinner,desserts]
#
# print(food[1][2])


## Tuple

# student = ("Peter",31,"male")
#
# print(student.count("Peter"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Peter" in student:
#     print("Jest obecny!")



## SET

# utensils = {"Fork","Spoon","Knife"}
# kitchen = {"Knife","Sink","Table"}
#

# utensils.add("napkin")


## DICTIONARY

# capitals = {'USA':'Washington DC',
#             'India':'New Delhi',
#             'Russia':'Moscow',
#             'Poland':'Warsaw'}
#
# capitals.update({'Germany':'Berlin'})
# capitals.pop('Russia')
#
# # print(capitals['Russia'])
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())
#
# for key, value in capitals.items():
#     print(key, value)


## INDEX operator [] = gives acces to a sequence's element (str,list,tuplets)

# name = "Piotr Oko?"
# if(name[0].isupper()):
#     name = name.casefold()
#
# first_name = name[:5].upper()
# last_name = name[6:].lower()
# last_char = name[-2]
#
# print(first_name)
# print(last_name)
# print(last_char)


## FUNCTIONS = a block of code which is executed only when its called
#
# def hello(first_name, last_name, age):
#     print("Hello " +first_name+" "+last_name+". You are "+str(age)+" year(s) old.")
#     print("Have a nice day")
#
#
# hello("Oko", "Krzyżanowskie", 32)


## RETURN STATEMENT = function sen python values/objects back to the caller.
# These values/obj are known as the function's return value

# def multiply(num1,num2):
#     return num1 * num2
#
# x = multiply(9,865645)
# print(x)


## KEYWORD ARGUMENTS =  arguments preceded by an identifier when we pass them to a function
##                      the order pf the arguments doesn't matter, unlike positional arguments
##                        Python knows the names of the arguments that our function receives

# def hello(first, middle, last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello(last="Oko", first="Kamiś", middle="Hehe")


## NESTED FUNCTION CALLS = function calls inside other function calls
# innermost function calls are resolved first
# returned value is used as argument for the next outer function
#
# print(round(abs(float(input("Enter a whole, positive number: ")))))

### SCOPE - The region that a variable is recognized
# A variable is only available from inside the region it is created
# A global and locally scoped versions of a variable can be created

# name = "Piotr" #global
#
# def display_name():
#     name = "Oko" #local
#     print(name)
#
# display_name()
# print(name)


## ARGS = parameter that will pach all arguments into a tuple

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff) #casting arguments as a list
#     stuff[0] = 2220
#     for i in stuff:
#         sum+= i
#     return sum
#
# print(add(1,2,3,4,5,6))


## KWARGS = parameter that will pach all arguments into a dictionary

# def hello(**kwargs):
#     #print("Hello "+kwargs['first']+" "+ kwargs['last'])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
# hello(title="Mr",first="Oko",middle="Penomoe",last="Krzyżanowskie")

## STR.FORMAT() =  optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"
#
# #print("The "+animal+" jumped over the "+item)
# # print("The {} jumped over the {}".format(animal, item))
# # print("The {0} jumped over the {0}".format(animal, item))
# # print("The {} jumped over the {}".format(animal="cow", item="moon")) # positional argument
# #print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal,item))
#
# name = "Oko"
#
# print("Hello. My name is {}. Nice to meet you".format(name))
# print("Hello. My name is {:10}. Nice to meet you".format(name))
# print("Hello. My name is {:>10}. Nice to meet you".format(name))
# print("Hello. My name is {:<10}. Nice to meet you".format(name))
# print("Hello. My name is {:^10}. Nice to meet you".format(name))
#
#
# number = 1000002200
# print("The number pi is {:.8f}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:x}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:E}".format(number))


## RANDOM

# import random
# x = random.randint(1,6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#
# random.shuffle(cards)
# print(cards)


## EXCEPTION - events detected during execution that interrupt the flow of a program

#
# try:
#
#     num = int(input("Enter a number to divide: "))
#     denom = int(input("Enter a number to divide by: "))
#     result = num / denom
#
# except ZeroDivisionError as e:
#     print(e)
#     print("You cannot divide be zero you moron")
#
# except ValueError as e:
#     print(e)
#     print("Enter only numbers please")
# # except Exception as e:
# #     print("Something went wrong")
#
# else:
#     print(result)
#
# finally:
#     print("This will always execute")


## FILE DETECTION

import os

# path = "C:\\Users\\Oko\\Desktop\\folder"

# if os.path.exists(path):
#     print("Yes")
#     if os.path.isfile(path):
#         print("That is a file")
# else:
#     print("No...:(")

# if os.path.exists(path):
#     print("Yes")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("No...:(")


## FILES IN PYTHON

# try:
#
#     with open('C:\\Users\\Oko\\Desktop\\text.tx') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Missing file I guess...")


### WRITING FILES

# text = "Have a good day"
# with open('C:\\Users\\Oko\\Desktop\\test.txt','a') as file:
#     file.write(text)


### COPYING FILES
# copyfile()    -copies content of a file
# copy()        -copyfile() + permission mode + destination can be a directory
# copy2()       -copy() + copies metadata (file's creation and modification times)

# import shutil
#
# shutil.copyfile('text.txt','copytext.txt')


# import os
#
# source = "movingfiles.txt"
# destination = "C:\\Users\\Oko\\Desktop\\movedFile.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source+ " file was moved")
# except FileNotFoundError:
#     print("File missing")


## DELETING FILES
#
# import os
# import shutil
#
# path = "empty"
# try:
#     # os.remove(path)
#     # os.rmdir(path)
#     #####shutil.rmtree(path) - DANGEROUS!!!
#
# except FileNotFoundError:
#     print("Missing file")
# except PermissionError:
#     print("DENIED!")
# except OSError:
#     print("You cannot delete it using this function")
# else:
#     print(path+" was deleted")
# finally:
#     print("You're doing great job!")


## MODULES - a file containing python code. May contain functions, classes, etc.
#             Used with modular programming, which is to separate a program into parts

# import messages as msg
#
# msg.hello()
# msg.bye()


## ROCK,PAPER,SCISSORS GAME

# import random
#
# while True:
#     choices = ['rock','paper','scissors']
#
#     computer = random.choice(choices)
#
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper or scissors: ").lower()
#
#     if player == computer:
#         print("Computer: ",computer)
#         print("Player: ",player)
#         print("Tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#
#     elif player == "paper":
#         if computer == "scissors":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#
#     elif player == "scissors":
#         if computer == "rock":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#
#     play_again = input("Play again? (Y/N): ").lower()
#
#     if play_again != "y":
#         break
# print("Bye!")


### QUIZ

#
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("---------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
#     display_score(correct_guesses, guesses)
# #---------------------------
# def check_answer(answer, guess):
#     if answer == guess:
#         print("CORRECT!!")
#         return 1
#     else:
#         print("WRONG!!")
#         return 0
# #---------------------------
# def display_score(correct_guesses, guesses):
#     print("---------------------------")
#     print("RESULTS")
#     print("---------------------------")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end="")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end="")
#     print()
#
#     score = (correct_guesses/len(questions))*100
#     print("Your score is: " +str(score)+"%")
# #---------------------------
# def play_again():
#     response = input("Play again(Y/N)?: ")
#     response = response.upper()
#
#     if response == "Y":
#         return True
#     else:
#         return False
# #---------------------------
#
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Phyton created: ": "B",
#     "Which group?: ": "C",
#     "Is Moon emiting light?: ": "D"
# }
#
# options = [['A. Guido von Rossum','B. Kamisia','C. Elon Musk','D. Mój stary'],
#            ['A. 1969','B. 1991','C. 1987','D. 2024'],
#            ['A. Lonley Island','B. Smosh','C. Monty Phyton','D. Polska reprezentacja'],
#            ['A. Yes','B. What?','C. Moon?','D. No...idiot']]
#
# new_game()
# while play_again():
#     new_game()
#
# print("Bye bye")

### OBJECT ORIENTED PROGRAMMING

# from car import Car
#
# car_1 = Car('Mercedes','B180', 2008, "Niebieski")
# car_2 = Car('Ford','Mustang','2022','black')
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
#
# car_2.drive()
# car_1.stop()


### CLASS vs INSTANCE VARIABLES


# from car import Car
#
# car_1 = Car('Mercedes','B180', 2008, "Niebieski")
# car_2 = Car('Ford','Mustang','2022','black')
#
# Car.wheels = 3
#
# print(Car.wheels)

### ANIMALS - 3:48:55

# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating.")
#
#     def sleep(self):
#         print("This animal is sleeping.")
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# rabbit.run()
# fish.swim()
# hawk.fly()


### multi-level inheritance = when a derived (child) class inherits another derived (child) class

# class Organism:
#
#     alive = True
#
# class Animals(Organism):
#
#     def eyes(self):
#         print("This animal has eyes")
#
# class Rabbit(Animals):
#
#     def run(self):
#         print("This rabbit can run")
#
# rabbit = Rabbit()
#
# rabbit.eyes()


### MULTIPLE INHERITANCE - child is derived from more than one parent

#
# class Prey:
#
#     def flee(self):
#         print("Animal is fleeing")
#
# class Predator:
#
#     def hunt(self):
#         print("Animal is hunting")
#
# class Hippo(Prey, Predator):
#     def fat(self):
#         print("This Hippo is fat")
#
# hippo = Hippo()
#
# hippo.flee()
# hippo.hunt()


### METHOD OVERWRITING
#
# class Animal:
#
#     def eat(self):
#         print("This animal is eating")
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
# rabbit = Rabbit()
# rabbit.eat()


### METHOD CHAINING - calling multiplemethods sequentially. Each call performs an action on the same object and returns self

# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def turn_off(self):
#         print("You stopped the engine")
#         return self
#     def drive(self):
#         print("You are driving a car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
# car = Car()
#
# (car.turn_on()
#  .drive()
#  .brake()
#  .turn_off())


### SUPER() - Function used to give access to the methods of a parent class
#             Returns a temporary object of a parent class when used

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(6,3)
# cube = Cube(3,56,3)
# print(square.area())
# print(cube.volume())


### ABSTRACT CLASSES = a class which contains one or more abstract methods
### ABSTRACT METHOD = a method that has a declaration but oes not have an implementation
#
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive a car")
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You drive a motorcycle")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# vehicle.go()
# car.go()
# motorcycle.go()


### PASSING OBJECTS AS ARGUMENTS

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
# def change_color(car, color):
#     car.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
# bike_2 = Motorcycle()
# bike_3 = Motorcycle()
#
# change_color(car_1, "red")
# change_color(car_2, "yellow")
# change_color(car_3, "green")
#
# change_color(bike_1, "black")
# change_color(bike_2, "blue")
# change_color(bike_3, "white")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)
# print(bike_2.color)
# print(bike_3.color)

### Duck typing - concept where the class ofan object is less important than the methods/attributes
                    # class type is not checked if minimum methods/attributes are present
                    # "If it walks like a duck, and it quacks like a duck, then it must be a duck"

#
# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is quacking")
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught it!")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)


### WALRUS OPERATOR :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy = True) - wrong
# print(happy := True) # correct

# old way
# foods = list()
# while True:
#     food = input("What food do you like?: ").lower()
#     if food == "quit":
#         break
#
#     foods.append(food)
## with walrus
# foods = list()
# while food := input("What food do you like?: ").lower() != "quit":
#     foods.append(food)


### 4:31:50






























































































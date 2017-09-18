#!/usr/bin/python3

print("Hello, World")

name = raw_input(" Enter your name: ")

print("Hi ", name)

age = input('Enter your age: ')
age = int(age)

if (age==35):
    print("you are the same age as me")
else:
    print("you are different age than me")

print (type(age))  # <type 'int'>



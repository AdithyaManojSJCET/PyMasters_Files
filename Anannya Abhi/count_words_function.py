'''
Name: Anannya Abhi
Date: 5.12.24
Python program to define a function that count words in a sentence
'''
def count_words():
    value=input("Enter a sentence: ")
    words=value.split()
    count=0
    for i in words:
        count=count+1
    print(f"Count of words in the sentence is: {count}")
count_words()
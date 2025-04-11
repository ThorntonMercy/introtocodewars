#1 Even or Odd (using a ternary operator to condense the code)
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd" 

#otherwise the code would/could be: 
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#2 Convert Integer to String 
def number_to_string(num):
    return str(num)

#3 Return the number of vowels in a given string
def get_count(sentence):
    vowels = "aeiouAEIOU" #all of the vowels capitalized and lowercase minus yY
    count = 0  #start with 0 count
    for char in sentence: 
        if char in vowels:
            count += 1 #add one count per vowel found
    return count
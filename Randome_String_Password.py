#String Constants -

#Below is the list of string constants you can use to get a different set of characters as a
#source for creating a random string.

#ascii_lowercase  - Contain all lowercase letters
#ascii_uppercase  - Contain all uppercase letters
#ascii_letters	  - Contain both lowercase and uppercase letters
#digits	          - Contain digits ‘0123456789’.
#punctuation      - All special symbols - !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
#whitespace	      - Includes the characters space, tab, linefeed, return, formfeed, and vertical
#                   tab [^ \t\n\x0b\r\f]
#printable	      - characters that are considered printable. This is a combination of constants
#                   digits, letters, punctuation, and whitespace.

#How to create a random string
#1. Import string and random module
#2. Use the string constant ascii_lowercase
#3. Decide the length of a string
#4. Use a for loop and random choice() function to choose characters from a source
#5. Generate a random Password


#Ex - generate a random string of any length
import random
import string
'''
def str(length):
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result)

str(8)
str(9)


#Randome string of lower case and upper case individually
def strlower(length):
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of lower length", length, "is:", result)

strlower(8)


def strlower(length):
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of upper length", length, "is:", result)

strlower(8)


#Randome string withour repeating char
#Choice method can repeate the char so if you want char without repeat then use sample method
letters = string.ascii_letters
result = ''.join(random.sample(letters,8))

print(result)

'''
#Create Random Password with Special characters, letters, and digits
#A password that contains a combination of characters, digits, and special symbols is
#considered a strong password.

#Combine the following three constants and use them as a data source for the random.choice()
#function to select random characters from it.
#1. string.ascii_letters: To include letters from a-z and A-Z
#2. string.digits: To include digits from 1 to 10
#3. string.punctuation: to get special symbols

#or we can also Use the string.printable constant and choice() function. The string.printable
# contains a combination of digits, ascii_letters (lowercase and uppercase letters), punctuation,
# and whitespace.

#ex

character = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(character) for i in range(8))

print(password)

#or with string.printable
passwrd = ''.join(random.choice(string.printable) for i in range(8))
print(passwrd)

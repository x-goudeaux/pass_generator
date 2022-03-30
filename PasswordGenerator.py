import random 
import string

#password requires at least 1 uppercase letter and 1 special symbol
#string.ascii_letters
#string.digits
#string.punctuation

def generate_password(length):
        password = []  #using a list allows us to shuffle the characters around for a more random password
        if length < 8:
            for i in range(length):
                password.append(chr(random.randint(33, 125))) #generates a random asii character 
        
            random.shuffle(password)
            result = "".join(password) 

            return result
        else:

            password.append(random.choice(string.ascii_uppercase)) #strong passwords usually have an uppercase, special character, and a mix of numbers
            password.append(random.choice(string.punctuation))
            password.append(random.choice(string.digits))
            password.append(random.choice(string.digits))

            for i in range(length - 4):
                password.append(chr(random.randint(33, 125))) #random.randint(a , b + 1)
        
            random.shuffle(password)
            result = "".join(password) 

            return result



input = int(input("Enter password length (Strong passwords are at least 8 characters long): "))
print("Password: " + generate_password(input))


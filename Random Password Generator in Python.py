#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 5:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for password length.")


# In[ ]:





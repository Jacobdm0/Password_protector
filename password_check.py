import csv
import random
import math
def file_read(filename):
    """
    A function that reads a file and returns a list of its content.
    Parameters:
        filename (str): The name of the file to be read.
    Return:
        list: A list containing the content of the file.
    """
    try:
        data = open(filename, 'r')
        pass_list = list(csv.reader(data))
        return pass_list
        data.close()
    except FileNotFoundError:
        print("Error! file not found")
        exit()
def pass_gen():
    alpha_list = ['a','A', 'b', 'B', 'c','C', 'd','D', 'e','E', 'f','F', 'G', 'g', 'h', 'H', 'i', 'I', 'j','J', 'k','K', 'L','l', 'm', 'M', 'n','N', 'o','O', 'p', 'P','q', 'Q','r','R', 's', 'S','t', 'T','u', 'U','v', 'V','w','W', 'x', 'X','y', 'Y','z','Z']
    pass_len = int(input('How long would you like a new password to be? '))
    pass_num = int(input('How many numbers would you like to include? '))
    pass_char = pass_len - pass_num
    pass_str =''
    for i in range(1, pass_num+1):
        num = str(random.randint(0, 9))
        pass_str = pass_str + num
    for i in range(1, pass_char+1):
        alpha = random.choice(alpha_list)
        length = len(pass_str)
        alpha_index = random.randint(1, length)
        pass_str = pass_str[:alpha_index] + alpha + pass_str[alpha_index:]
    return pass_str
    

def sub_list(fun_list, user_value):
    """
    Generate a sorted list of words from a given list of words based on the first character of the user input.

    Parameters:
        fun_list (list): An array of words.
        user_value (str): The user input.

    Returns:
        list: A sorted list of words.

    Raises:
        AssertionError: If the first character of the user input is not alphanumeric.
    """
    check_list = []
    first_chr = user_value[0].lower()
    assert first_chr.isalnum(), "Error! Only letters and numbers"
    index = 0
    test = fun_list[index][0]
    while first_chr != test:
        test = fun_list[index][0]
        index += 1
    if first_chr == test:
        if index == 0:
            check_list = fun_list[index]
        else:
            check_list = fun_list[index-1]
    check_list.pop(0)
    check_list.sort()
    return check_list  

def clean(fun_list):
    """
    Remove empty strings from the input list and return the cleaned list.
    """
    list_length = len(fun_list)
    fun_list.sort()
    i = 0
    while i < list_length:
        if fun_list[i] == '':
            fun_list.pop(i)
            list_length = len(fun_list)
        elif fun_list[i] != '':
            break
    return fun_list 
     
def pass_check(check_list, user_value):
    """
    Check if a given password is found in a list of common passwords.

    Args:
        check_list (list): A list of common passwords.
        user_value (str): The password to be checked.

    Returns:
        bool: True if the password is found in the list, False otherwise.

    This function performs a binary search to check if a given password is found in a list of common passwords. 
    """
    #check_list = ['abc', 'abc123', 'abc12345', 'asdf1234', 'asdfghjkl', 'asdfghjkl12345', 'awdrgyj'] # testing only
    value_found = False
    x = 0
    start = 0
    end = len(check_list) - 1 
    while end >= 0:   
        middle_list = math.floor((end+start)/2)
        check_value = check_list[middle_list]
        if x < len(check_list): # Makes sure that it can't get stuck in an infinite loop
            if user_value.lower() < check_value.lower():
                x = x + 1
                end = middle_list + 1
            elif user_value.lower() > check_value.lower():
                x = x + 1
                start = middle_list - 1
            elif user_value.lower() == check_value.lower():
                x += 1
                value_found = True
                end = -1
        elif x >= len(check_list): # Checks the first index, which is missed in the other loops
            if user_value.lower() == check_list[0].lower():
                value_found = True
            end = -1
    if value_found==False:
        print(f'Your password has not been found as a common password.')
        print('You can still change your password if you want to.')
        return value_found
    elif value_found==True:
        print('Your password has been found as a common password.') 
        print('It is suggested that you change your password.')
        return value_found

def changer():

    user_pass = input("Please enter a password that you have used previously: ")
    if user_pass != '':
        csv_list = file_read("password_list.csv") #opens the file
        smaller_list = sub_list(csv_list, user_pass) #pulls a smaller list to check through 
        clean_list = clean(smaller_list)
        is_common = pass_check(clean_list, user_pass) # searches the password list to see 
        if is_common:
            print()
        else:
            print('Your password has not been found as a common password.')
            print()
        change = input('Would you like to change your password? y/n: ')
        if change.lower() == 'y':
            new_pass = pass_gen()   
            print(f'Your new password is: {new_pass}')
    
    else:
        print('You Must enter a password.')

def hasher():
    user_hash = str(input('Please enter the Hash: '))
    

def main():
    if int(input('use')) == 1:
        changer()
    elif int(input('use')) == 2:
        hasher()

if __name__ == "__main__":
    main()
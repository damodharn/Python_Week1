# *********************************************************************************************
# Purpose: Program to Input name from user and Replace String Template.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
while 1:
    name = input("plz Enter User Name:")
    if len(name) > 2:
        print("Hello", name, "How are you ?")
        break
    else:
        print("Please Enter at least 3 Characters")

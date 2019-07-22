# *********************************************************************************************
# Purpose: Program to Input name from user and Replace String Template.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
name = input("plz Enter User Name:")
if len(name) > 2:
    print("Hello", name, "How are you ?")
else:
    print("Please Enter atleast 3 Characters")

"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

#asking if you need to add anything to the list
z= input("what do you need to buy, type exit if you are not adding to the list")


#loop for adding things to the list
shopping_list = []
while z !="exit":
    shopping_list.append(z)
    z=input("what do you need to buy, press exit if you are done?")


#shows what is in the shopping list
print(shopping_list)


#asking if you need to remove anything from the list
x=input("what do you need to remove, if you are not removing anything type exit")


#loop for removing items from the shopping list
while x !="exit":
    shopping_list.remove(x)
    x=input("what do you need to remove, press exit if you are done?")


#shows whats left in your list
print(shopping_list)


#command that allows user to check list anytime
print("whenever you want to check the list type print(shopping_list)")



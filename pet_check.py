# For example, the following program lets the user type in a pet name and then checks to see whether the name is in a list of pets.

def pet_check():
    cat_list = ['Joey', 'Fluffy', 'Poodle', 'Bingo']
    cat_list_lower = [x.lower() for x in cat_list]
    user_cat = input('Which cat are you looking for?').lower()
    print(user_cat)
    if user_cat in cat_list_lower:
        print(f"Your cat {user_cat} is in my pet shop!")
    else:
        print(f"Sorry - {user_cat} is not here.")
        

pet_check()


# If you type # %% in your Visual Studio Code editor while editing a .py file, then an interactive cell is created and it can be evaluated.
# The nice part of this is that # denotes a comment in a .py file, so you can save and run your code as a script.

#%%
1+1
# %%

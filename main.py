# Setup
import json

with open('data.json','r') as f:
    data = json.loads(f.read())

# Input

def get_subcategories(category,data):
    prompt = data[category]['strings']['first_prompt'].format(parent_keys = ", ".join((value_list)))
    user_input = input(prompt)
    if user_input in data[category]["data"].keys(): #is a cuisine key :
        pass#do something
    elif user_input in data[category]["data"].values():
        pass#do something
    else:
        #do something
        pass

# Transform

# Output


# ----- Main ----
def main():
    is_category = False
    while not is_category:
        user_input = input("Enter a category: \n") #prompt for category
        if user_input in data: # Is Category?
            # get top - level category
            #get_subcategories(user_input,data)
            is_category = True
            print("True!")
        else:
            print("Category not found, please try again.")


main()

if __name__ == "__main__":
    import doctest

    doctest.testmod()

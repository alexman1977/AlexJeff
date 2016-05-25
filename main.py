# Setup
import json

with open('data.json','r') as f:
    data = json.loads(f.read())

# Input

def get_subcategories(category,data):
    user_input = input(build_first_prompt(category))
    if user_input in data[category]["data"].keys() #is a cuisine key :
        pass#do something
    elif user_input in data[category]["data"].values():
        pass#do something
    else:
        #do something
        pass

def get_category(data):
    while False:
        user_input = input("Enter a category: \n") #prompt for category
        if user_input in dictionary: # Is Category?
            # get top - level category
            get_subcategories(user_input,data)
            print("True!")
        else:
            print("Category not found, please try again.")

def build_first_prompt(category):
    value_list = list(data[category]["data"].keys())
    value_list.sort()

    return data[category]['strings']['first_prompt'].format(parent_keys = ", ".join((value_list)))


# Transform

# Output


# ----- Main ----
def main():
    get_category(data)


main('data.json')

if __name__ == "__main__":
    import doctest

    doctest.testmod()

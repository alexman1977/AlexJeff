# Setup
import json

# Input

def get_subcategories(category,data):
    user_input = input(data[category]['strings']['first_prompt'].format(parent_keys = ", ".join(list(data[category]["data"].keys()))))
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

# Transform
def json_to_dict(file_name):
    with open(file_name,'r') as f:
        json_data = json.loads(f.read())
        return json_data


# Output


# ----- Main ----
def main(data):
    dictionary = json_to_dict(data)
    get_category(data)


main('data.json')

if __name__ == "__main__":
    import doctest

    doctest.testmod()

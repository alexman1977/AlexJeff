# Setup
import json

with open('data.json','r') as f:
    data = json.loads(f.read())

# Input

def start_again():
    answer=input("Would you like to start again?")
    if answer == 'Yes':
        main()
    else:
        pass


def user_results(input, ingredient = True):
    #input can either be ingredient or dish

    if ingredient == True:
        # Found in dishes
        pass
    else:
        # Return ingredients in dish
        pass


    # Prints Outputs

def get_subcategories(category):
    # Building a Prompt
    value_list = list(data[category]["data"].keys()) # [Thai, Indian, Italian, Mexican]
    value_list.sort() # [Italian, Indian, Mexican, Thai]
    strings = data[category]['strings']
    prompt = strings['first_prompt'].format(parent_keys = ", ".join(value_list))

    #please enter a cuisine or ingredient

    # Input
    user_input = input(prompt)
    if user_input in data[category]["data"].keys(): # Is a subcategory ex Thai
        # Build Second Prompt
        subcategory = user_input
        child_key_list = list(data[category]["data"][subcategory].keys())
        child_key_list.sort()
        child_key_list_formatted = ", ".join(child_key_list)
        second_prompt = strings['second_prompt'].format(child_keys = child_key_list_formatted)
        response = input(second_prompt)
        # return two_inputs_output
        if response in child_key_list:
            #return ingredient/two input outputs
            print(strings[two_inputs_output])
            start_again()
        else:
            #repeat  prompt
            pass



    elif user_input in data[category]["data"].values():
        # Search List Items example ingredient
        # return one input output
        pass
    else: # If not cuisine or dish
        print("Sorry, {user_input} was not found, please try again.".format(user_input = user_input))
        get_subcategories(category)


# Transform

# Output

# ----- Main ----
def main():
    is_category = False
    while not is_category:
        user_input = input("Enter a category: \n") #prompt for category
        if user_input in data: # Is Category?
            # get top - level category
            get_subcategories(user_input)
            is_category = True
        else:
            print("Category not found, please try again.")


main()

if __name__ == "__main__":
    import doctest

    doctest.testmod()

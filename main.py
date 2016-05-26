# Setup
import json

with open('data.json','r') as f:
    data = json.loads(f.read())

# Input

def start_again():
    answer=input("Would you like to start again? (y/n)")
    if answer == 'Yes' or answer == 'y':
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
    item_list = []
    for cuisine in data[category]["data"]:
        for dish in data[category]["data"][cuisine]:
            item_list = item_list + data[category]["data"][cuisine][dish]

    ## Case 1 is top level key
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

            # for i in child_key_list[response]:
            #     print(i)

            list_of_ingredients = data[category]["data"][subcategory][response]
            ingredients_string = "\n• ".join(list_of_ingredients)


            print(strings['two_inputs_output'].format(parent_key = user_input, child_key = response, items = ingredients_string))


            start_again()
        else:
            #repeat  prompt
            print ("Please enter another item")
            get_subcategories(category)


    ## Case 2 is list item
    elif user_input in item_list:
        # Search List Items example ingredient
        list_of_child_keys = []
        # return one input output
        for cuisine in data[category]["data"]:
            for dish in data[category]["data"][cuisine]:
                if user_input in data[category]["data"][cuisine][dish]:
                    list_of_child_keys.append((cuisine,dish))

        for tuple_item in list_of_child_keys:
            print(strings["one_input_output"].format(list_item = user_input, parent_key = tuple_item[0], child_key = tuple_item[1]))

    ## Case 3 is not list item or top level key
    elif user_input is "":
        start_again()
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
        elif user_input == "":
            break
        else:
            print("Category not found, please try again.")

        #allow exit of the loop for user


main()

if __name__ == "__main__":
    import doctest

    doctest.testmod()

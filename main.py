import json


def user_name(dataset):
    f = open(dataset, 'r')
    contents = f.read()
    variable_1 = json.load(contents)
 #   user_question = input("What are you interested in??" )
    print (variable_1)

user_name('data1.json')



   
 

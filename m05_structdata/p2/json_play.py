"""
Your task today is to "play" using data in the JSON file format

NOTE: once you open a JSON file in PyCharm, you can format in a pretty and readable fly using Ctrl+Alt+L

A couple of interesting tutorials about JSON in Python:
https://www.programiz.com/python-programming/json  (very minimal tutorial)
https://realpython.com/python-json/  (you can stop at encoding/decoding custom types, it may get complicated from there...)

"""

import json

def create_user_info_todo_list(todo_file, output_file_name):
    """
    This function reads the content of of a json file todo_file
    (an example is provided: todos.json)
    and returns a JSON
    object with information about users in the form:
    [{
        "userId": 1,
        "number": 24,
        "completed": 12,
        "incomplete": 12
     }
     {
        "userId": 2,
        ...
     }
    ...]

    As you can see, for each user, the total number of todos,
    number of completed todos, and number of incomplete todos
    are recorded

    Before returning, the function also dumps the created JSON object
    onto a file "output_file_name".json
    """


    f = open(todo_file)
    s = json.load(f)
    f.close()

    data = {}
    data['user-info'] = []
    user = {
        'userId': 1,
        'number': 0,
        'completed': 0,
        'incomplete': 0
    }
    data['user-info'].append(user)

    for todo in s:
        last = data['user-info'][-1]
        if todo['userId'] == last['userId']:
            last['number'] += 1
            if (todo['completed']):
                last['completed'] += 1
            else:
                last['incomplete'] += 1
        else:
            newUser = {
                'userId': todo['userId'],
                'number': 1,
                'completed': 0,
                'incomplete': 0
            }
            if (todo['completed']):
                newUser['completed'] += 1
            else:
                newUser['incomplete'] += 1
            data['user-info'].append(newUser)
    
    with open(output_file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def count_busy_users(todo_file, num):
    """

    This function reads the content of a JSON file todo_file
    and counts the number
    of users with a number of incomplete todos equal to or greater than num

    Note: it may be convenient to use the output of the function
    create_user_info_todo_list to speed up the implementation of
    this function
    """
    f = open(todo_file)
    s = json.load(f)
    f.close()

    thelist = s['user-info']
    totalBusy = 0
    for i in thelist:
        if i['completed'] <= i['incomplete']:
            totalBusy += 1
    return totalBusy


def create_user_info_blogs(blogs_file, output_file_name):
    """
    This function reads the content of a JSON file blogs_file
    (an example blogs.json is provided) and returns a JSON object
    recording =, for each users, the total number of words
    of their posts (i.e., the sum of all the number of words of all
    the posts that a user has made) and the number of posts:
    [{
        "userId": 1,
        "number_of_posts": 7,
        "words": 453,

     }
     {
        "userId": 2,
        ...
     }
    ...]

    Before returning, this function also dumps the content of the
    created JSON object in the file named "output_file_name".json
    """
    f = open(blogs_file)
    s = json.load(f)
    f.close()

    data = {}
    data['blogs'] = []
    user = {
        'userId': 1,
        'number_of_posts': 0,
        'words': 0,
    }
    data['blogs'].append(user)

    for post in s:
        last = data['blogs'][-1]
        if post['userId'] == last['userId']:
            last['number_of_posts'] += 1
            last['words'] += _number_of_words(post['body'])            
        else:
            new = {
                'userId': post['userId'],
                'number_of_posts': 1,
                'words': _number_of_words(post['body'])
            }
            data['blogs'].append(new)
    
    with open(output_file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)



def _number_of_words(s):  # simple function to calculate number of words in post
    s_split = s.split(" ")
    return len(s_split)


if __name__ == '__main__':
    create_user_info_todo_list("todos.json", "todos_output.json")

    print("Busy users: {0}".format(count_busy_users("todos_output.json", 10)))  # there should be 6 busy users

    create_user_info_blogs("blogs.json", "blogs_output.json")

fruits = ["Apple", "Pear", "Orange"]

"""We've got some buggy code. Try running the code. The code will crash and
 give you an IndexError. This is because we're looking through the list of fruits 
 for an index that is out of range.
 
 Use what we've learnt about exception handling to prevent the program from crashing.
If the user enters something that is out of range just print a default output of "Fruit pie". e.g.
 """

def make_pie(index):
    try:
        fruit = fruits[index]
        
    except IndexError:
        print("We need a few more fruits")
    else: 
        print(fruit + " pie")

make_pie(3)

"""We've got some buggy code, try running the code. The code will crash 
and give you a KeyError. This is because some of the posts in the
 facebook_posts don't have any "Likes"."""

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
import random
students = ["Emily", "Alex", "Peter", "Alex", "Freddie"]

"""Generates a certain score for every student"""
student_score = {student : random.randint(1,10) for student in students}
"""Filters wich students passed """
passed_students ={student:grades for (student,grades) in student_score.items() if grades >= 5}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
"""Makes a dict that counts how many characters are in a word"""
# sentence_list = list(sentence.split(" "))
letter_count ={word:len(word) for word in sentence.split(" ")}
print(letter_count)




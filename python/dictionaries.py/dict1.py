#A dictionary in Python is a built‑in data structure that stores data as key–value pairs.
#Key → unique identifier (like a word in a real dictionary).
#Value → data associated with that key (like the definition of the word).
'''
student = {

    "name": "vara prasad",
    "age": 11,
    "height":12,
    "addres": {
        "city": "chennai",
        "pin": 60103
    }
}
for key in student:
    print(key,'=',student[key])
print(student)

#accessing values
student = {
    "name": "saran",
    "age": 69,
    "name1": "jaswanth",
    "age2": 21
}
print(student["name"])
print(student["age2"])

#adding more elements
student_details = {
    'jaggu': {
        'father name':'jagan',
        'mother name': 'swetha'
    },
    'arun': 143,
    'reddy': 1094
}
print(student_details)
student_details['reddy'] = 1234
student_details['mubarak']={1120,1081}
student_details['arun']={'bestie':'sanjuu','gf':'sureka'}
student_details['pratap']={'mobile':8688}
print(student_details)
print(student_details['arun']['gf'])
print(student_details.get('reddy'))
del student_details['jaggu']
print(student_details)



#example1
fruits = {
    'banana': 123,
    'apple': 270,
    'pineapple': 180
}
print(fruits)
del fruits['apple']
fruits.update({'orange': 110})
print(fruits)
r = fruits.pop('banana')
print(r)
fruits.popitem()                            #removes last element
print(fruits)
copy_details = fruits.copy()                #used to copy the dictionary
print(copy_details)

#whether an element is there in a dictionaries or not
if 'pineapple' in fruits:
    print(fruits['pineapple'])
if 'salary' not in fruits:
    print("salary")

#ex 2
avengers = {
    'spidey': 1,
    'thor': 2,
    'ironman':3
}
print(len(avengers))

#looping through dictionary
for key in avengers:
    print(key)
for value in avengers.values():
    print(value)
for key,value in avengers.items():
    print(key,value)
#accesing in lits are like 0,1,2. But in dictionaris it is accesing keys to get values.
print(avengers['spidey'])
#keys must be unique but values should can be repeated. 
# and if a key is repeated,the last repeated key value is given assingned to the key
social = {
    'insta':'good',
    'twitter':'great',
    'youtube':'excellent',
    'insta':'okayish',
    'linkedin': 'great'
}
print(social)
print(social['insta'])
#Operation	Average
#Access	      O(1)
#Insert	      O(1)
#Update	      O(1)
#Delete	      O(1)
#Search key   O(1)

#dictionaries + string
college = "sathyabamauniii"
one = dict()
for i in college:
    if i in one:
        one[i]+=1
    else:
        
        one[i] = 1
print(one)


college = "sathyabama"
one = {}
for i in college:
    one[i] = one.get(i,0)+1
print(one)
'''


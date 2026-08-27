#dictionary + list
name = {
    'd':[1,22,3,4],
    'e':[2,5,6]
}
print(name)
print(name['d'])
print(name['d'][0])

#list of  dictionaries
students = [
    {"name": "Rahul", "age": 20},
    {"name": "Arun", "age": 21},
    {"name": "Kiran", "age": 19}
]
print(students[0]['name'])

#nested dictionaries
students = {
    "Rahul": {
        "age": 20,
        "marks": 90
    },
    "Arun": {
        "age": 21,
        "marks": 85
    }
}
print(students['Rahul']['age'])

#dict + sets
students = {
    "Rahul": {"Python", "SQL", "HTML"},
    "Arun": {"Python", "Java"}
}
print(students['Rahul'])

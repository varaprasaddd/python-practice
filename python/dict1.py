#A dictionary in Python is a built‑in data structure that stores data as key–value pairs.
#Key → unique identifier (like a word in a real dictionary).
#Value → data associated with that key (like the definition of the word).

student = {

    "name": "vara prasad",
    "age": 11,
    "height":12,
    "addres": {
        "city": "chennai",
        "pin": 60103
    }
}
print(student)

#keys must me hashable 
d = {
    "name": "Rahul",
    10: "ten",
    3.14: "pi",
    (1, 2): "tuple"
}

#accessing values
student = {
    "name": "saran",
    "age": 69,
    "name1": "jaswanth",
    "age2": 21
}
print(student["name"])
print(student["age2"])
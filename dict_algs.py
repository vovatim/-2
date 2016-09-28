anton = {
    "name": "anton",
    "age": 39,
    "children": [{
        "name": "artem",
        "age": 15,
    },
        {
        "name": "petja",
        "age": 10,
    }
    ],
}
polina = {
    "name": "polina",
    "age": 38,
    "children": [{
        "name": "daria",
        "age": 19,
    },
    {
        "name": "sacha",
        "age": 25 ,
    }
    ],
}

emps = [anton, polina]

for el in emps:
    for el1 in el["children"]:
        if el1['age'] > 18:
            print(el["name"])
            break
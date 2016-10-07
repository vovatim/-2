def children18(masdic):
    mas = []
    for dic in masdic:
        for child in dic['children']:
            if child['age'] > 18:
                mas.append(dic['name'])
                break
    return mas

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
print(children18(emps))

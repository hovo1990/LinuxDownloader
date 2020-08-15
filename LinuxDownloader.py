import yaml

with open('example.yml') as f:
    # data = yaml.load(f, Loader=yaml.FullLoader)
    data = yaml.load(f)
    print(data)

    for doc in data:
        for k, v in doc.items():
            print(k, "->", v)


test = 1
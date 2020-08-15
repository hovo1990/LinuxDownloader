import yaml
import sys
import os

def create_folder(dirName):
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")


with open('example.yml') as f:
    # data = yaml.load(f, Loader=yaml.FullLoader)
    data = yaml.load(f)
    print(data)

    try:
        sub_stuff = data[0]['Folders']
    except Exception as e:
        print('Please follow the official example.yml file')
        sys.exit(0)


    print(sub_stuff)

    for folder in sub_stuff:
        print('Folder is: ', folder)

        folder_to_create = folder['name']
        create_folder(folder_to_create)

        print('----------------------\n')


test = 1
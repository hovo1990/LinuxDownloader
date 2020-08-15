import yaml
import sys
import os
import subprocess

def create_folder(dirName):
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")


def strip_filename(url):
    path = url
    firstpos = path.rfind("/")
    lastpos = len(path)
    filename = path[firstpos + 1:lastpos]
    path = filename
    if 'torrent' in filename:
        firstpos = 0
        lastpos = path.rfind(".torrent")
        filename = path[firstpos:lastpos]
    return filename

test = 'https://pop-iso.sfo2.cdn.digitaloceanspaces.com/20.04/amd64/nvidia/11/pop-os_20.04_amd64_nvidia_11.iso.torrent'
test1 = strip_filename(test)
print(test1)


def download_file_aria2c(url, download_folder):
    # download (using aria2c) files
    afile = ''
    if os.path.exists(afile) and not os.path.exists(afile + '.aria2'):
        print('Skipping already-retrieved file: ' + afile)
    else:
        print('Downloading file: ' + afile)
        subprocess.Popen(["aria2c", "-x", "16", "-s", "20", "-d", "{}".format(download_folder), str(afile)]).wait()


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
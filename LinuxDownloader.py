import argparse
import yaml
import sys
import os
import subprocess
from pathlib import Path


def create_folder(dirName):
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")


def strip_filename(url):
    path = url
    first_pos = path.rfind("/")
    last_pos = len(path)
    filename = path[first_pos + 1:last_pos]
    path = filename
    if 'torrent' in filename:
        first_pos = 0
        last_pos = path.rfind(".torrent")
        filename = path[first_pos:last_pos]
    return filename


def download_file_aria2c(url, download_folder):
    # download (using aria2c) files
    afile = strip_filename(url)
    if os.path.exists(afile) and not os.path.exists(afile + '.aria2'):
        print('Skipping already-retrieved file: ' + afile)
    else:
        print('Downloading file: ' + afile)
        subprocess.Popen(["aria2c", "-x", "16", "-s", "20", "-d", "{}".format(download_folder), str(url)]).wait()


def main(config_file, download_location):
    with open(config_file) as f:
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

            urls = folder['url']

            folder_download = './{}'.format(folder_to_create)
            for url in urls:
                download_file_aria2c(url, folder_download)

            print('----------------------\n')


if __name__ == "__main__":

    path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument("--config_file", help='config file in YAML format to download images')

    parser.add_argument("--directory", help='directory to download images', default=path_to_download_folder)

    args = parser.parse_args()

    # load arguments
    config_file = args.config_file
    directory = args.directory

    main(config_file, directory)

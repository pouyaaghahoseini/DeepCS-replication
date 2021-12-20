# importing required modules
from zipfile import ZipFile
import parser
import os
# specifying the zip file name
DIRECTORY = "/Users/pouya/Documents/Github/deep-code-search/DataCollection/Code-Repoes/"
EXTRACT_PATH = "/Users/pouya/Documents/Github/deep-code-search/DataCollection/Extracted/"
file_paths = []

# crawling through directory and subdirectories
# for root, directories, files in os.walk(DIRECTORY):
#     print(root, directories, files)
#     for file in files:
#         with ZipFile(str(root + file), 'r') as zip:
#             # printing all the contents of the zip file
#             zip.printdir()
#             # extracting all the files
#             print('Extracting all the files now...')
#             zip.extractall(path = EXTRACT_PATH)
#             print('Done!')

for root, directories, files in os.walk(EXTRACT_PATH):
    print(root)
    print(directories)
    print(files)
    print("----------------")
    for file in files:
        if file[-3:] == ".py":
            file_address = root + "/" + str(file)
            parser.extract_features(file_address)
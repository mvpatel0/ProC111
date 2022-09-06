import os
import shutil

from_dir ="C:/Users/Meet/Downloads/Document_Files"
to_dir = "C:/Users/Meet/Desktop/downloadedImage"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
  
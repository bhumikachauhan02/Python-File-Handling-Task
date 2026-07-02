import os
import shutil

def write_file():
    try:
        with open("sample.txt","w") as f:
            f.write("Hello, this is my first file handling task.")
            print("File written successfully")
    except Exception as e:
            print("Error:",e)
write_file()

def read_file():
    try:
        with open("sample.txt","r") as f:
            data= f.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
         print("File not found")
read_file()

def rename_file():
    try:
        if not os.path.exists("renamed_sample.txt"):
            os.rename("sample.txt", "renamed_sample.txt")
            print("File renamed successfully")
        else:
            print("File already exists, skipping rename")
    except FileNotFoundError:
        print("File not found")

os.makedirs("test_folder", exist_ok=True)

def move_file():
    try:
        shutil.move("renamed_sample.txt", "test_folder/renamed_sample.txt")
        print("File moved successfully")
    except FileNotFoundError:
        print("File not found")
move_file()        

def delete_file():
    try:
        os.remove("test_folder/renamed_sample.txt")
        print("File deleted successfully")
    except FileNotFoundError:
        print("File not found")
delete_file()

















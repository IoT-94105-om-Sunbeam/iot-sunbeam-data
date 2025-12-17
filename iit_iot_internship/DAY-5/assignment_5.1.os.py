import os

print("Current Directory:", os.getcwd())
print("Files and folders:", os.listdir())

os.mkdir("demo_folder")
print("Folder created")

print("Folder exists:", os.path.exists("demo_folder"))

os.rename("demo_folder", "new_folder")
print("Folder renamed")

os.rmdir("new_folder")
print("Folder removed")

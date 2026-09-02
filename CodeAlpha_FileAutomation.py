import os
import shutil

print("===================================")
print("      JPG FILE AUTOMATION TOOL")
print("===================================")

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Check if source folder exists
if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    exit()

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created.")

# Find and move JPG files
count = 0

for file in os.listdir(source_folder):

    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")
        count += 1

print("-----------------------------------")
print(f"Total JPG files moved: {count}")
print("File automation completed!")
print("-----------------------------------")
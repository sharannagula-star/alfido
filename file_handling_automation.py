import os
import shutil

try:
    # STEP 1: Create and write data to a text file
    file = open("sample.txt", "w")
    file.write("Name,Age\n")
    file.write("sharan,19\n")
    file.write("harini,20\n")
    file.close()

    print("Text file created successfully.")

    # STEP 2: Read the text file
    file = open("sample.txt", "r")
    print("\nContents of sample.txt:")
    print(file.read())
    file.close()

    # STEP 3: Rename the file
    os.rename("sample.txt", "students.csv")
    print("\nFile renamed to students.csv")

    # STEP 4: Create Backup folder
    if not os.path.exists("Backup"):
        os.mkdir("Backup")

    # STEP 5: Move file to Backup folder
    shutil.move("students.csv", "Backup/students.csv")
    print("File moved to Backup folder")

    # STEP 6: Read CSV file
    file = open("Backup/students.csv", "r")
    print("\nCSV File Content:")
    print(file.read())
    file.close()

    # STEP 7: Delete file
    os.remove("Backup/students.csv")
    print("File deleted successfully")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("\\nProgram Execution Completed.")

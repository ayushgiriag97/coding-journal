#import
import os

#Helper Function
def cleaner(f_path, target_ext):
    files = os.listdir(f_path)
    count = 1
    
    for value in files:
        if value.endswith(f".{target_ext}"):
            if value == f"{count}.{target_ext}":
                count += 1
                continue

            # Construct full absolute/relative paths
            old_path = os.path.join(f_path, value)
            new_path = os.path.join(f_path, f"{count}.{target_ext}")
            
            os.rename(old_path, new_path)
            count += 1
            
    print("Successfully changed the names!")

#Main Execution Block
folder_path = input("Enter your folder path : ")
target_ext = input("Enter file extension to clean (e.g., png, txt, pdf): ").strip(".")
cleaner(folder_path)
import os
import shutil

'''
Delete the Star Citizen user folder
'''

def delete_folder_and_files(folder):
    try:
        shutil.rmtree(folder)
        print("Folder and Files deleted....")
    except PermissionError:
        print("Can't access file")
    except FileNotFoundError:
        print("File Not found!")
        
star_citizen_user_location= "C:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE\\User"

delete_folder_and_files(star_citizen_user_location)

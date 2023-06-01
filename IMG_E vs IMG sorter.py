import os

# Specify the folder path where the pictures are located
folder_path = './pictures/'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Iterate through each file in the folder
for file_name in files:
    # Check if the file has the format IMG_*.png
    if file_name.startswith('IMG_') and file_name.endswith('.JPG'):
        # Extract the number from the file name
        file_number = file_name.split('_')[1].split('.')[0]

        # Check if the corresponding IMG_E file exists
        e_file_name = f'IMG_E{file_number}.JPG'
        e_file_path = os.path.join(folder_path, e_file_name)
        
        if os.path.exists(e_file_path):
            # Delete the file without the E
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            print(f"Deleted file: {file_name}")

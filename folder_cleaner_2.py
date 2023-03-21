# this is an example of what ChatGPT can create 
# This file was created by excecuting the python-chatgpt.py file

import os, shutil, time

# Path of the downloads folder
src_dir = "/Users/rinchinshoysoronov/Downloads"
# Path of the to_delete folder
dst_dir = "/Users/rinchinshoysoronov/to_delete_1"
# Get the current time in seconds
now = time.time()

# Check all the files in the downloads folder
for file in os.listdir(src_dir):
    # Get the path of the file
    file_path = os.path.join(src_dir, file)
    # Get the modification time of the file
    mtime = os.stat(file_path).st_mtime
    # Check if the file is older than 30 days
    if now - mtime > 30 * 86400:
        # Move the file to the to_delete folder
        shutil.move(file_path, dst_dir)

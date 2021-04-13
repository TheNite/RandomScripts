import os

pic_ext = [".jgp", ".jpeg", ".heic", ".png", ".heif", ".gif", ".raw"]
for root, folders, files in os.walk("C:\\"):
    for file in files:
        if os.path.splitext(file)[1] in pic_ext:
            with open("pdf_files.txt", "a") as log_file:
                log_file.write(
                    f"File: {file:<100s} Location: {os.path.abspath(os.path.join(root, file)):<100s}\n"
                )

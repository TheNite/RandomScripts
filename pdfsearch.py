import os

for root, folders, files in os.walk('C:\\'):
    for file in files:
        if file.lower().endswith('.pdf'):
             with open('pdf_files.txt', 'a') as log_file:
                 log_file.write(f'File: {file:<100s} Location: {os.path.abspath(os.path.join(root, file)):<100s}\n')


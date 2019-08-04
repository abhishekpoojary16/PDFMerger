#import libraries
import os
from PyPDF2 import PdfFileMerger

# traverse root directory, and list directories as dirs and files as file
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    
    #print(root) #Absolute path
    
    #check if folder contains PDF files
    if any(file.endswith(".pdf") for file in files):
        print("Merging PDFs in this folder !")
        
        #initiate merging
        merger = PdfFileMerger()
        for file in files:
            if file.endswith(".pdf"):
                merger.append(root + '\\' + file)
                #print(len(path) * '---', file)
        merger.write('Merged_' + os.path.basename(root) + ".pdf")
        merger.close()
        
        #copy the merged file to destination file
        os.rename('Merged_' + os.path.basename(root) + ".pdf", root + '\\' + 'Merged_' + os.path.basename(root) + ".pdf")
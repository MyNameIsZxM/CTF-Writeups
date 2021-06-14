# importing required modules
from zipfile import ZipFile
  
# specifying the zip file name
file_name = "flag.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')

i=999
while i>=1:
    file_lanjut = str(i) + '.zip'
    print(file_lanjut)
    with ZipFile(file_lanjut, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
    
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
    i =i-1    

print(i)
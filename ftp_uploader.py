import os, sys
from ftplib import FTP

ftp = FTP("100.68.128.91")
ftp.login('dikshant','d26092001')
ftp.cwd('/volume(sda5)/Photos')
print(ftp.retrlines('LIST'))


# print(sys.argv[1])
# path = sys.argv[1] #or you can assign the return value of your 
#                    #function (the updated path as per your question) 
#                    #which operates on the file 'new_file'  to this variable. 
# files = os.listdir(path);
# print (files)

# def placeFile():
#     filename=sys.argv[2]
#     file =path+'/'+filename
#     ftp.storbinary('STOR '+filename, open(file, 'rb'))

# placeFile()
# print(ftp.retrlines('LIST'))
# ftp.quit()
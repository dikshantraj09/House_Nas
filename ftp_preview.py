import paramiko
from ftplib import FTP
from PIL import Image
from io import BytesIO

ftp = FTP("100.68.128.91")
ftp.login('dikshant','d26092001')
ftp.cwd('/volume(sda5)/Photos')
print(ftp.retrlines('LIST'))
file_list=ftp.nlst()
print(file_list)

bio =BytesIO()
def handle_binary(more_data):
    bio.write(more_data)
    
def grabFile():

    filename = 'Untitled-3.jpg'
    #localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+filename,callback=handle_binary)
    im= Image.open(bio)
    im.show()
    #ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    #localfile.close()
    ftp.quit()   
grabFile()

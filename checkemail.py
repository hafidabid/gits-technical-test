#HAFID ABI DANISWARA
#SOAL NO 2, DIBUAT DENGAN PYTHON

import re

def cekemail(myemail : str) -> bool:
    split = myemail.split("@") #split email jadi 2 bagian, sebelum dan sesudah @ untuk mempermudah
    if len(split[0])>20:
        #jika bagan sebelum @ lebih dari 20 karakter maka lemparkan false
        return False
    
    if re.match("([\w]+)[@]([a-zA-Z0-9]+)(.co.id|.id)",myemail):
        #pencocokan dengan regex
        return True
    
    return False

if __name__=='__main__':
    emailku = input("masukkan email anda : ")
    if cekemail(emailku):
        print("email sesuai dengan format")
    else:
        print("MAAF EMAIL TIDAK SESUAI DENGAN FORMAT")
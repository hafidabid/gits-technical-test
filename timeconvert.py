#HAFID ABI DANISWARA
#SOAL NO 3, DIBUAT DENGAN PYTHON

import re

def convert_date1(date : str):
    #Konversi waktu 12H -> 24H

    #melakukan regex terlebih dahulu untuk cek format
    if re.match('(([0][0-9]|[1][0-2])[:])([0-5][0-9][:])([0-5][0-9])([ AM]|[ PM])', date):
        waktu = date.split(' ') #membagi berdasar spasi untuk mempermudah
        break_date = waktu[0].split(':') #memecah waktu[0] berdasar : untuk mempermudah
        jam = int(break_date[0]) 
        menit = int(break_date[1])
        detik = int(break_date[2])
        sum_second = jam*3600 + menit*60 + detik #ubah kedetik terlebih dahulu
        menit = sum_second//60

        #jika detik >0 maka bulatkan menit keatas
        if sum_second%60!=0:
            menit +=1

        #ubah lagi ke dalam jam dan menit
        jam = menit//60
        menit -= jam*60
        
        #untuk menangani kasus khusus 12 seperti pada contoh
        if jam == 12:
            if "AM" in waktu[1]:
                jam = 0
        else:
            if "PM" in waktu[1]:
                jam += 12
        
        #assersi untuk memastikan program benar dan output tidak melanggar aturan waktu
        assert jam>=0 and jam<24
        assert menit>=0 and menit<60

        if jam<10:
            jam = '0'+str(jam)
        if menit<10:
            menit = '0'+str(menit)

        return str(jam)+":"+str(menit)

    else:
        raise Exception("Format date salah, format benar : 10:00:00 AM atau 09:00:03 PM")

def convert_date2(date : str):
    #Konversi waktu 24H -> 12H

    #pencocokan dengan regex
    if re.match('([0-1][0-9]|[2][0-4])[:][0-5][0-9]', date):
        waktu = date.split(":")
        jam = int(waktu[0])
        menit = int(waktu[1])

        #jika jam >=12 dikurangi 12 jam lalu nanti sebagai PM
        if jam>=12:
            jam -=12
            if jam<10:
                jam = '0'+str(jam)
            if menit<10:
                menit = '0'+str(menit)
            return str(jam)+":"+str(menit)+":00 PM" 

            #Jika tidak maka akan sebagai AM
        else:
            if jam<10:
                jam = '0'+str(jam)
            if menit<10:
                menit = '0'+str(menit)
            return str(jam)+":"+str(menit)+":00 AM" 
        
    else:
        raise Exception("Format date salah, format benar : 10:00 atau 19:00")

#untuk opsi konversi
opsi_konversi = {
    1 : convert_date1,
    2 : convert_date2
}

if __name__=='__main__':
    n = int(input("masukkan mode konversi waktu (1. 12H->24H; 2. 24H->12H): "))

    while(n<1 or n>2):
        print("inputan salah woy")
        n = int(input("masukkan mode konversi waktu (1. 12H->24H; 2. 24H->12H): "))
    
    waktu = input("masukkan waktu yang ingin diconvert: ")
    print("hasil konversi waktu "+str(opsi_konversi[n](waktu)))
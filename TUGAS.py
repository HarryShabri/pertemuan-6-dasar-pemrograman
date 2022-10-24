import os
list_nim=[]
list_hadir=[]
list_tugas=[]
list_uts=[]
list_uas=[]
list_nilaiakhir=[]
ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan Nim anda : "))
    list_hadir.append(0.2*int(input('Masukkan Nilai Kehadiran : ')))
    list_tugas.append(0.25*int(input('Masukkan Nilai Tugas : ')))
    list_uts.append(0.25*int(input("Masukkan Nilai UTS anda :")))    
    list_uas.append(0.3*int(input("Masukkan Nilai UAS : ")))    
    list_nilaiakhir.append(list_hadir[i]+list_tugas[i]+list_uts[i]+list_uas[i])
    os.system('cls')   
print('''
|   NIM   |   Nilai Kehadiran   |   Nilai Tugas   |   Nilai UTS   |   Nilai UAS   |   Nilai Akhir   |
-----------------------------------------------------------------------------------------------------''')
for i in range(ulang):
    print('  %s\t     %i\t\t\t   %i\t\t %i\t\t %i\t\t %i'%(list_nim[i],list_hadir[i],list_tugas[i],list_uts[i],list_uas[i],list_nilaiakhir[i]))
print('''
-----------------------------------------------------------------------------------------------------''')
#CODE TO MAKE ALL EXTENSIONS DESIRED THE SAME IN THE DIRECTORY WHERE THE CODE IS LOCATED

import os
giris = input("The extension you want to change in the directory:")
giris2 = input("The new extension you want to change:")
liste = []
print("txt files in the folder; ")
with os.scandir(os.getcwd()) as tarama:
    for belge in tarama:

        if belge.name.endswith("."+giris): #add this extension to the list
    
            liste.append(belge.name)

sozluk = dict()
for i in liste:
    a = i.split(".")
    sozluk[a[0]]=a[1]
    
liste2 = list()
for i,j in sozluk.items():
    j= giris2
    print(i+ " . "+j) 
    liste2.append(i+"."+j) #change the file information extension and add it to the list

for i in liste2:
    print(i)

sayac = 0
with os.scandir(os.getcwd()) as tarama:
    for belge in tarama:
        if belge.name.endswith("."+giris):
            os.rename(belge,liste2[sayac]) #apply the change in the list
            sayac+=1
            


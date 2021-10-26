#membuat program menghitung luas lingkaran dan keliling lingkarang

print(30*"=")
print(" operasi matematika ")
print('  1. luas lingkaran \t ')
print('  2. keliling lingkaran \t ')
print(30*"=")

pilihan = input(" pilih operasi (1/2) : ")
phi = float(input(" masukan phi = "))
r = float(input(" Masukan jari jari = "))

#rumus luas lingkaran (luas =phi*r*r)
#rumus keliling lingkarang(kel= 2*phi*r)

print(30*'=')

if pilihan == "1":
    luas =  phi*r*r
    print(" luas lingkaran dari = ",phi,"*",r,"*",r,"\n adalah = ", luas)
elif pilihan == "2":
    keliling = 2*phi*r
    print(" keliling lingkaran dari = 2 *",phi,"*",r,"\n adalah = ", keliling)
else:
    print("pilihan tidak di temukan")
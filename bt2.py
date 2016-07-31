import random

so_lan_doan = 0
print 'Tro Choi Doan So'
print 'Nhap ten : '

ten = raw_input()

so = random.randint(1, 25)

de = '1'
trung_binh = '2'
kho = '3'

print('Chao ' + ten + ', Moi ban chon cap do ')
print('De = 1 ; Trung Binh = 2 ; Kho = 3')

cap_do = raw_input()

if cap_do == '1':
    print 'OK. Ban da chon cap do de ,so lan doan cua ban la 20'
    so_mang = 20

elif cap_do == '2':
    print 'OK. Ban da chon cap do trung binh , so lan doan cua ban la 10'
    so_mang = 10
else: 
    print 'OK. Ban da chon cap do kho, so lan doan cua ban la 5'
    so_mang = 5

while so_lan_doan < so_mang:
    print ('Moi ban doan, ban con ' + str(so_mang - so_lan_doan) + ' lan doan')
    so_doan = raw_input()
    so_doan = int(so_doan)
    so_lan_doan = so_lan_doan + 1

    if so_doan < so:
        print 'So ban doan nho hon so can tim'

    if so_doan > so:
        print 'So ban doan lon hon so can tim'

    if so_doan == so:
        break

if so_doan == so:
    print ('Chuc mung ' + ten + ', ban da doan dung')

if so_doan != so:
    so = str(so)
    print ('Khong phai , so can tim la ' + so)

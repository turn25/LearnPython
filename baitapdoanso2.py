import random

so = random.randint(1, 20)

so_lan_choi = 0

de = '1'

trung_binh = '2'

kho = '3'

print '---TRO CHOI DOAN SO---'
print "nhap 'ok' de tiep tuc:"

dong_y = raw_input()

if dong_y == 'ok':
    print 'OK. Moi ban nhap ten'
    ten = raw_input()

else:
    print 'Tro choi ket thuc.'
    exit(0)
while True:
    so_lan_choi = 0

    print ('Chao, ' + ten + '. Moi ban chon cap do.')
    print '(De = 1; Trung Binh = 2; Kho = 3 )'

    cap_do = raw_input()

    if cap_do == '1':
        print 'Ban da chon cap do de. Ban co 10 luot choi.'
        luot_choi = 10

    if cap_do == '2':
        print 'Ban da chon cap do trung binh. Ban co 5 luot choi.'
        luot_choi = 5

    if cap_do == '3':
        print 'Ban da chon cap do kho. Ban co 3 luot choi.'
        luot_choi = 3

    print 'Ban hay doan 1 so tu 1 den 20'

    while so_lan_choi < luot_choi:
        print '\nMoi ban doan:'
        so_doan = raw_input()
        so_doan = int(so_doan)

        so_lan_choi = so_lan_choi + 1

        if so_doan < so:
            print('So ban doan nho hon so can tim (ban con ' + str(luot_choi - so_lan_choi) + ' luot choi).')

        if so_doan > so:
            print('So ban doan lon hon so can tim (ban con ' + str(luot_choi - so_lan_choi) + ' luot choi).')

        if so_doan == so:
            break

    if so_doan == so:
        so_lan_choi = str(so_lan_choi)
        print('Chuc mung ' + ten + '. Ban da chien thang tro choi trong vong ' + so_lan_choi + ' lan choi.')

    if so_doan != so:
        so = str(so)
        print('Khong phai. So can tim la ' + so)

    print '\nTro choi ket thuc.'
    print '\nBan co muon choi lai? (co / khong)'

    co = raw_input()

    if co == 'co':
        print 'OK. Cung choi lai nao!!!'

    else:
        exit(0)

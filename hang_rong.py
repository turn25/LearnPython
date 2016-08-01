import random
import time

def chon_cap_do():
    print 'Chon cap do :'
    print '(de = 1 ; trung binh = 2 ; kho = 3 )'
    cap_do = raw_input()

    if cap_do == '1':
        print 'Ban da chon cap do de'
        tong_hang = '2'
    return tong_hang

def hien_gioi_thieu(hang1):
    print 'Ban dang song o mot vung dat cua rong. Truoc mat ban'
    print ('la ' + hang + ' cai hang dong lon. 1 cai la noi o cua con rong')
    print 'rat than thien, no se chia se cho ban kho bau cua no.'
    print 'Con lai la noi o cua nhung con rong rat tham lam va '
    print 'khat mau, chung se an tuoi nuot song ban... '

def chon_hang_rong():
    hang = ''
    while hang != '1' and hang != '2' and hang != '3' and hang != '4':
        print 'Hay chon hang dong (1 / 2 / 3)'
        hang = raw_input()

    return hang

def kiem_tra_hang(hang_da_chon):
    print 'Ban tu tu tien vao trong hang ...'
    
    time.sleep(3)
    
    print 'Trong hang rat toi va dang so...'
    
    time.sleep(2)
    
    print 'Bong nhien mot con rong bay den truoc va ban , mo rong'
    print 'quai ham va ...'
    
    time.sleep(2)
    
    rong_tot = random.randint(1, 3)

    if hang_da_chon == str(rong_tot):
        print 'chia se cho ban kho bau cua no.'

    else:
        print 'nuot chung ban.'

dong_y = 'co'
while dong_y == 'co' or dong_y == 'y' or dong_y == 'yes' or dong_y == 'ok':
    hang = chon_cap_do() 
    hien_gioi_thieu(hang)
    so_hang = chon_hang_rong()
    kiem_tra_hang(so_hang)

    print ('Ban co muon choi lai? (co/khong)')
    dong_y = raw_input()

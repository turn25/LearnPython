#coding:utf-8
import random
import time

def chon_cap_do():
    print '\nChọn cấp độ :'
    print '(Dễ = 1 ; Trung bình = 2 ; Khó = 3 )'
    cap_do = raw_input()

    if cap_do == '1':
        print 'Bạn đã chọn cấp độ Dễ'
        tong_hang = '2'
        
    elif cap_do == '3':
        print 'Bạn đã chọn cấp độ Khó'
        tong_hang = '4'

    else:
        print 'Bạn đã chọn cấp độ Trung bình'
        tong_hang = '3'

    return tong_hang

def hien_gioi_thieu(so_hang_gioi_thieu):
    print '\nBạn đang sống ở 1 vùng đất của rồng. Trước mắt bạn'
    print ('là ' + so_hang_gioi_thieu + ' cái hang động lớn. 1 cái là nơi ở của con rồng ')
    print 'thân thiện, nó sẻ chia sẻ kho báu của nó cho bạn. '
    print 'Còn lại là nơi ở của những con rồng tham lam, độc ác '
    print 'và rất khát máu, chúng sẽ ăn tươi nuốt sống bạn... '

def chon_hang_rong(so_hang_gioi_thieu):
    hang = ''
    tong_hang = [str(x + 1) for x in range(int(so_hang_gioi_thieu))]
    chuoi_hang = ' / '.join(tong_hang)
    while hang not in tong_hang:
        print ('Hãy chọn hang động ' + chuoi_hang)
        hang = raw_input()

    return hang

def kiem_tra_hang(hang_da_chon, so_hang_kiem_tra):
    print 'Bạn từ từ tiến vào trong hang...'

    time.sleep(3)

    print 'Bên trong hang rất tối và đáng sợ...'

    time.sleep(2)

    print 'Bỗng nhiên một con rồng bay đến trước mặt bạn, mở rộng '
    print 'quai hàm và ...'

    time.sleep(3)

    rong_tot = random.randint(1, int(so_hang_kiem_tra))

    if hang_da_chon == str(rong_tot):
        print 'chia sẻ cho bạn kho báu của nó.'

    else:
        print 'nuốt chửng bạn.'

dong_y = 'co'
while dong_y == 'co' or dong_y == 'y' or dong_y == 'yes' or dong_y == 'ok':
    hang = chon_cap_do()
    hien_gioi_thieu(hang)
    so_hang = chon_hang_rong(hang)
    kiem_tra_hang(so_hang, hang)

    print ('Bạn có muốn chơi lại? (co/khong)')
    dong_y = raw_input()
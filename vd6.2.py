import time
import random   
print('TRO CHOI NHAN PHAM:')
def gioithieu():
    print('Chao ban den voi tro choi chon cua may man:')
    print('An nut bat ki de tiep tuc:...')
    raw_input()
    time.sleep(1)
    print('Co 3 o cua trong do co :')
    print('(1 o tang diem / 2 o tru diem )')
    time.sleep(1)
    print('Bat dau ban se co 50 diem \nSau 5 luot choi neu so diem tren 100 thi thang , duoi 100 thi thua')
def choncua():
    cua=''
    while cua!='1' and cua!='2'and cua!='3':
        print('Moi ban chon o cua may man (1 / 2 / 3 )')
        cua=raw_input()
    return cua
def cuadcchon(nodo):
    luotchoi=0
    diem=50
    #print('Va o cua ban da chon la')
    time.sleep(2)
    #print('O CUA')
    time.sleep(2)
    while luotchoi <5:
        diemnhan=random.randint(1,25)
        cuadung=random.randint(1,3)
        luotchoi=luotchoi+1
        print('Va o cua ban da chon la')
        time.sleep(1)
        print('O CUA')
        time.sleep(2)
        if nodo==str(cuadung):
            print('MAY MAN~~~')
            time.sleep(1)
            print('Chuc mung, ban da nhan dc '+str(diemnhan)+'diem')
            diem=diem+diemnhan
            print('Diem ban co:'+str(diem)+'\n')   
        if nodo!='1' and nodo!='2' and nodo!='3':
            print('wut')
        if nodo!=str(cuadung): #and int(nodo)>=1 and int(nodo)<=3:
            print('XUI XEO!!')
            time.sleep(1)
            print('Ban bi tru'+str(diemnhan)+'diem'+'')
            diem=diem-diemnhan
            print('Diem ban co:'+str(diem)+'\n')
        if luotchoi<5:
            time.sleep(1)
            print('Moi ban chon o may man: \n( Chon so khac ngoai 1 / 2 / 3 auto xui xeo nhe ;) )')
            cua=raw_input()
    if diem >= 100 :
        print('CHUC MUNG BAN DA CHIEN THANG TRO CHOI NAY!!')
    else :
        print('BAN DA THUA:(\nBan co muon choi lai? (y/n, yes/no)')
choilai='y'
while choilai=='y' or choilai=='yes':
    gioithieu()
    cuachon=choncua()
    cuadcchon(cuachon)
    choilai=raw_input()

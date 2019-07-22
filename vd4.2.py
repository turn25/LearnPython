import random
print('Tro choi doan so')
print('Moi ban chon che do: (1:bat tu,  2: 3 mang)')
chedo=raw_input()
luotchoi=0
print("('-')")
so=random.randint(1,44)
while chedo == '1' and luotchoi==0:
    print('Moi ban doan so')
    doan=input()
    if doan<so:
        print('so BE hon so can tim')
    if doan>so:
        print('so LON hon so can tim')
    if doan==so:
        print('oki doan dung r')
        break
while chedo== "2" and luotchoi<3:
    print('Moi ban doan so')
    doan=input()
    luotchoi=luotchoi +1
    if doan<so:
        print("so BE hon so can tim, ban con "+str(3-luotchoi)+' luot choi')       
    if doan>so:
        print('so LON hon so can tim, ban con '+str(3-luotchoi)+' luot choi') 
    if doan==so:
        print('omedetou')
        break 
    if luotchoi==3 and doan!=so:
        print('F')
if chedo!='1' and chedo!='2':
    print('chon sai che do roi choi gi nua')

    

l=[1,2,3,4,5,6,7,8,9]

def board():
     print(l[0],l[1],l[2])
     print(l[3],l[4],l[5]) 
     print(l[6],l[7],l[8])

n='true'
def check():
    if l[0]==l[1]==l[2]=='X'or l[3]==l[4]==l[5]=='X' or l[6]==l[7]==l[8]=='X' or l[0]==l[3]==l[6]=='X' or l[1]==l[4]==l[7]=='X' or l[2]==l[5]==l[8]=='X' or l[0]==l[4]==l[8]=='X' or l[2]==l[4]==l[6]=='X':
        return 'p1 is the winner'

    elif l[0]==l[1]==l[2]=='O'or l[3]==l[4]==l[5]=='O' or l[6]==l[7]==l[8]=='O' or l[0]==l[3]==l[6]=='O' or l[1]==l[4]==l[7]=='O' or l[2]==l[5]==l[8]=='O' or l[0]==l[4]==l[8]=='O' or l[2]==l[4]==l[6]=='O':
        return 'p2 is the winner'
    else:
        for i in l:
                if i==int:
                    print('draw')
                    break
                else:
                    if i!=str:
                        print('tie....')
                        break
while n:
    board()
    p1=int(input('enter the slot for p1:'))
    l[p1-1]='X'
    res=check()
    if res:
        print(res)
        break
    board()
    p2=int(input('enter the slot for p2:'))
    l[p2-1]='O'
    check()
    res=check()
    if res:
        print(res)
        break
    board()





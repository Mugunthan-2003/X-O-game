import random
from tkinter.messagebox import *
from tkinter import *

def main(t_m,wcl):
    def show(d):
        print('|1\t|2\t|3\t|\n|',d['1'],'\t|',d['2'],'\t|',d['3'],'\t|')
        print('|4\t|5\t|6\t|\n|',d['4'],'\t|',d['5'],'\t|',d['6'],'\t|')
        print('|7\t|8\t|9\t|\n|',d['7'],'\t|',d['8'],'\t|',d['9'],'\t|')
        print()
    
    ######################################################
    
    d={}
    for i in range(1,10):
        d[str(i)]=' '
    s=None
    p1ic=p2ic=None

    #######################################################
    
    def choice():
        num=random.randint(1,100)
        choice=num%2
        print(l[choice],'You won the toss.')
        p1ic=p2ic=None
        if choice==0:
            p1ic=input('Your choice(X or O):')
            if p1ic.upper()=='X':
                p2ic='O'
            else:
                p2ic='X'
            print(l[choice+1],' you have got \'',p2ic,'\' as your symbol.')
            s=0
        elif choice==1:
            p2ic=input('Your choice(X or O):')
            if p2ic.upper()=='X':
                p1ic='O'
            else:
                p1ic='X'
            print(l[choice-1],' you have got \'',p1ic,'\' as your symbol.')
            s=1
        print()
        return s,p1ic,p2ic

    #########################################################
                        
    def game(s,p1ic,p2ic,wcl):
        global inserted,winner,ch_li
        inserted=[]
        ch_li=[['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],
            ['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
        winner=None
        print('Now the game starts.You can insert positions from 1 to 9.\n')

        #for loop starts.
        
        for i in range(9):
            global pos
            pos=''
            print(l[s],'now your Turn.')
            if s==0:
                def s0():
                    print('You want to insert ',p1ic,' at which position : ',end='')
                    pos=input('')
                    if pos in ['1','2','3','4','5','6','7','8','9']:
                        if d[pos]==' ':
                            d[pos]=p1ic
                            return False
                        else:
                            print('You have given wrong input.')
                            return True
                    else:
                        print('You have given wrong input.')
                        return True
                sc0=s0()
                while sc0:
                    sc0=s0()
                for i in ch_li:
                    if d[i[0]]==d[i[1]] and d[i[0]]==d[i[2]]:
                        if d[i[0]]!=' ':
                            winner=l[s]
                print()
                s+=1
            else:
                def s1():
                    print('You want to insert ',p2ic,' at which position : ',end='')
                    pos=input('')
                    if pos in ['1','2','3','4','5','6','7','8','9']:
                        if d[pos]==' ':
                            d[pos]=p2ic
                            return False
                        else:
                            print('You have given wrong input.')
                            return True
                    else:
                        print('You have given wrong input.')
                        return True
                sc1=s1()
                while sc1:
                    sc1=s1()
                for i in ch_li:
                    if d[i[0]]==d[i[1]] and d[i[0]]==d[i[2]]:
                        if d[i[0]]!=' ':
                            winner=l[s]
                print()
                s-=1
            show(d)
            if winner!=None:
                break

            #for loop ends.
        
        if winner==l[0]:
            wcl[0]+=1
        elif winner==l[1]:
            wcl[1]+=1
        else:
            wcl[2]+=1
        s1='\n\nTotal matches played : '+str(t_m)
        s2='\nNo.of matches won by '+l[0]+' : '+str(wcl[0])
        s3='\nNo.of matches won by '+l[1]+' : '+str(wcl[1])
        s4='\nNo.of draw matches : '+str(wcl[2])
        s5=s1+s2+s3+s4
        if winner==None:
            showinfo('Result','\nGame Over.This is a draw match.'+s5)
        else:
            showinfo('Result','Game Over.The Winner is !!!!   '+winner+'   !!!!.'+s5)
    
    ###########################################################
    
    r=choice()
    show(d)
    game(r[0],r[1],r[2],wcl)

root=Tk()
root.withdraw()
showinfo('Information','X or O game welcomes you.')
print('\t\t\t\t  X OR O GAME')
Player_1=input('Enter Player 1 Name:')
Player_2=input('Enter Player 2 Name:')
global l
l=[Player_1,Player_2]
t_m=1
wcl=[0,0,0]
m_c=True
while m_c:
    main(t_m,wcl)
    print()
    q=askquestion('','Do you want to continue the Game?')
    if q=='no':
        showinfo('Information','Thank you for playing the game.')
        m_c=False
    else:
        print('You can continue now.')
        t_m+=1
        print()

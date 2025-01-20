import threading,time,os
from pynput.keyboard import Listener

def make_global():
            global sorvaltozo
            global elemvaltozo
            global a
            a=0 
            sorvaltozo=0
            elemvaltozo=-2
make_global()
def task1():
    global sorvaltozo,elemvaltozo,a
    while a==0:
        

        t=[["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"], 
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"], 
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"], 
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"], 
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"], 
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ]

        os.system("cls")
        for row in t:
            print(" ".join(row))
         

        sor=int(7)
        elem=int(15) 
        
        lepesek=[]

        while a==0:
                
            if sor>=16 and sorvaltozo==1:
                sor=0
            if sor<=0 and sorvaltozo==-1:
                sor=15
            if elem>=31 and elemvaltozo==2:
                elem=1
            if elem<=0 and elemvaltozo==-2:
                elem=29
                    
            lepesek.append(sor)
            lepesek.append(elem)
            if len(lepesek)>14:
                print(f"\033[{lepesek[0]};{lepesek[1]}H*", end="", flush=True) 
                del lepesek[0]
                del lepesek[0]
            
            
            print(f"\033[{sor};{elem}H■", end="", flush=True) 
            time.sleep(0.1)

            sor+=sorvaltozo
            elem+=elemvaltozo
        

def task2():
    global sorvaltozo, elemvaltozo,a
    while a==0:
        
        
        def show(key):
            global sorvaltozo, elemvaltozo
            
            if key == key.down:
                if sorvaltozo!=-1:
                    sorvaltozo=1
                    elemvaltozo=0
            if key == key.up:
                if sorvaltozo!=1:
                    sorvaltozo=-1
                    elemvaltozo=0
            if key == key.left:
                if elemvaltozo!=2:
                    sorvaltozo=0
                    elemvaltozo=-2
            if key == key.right:
                if elemvaltozo!=-2:
                    sorvaltozo=0
                    elemvaltozo=2
            if key == key.esc:
                os.system('cls')
                global a
                a=1
                print("viszlát!")
                exit()

        with Listener(on_press=lambda k: show(k.char if hasattr(k, 'char') else k)) as listener:
            listener.join()

        

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

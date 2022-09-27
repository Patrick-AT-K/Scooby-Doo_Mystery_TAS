import pyautogui

move = 12451
lag = 12598
file = open('C:\\Users\\18564\\Desktop\\test\\hello.txt',”w”) 
pyautogui.keyDown('win')
pyautogui.press('down')
pyautogui.keyUp('win')
pyautogui.PAUSE = 1

pyautogui.moveTo(95, 50)
pyautogui.click()
pyautogui.moveTo(95, 75)
pyautogui.click()
pyautogui.PAUSE = 8
for x in range(0,449):
    i = str(x)
    im = pyautogui.screenshot('C:\\Users\\18564\\Desktop\\test\\blanks\\my_screenshot'+ i + '.png')

pyautogui.moveTo(95, 50)
pyautogui.click()
pyautogui.moveTo(95, 75)
pyautogui.click()
l = []

for x in range(0,449):
    i = str(x)
    j = str('C:\\Users\\18564\\Desktop\\test\\blanks\\my_screenshot'+ i + '.png')
    m = pyautogui.locate('C:\\Users\\18564\\Desktop\\kitchen.png', j , grayscale=False, region=(0, 251, 300, 65))
    l.append(m)

xx = 0
ll = []

for f in l:
    d = str(f)
    if d == 'None':
        ll.append(str(xx))
    xx += 1

k = []
kk = []
oh = []
oo = []
BB = []

for ff in ll:
    B = []
    ii = str(ff)
    jj = str('C:\\Users\\18564\\Desktop\\test\\blanks\\my_screenshot'+ ii + '.png')
    ml = pyautogui.locate('C:\\Users\\18564\\Desktop\\Lkitchen.png', jj , grayscale=False, region=(0, 250, 300, 65))
    mml = str(ml)
    print(mml)
    if mml == 'None':
        kl = pyautogui.locate('C:\\Users\\18564\\Desktop\\kitchenL1.png', jj , grayscale=False, region=(42, 253, 293, 61))
        k1 = str(kl)
        if k1 == 'None':
            kll = pyautogui.locate('C:\\Users\\18564\\Desktop\\kitchenL4.png', jj , grayscale=False, region=(0, 253, 293, 61))
            if kll == 'None':
                kll = ii
                k.append(kll)
            if kll != 'None':
                kll = 'L1'
        if k1 != 'None':
            kll = 'L2'
    if mml != 'None':
        lk = pyautogui.locate('C:\\Users\\18564\\Desktop\\kitchenR1.png', jj , grayscale=False, region=(42, 252, 250, 64))
        et = str(lk)
        if et != 'None':
            kll = 'R2'
        if et == 'None':
            tt = pyautogui.locate('C:\\Users\\18564\\Desktop\\kitchenR2.png', jj , grayscale=False, region=(42, 252, 293, 61))
            if tt == 'None':
                kll = ii
                k.append(kll)
            if tt != 'None':
                kll = 'R1'
    B.append(kll)
    B.append(ii)
    k.append(B)


o = []
m = 0

for fff in k:
    BB = []
    h = str(fff[1])
    jjj = str('C:\\Users\\18564\\Desktop\\test\\blanks\\my_screenshot'+ h + '.png')
    if fff[0] == 'L1':
        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
        if ch != 'None':
            o.append('HL1')
        if ch == 'None':
            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\hamf2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))            
            if ch2 != 'None':
                o.append('HL1')
            if ch2 == 'None':
                ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham3.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                if ch3 != 'None':
                    o.append('HL1')
                if ch3 == 'None':
                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salami2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                    if ch != 'None':
                        o.append('SL1')
                    if ch == 'None':
                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salamif2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                        if ch2 != 'None':
                            o.append('SL1')
                        if ch2 == 'None':
                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese3.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                            if ch != 'None':
                                o.append('CL1')
                            if ch == 'None':
                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheesef2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                if ch2 != 'None':
                                    o.append('CL1')
                                if ch2 == 'None':
                                    ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese4.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                    if ch3 != 'None':
                                        o.append('CL1')
                                    if ch3 == 'None':
                                        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomato3.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                        if ch != 'None':
                                            o.append('TL1')
                                        if ch == 'None':
                                            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomatof3.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                            if ch2 != 'None':
                                                o.append('TL1')
                                            if ch2 == 'None':
                                                ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken4.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                if ch != 'None':
                                                    o.append('ChL1')
                                                if ch == 'None':
                                                    ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken7.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                    if ch2 != 'None':
                                                        o.append('ChL1')
                                                    if ch2 == 'None':
                                                        ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chickenf2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                        if ch3 != 'None':
                                                            o.append('ChL1')
                                                        if ch3 == 'None':
                                                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\pickle6.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                            if ch != 'None':
                                                                o.append('PL1')
                                                            if ch == 'None':
                                                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\picklef2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                                if ch2 != 'None':
                                                                    o.append('PL1')
                                                                if ch2 == 'None':
                                                                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana6.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                                    if ch != 'None':
                                                                        o.append('BL1')         
                                                                    if ch == 'None':
                                                                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\bananaf2.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                                        if ch2 != 'None':
                                                                            o.append('BL1')
                                                                        if ch2 == 'None':
                                                                            ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana7.png', jjj, grayscale=True, region=(42, 246, 125, 70)))
                                                                            if ch3 != 'None':
                                                                                o.append('BL1')
                                                                            if ch3 == 'None':
                                                                                o.append('L1')
        BB.append(o[m])
        BB.append(h)
        oo.append(BB)
        m += 1
    if fff[0] == 'L2':
        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
        if ch != 'None':
            o.append('HL2')
        if ch == 'None':
            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\hamf2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))            
            if ch2 != 'None':
                o.append('HL2')
            if ch2 == 'None':
                ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham3.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                if ch3 != 'None':
                    o.append('HL2')
                if ch3 == 'None':
                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salami3.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                    if ch != 'None':
                        o.append('SL2')
                    if ch == 'None':
                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salamif2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                        if ch2 != 'None':
                            o.append('SL2')
                        if ch2 == 'None':
                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese3.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                            if ch != 'None':
                                o.append('CL2')
                            if ch == 'None':
                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheesef2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                if ch2 != 'None':
                                    o.append('CL2')
                                if ch2 == 'None':
                                    ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese4.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                    if ch3 != 'None':
                                        o.append('CL2')
                                    if ch3 == 'None':
                                        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomato3.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                        if ch != 'None':
                                            o.append('TL2')
                                        if ch == 'None':
                                            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomatof3.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                            if ch2 != 'None':
                                                o.append('TL2')
                                            if ch2 == 'None':
                                                ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken7.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                if ch != 'None':
                                                    o.append('ChL2')
                                                if ch == 'None':
                                                    ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken9.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                    if ch2 != 'None':
                                                        o.append('ChL2')
                                                    if ch2 == 'None':
                                                        ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chickenf2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                        if ch3 != 'None':
                                                            o.append('ChL2')
                                                        if ch3 == 'None':
                                                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\pickle6.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                            if ch != 'None':
                                                                o.append('PL2')
                                                            if ch == 'None':
                                                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\picklef2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                                if ch2 != 'None':
                                                                    o.append('PL2')
                                                                if ch2 == 'None':
                                                                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana6.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                                    if ch != 'None':
                                                                        o.append('BL2')         
                                                                    if ch == 'None':
                                                                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\bananaf2.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                                        if ch2 != 'None':
                                                                            o.append('BL2')
                                                                        if ch2 == 'None':
                                                                            ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana7.png', jjj, grayscale=True, region=(0, 252, 65, 67)))
                                                                            if ch3 != 'None':
                                                                                o.append('BL2')
                                                                            if ch3 == 'None':
                                                                                o.append('L2')
        BB.append(o[m])
        BB.append(h)
        oo.append(BB)
        m += 1
    if fff[0] == 'R1':
        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham2.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
        if ch != 'None':
            o.append('HR1')
        if ch == 'None':
            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\hamf2.png', jjj, grayscale=True, region=(165, 246, 80, 67)))            
            if ch2 != 'None':
                o.append('HR1')
            if ch2 == 'None':
                ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham3.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                if ch3 != 'None':
                    o.append('HR1')
                if ch3 == 'None':
                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salami3.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                    if ch != 'None':
                        o.append('SR1')
                    if ch == 'None':
                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salamif3.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                        if ch2 != 'None':
                            o.append('SR1')
                        if ch2 == 'None':
                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese4.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                            if ch != 'None':
                                o.append('CR1')
                            if ch == 'None':
                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheesef2.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                if ch2 != 'None':
                                    o.append('CR1')
                                if ch2 == 'None':
                                    ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese5.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                    if ch3 != 'None':
                                        o.append('CR1')
                                    if ch3 == 'None':
                                        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomato3.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                        if ch != 'None':
                                            o.append('TR1')
                                        if ch == 'None':
                                            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomatof4.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                            if ch2 != 'None':
                                                o.append('TR1')
                                            if ch2 == 'None':
                                                ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken7.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                if ch != 'None':
                                                    o.append('ChR1')
                                                if ch == 'None':
                                                    ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken9.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                    if ch2 != 'None':
                                                        o.append('ChR1')
                                                    if ch2 == 'None':
                                                        ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chickenf3.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                        if ch3 != 'None':
                                                            o.append('ChR1')
                                                        if ch3 == 'None':
                                                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\pickle6.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                            if ch != 'None':
                                                                o.append('PR1')
                                                            if ch == 'None':
                                                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\picklef2.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                                if ch2 != 'None':
                                                                    o.append('PR1')
                                                                if ch2 == 'None':
                                                                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana6.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                                    if ch != 'None':
                                                                        o.append('BR1')         
                                                                    if ch == 'None':
                                                                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\bananaf2.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                                        if ch2 != 'None':
                                                                            o.append('BR1')
                                                                        if ch2 == 'None':
                                                                            ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana7.png', jjj, grayscale=True, region=(165, 246, 80, 67)))
                                                                            if ch3 != 'None':
                                                                                o.append('BR1')
                                                                            if ch3 == 'None':
                                                                                o.append('R1')
        BB.append(o[m])
        BB.append(h)
        oo.append(BB)
        m += 1
    if fff[0] == 'R2':
        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham2.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
        if ch != 'None':
            o.append('HR2')
        if ch == 'None':
            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\hamf2.png', jjj, grayscale=True, region=(246, 246, 55, 67)))            
            if ch2 != 'None':
                o.append('HR2')
            if ch2 == 'None':
                ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\ham3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                if ch3 != 'None':
                    o.append('HR2')
                if ch3 == 'None':
                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salami3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                    if ch != 'None':
                        o.append('SR2')
                    if ch == 'None':
                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\salamif3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                        if ch2 != 'None':
                            o.append('SR2')
                        if ch2 == 'None':
                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese4.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                            if ch != 'None':
                                o.append('CR2')
                            if ch == 'None':
                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheesef2.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                if ch2 != 'None':
                                    o.append('CR2')
                                if ch2 == 'None':
                                    ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\cheese5.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                    if ch3 != 'None':
                                        o.append('CR2')
                                    if ch3 == 'None':
                                        ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomato3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                        if ch != 'None':
                                            o.append('TR2')
                                        if ch == 'None':
                                            ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\tomatof2.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                            if ch2 != 'None':
                                                o.append('TR2')
                                            if ch2 == 'None':
                                                ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken7.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                if ch != 'None':
                                                    o.append('ChR2')
                                                if ch == 'None':
                                                    ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chicken9.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                    if ch2 != 'None':
                                                        o.append('ChR2')
                                                    if ch2 == 'None':
                                                        ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\chickenf2.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                        if ch3 != 'None':
                                                            o.append('ChR2')
                                                        if ch3 == 'None':
                                                            ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\pickle6.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                            if ch != 'None':
                                                                o.append('PR2')
                                                            if ch == 'None':
                                                                ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\picklef3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                                if ch2 != 'None':
                                                                    o.append('PR2')
                                                                if ch2 == 'None':
                                                                    ch = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana6.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                                    if ch != 'None':
                                                                        o.append('BR2')         
                                                                    if ch == 'None':
                                                                        ch2 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\bananaf3.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                                        if ch2 != 'None':
                                                                            o.append('BR2')
                                                                        if ch2 == 'None':
                                                                            ch3 = str(pyautogui.locate('C:\\Users\\18564\\Desktop\\banana7.png', jjj, grayscale=True, region=(246, 246, 55, 67)))
                                                                            if ch3 != 'None':
                                                                                o.append('BR2')
                                                                            if ch3 == 'None':
                                                                                o.append('R2')
        BB.append(o[m])
        BB.append(h)
        oo.append(BB)
        m += 1


BBB = []
ez = 1

for ze in range(0, len(oo)-1):
    if oo[ze][0] == oo[ez][0]:
        g = int(oo[ze][1])
        h = int(oo[ez][1])
        g += 1
        if g != h:
            BBB.append(oo[ze])
    if oo[ze][0] != oo[ez][0]:
        BBB.append(oo[ze])
    ez += 1

BBB

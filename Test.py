from time import sleep, time

how_many_time = 0
CAN_loop = True
can_do = True

eric_ok = "eric : no you are stupid"
george_ok = "george : no you are stupid"

while CAN_loop:
    if can_do:
        print(eric_ok)
        sleep(0.3)
        how_many_time = how_many_time + 1
        can_do = False
    elif can_do == False:
        print(george_ok)
        sleep(0.3)
        can_do = True
        if how_many_time == 8:
            sleep(1)
            print("eric : wait? are we both stupid?")
            sleep(1)
            print("george : ye i think so")
            sleep(1)
            print("eric : yay. both stupid best friends")
            sleep(1)
            print("george : ye")
            sleep(1)
            print("eric : so we are ")
            sleep(1)
            print("george : emmm, i still think you are more stupid than me")
            george_ok = "george : no youre are more stupid"
            eric_ok = "eric : no youre are more stupid" 
            while CAN_loop:
                if can_do:
                    print(eric_ok)
                    sleep(0.3)
                    how_many_time = how_many_time + 1
                    can_do = False
                elif can_do == False:
                    print(george_ok)
                    sleep(0.3)
                    can_do = True
print(1)
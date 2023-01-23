def RaceCar(string):
    direction=1
    acceleration=0
    movement=0
    for car in string:
        if car == "A":
            movement+=direction*2**acceleration
            acceleration+=1

        # if car == "A" and direction==-1:
        #     movement+=direction*2**acceleration
        #     acceleration+=1
        elif car == "R":
            acceleration=0;
            direction=direction*-1



    return movement

print(RaceCar("AAARAAA RARA RARA RARA RARA RARA RA"))

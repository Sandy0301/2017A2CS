ina = "System is inactive"
ac = "System is active"
alert = "alert!"
alarm = "ring ring!"
def start(state) :
    if state ==ina :
        state=ac
    print(state)
    return(state)

def enter(state, time) :
    if state==ac:
        state=ina
    if state == alert :
        time=0
        state=ina
    if state ==alarm:
        state =ina
    print(state)
    return(state, time)

def activate(state) :
    if state == ac :
        state=alert
    print(state)
    return(state)

def timec(state, time):
    if state == alert:
        time=time+1
    return(time)

def bell(state, time) :
    if time==2 and state==alert:
        state=alarm
    print(state)

def inputn() :
    print('a:Start button. b:Enter PIN. c:Activate Sensor')

def main() :
    time=0
    state=ina
    print(state)
    while True :
        inputn()
        inp= input('choose from a, b, c')
        if inp == "a" :
            state =start(state)
        if inp == "b" :
            state, time= enter(state, time)
        if inp== "c" :
            state = activate(state)
        else:
            while not 'a' or not 'b' or not 'c':
                inp=input('choose from a, b, c')
        time= timec(state, time)
        state= bell(state, time)
main()

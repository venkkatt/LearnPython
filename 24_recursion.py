# finding factorial

def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)

fact(4)

'''
fact(4) ==> 4*fact(4-1) =>4!
fact(3) ==> 3*fact(3-1) =>3!
fact(2) ==> 2*fact(2-1) => 2!
fact(1) ==> 1*fact(0)   => 1!
fact(0) ==> return with 1
'''
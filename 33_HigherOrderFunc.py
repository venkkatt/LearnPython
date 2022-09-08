def happy():
    print("Jumping>>>")


def sad():
    print("crying???")


print(happy)  # <function happy at 0x000001CD03CC3E20>

joy = happy

joy()  # Jumping>>>

sorrow = sad
sorrow()

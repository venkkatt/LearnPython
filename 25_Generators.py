def sq_num(num):
    sq = []
    for i in range(1, num + 1):
        sq.append(i * i)
    return sq


print(sq_num(4))


def sq_num_gen(num):
    for i in range(1, num + 1):
        yield i * i


sq_gen = sq_num_gen(2)
for i in sq_gen:
    print(i)

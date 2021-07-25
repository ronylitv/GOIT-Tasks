import random

def gen_numbers():
    answer = []
    while len(answer) <3:
        b = random.randint(1,10)
        if b not in answer:
            yield b
            answer.append(b)


for i in gen_numbers():
    print(i)




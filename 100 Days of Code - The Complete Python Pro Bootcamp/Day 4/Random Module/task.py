import random
# random_num=random.randint(2,10)
# print(random_num)

# random_float=random.random()
# print(round(random_float,2))

# random_rand=random.uniform(10,15)
# print(round(random_rand,3))

random_num=random.randint(1,20)
print(random_num)
rand=random.uniform(0.0,15.5)
print(round(rand,2))
print(round(random.random(),2))

rand=random.randint(0,1)
if rand==0:
    print("Heads")
else:
    print("Tails")

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_num= random.randint(0,4)
# if random_num==0:
#     print("Alice")
# elif random_num==1:
#     print("Bob")
# elif random_num==2:
#     print("Charlie")
# elif random_num==3:
#     print("David")
# else:
#     print("Emanuel")
print(random.choice(friends))
print(friends[random_num])
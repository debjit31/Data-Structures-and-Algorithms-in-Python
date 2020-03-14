#There are n people in the party. Each person is wearing T-shirts with 
#numbers written on the T-shirts. The numbers on the T-shirts can be unique or the same.
# In three turns 3 people leave the party one at a time. 
#You are provided with the people remaining in the party after every turn.
# You need to print the T-shirt number of people who left the party in the order they left. 


ar = list(map(int, input().split(',')))
total = sum(ar)
left=[]
for _ in range(3):
    turn = list(map(int, input().split(',')))
    tmp = sum(turn)
    left.append(total - tmp)
    total = tmp
print(*left)
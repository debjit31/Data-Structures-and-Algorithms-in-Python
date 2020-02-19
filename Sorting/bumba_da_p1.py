s = input()
s1 = ''
s1+=s[5:len(s)]
prev_sum = 0
for i in range(ord('A'), ord(s1[0])):
    prev_sum+= 9999
prev_sum += int(s1[2:])
print(prev_sum)




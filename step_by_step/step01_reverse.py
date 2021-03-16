f_in = int(input())
s_in = input()
r_in = reversed(s_in)
for i in r_in:
    print(f_in * int(i))

print(f_in * int(s_in))
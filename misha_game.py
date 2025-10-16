n = int(input())
count = 0
j = 0
for i in range(n):
    m_i, c_i = map(int, input().split())
    if m_i > c_i:
        j += 1
    elif c_i > m_i:
        count += 1

if j > count:
    print("Mishka")
elif count > j:
    print("Chris")
else:
    print("Friendship is magic!^^")

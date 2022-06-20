# 10809에 대한 대체 풀이

s = str(input())
alphabet = [-1]*26 # 여기까지는 동일

for i in range(len(s)):
    if s[i] not in s[0:i]: # 해당 문자가 처음 등장하는 경우에만
        alphabet[ord(s[i])-97] = i # alphabet 리스트에서 자기 자리를 찾아서 자기 위치(i)를 할당
print(*alphabet)

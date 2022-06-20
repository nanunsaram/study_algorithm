s = str(input()) # 문자열로 입력 받기
alphabet = [-1]*26 # 출력될 리스트를 초기화(-1)

for i in range(len(s)): # 문자열 상 문자를 처음부터 하나씩 체크
    if alphabet[ord(s[i])-97] == -1: # 아직 해당 문자가 나오지 않은 경우(초기화된 -1 상태로 유지된 경우) 
        alphabet[ord(s[i])-97] = i # 리스트 상 해당 문자에 해당하는 자리를 찾아가서 자기 위치를 입력
print(*alphabet) # 문자열을 언패킹해서 출력

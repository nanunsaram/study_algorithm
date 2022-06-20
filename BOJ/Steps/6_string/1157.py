# set을 이용하여 주어진 word에서 unique한 letter들만 뽑아낸다
# 그러나 이후에 순서가 필요하므로 set를 list로 만든다 
word = str(input()).lower() # 예시: abracaDabRa -> abracadabra
word_set = list(set(word)) # 예시: {'b', 'd', 'r', 'c', 'a'} -> ['b', 'd', 'r', 'c', 'a']
count = []

# 이 word_set에 들어있는 letter를 기준으로 본래 주어진 word에 count()를 써서
# word_set에 들어있는 letter별 등장 횟수를 count에 저장한다

for each_letter in word_set:
    count.append(word.count(each_letter))  

# 아주 긴 word가 주어질 경우도 있기 때문에,
# word의 각 letter에 대해 반복하면서 count를 하나씩 더 해가는 방식보다,
# 이렇게 word_set으로 만들어서 최대 26개에 대해서만 반복하는 것이 유리한 것으로 보인다.
# 여기서 count()는 상당히 빠르게 계산되는 것으로 추정된다.

max_count = max(count)

if count.count(max_count) >= 2:
  print("?")
else:
  print(word_set[count.index(max_count)].upper())

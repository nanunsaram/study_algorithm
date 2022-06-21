croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
count = len(word)

for alphabet in croatian_alphabet:
    count -= word.count(alphabet)
# 여기서 'dz='가 포함되어 있는 경우 유의해야 한다(다만 운좋게 문제가 생기지 않은 경우다).
# 첫째, 'dz='는 세 글자이기 때문에 한번 등장할 때 count에서 두 번 빼줘야 한다. 즉 현 상태에서 1만큼 더 빼야 한다(+1 상태)
# 둘째, 'dz='는 'z='를 포함하고 있어서, 'dz='가 한 번 등장할 때 'z='가 한 번 빼지는 효과가 생긴다. 즉 현 상태는 1만큼 더 빠진 것이다(-1 상태)
# 이 두 가지를 결합하면 'dz='가 한 번 등장 할 때 (+1) + (-1) = 0으로 딱 맞게 계산되어서 별도 조치를 해주지 않아도 된다
    
print(count)

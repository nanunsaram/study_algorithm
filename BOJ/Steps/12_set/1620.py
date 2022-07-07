import sys
N, M = map(int, input().split())

pokemon_names = []
for i in range(N):
    pokemon_names.append(sys.stdin.readline().rstrip()) 

poke_dict = dict(zip(pokemon_names, range(1, N+1)))

# If we get the query and print the answer in the loop, timeout error happens
pokemon_query = [sys.stdin.readline().rstrip() for i in range(M)]

for each_query in pokemon_query:
    if ord(each_query[0]) < 58:
        print(pokemon_names[int(each_query)-1])
    else:
        print(poke_dict[each_query])

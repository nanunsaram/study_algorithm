def pattern(n):
    if n == 3:
        return "***" + "\n" + "* *" + "\n" + "***"
    sub_pattern = list(pattern(n//3).split("\n"))

    p_first = '\n'.join([i*3 for i in sub_pattern])
    p_third = '\n'.join([i*3 for i in sub_pattern])
  
    p_second = '\n'.join([i+" "*(n//3)+i for i in sub_pattern])
    return '\n'.join([p_first, p_second, p_third])

n = int(input())
print(pattern(n))

# https://www.hackerrank.com/challenges/staircase/problem?h_r=profile

def staircase(n):
    str_line = ""
    for i in range(n):
        str_line = " " * (n - i -1) + "#" * (i + 1)
        print(str_line)


staircase(10)
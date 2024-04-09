import sys
input = sys.stdin.readline

n = int(input())


for i in range(n):
    r, c =map(int, input().split())

matrix = [0] * (r+1) for _ in range(c+1):
    d
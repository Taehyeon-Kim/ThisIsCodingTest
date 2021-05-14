'''
boj18310+안테나

(아이디어)에서 확신을 못가짐
확실히 중간에 놓으면 최소가 될 것 같다는 생각은 했는데 확신을 못함..
수직선으로 생각해보면 맞기는 한 것 같은데,, ㅜㅜ
'''
import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

houses.sort()
print(houses[(n-1)//2])

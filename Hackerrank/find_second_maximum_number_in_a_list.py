'''
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    numbers = {}
    for n in arr:
        if n in numbers.keys():
            numbers[n] += 1
        else:
            numbers[n] = 1
    numbers = sorted(numbers.items(), key=lambda k: k[0], reverse=True)
    print(numbers[1][0])

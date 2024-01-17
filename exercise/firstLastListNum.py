def solution(n):
    if(n[0] == n[-1]):
        print("result is True")
    else:
        print("result is False")



number = []
n = int(input("Enter the number of elements: "))

for _ in range(n):
    num = int(input("Enter a number: "))
    number.append(num)
print(number)
solution(number)
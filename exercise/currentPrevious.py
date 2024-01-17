def solution(n):
    prevNum = 0
    Sum = 0
    for i in range(n):
        Sum = prevNum + i
        print("Current Number ", i, "Previous Number ", prevNum, "Sum: ",Sum)
        prevNum = i


x = int(input("Please input a number: "))
print("Printing current and previous number sum in a range(", x, ")")
solution(x)
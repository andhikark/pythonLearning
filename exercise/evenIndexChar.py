def solution(s):
    for i in range(0,len(s),2):
        print(s[i])


s = input("Input string: ")
print("Printing only even index chars")
solution(s)


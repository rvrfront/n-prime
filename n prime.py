n = int(input("Please, insert a number: "))
numbers = list(range(2, n+1))
idx1 = 0
while numbers[idx1] != numbers[-1]:
    idx2 = idx1 + 1
    l = len(numbers)
    while idx2 < l:
        if numbers[idx2] % numbers[idx1] == 0:
            numbers.pop(idx2)
            l = len(numbers)
        idx2 += 1
    idx1 += 1

print("Prime number list is: {}".format(numbers))
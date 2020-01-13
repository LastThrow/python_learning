nums = []
data = eval(input('Enter an integer , the input ends if it is 0:'))
while data != 0:
    nums.append(data)
    data = eval(input('Enter an integer , the input ends if it is 0:'))

print('the positive numbers are : ', end=' ')
for i in range(len(nums)):
    if nums[i] < 0:
        print(nums[i], end=' ')
print()

print('the negative numbers are : ', end=' ')
for i in range(len(nums)):
    if nums[i] > 0:
        print(nums[i], end=' ')
print()

print('The total is', sum(nums))
print('The average is', sum(nums) / len(nums))

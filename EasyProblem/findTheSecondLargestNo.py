list = [1,2,3,4,5,6]
# #brute force
# def secondLargest(list):
#     list.sort()
#     return list[-2]
# print(f'the second largest number is : {secondLargest(list)}')


#second way

def secondLargest(list):
    secondLargest = -float("inf")
    largest = -float("inf")
    for i in list:
        if largest<i:
            largest=i
    
    for p in list:
        if secondLargest < p and p !=largest:
            secondLargest = p
    print(f'second largest number is : {secondLargest}')
secondLargest(list)
def find_zero_sum(nums) :
    if len(nums) < 3 :
        print("Array Input Length Must More Than 2")

    triplets = []
    nums.sort()

    for i in range(len(nums) - 2) :
        if i > 0 and nums[i] == nums[i-1] :
            continue

        left, right = i + 1, len(nums) - 1 

        while left < right :
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0 :
                triplets.append([nums[i], nums[left], nums[right]])

                left += 1
                while left < right and nums[left] == nums[left - 1] :
                    left += 1

            elif current_sum < 0 :
                left += 1
            
            else :
                right -= 1
    
    return triplets

input_str = input("Enter Your List : ")
numbers = [int(num) for num in input_str.split()]

result = find_zero_sum(numbers)

if len(numbers) > 3 :
    print(result)
else :
    print("")

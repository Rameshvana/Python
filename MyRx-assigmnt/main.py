def sortedSquares(nums):
    squared_nums = [num ** 2 for num in nums]
    return squared_nums.sort()

nums = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(sortedSquares(nums))
print(15**2)


def simpleSortColors(nums):
    countR = nums.count('R')
    countG = nums.count('G')
    countB = nums.count('B')
    
    sorted_nums = ['B'] * countB + ['G'] * countG + ['R'] * countR
    return sorted_nums

# Example usage
nums = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
sorted_nums = simpleSortColors(nums)
print(sorted_nums)


def find_max_platforms(arrival_times, departure_times):
    arrival_times.sort()
    departure_times.sort()

    max_platforms = 0
    current_platforms = 0

    arrival_index = 0
    departure_index = 0

    while arrival_index < len(arrival_times) and departure_index < len(departure_times):
        if arrival_times[arrival_index] <= departure_times[departure_index]:
            current_platforms += 1
            arrival_index += 1
        else:
            current_platforms -= 1
            departure_index += 1

        max_platforms = max(max_platforms, current_platforms)

    return max_platforms
            

  


arr = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]

dep = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

arr_minutes = [int(t.split(':')[0]) *60 + int(t.split(':')[1]) for t in arr]

dep_minutes = [int(t.split(':')[0]) *60 + int(t.split(':')[1]) for t in dep]

arr2 = ["09:00", "09:40"]

dep2 = ["09:10", "12:00"]

arr2_minutes = [int(t.split(':')[0]) *60 + int(t.split(':')[1]) for t in arr2]

dep2_minutes = [int(t.split(':')[0]) *60 + int(t.split(':')[1]) for t in dep2]


result1 = find_max_platforms(arr_minutes, dep_minutes)
result2 = find_max_platforms(arr2_minutes, dep2_minutes)
print("Maximum platforms needed for first set of trains:", result1)
print("Maximum platforms needed for second set of trains:", result2)


my_dict = {101: 'John Doe', 102: 'Jane Smith', 103: 'Peter Johnson'}

sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict_by_values)
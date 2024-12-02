import math
 

def valid(per_day, task, d):
 
 
    cur_day = 0
    for index in range(0, len(task)):
 
        day_req = math.ceil((task[index]) / (per_day))
 
        cur_day += day_req
 

        if (cur_day > d):
            return False
 

    return cur_day <= d

def minimumTask(task, d):
 
    left = 1
    right = 1e9 + 7
 
    for index in range(0, len(task)):
        right = max(right, task[index])
 
    # Variable to store answer
    per_day_task = 0
 
    while (left <= right):
 
        mid = left + (right - left) // 2
 

        if (valid(mid, task, d)):
            per_day_task = mid
            right = mid - 1
 
        else:
            left = mid + 1
 
    # Print answer
    return math.trunc(per_day_task)
 

task = [3, 4, 7, 15]
D = 10
 
print(minimumTask(task, D))
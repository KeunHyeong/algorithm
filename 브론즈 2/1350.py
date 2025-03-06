#1350
import math

def solutions():
    N = int(input())
    input_arr = list(map(int, input().split()))
    disk = int(input())

    cluster_count = 0
    for size in input_arr:
        if size > 0:
            cluster_count += math.ceil(size/disk)
        
    print(cluster_count * disk)

solutions()

# def solutions():
#     N = int(input())
#     input_arr = list(map(int, input().split()))
#     disk = int(input())

#     cluster_count = 0
#     for i in input_arr:
#         if i != 0:
#             if i <= disk and i != 0:
#                 cluster_count += 1
#             else:
#                 j = 0
#                 while i > disk * j:
#                     cluster_count += 1
#                     j+=1
    
#     print(disk * cluster_count)

# solutions()
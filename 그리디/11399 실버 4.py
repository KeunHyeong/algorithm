N = int(input())
peoples = list(map(int, input().split()))

peoples.sort()

current_time = 0
total_time = 0
for time in peoples:
    current_time += time
    total_time += current_time

print(total_time)

    
#5800

def solutions():
    K = int(input())
    
    grades = []
    for i in range(K):
        input_data = input().split()
        row = []
        for j in range(1, int(input_data[0]) + 1):
            row.append(int(input_data[j]))
        
        row.sort(reverse=True)
        grades.append(row)
    
    idx = 0
    for row in grades:
        gap = 0
        idx += 1
        for i in range(len(row) - 1):
            if gap < row[i] - row[i+1]:
                gap = row[i] - row[i+1]
        print(f"Class {idx}")
        print(f"Max {max(row)}, Min {min(row)}, Largest gap {gap}")

solutions()

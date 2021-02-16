# Exam _ Soal No 2
# 
# Problem 2 - List Spinner (30 Points)
# Create a return function with 1 argument that can rotate the list of numbers (Round 1X counter-clockwise) as described below.

# Initial List

# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# [13, 14, 15, 16]]
# Function

# Output:

# [[4, 8, 12, 16]
# [3, 7, 11, 15],
# [2, 6, 10, 14],
# [1, 5, 9, 13]]

# # Function Initialization# 

Angka = [
    [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
]

print(Angka)

def counterClockwise():
    try:
       Angka=[]
       for j in range(len(Angka)):
           clockwise=[]
           for i in range(len(Angka)-1,-1,-1): 
               clockwise.append(Angka[i][j])
           Angka1.append(clockwise)
           return Angka1
       else:
           kata = kalimat.split(' ')
           for k in kata:
               print(k[::-1], end=' ') 
    except:
        print("Hanya Menerima Angka")

print(counterClockwise())


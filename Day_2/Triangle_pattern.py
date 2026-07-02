
#make trangle 
"""output:
    1 
   1 2 
  1 2 3 
 1 2 3 4"""
 
for i in range(1, 4 + 1):
    print(" " * (4 - i), end="")
    
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()

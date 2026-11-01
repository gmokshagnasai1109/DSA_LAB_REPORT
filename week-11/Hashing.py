#CSE25111, Mokshagnasai
size = 10 
chain = [[] for i in range(size)] 
 
def separate_chaining(key): 
    index = key % size 
    chain[index].append(key) 
 
linear = [None] * size 
 
def linear_probing(key): 
    index = key % size 
    while linear[index] is not None: 
        index = (index + 1) % size 
    linear[index] = key 
 
quadratic = [None] * size 
 
def quadratic_probing(key): 
    index = key % size 
    i = 0 
    while i < size: 
        new_index = (index + i * i) % size 
        if quadratic[new_index] is None: 
            quadratic[new_index] = key 
            return 
        i += 1 
    print("Hash table is full") 

print("cse25111, Mokshagnasai") 
n = int(input("Enter number of elements: ")) 
keys = [] 
 
for i in range(n): 
    key = int(input("Enter key: ")) 
    keys.append(key) 
    separate_chaining(key) 
    linear_probing(key) 
    quadratic_probing(key) 
 
print("\nSeparate Chaining:") 
for i in range(size):  
    print(i, ":", chain[i]) 
print("\nLinear Probing:") 
print(linear) 
print("\nQuadratic Probing:") 
print(quadratic)




# arr=[2,3,4,5,6,7]

#square


# list comprehension to find square

# square=[num**2 for num in arr]


# print(square)


# cubes=[num**3 for num in arr]

# print(cubes)

# odd_num=[num for num in arr if num%2!=0]

# print(odd_num)

# even=[num for num in arr if num%2==0]
# print(even)

# num_graterthan5=[num for num in arr if num>5]
# print(num_graterthan5)

#mapping  no condition is present

# map_num=[num-1 if num>5 else num+1 for num in arr]
# print(map_num)


text=["apple","iphone","orange","potatto"]

#words starting with vowels

vowels_word=[ch for ch in text if ch=="a,e,i,o,u"]
print(vowels_word)
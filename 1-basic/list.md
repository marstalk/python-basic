# Python List Examples

## Basic List Operations

### Creating a List
```python
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
```

### Accessing List Elements
```python
# Accessing elements by index
first_number = numbers[0]  # 1
second_fruit = fruits[1]   # "banana"
```

### Modifying List Elements
```python
# Changing an element by index
numbers[2] = 10  # numbers is now [1, 2, 10, 4, 5]
```

### Adding Elements to a List
```python
# Using append() to add an element at the end
numbers.append(6)  # numbers is now [1, 2, 10, 4, 5, 6]

# Using insert() to add an element at a specific position
fruits.insert(1, "blueberry")  # fruits is now ["apple", "blueberry", "banana", "cherry"]
```

### Removing Elements from a List
```python
# Using remove() to remove a specific element
numbers.remove(10)  # numbers is now [1, 2, 4, 5, 6]

# Using pop() to remove an element by index
last_fruit = fruits.pop()  # "cherry", fruits is now ["apple", "blueberry", "banana"]
```

## Advanced List Operations

### List Comprehensions
```python
# Creating a list of squares
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Filtering with List Comprehensions
```python
# Creating a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Nested List Comprehensions
```python
# Creating a 2D list (matrix)
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

### Using `map` and `filter`
```python
# Using map to apply a function to all elements
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Using filter to filter elements
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### List Slicing
```python
# Slicing a list
sublist = numbers[1:4]  # [2, 3, 4]
```

### List Methods
```python
# Using sort() to sort a list
numbers.sort()  # [1, 2, 3, 4, 5]

# Using reverse() to reverse a list
numbers.reverse()  # [5, 4, 3, 2, 1]
```

### Combining Lists
```python
# Using + operator to concatenate lists
combined_list = numbers + fruits  # [5, 4, 3, 2, 1, "apple", "blueberry", "banana"]
```

### List Unpacking
```python
# Unpacking list elements into variables
a, b, c, d, e = numbers  # a=5, b=4, c=3, d=2, e=1
```

---
sum(list)
len(list)

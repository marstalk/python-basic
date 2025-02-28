# Python Arrays

## Basic Usage

In Python, arrays can be created using the `array` module. Here is an example of how to create and use an array:

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

# Modify elements
arr[1] = 10
print(arr)  # Output: array('i', [1, 10, 3, 4, 5])
```

## Advanced Usage

### Array Operations

You can perform various operations on arrays such as appending, inserting, and removing elements:

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Append an element
arr.append(6)
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Insert an element at a specific position
arr.insert(2, 7)
print(arr)  # Output: array('i', [1, 2, 7, 3, 4, 5, 6])

# Remove an element
arr.remove(4)
print(arr)  # Output: array('i', [1, 2, 7, 3, 5, 6])
```

### Array Slicing

You can also slice arrays to get a subset of elements:

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slice the array
sub_arr = arr[2:5]
print(sub_arr)  # Output: array('i', [3, 4, 5])

# Slice with step
sub_arr_step = arr[1:10:2]
print(sub_arr_step)  # Output:
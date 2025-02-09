# Python String Usage Samples

## Basic String Operations

### Creating Strings
```python
# Single quotes
single_quote_str = 'Hello, World!'

# Double quotes
double_quote_str = "Hello, World!"

# Triple quotes for multi-line strings
multi_line_str = '''Hello,
World!'''
```


### String Concatenation
```python
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + ", " + str2 + "!"
print(concatenated_str)  # Output: Hello, World!
```

### String Formatting
```python
name = "Alice"
age = 30

# Using f-strings (Python 3.6+)
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)  # Output: My name is Alice and I am 30 years old.

# Using format() method
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Output: My name is Alice and I am 30 years old.
```

### String Methods
```python
sample_str = "hello, world!"

# Convert to uppercase
upper_str = sample_str.upper()
print(upper_str)  # Output: HELLO, WORLD!

# Convert to lowercase
lower_str = sample_str.lower()
print(lower_str)  # Output: hello, world!

# Capitalize the first letter
capitalized_str = sample_str.capitalize()
print(capitalized_str)  # Output: Hello, world!

# Replace a substring
replaced_str = sample_str.replace("world", "Python")
print(replaced_str)  # Output: hello, Python!
```

## Advanced String Operations

### String Slicing
```python
sample_str = "Hello, World!"

# Get substring from index 0 to 4
substring = sample_str[0:5]
print(substring)  # Output: Hello

# Get substring from index 7 to the end
substring = sample_str[7:]
print(substring)  # Output: World!

# Get substring with negative indices
substring = sample_str[-6:-1]
print(substring)  # Output: World
```

### String Splitting and Joining
```python
sample_str = "apple,banana,cherry"

# Split string into a list
fruits_list = sample_str.split(',')
print(fruits_list)  # Output: ['apple', 'banana', 'cherry']

# Join list into a string
joined_str = ', '.join(fruits_list)
print(joined_str)  # Output: apple, banana, cherry
```

### String Encoding and Decoding
```python
sample_str = "Hello, World!"

# Encode string to bytes
encoded_str = sample_str.encode('utf-8')
print(encoded_str)  # Output: b'Hello, World!'

# Decode bytes to string
decoded_str = encoded_str.decode('utf-8')
print(decoded_str)  # Output: Hello, World!
```

### Regular Expressions
```python
import re

sample_str = "The rain in Spain"

# Find all occurrences of 'ai'
matches = re.findall(r'ai', sample_str)
print(matches)  # Output: ['ai', 'ai']

# Search for the first occurrence of 'ai'
match = re.search(r'ai', sample_str)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")  # Output: Found 'ai' at position 5
```

### String Checking Methods
```python
sample_str = "Hello, World!"

# Check if string starts with a substring
starts_with_hello = sample_str.startswith("Hello")
print(starts_with_hello)  # Output: True

# Check if string ends with a substring
ends_with_world = sample_str.endswith("World!")
print(ends_with_world)  # Output: True

# Check if all characters in the string are alphabetic
is_alpha = sample_str.replace(",", "").replace(" ", "").isalpha()
print(is_alpha)  # Output: False

# Check if all characters in the string are digits
is_digit = sample_str.isdigit()
print(is_digit)  # Output: False
```

### String Trimming
```python
sample_str = "   Hello, World!   "

# Trim whitespace from both sides
trimmed_str = sample_str.strip()
print(trimmed_str)  # Output: Hello, World!

# Trim whitespace from the left side
left_trimmed_str = sample_str.lstrip()
print(left_trimmed_str)  # Output: Hello, World!   

# Trim whitespace from the right side
right_trimmed_str = sample_str.rstrip()
print(right_trimmed_str)  # Output:    Hello, World!
```

### String Alignment
```python
sample_str = "Hello"

# Center align the string
center_aligned_str = sample_str.center(20, '-')
print(center_aligned_str)  # Output: -------Hello--------

# Left align the string
left_aligned_str = sample_str.ljust(20, '-')
print(left_aligned_str)  # Output: Hello---------------

# Right align the string
right_aligned_str = sample_str.rjust(20, '-')
print(right_aligned_str)  # Output: ---------------Hello
```

### String Casefolding
```python
sample_str = "Hello, World!"

# Casefold the string (more aggressive than lower)
casefolded_str = sample_str.casefold()
print(casefolded_str)  # Output: hello, world!
```

### String Partitioning
```python
sample_str = "Hello, World!"

# Partition the string into three parts
part1, separator, part2 = sample_str.partition(',')
print(part1)      # Output: Hello
print(separator)  # Output: ,
print(part2)      # Output:  World!
```

### String Zfill
```python
sample_str = "42"

# Pad the string with zeros
zero_filled_str = sample_str.zfill(5)
print(zero_filled_str)  # Output: 00042
```

### String Translation
```python
sample_str = "hello world"

# Create a translation table
translation_table = str.maketrans("hlo", "HLO")

# Translate the string
translated_str = sample_str.translate(translation_table)
print(translated_str)  # Output: HeLLO wOrLd
```

### String Count
```python
sample_str = "hello world"

# Count occurrences of a substring
count_l = sample_str.count('l')
print(count_l)  # Output: 3
```

### String Find and Index
```python
sample_str = "hello world"

# Find the first occurrence of a substring
first_occurrence = sample_str.find('o')
print(first_occurrence)  # Output: 4

# Find the first occurrence of a substring (raises ValueError if not found)
first_occurrence_index = sample_str.index('o')
print(first_occurrence_index)  # Output: 4
```
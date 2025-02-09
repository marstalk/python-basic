single_quote = 'hello'

double_quote = "hello"

multiple_line = '''hello
world''';

print(single_quote)
print(double_quote)
print(multiple_line)


print('hello' + 'world')
print(single_quote + 'world')
print(double_quote + multiple_line)

print(f"formate string {single_quote} world")

formatted_string = f"formatted string {single_quote} world"
print(formatted_string)

# in java: String.format("formatted string %s world", single_quote)
# in rust: format!("formatted string {} world", single_quote)
# in java log: log.info("formatted string {} world", single_quote)

# %s, %f, %d, %i, {}, {variable_name}, ${variable_name}, 

# Methods
sample_str = "hello world"
print(sample_str.upper())
print(sample_str.lower())

## in java: "hello world".toUpperCase(), toLowerCase()
## in rust: "hello world".to_uppercase(), to_lowercase()

## capitalize
print(sample_str.capitalize())
## no such metho in java, rust

## replace all!!!
sample_str = "hello world, world"
print(sample_str.replace("world", "python"))


# slice
sample_str = "hello world"
print(sample_str[0])
print(sample_str[0:5])
print(sample_str[-5:]) # equals to print(sample_str[6:11])

print(f"mark {sample_str[-5:1]}")

## in rust: &sample_str[0..5], &sample_str[6..11]
## in java: sample_str.substring(0, 5), sample_str.substring(6, 11)

# split
sample_str = "apple,banana,orange"
fruits = sample_str.split(",")
print(fruits)
print(fruits[0:2])
print(fruits[-1:]) # return list
print(fruits[-1]) # return string

## in rust: sample_str.split(",").collect::<Vec<&str>>(), just borrow.
## in java: sample_str.split("\\s+")

# join
joined_str = "+".join(fruits)
print(joined_str)

## in java: String.join("+", fruits)
## in rust: fruits.join("+")


# encoding
sample_str = "hello world"
encoded_str = sample_str.encode("utf-8")
print(encoded_str)
print(encoded_str.decode("utf-8"))

## in java: "sss".getBytes("utf-8");
## in rust: "sss".as_bytes()

import re
sample_str = "The rain in Spain"

matches = re.findall(r"\b\w*ai\w*\b", sample_str)
print(matches)

## in java: Pattern.compile("\\b\\w*ai\\w*\\b").matcher(sample_str).find()
## in rust: Regex::new(r"\b\w*ai\w*\b").unwrap().find(sample_str).is_some()

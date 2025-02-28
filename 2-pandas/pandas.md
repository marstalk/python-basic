

```python
import pandas as pd

some_dataset = pd.read_csv("path/to/csv/file");
some_dataset.head();
some_dataset.


```

pd.read_csv('data.csv', delimiter=',', encoding='utf-8', nrows=100, usecols=['name', 'age'])
1. path to file
2. delimiter: specify column separator(default is comma)
3. encoding, default utf-8
4. nrows: read only the first N rows
5. usecols: select specific columns

---
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

sheet_name

---
# Data Structure - Series
Think of Series like a single column of data in the spreadsheet
```python
pd.Series([], name="ss")
```
Key features:
1. single dimensional(list a Python list but with labeled indices)
2. can hold any data type
3. default index but can be customized.

```python
pd.Series([], index=["a", "b", "C"])
```

---
# Data Structure - DataFrame
A DataFrame just like a spreadsheet or a SQL table, consist of mulpile Series.
two dimensional data structure.
```python
data = {
    "name": [],
    "Age": [],
    "Score": []
}
df = pd.DataFrame(data)

df["name"] # returns a Series

```

key features:
1. two-dimensinal
2. each columns is a Series
3. can handle missing value/large datasets.


---
# Ways to query data in DataFrame/Series

## df["<COLUMN>"] is a Series, but can be treated as a instance of it's item type.
can perform basic operation */+- with basic types then retuen a Series.
Series */+- Series return Series
```py
df[df["a"] == "b"] # df['Department'] == 'IT' creates a boolean mask.

sr[sr > 100]
```


## python(sql) like expression: **Recommendation**
```py
df.query("Salary > 70_000 and Department == 'IT'")
```
Series doesn't support query.

like: 
```py
org_df.query("<COLUMN>.str.contains('Sons')")
```

## groupby

### multiple aggregation, agg() return a **DataFrame**
```py
org_df.groupby("<COLUMN>")
    .agg(
        custom_name = ("<COLUMN", "mean/max/min/sum.."),
        custom_name = (),
    )
    .sort_values(by="<COLUMN>", ascending=False)
```


### single aggregation, return a **Series**
```py
sales_df.groupby("Customer_Segment")["Profit"].mean()
```

### custom functions
```py
sales_df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Profit_to_Sales_Ration = ("Profit", lambda x: x.sum() / sales_df["Sales"].sum())
)
```


## idxmax
```python
print(sales_df["Date"].dtype)
# Date is object, change to DateTime
sales_df["Date"] = pd.to_datetime(sales_df["Date"])
print(sales_df["Date"].dtype)
# now it's datetime
daily_sales_sr = sales_df.groupby("Date")["Sales"].sum()
print(daily_sales_sr)
print(type(daily_sales_sr))
# use idxmax() to return it's label of max value item in Series
print(f"highest_sales_day: {daily_sales_sr.idxmax()}")
```


## .rolling: 
1. use DateTime as key(ID) in a Series
2. Calculate the 7-Day Moving Average: Use the rolling() method with a window of 7 days and then apply the mean() function
```py
# moving average
Series.rolling(window=7).mean()
```


## .nlargest(int, columns) : select * from table order by <ColummA>, <ColumnB> desc limit N.


## df = df.reset_index() : add a new index column starting from zero

## df.describe() basic math operation on number type of Series.


## .loc["<LABEL>"] return Series of a row.
sr.loc


## 

# read_sql
1. fetch all data into memory, can use chunk to optimize performance.


# settingWithCopyWarning

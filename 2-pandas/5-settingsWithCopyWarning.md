# 
get and set chain operation > settingWithCopyWarning

# detail

pandas不允许先筛选出dataframe，再进行修改写入，否则会settingWithCopyWarning

一单出现这个告警，set 有可能成功也有可能失败。

df[][] = xx
这里的df[][]涉及到a chain operation contais get and set:
1. get: df[]
2. set df[][] = 

so, here will throw settingsWithCopyWarning, to resolve this:

```py
df.loc[aa, bb] = xx
```
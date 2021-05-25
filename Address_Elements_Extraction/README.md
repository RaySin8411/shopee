# Useful Module

## pandarallel
python多進程最常用的幾種方式

1. multiprocessing
2. concurrent.futures.ProcessPoolExecutor()
3. joblib
4. ppserver
5. 對於經常使用pandas的人非常友好的一個工具pandarallel

没有并行化 |	通过并行化
--- | ---
df.apply(func)|df.parallel_apply(func)
df.applymap(func)|df.parallel_applymap(func)
df.groupby(args).apply(func)|df.groupby(args).parallel_apply(func)
df.groupby(args1).col_name.rolling(args2).apply(func)|df.groupby(args1).col_name.rolling(args2).parallel_apply(func)
series.map(func)|series.parallel_map(func)
series.apply(func)|series.parallel_apply(func)
series.rolling(args).apply(func)|series.rolling(args).parallel_apply(func)


## pyahocorasick

### AC自動機演算法
1. 用於在輸入的一串字串中匹配有限組「字典」中的子串。

2. 它與普通字串匹配的不同點在於同時與所有字典串進行匹配。

3. 演算法均攤情況下具有近似於線性的時間複雜度，約為字串的長度加所有匹配的數量。

    然而由於需要找到所有匹配數，如果每個子串互相匹配（如字典為a，aa，aaa，aaaa，輸入的字串為aaaa），演算法的時間複雜度會近似於匹配的二次函式。

```python
import ahocorasick

checkwords = ["英文", "英国", "英国人", "希腊", "瑞典", "瑞士"]
query = "一个英国人在瑞典，一个美国人在丹麦。"

A = ahocorasick.Automaton()
for index, word in enumerate(checkwords):
    A.add_word(word, (index, word))
A.make_automaton()
# A可以用pickle.dump()和load()方法保存到本地并读取

for i in A.iter(query):
    print(i)    
# (3, (1, '英国'))  
# (4, (2, '英国人'))
# (7, (4, '瑞典'))
# 每一项都是 (end_index, value)，其中end_index是匹配到的字符串末尾在query中的位置索引
```

## Reference
* [加速pandas](https://www.yuque.com/7125messi/wydusr/wweetn#articleHeader6)
* [简单粗暴进行中文文本匹配的Python代码片段](https://sighsmile.github.io/2017-05-11-string-pattern-matching-snippet/)
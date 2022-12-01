# advent-of-code-2022
Advent of Code 2022



## Tips

### Group by empty lines

Given input like

```
1000
2000

1000
2333

44454
```

Group by empty line using

```python
>>> data.split("\n\n")
["1000\n2000", "1000\n23333", "44454"]
```

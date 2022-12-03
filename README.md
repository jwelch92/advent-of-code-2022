# advent-of-code-2022
Advent of Code 2022

## Workflow

First, add session cookie to `.session`. 

Adding a new day

```bash
poetry shell
./lib.py DAY
# creates day_02.py from template.py.txt
./lib.py 2
```

Watch files shortcut

```bash
./watch DAY
# Watch day_01.py running main() function
./watch 1
```

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


### Itertools

See https://docs.python.org/3/library/itertools.html and https://pypi.org/project/more-itertools/

More itertools builds on itertools to provide things like sliding windows, grouping, augmenting, combining, etc.

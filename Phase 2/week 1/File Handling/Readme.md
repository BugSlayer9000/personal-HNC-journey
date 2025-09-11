# 🔹 Part 1: File Handling in Python (HNC-Level + Level 8 Add-ons)

## 1. Opening & Closing Files
```python
f = open("data.txt", "r")  # "r" = read mode
content = f.read()
f.close()
```

**Tips**
- Use .readlines() if you want the raw file (newlines included).
- Use .splitlines() if you want just the text, without worrying about platform differences.


**Modes:**
- `"r"` = read  
- `"w"` = write (overwrites)  
- `"a"` = append  
- `"b"` = binary  
- `"x"` = create new file, fail if exists  

---

## 2. Best Practice: `with` Statement
```python
with open("data.txt", "r") as f:
    content = f.read()
# file auto-closes here
```

---

## 3. Reading Data
```python
f.read()        # whole file
f.readline()    # one line
f.readlines()   # list of all lines
```

---

## 4. Writing Data
```python
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])
```

---

## 5. Working with Paths
```python
from pathlib import Path

path = Path("folder") / "file.txt"
with open(path, "r") as f:
    print(f.read())
```

---

## 6. Exception Handling
```python
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
```

---

## 7. File Pointers (`seek` / `tell`)
```python
with open("data.txt", "r") as f:
    print(f.read(5))  # read 5 chars
    print(f.tell())   # current position
    f.seek(0)         # reset pointer
```

---

## 8. Level 8 Concepts

### CSV Handling
```python
import csv

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### JSON Handling (common in APIs & configs)
```python
import json

with open("data.json") as f:
    data = json.load(f)
```

### Pickle (serialization)
```python
import pickle

data = {"x": 1, "y": 2}
with open("save.pkl", "wb") as f:
    pickle.dump(data, f)
```

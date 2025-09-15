# 📂 JSON File Handling in Python

## 1. What is JSON?

- **JSON** = JavaScript Object Notation  
- A text-based format for representing structured data  
- Think of it as a portable **dictionary + list combo** written to disk  
- Widely used in **APIs, databases, configs**, etc.  

### Example JSON
```json
{
  "students": [
    {"id": 1, "name": "Sam", "course": "HNC Computing"},
    {"id": 2, "name": "Alex", "course": "HND Software Development"}
  ]
}
```

---

## 2. Python’s JSON Module

### Import
```python
import json
```

### 🔹 Writing (Create/Overwrite)
```python
data = {"course": "HNC Software Development", "level": 7}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 → pretty printing
```

### 🔹 Reading
```python
with open("data.json", "r") as f:
    data = json.load(f)
print(data)  # dict
```

### 🔹 Appending (Read → Modify → Write Back)
```python
with open("data.json", "r") as f:
    data = json.load(f)

data["level"] = 8   # add/update

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### 🔹 Deleting Data
```python
del data["level"]   # remove a key
```

### 🔹 Nested Structures
- JSON supports:
  - **Dictionaries** (`{}`)
  - **Lists** (`[]`)
  - **Strings, numbers, booleans, null**

#### Example
```json
{
  "users": [
    {"id": 1, "name": "Alice", "roles": ["admin", "editor"]},
    {"id": 2, "name": "Bob", "roles": ["viewer"]}
  ]
}
```

---

## 3. Error Handling (Level 8+)

Always anticipate:

- `FileNotFoundError` → if file doesn’t exist  
- `json.JSONDecodeError` → if JSON is invalid  

### Example
```python
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found.")
    data = {}
except json.JSONDecodeError:
    print("Corrupted JSON.")
    data = {}
```

# 📘 CSV File Handling in Python (HNC Level 7 + Level 8 Add-ons)

## 🔹 Topics Covered

-   What is a CSV file?\
-   Python's `csv` module\
-   Reading CSV files (`csv.reader`)\
-   Writing CSV files (`csv.writer`)\
-   Working with Dictionaries (`csv.DictReader`, `csv.DictWriter`)\
-   Level 8 Extensions (advanced concepts)

------------------------------------------------------------------------

## 1. What is a CSV file?

-   **CSV = Comma-Separated Values**\
-   Plain text file storing data in rows and columns.\
-   **Each line = one record**\
-   **Each value = one field**, separated by `,` (sometimes `;` or
    `\t`).

**Example (`students.csv`):**

``` csv
id,name,grade
1,Alice,A
2,Bob,B
3,Charlie,C
```

-   Think of it as a **mini spreadsheet**.

------------------------------------------------------------------------

## 2. Python's `csv` module

-   Built-in library in Python.\
-   Helps with:
    -   Reading CSVs line by line.\
    -   Writing new rows.\
    -   Handling delimiters, quotes, etc.

------------------------------------------------------------------------

## 3. Reading a CSV File (HNC Level 7)

-   Use `csv.reader` to open and read rows.\
-   Each row is returned as a **list of strings**.\
-   Typically loop through rows for processing.

------------------------------------------------------------------------

## 4. Writing to a CSV File

-   Use `csv.writer`.\
-   Add rows **one by one** → `writer.writerow()`\
-   Add **multiple rows** → `writer.writerows()`

------------------------------------------------------------------------

## 5. Working with Dictionaries

-   Instead of lists, use dictionaries:
    -   `csv.DictReader` → reads rows as dictionaries (keys = column
        headers).\
    -   `csv.DictWriter` → writes rows using dictionaries.\
-   Advantage: No need to remember index positions.

------------------------------------------------------------------------

## 6. Level 8 Extensions

-   Handle different delimiters (`;`, `\t`).\
-   Add error handling (`try/except` for malformed files).\
-   Work with large CSVs (streaming vs. loading all at once).\
-   Convert CSV → JSON or SQL database.\
-   Data validation before saving (e.g., grade must be `A–F`).

# Custom CSV Reader & Writer

## Overview & Objective

This project implements a **custom CSV (Comma-Separated Values) reader and writer from scratch in Python**. The goal is to understand the low-level mechanics of CSV parsing and serialization, a fundamental skill for data engineers working with diverse text-based datasets, including non-standard or malformed files.

By building your own parser, you will:

- Learn **file I/O**, **string manipulation**, and **state-based parsing**.
- Understand how standard libraries like Python's `csv` module handle complex CSV data.
- Handle common edge cases, including:
  - Fields with commas
  - Quoted fields
  - Escaped quotes (`""`)
  - Newlines inside quoted fields

The project also includes **benchmarking** to measure read and write performance against Python’s standard CSV library, using a dataset with 10,000+ rows.

---

## Core Features

### Reader (`CustomCsvReader`)

- Implemented as an **iterator class** (`__iter__` and `__next__`).
- Reads CSV files **line by line**, without loading the entire file into memory.
- Correctly parses:
  - Comma-delimited fields
  - Quoted fields
  - Escaped double quotes
  - Newlines inside quoted fields

### Writer (`CustomCsvWriter`)

- Implemented as a **class** that writes a list of lists to CSV.
- Automatically quotes fields containing commas, quotes, or newlines.
- Escapes internal quotes correctly by doubling them (`""`).

### Benchmarking

- Compares performance of custom reader/writer against Python’s built-in `csv.reader` and `csv.writer`.
- Uses a synthetically generated CSV with 10,000+ rows and 5 columns.
- Presents and analyzes results in a clear, reproducible manner.

---

## Expected Outcomes

- A **working Python module** with `CustomCsvReader` and `CustomCsvWriter`.
- Correct parsing and writing of CSV files, including all edge cases.
- **Benchmark results** demonstrating performance differences with Python’s standard library.
- Clean, well-structured, and well-documented code adhering to **PEP 8**.


## 📁 Project Structure

```

csv-parser-solved-23P31A0528/
│
├── README.md           # Project documentation
├── custom_csv.py       # Implementation of CustomCsvReader & CustomCsvWriter
├── requirements.txt    # Dependencies for the project
├── benchmark.py        # Script to benchmark custom vs built-in CSV reader/writer
├── test.csv            # Sample CSV file covering edge cases (quotes, commas, newlines)
├── test_reader.py      # Script to test CustomCsvReader functionality
└── test_writer.py      # Script to test CustomCsvWriter functionality

```

### Notes:
- `custom_csv.py` contains all core classes.
- `benchmark.py` generates large datasets and compares performance.
- `test_reader.py` and `test_writer.py` are provided to verify the correctness of the implementation. Evaluators can replace the test file in these scripts with their own CSV files to run their own test cases.
- `test.csv` contains diverse edge cases for testing (commas, quotes, multiline fields).
```
```
## 🚀 Clear Instructions for Evaluators: Setup & Running the Code

These instructions guide you to set up the environment and test the implementation using **your own CSV files or test suites**.

---
### 1.Clone the Repository

```bash
git clone https://github.com/<your-username>/csv-parser-solved-23P31A0528.git
cd csv-parser-solved-23P31A0528
```
---

### 2.Create and Activate a Python Virtual Environment

```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

---

### 3.Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The core reader/writer does **not require external libraries**, but `pytest` is included if you want to run tests.

---

### 4.Accessing the Custom CSV Reader and Writer

Your test suite can use the classes **directly from `custom_csv.py`**:

```python
from custom_csv import CustomCsvReader, CustomCsvWriter
```

* No installation or extra setup is needed.
* `custom_csv.py` is in the root folder, so Python can import it directly.

---

### 5.Testing Your Own CSV Files

#### Using `CustomCsvReader`:

```python
with open("your_test_file.csv", "r", encoding="utf-8", newline="") as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)  # Each row is a list of strings
```

* Correctly handles:

  * Comma-separated fields
  * Quoted fields
  * Escaped quotes (`""`)
  * Newlines inside quoted fields

#### Using `CustomCsvWriter`:

```python
data = [
    ["Header1", "Header2", "Header3"],
    ["Value1", "Value, with comma", "Value3"],
    ['Field "with quotes"', "Value2", "Value3"],
    ["Multi\nLine Field", "Value2", "Value3"]
]

with open("output_file.csv", "w", encoding="utf-8", newline="") as f:
    writer = CustomCsvWriter(f)
    writer.writerows(data)
```

* Automatically quotes fields when necessary.
* Escapes internal quotes correctly.
* Produces **well-formed CSV files** that can be read by any standard CSV parser.

---

### 6.Running Benchmarks (Optional)

```bash
python benchmark.py
```

* Measures performance of `CustomCsvReader/Writer` vs Python’s built-in `csv.reader` and `csv.writer`.
* Works with the synthetic 10,000-row dataset or any CSV file you provide.
* Output shows read/write timings for comparison.

---

### 7.Notes for Evaluators

* Replace `"your_test_file.csv"` with any file from your test suite.
* Always open files with `newline=""` when reading/writing to handle cross-platform newlines correctly.
* The implementation **fully supports edge cases**: commas, quotes, escaped quotes, and multiline fields.
* Works efficiently with **large files** because reading is done row by row (streaming).
* To test your own CSV files with this implementation, **place your test files inside the repository** or provide a correct relative or absolute path when opening the file.  

## Usage Examples

These examples demonstrate how to use `CustomCsvReader` and `CustomCsvWriter` with any CSV file, including tricky edge cases.

---

### 1.Reading CSV using CustomCsvReader

```python
from custom_csv import CustomCsvReader

# Open a CSV file (replace "input.csv" with your file)
with open("input.csv", "r", encoding="utf-8", newline="") as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)  # Each row is returned as a list of strings
```

**Features handled:**

* Comma-separated fields
* Fields enclosed in quotes
* Escaped quotes (`""`) inside fields
* Newlines inside quoted fields

**Sample input (`input.csv`):**

```
Name,Age,City,Notes
Alice,30,New York,"Line1
Line2"
"Bob, Jr.",25,San Francisco,"Contains a comma, and ""quotes"""
```

**Sample output:**

```python
['Name', 'Age', 'City', 'Notes']
['Alice', '30', 'New York', 'Line1\nLine2']
['Bob, Jr.', '25', 'San Francisco', 'Contains a comma, and "quotes"']
```

---

### 2.Writing CSV using CustomCsvWriter

```python
from custom_csv import CustomCsvWriter

data = [
    ["Name", "Age", "City", "Notes"],
    ["Alice", "30", "New York", "Line1\nLine2"],
    ["Bob, Jr.", "25", "San Francisco", 'Contains a comma, and "quotes"']
]

# Write to a CSV file
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = CustomCsvWriter(f)
    writer.writerows(data)
```

**Key features:**

* Automatically quotes fields containing commas, quotes, or newlines
* Escapes internal quotes (`"` → `""`)
* Produces valid CSV that can be read by any standard CSV reader

**Output in `output.csv`:**

```
Name,Age,City,Notes
Alice,30,New York,"Line1
Line2"
"Bob, Jr.",25,San Francisco,"Contains a comma, and ""quotes"""
```

---

### 3.Using Your Own CSV Files

Evaluators can replace `"test.csv"` with **any CSV file from their test suite**:

```python
from custom_csv import CustomCsvReader, CustomCsvWriter

with open("evaluator_test.csv", "r", encoding="utf-8", newline="") as f:
    reader = CustomCsvReader(f)
    for row in reader:
        print(row)
```

```python
with open("evaluator_output.csv", "w", encoding="utf-8", newline="") as f:
    writer = CustomCsvWriter(f)
    writer.writerows([...])  # Replace with your own data
```

> ✅ These examples demonstrate full functionality and correctness, including edge cases, for both reading and writing CSV files.

## 📊 Benchmark

This section demonstrates the performance of `CustomCsvReader` and `CustomCsvWriter` compared to Python’s built-in `csv` module.

---

### 1.Running the Benchmark

Run the benchmark script using:

```bash
python benchmark.py
````

* This script generates a synthetic CSV dataset with **10,000 rows and 5 columns**.
* It measures **reading and writing times** for both your custom implementation and Python’s built-in CSV module.
* Evaluators can also replace the synthetic dataset with their **own CSV files** to test performance on real-world data.

---

### 2.Example Output (Sample)

```
Generating test data...

=========== Benchmark Results ===========
Custom Writer Time   : 0.0142 sec
CSV Writer Time      : 0.0091 sec
-----------------------------------------
Custom Reader Time   : 0.0189 sec
CSV Reader Time      : 0.0123 sec
=========================================
```

> Times are in seconds and will vary based on hardware and file size.

---

### 3.Analysis

* **Python’s built-in CSV library is faster** because it is implemented in C and optimized for performance.
* **CustomCsvReader/Writer are slower**, but they provide:

  * Full control over parsing and writing logic
  * Correct handling of all edge cases (quotes, escaped quotes, newlines, commas)
* Performance depends on:

  * File size
  * Number of rows
  * Field complexity (number of quotes, multiline fields)

> The benchmark demonstrates that while custom implementations may be slower, they are fully **correct and reliable**, which is critical for understanding CSV parsing logic and handling non-standard CSV files.

---

### 4.Using Custom Test Files

Evaluators can benchmark their own CSV files by replacing the dataset generation in `benchmark.py`:

```python
with open("evaluator_test.csv", "r", encoding="utf-8") as f:
    reader = CustomCsvReader(f)
    # measure read time
```

```python
with open("evaluator_output.csv", "w", encoding="utf-8", newline="") as f:
    writer = CustomCsvWriter(f)
    # measure write time
```

> This ensures that the benchmark can be **fully reproducible with any dataset**.


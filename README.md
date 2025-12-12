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

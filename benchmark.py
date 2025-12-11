"""
Benchmark script to compare:
- CustomCsvReader vs csv.reader
- CustomCsvWriter vs csv.writer

Creates a synthetic CSV file with 10k rows and 5 columns.
Measures read and write times for both.
"""

import csv
import time
from custom_csv import CustomCsvReader, CustomCsvWriter


ROW_COUNT = 10000
COLUMN_COUNT = 5
TEST_FILE_CUSTOM = "test_custom.csv"
TEST_FILE_STANDARD = "test_standard.csv"


def generate_data():
    """
    Creates a list of mock rows to use for writing and reading tests.
    Includes commas, quotes, and newlines in some cells.
    """
    data = []

    for i in range(ROW_COUNT):
        row = [
            f"text {i}",
            f"value,{i}",
            f"hello \"world\" {i}",
            f"multi\nline {i}",
            f"normal{i}"
        ]
        data.append(row)

    return data


def benchmark_custom_writer(data):
    start = time.time()

    with open(TEST_FILE_CUSTOM, "w", encoding="utf-8") as f:
        writer = CustomCsvWriter(f)
        writer.writerows(data)

    end = time.time()
    return end - start


def benchmark_standard_writer(data):
    start = time.time()

    with open(TEST_FILE_STANDARD, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    end = time.time()
    return end - start


def benchmark_custom_reader():
    start = time.time()

    with open(TEST_FILE_CUSTOM, "r", encoding="utf-8") as f:
        reader = CustomCsvReader(f)
        for _ in reader:
            pass

    end = time.time()
    return end - start


def benchmark_standard_reader():
    start = time.time()

    with open(TEST_FILE_STANDARD, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass

    end = time.time()
    return end - start


def main():
    print("Generating test data...")
    data = generate_data()

    print("\nRunning benchmarks...\n")

    # Write benchmarks
    custom_write_time = benchmark_custom_writer(data)
    standard_write_time = benchmark_standard_writer(data)

    # Read benchmarks
    custom_read_time = benchmark_custom_reader()
    standard_read_time = benchmark_standard_reader()

    print("=========== Benchmark Results ===========")
    print(f"Custom Writer Time   : {custom_write_time:.4f} sec")
    print(f"CSV Writer Time      : {standard_write_time:.4f} sec")
    print("-----------------------------------------")
    print(f"Custom Reader Time   : {custom_read_time:.4f} sec")
    print(f"CSV Reader Time      : {standard_read_time:.4f} sec")
    print("=========================================")


if __name__ == "__main__":
    main()

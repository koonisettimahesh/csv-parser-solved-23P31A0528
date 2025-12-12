import csv
from custom_csv import CustomCsvReader  # correct import

def read_builtin(path):
    """Read CSV using Python's built-in csv.reader."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.reader(f))

def read_custom(path):
    """Read using your custom CSV reader."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = CustomCsvReader(f)
        return list(reader)

def compare(builtin, custom):
    print("\n=== Comparing CustomCsvReader with csv.reader ===")
    ok = True

    if len(builtin) != len(custom):
        print("\n❌ Row count mismatch!")
        print("Built-in:", len(builtin))
        print("Custom  :", len(custom))
        return False

    for i, (b_row, c_row) in enumerate(zip(builtin, custom)):
        if b_row != c_row:
            ok = False
            print(f"\n❌ Row {i+1} mismatch:")
            print("Built-in:", b_row)
            print("Custom  :", c_row)
        else:
            print(f"✔ Row {i+1} OK")

    return ok

if __name__ == "__main__":
    test_file = "test.csv"

    builtin_rows = read_builtin(test_file)
    custom_rows = read_custom(test_file)

    if compare(builtin_rows, custom_rows):
        print("\n🎉 READER TEST PASSED!")
    else:
        print("\n❌ READER TEST FAILED!")

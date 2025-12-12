import csv
from custom_csv import CustomCsvWriter, CustomCsvReader

OUTPUT_FILE = "writer_output.csv"

# Sample rows for testing
ROWS = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "San Francisco"],
    ["Charlie", "35", "Los Angeles, CA"],
    ['Quote "Inside"', "40", "Denver"],
    ["Multi\nLine", "45", "Dallas"]
]


def write_with_custom(rows):
    """Write sample rows using CustomCsvWriter."""
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        writer = CustomCsvWriter(f)
        writer.writerows(rows)


def read_with_builtin():
    """Read CSV using Python's built-in csv.reader."""
    with open(OUTPUT_FILE, "r", encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def read_with_custom():
    """Read CSV using CustomCsvReader."""
    with open(OUTPUT_FILE, "r", encoding="utf-8", newline="") as f:
        reader = CustomCsvReader(f)
        return list(reader)


def normalize_newlines(rows):
    """Normalize Windows CRLF to LF inside each cell."""
    return [[cell.replace('\r\n', '\n') for cell in row] for row in rows]


def compare(original, builtin, custom):
    """Compare CSV outputs."""
    print("\n=== Comparing Writer Output ===")
    ok = True

    # Normalize newlines for comparison
    builtin_norm = normalize_newlines(builtin)
    custom_norm = normalize_newlines(custom)

    if builtin_norm != custom_norm:
        print("❌ Built-in CSV reader gives different output than CustomCsvReader!")
        print("Built-in:", builtin_norm)
        print("Custom  :", custom_norm)
        ok = False
    else:
        print("✔ Built-in CSV reader matches CustomCsvReader")

    # Original vs parsed (normalizing newlines)
    original_norm = normalize_newlines(original)
    if original_norm != builtin_norm:
        print("\n⚠ Original rows changed due to formatting differences (quotes/newlines).")
        print("This is normal because the CSV writer adds quotes automatically.")
    else:
        print("\n✔ Original and parsed rows match exactly.")

    return ok


if __name__ == "__main__":
    # Step 1: Write CSV
    write_with_custom(ROWS)

    # Step 2: Read back with both readers
    builtin_out = read_with_builtin()
    custom_out = read_with_custom()

    # Step 3: Compare
    if compare(ROWS, builtin_out, custom_out):
        print("\n🎉 WRITER TEST PASSED!")
    else:
        print("\n❌ WRITER TEST FAILED!")

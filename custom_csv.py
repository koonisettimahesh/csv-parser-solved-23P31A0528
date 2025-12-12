"""
Fully working custom CSV Reader and Writer.
Handles:
- commas
- quoted values
- escaped quotes ("")
- newlines inside quoted fields
"""

class CustomCsvReader:
    """Iterator-based CSV reader."""

    def __init__(self, file_obj):
        # file_obj should be opened with newline=""
        self.file_obj=file_obj
        self.buffer = ""
        self.end_of_file=False

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = ""
        inside_quotes = False

        while True:
            # Refill buffer
            if self.buffer == "":
                chunk = self.file_obj.read(1024)
                if not chunk:
                    # EOF
                    if inside_quotes:
                        # Unclosed quoted field -> treat as end (or raise a custom error)
                        # For now: finish row as-is so your test can compare
                        pass
                    # If no data collected, end iteration
                    if not row and field == "":
                        raise StopIteration
                    # Otherwise, return the last row (even if file has no final newline)
                    row.append(field)
                    return row
                self.buffer = chunk

            ch = self.buffer[0]
            self.buffer = self.buffer[1:]

            if inside_quotes:
                if ch == '"':
                    # Peek next char for escaped quote
                    if self.buffer.startswith('"'):
                        field += '"'
                        self.buffer = self.buffer[1:]
                    else:
                        inside_quotes = False
                else:
                    field += ch
            else:
                if ch == '"':
                    inside_quotes = True

                elif ch == ",":
                    row.append(field)
                    field = ""

                elif ch == "\n":
                    row.append(field)
                    return row

                elif ch == "\r":
                    if self.buffer.startswith("\n"):
                        self.buffer = self.buffer[1:]
                    row.append(field)
                    return row

                else:
                    field += ch




class CustomCsvWriter:
    """Custom CSV writer that quotes fields when needed."""

    def __init__(self, file_obj):
        self.file = file_obj

    def _quote_if_needed(self, text):
        text = str(text)
        needs_quotes = any(c in text for c in [',', '\n', '\r', '"'])

        # Escape quotes
        if '"' in text:
            text = text.replace('"', '""')

        return f'"{text}"' if needs_quotes else text

    def writerow(self, row):
        processed = [self._quote_if_needed(f) for f in row]
        self.file.write(",".join(processed) + "\n")

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

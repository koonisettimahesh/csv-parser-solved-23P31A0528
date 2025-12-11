"""
Simple custom CSV reader and writer.

This file contains:
- CustomCsvReader: reads CSV files manually without using csv module
- CustomCsvWriter: writes CSV files with proper quoting rules

The goal is to handle:
- commas
- quoted fields
- escaped quotes ("")
- newlines inside quotes
"""

class CustomCsvReader:
    def __init__(self, file_obj):
        self.file_obj = file_obj
        self.buffer = ""
        self.end_of_file = False

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next row from the CSV file.
        Uses a very simple character-by-character parsing approach.
        """

        row = []
        field = ""
        inside_quotes = False
        last_char_was_quote = False

        while True:

            # Fill buffer if empty
            if self.buffer == "":
                chunk = self.file_obj.read(1024)
                if not chunk:
                    self.end_of_file = True
                    break
                self.buffer = chunk

            ch = self.buffer[0]
            self.buffer = self.buffer[1:]

            # If we are inside quotes
            if inside_quotes:
                if ch == '"':
                    # Possible escaped quote or end of quotes
                    if last_char_was_quote:
                        field += '"'   # add literal quote
                        last_char_was_quote = False
                    else:
                        last_char_was_quote = True
                else:
                    if last_char_was_quote:
                        # Quote just closed the quoted field
                        inside_quotes = False
                        last_char_was_quote = False
                        # process this character again outside quotes
                        self.buffer = ch + self.buffer
                    else:
                        field += ch

            else:
                # Normal mode
                if ch == '"':
                    inside_quotes = True

                elif ch == ",":
                    row.append(field)
                    field = ""

                elif ch == "\n":
                    row.append(field)
                    return row

                elif ch == "\r":
                    # handle Windows \r\n
                    if self.buffer.startswith("\n"):
                        self.buffer = self.buffer[1:]
                    row.append(field)
                    return row
                else:
                    field += ch

        # If EOF and nothing to return
        if row == [] and field == "":
            raise StopIteration

        row.append(field)
        return row


class CustomCsvWriter:
    def __init__(self, file_obj):
        self.file_obj = file_obj

    def _quote_if_needed(self, text):
        """
        Adds quotes around a field if it contains:
        - comma
        - newline
        - quote
        And escapes internal quotes by doubling them.
        """
        text = str(text)
        needs_quotes = False

        if "," in text or "\n" in text or "\r" in text or '"' in text:
            needs_quotes = True

        # Escape quotes inside field
        if '"' in text:
            text = text.replace('"', '""')

        if needs_quotes:
            text = f'"{text}"'

        return text

    def writerow(self, row):
        processed = [self._quote_if_needed(f) for f in row]
        line = ",".join(processed) + "\n"
        self.file_obj.write(line)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

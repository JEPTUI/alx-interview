#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:
Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C)
print these statistics from the beginning:
     Total file size: File size: <total size>
     where <total size> is the sum of all previous <file size>
     Number of lines by status code:
       possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
       if a status code doesn’t appear or is not an integer,
       don’t print anything for this status code
            format: <status code>: <number>
status codes should be printed in ascending order"""


import sys

log_format = r'(\d+\.\d+\.\d+\.\d+) - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
lines_processed = 0

try:
    for line in sys.stdin:
        match = re.match(log_format, line)
        if match:
            ip_address, status_code, file_size = match.groups()
            total_size += int(file_size)
            status_codes_dict[status_code] += 1
            lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed % 10 == 0:
                print("Total file size: File size:", total_size)
                for code in sorted(status_codes_dict.keys()):
                    print(f"{code}: {status_codes_dictt[code]}")
                print()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Keyboard interruption detected. Printing final statistics.")
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes_dict.keys()):
        print(f"{code}: {status_codes_dict[code]}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Print final statistics after processing all input
print("Total file size: File size:", total_size)
for code in sorted(status_codes_dict.keys()):
    print(f"{code}: {status_codes_dict[code}")

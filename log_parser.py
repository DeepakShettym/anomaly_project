logfiles = '/home/deepak/Deepak/anomaly_project/syslog_snapshot.txt'

with open(logfiles, 'r') as file:
    lines = file.readlines()

print(f'Total lines read: {len(lines)}')

# Print first 5 lines to see structure
for line in lines[:5]:
    parts = line.split()
    timestamp = ' '.join(parts[0:3])  # Usually first 3 parts are date/time
    message = ' '.join(parts[4:])
    print(f'Time: {timestamp}\nMessage: {message}\n')


for line in lines[:20]:
    if "error" in line.lower():
        print("[ERROR]", line.strip())
    elif "warning" in line.lower():
        print("[WARNING]", line.strip())
    else:
        print("[INFO]", line.strip())


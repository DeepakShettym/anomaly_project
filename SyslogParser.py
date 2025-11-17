import pandas as pd

# Path to your saved syslog snapshot file
logfile = '/home/deepak/Deepak/anomaly_project/syslog_snapshot.txt'

# Read file lines into a list
with open(logfile, 'r') as file:
    lines = file.readlines()

# Prepare lists for each column
timestamps = []
hosts = []
services = []
messages = []

for line in lines:
    parts = line.split()
    if len(parts) < 5:
        continue  # skip malformed lines
    # Extract timestamp (first 3 parts), host (4th), service & message (rest)
    timestamps.append(' '.join(parts[0:3]))
    hosts.append(parts[3])
    services.append(parts[4].rstrip(':'))
    messages.append(' '.join(parts[5:]))

# Create a DataFrame
df = pd.DataFrame({
    'Timestamp': timestamps,
    'Host': hosts,
    'Service': services,
    'Message': messages
})

print(df.head())
print(f'Total log entries: {len(df)}')

# Save cleaned data as CSV for next steps
df.to_csv('/home/deepak/Deepak/anomaly_project/project/cleaned_syslog.csv', index=False)


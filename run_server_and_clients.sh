# THIS SCRIPT CURRENTLY DOES NOT WORK

#!/bin/bash

# Start the server.py script and let it run infinitely
nohup python3 bidirectional_server.py > server.log 2>&1 &

# Wait for a moment to ensure the server starts
sleep 2

# Start three instances of client.py and let each run infinitely
for i in {1..3}; do
    nohup python3 bidirectional_client.py > "client${i}.log" 2>&1 &
done

# Print process IDs for reference
echo "Started server.py with PID: $!"
for pid in $(pgrep -f client.py); do
    echo "Started client.py with PID: $pid"
done

# Wait for all background processes to finish (which won't happen in this case)
wait

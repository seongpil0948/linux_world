echo "Up Time 3 num: 1min, 5min, 15min"
uptime

echo "All Kernel Message ~"
dmesg | tail 

echo ">>> \n r: num of cpu's process \n free: free memory with kb \n si, so: swap-in/out Out of Memory if not Zero <<<"
vmstat 1




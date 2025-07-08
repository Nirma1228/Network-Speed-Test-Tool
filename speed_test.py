import speedtest

def convert_speed(bytes_per_second):
    return round(bytes_per_second / (1024 * 1024), 2)  # Convert to Mbps

# Create Speedtest object
st = speedtest.Speedtest()

print("Getting best server...")
st.get_best_server()


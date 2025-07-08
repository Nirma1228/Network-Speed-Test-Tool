import speedtest

def convert_speed(bytes_per_second):
    return round(bytes_per_second / (1024 * 1024), 2)  # Convert to Mbps

# Create Speedtest object
st = speedtest.Speedtest()

print("Getting best server...")
st.get_best_server()

print("Testing download speed...")
download_speed = st.download()

print("Testing upload speed...")
upload_speed = st.upload()

print("Testing ping...")
ping_result = st.results.ping

print("\n===== Network Speed Test Results =====")
print(f"Download Speed: {convert_speed(download_speed)} Mbps")
print(f"Upload Speed  : {convert_speed(upload_speed)} Mbps")
print(f"Ping          : {ping_result:.2f} ms")

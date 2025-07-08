import speedtest

def convert_speed(bytes_per_second):
    return round(bytes_per_second / (1024 * 1024), 2)  # Convert to Mbps

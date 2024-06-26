import subprocess
import re

def test_speed():
    try:
        # Run speedtest-cli command and capture output
        speedtest_output = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True, timeout=60)
        
        # Check if the command was successful
        if speedtest_output.returncode != 0:
            print("Speedtest command failed. Please check your network connection and try again.")
            return None, None
        
        # Parse the output to get download and upload speeds
        lines = speedtest_output.stdout.strip().split("\n")
        download = float(re.search(r"Download:\s+([\d.]+)", lines[0]).group(1))
        upload = float(re.search(r"Upload:\s+([\d.]+)", lines[1]).group(1))

        return download, upload
    
    except subprocess.TimeoutExpired:
        print("Speedtest took too long to complete. Please try again later.")
        return None, None
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

if __name__ == "__main__":
    download_speed, upload_speed = test_speed()
    if download_speed is not None and upload_speed is not None:
        print(f"Download speed: {download_speed:.2f} Mbps")
        print(f"Upload speed: {upload_speed:.2f} Mbps")
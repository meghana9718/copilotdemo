import os
import platform
import time

def get_uptime():
    if platform.system() == "Windows":
        # On Windows, use 'net stats srv' and parse the output
        try:
            output = os.popen('net stats srv').read()
            for line in output.split('\n'):
                if 'Statistics since' in line:
                    # Parse the time from the line
                    from datetime import datetime
                    boot_time_str = line.strip().split('since')[1].strip()
                    boot_time = datetime.strptime(boot_time_str, '%m/%d/%Y %I:%M:%S %p')
                    now = datetime.now()
                    uptime = now - boot_time
                    return uptime
        except Exception as e:
            return f"Error fetching uptime: {e}"
    else:
        # On Unix/Linux, read /proc/uptime
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_str = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
                return f"Uptime: {uptime_str} (hh:mm:ss)"
        except Exception as e:
            return f"Error fetching uptime: {e}"

if __name__ == "__main__":
    uptime = get_uptime()
    print(f"System uptime: {uptime}")

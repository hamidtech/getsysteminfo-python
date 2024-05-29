import os
import subprocess
import psutil
import csv

def get_processor_info():
    """Retrieve detailed processor information using wmic."""
    try:
        command = 'wmic cpu get name'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if process.returncode == 0:
            # Split the output by newlines and remove empty lines
            output_lines = output.decode().split('\n')
            # The processor name is usually on the second line after the header
            processor_name = output_lines[1].strip() if len(output_lines) > 1 else "Unknown Processor"
            return processor_name
        else:
            return f"Failed to retrieve processor information: {error.decode().strip()}"
    except Exception as e:
        return f"Error retrieving processor information: {str(e)}"

def get_storage_info():
    """Retrieve and convert storage information to gigabytes."""
    try:
        command = 'wmic diskdrive get model, size'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if process.returncode == 0:
            storage_details = output.decode().strip().split('\n')[1:]  # Skip the header
            storage_info = ""
            for detail in storage_details:
                if detail.strip():
                    parts = detail.strip().split()
                    model = " ".join(parts[:-1])
                    size_bytes = int(parts[-1])
                    size_gb = size_bytes / (1024**3)  # Convert bytes to gigabytes
                    storage_info += f"Model: {model}, Size: {size_gb:.2f} GB\n"
            return storage_info
        else:
            return f"Failed to retrieve storage information: {error.decode().strip()}"
    except Exception as e:
        return f"Error retrieving storage information: {str(e)}"

# Welcome message
print("Hi,\n\nWelcome to system information extractor.\n")

# Get user input
user_name = input("Please enter your Username: ")
PC_Name = input("Please enter your PC name: ")

# File name construction
txt_file_name = f"{PC_Name} - {user_name} - systeminfo.txt"
csv_file_name = f"{PC_Name} - {user_name} - systeminfo.csv"

# Write initial user info
with open(txt_file_name, 'w') as file:
    file.write(f"User Name: {user_name}\nPC Name: {PC_Name}\nComputer Name: {os.getenv('COMPUTERNAME', 'Unknown')}\n\n\n")

# Initialize CSV file and write headers
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Information"])

# Function to write data to both txt and CSV files
def append_to_files(header, data):
    with open(txt_file_name, 'a') as file:
        file.write(f"--- {header} ---\n")
        file.write(f"{data}\n\n\n")
    with open(csv_file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([header, data])

# Processor information
processor_info = get_processor_info()
append_to_files("Processor Information", processor_info)

# RAM information
ram_info = f"Total RAM: {str(round(psutil.virtual_memory().total / (1024 ** 3)))} GB"
append_to_files("Total RAM Capacity", ram_info)

# Storage information
storage_info = get_storage_info()
append_to_files("Storage Device Information", storage_info)

# Network interface information
network_info = ""
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == psutil.AF_LINK:
            network_info += f"Interface: {interface}\n  MAC Address: {addr.address}\n"
append_to_files("Network MAC Addresses", network_info.strip())


print(f"Information exported to {txt_file_name} and {csv_file_name}")

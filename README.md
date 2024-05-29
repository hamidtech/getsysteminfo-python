
### Windows 7 Compatible System and above Information Script

# System Information Script for Windows 7

## Overview
This Python script is designed to collect and export detailed system information, making it ideal for use in environments like Windows 7 where certain modern functionalities might be limited. The script retrieves processor details, RAM capacity, and storage device information, outputting the data to both a text file and a CSV file for easy review and reporting.

## Requirements
- Python 3.4 or newer (Tested on Python 3.8 and Python 3.12)
- Subprocess and psutil libraries installed

## Features
- **Processor Information**: Fetches the CPU model using the `wmic` command.
- **RAM Information**: Determines the total installed RAM.
- **Storage Information**: Provides details about each storage device, including the model and capacity in gigabytes.

## Installation
To run this script, ensure Python and the required libraries (`psutil`) are installed on your Windows 7 machine. Install psutil using pip:
```bash
pip install psutil
```

## Usage
1. Save the script to your local machine.
2. Open a command prompt.
3. Navigate to the directory containing the script.
4. Run the script by entering:
```bash
python script_name.py
```
5. Follow the on-screen prompts to input required information such as the user's email and branch name.

## Script Details

### Import Statements
```python
import os
import subprocess
import psutil
import csv
```
These libraries are necessary for system interaction, data processing, and file operations.

### Key Functions

#### `get_processor_info`
This function uses the `wmic cpu get name` command to retrieve the processor name from Windows Management Instrumentation (WMIC), making it compatible with older systems like Windows 7.

#### `get_storage_info`
Fetches storage device models and sizes, converting sizes from bytes to gigabytes for better readability. It also handles potential errors and ensures the data is presented clearly.

### Main Execution Flow
The script starts by printing a welcome message and gathering user inputs. It prepares filenames for output data and initializes files for writing. The data gathering functions (`get_processor_info`, `get_storage_info`) are called, and their outputs are appended to both text and CSV files.

### Error Handling
The script includes robust error handling, particularly for external command executions and data conversions, ensuring stability across various system configurations.

## Output
The script generates two files:
- **Text file**: Detailed system information in a readable format.
- **CSV file**: Same information in a tabular format suitable for importing into spreadsheets.
## Support

For any queries or issues, please open an issue in this repository or contact [hamid1375jamali@gmail](hamid1375jamali@gmail.com) :)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

import os
import re
import webbrowser

from PyQt5.QtWidgets import QMessageBox


# Function to format the size of deleted files
def format_size(size):
    if size > 1048576:  # greater than 1 MB
        return f"{size / 1024 / 1024:.2f} MB"
    else:
        return f"{size / 1024:.2f} KB"


# Function to initiate cleanup from the GUI
def initiate_cleanup():
    DayZFolder = os.path.join(os.getenv('LOCALAPPDATA'), 'DayZ')
    files_deleted, total_size = cleanup_files(DayZFolder)
    message = f"Deleted files total size: {format_size(total_size)}" if files_deleted else "No files were deleted."
    QMessageBox.information(None, "Cleanup", message)


# Function to clean up files
def cleanup_files(DayZFolder):
    total_size = 0
    files_deleted = False

    for root, dirs, files in os.walk(DayZFolder):
        for file in files:
            if file.endswith(('.log', '.RPT', '.mdmp')):
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                os.remove(file_path)
                files_deleted = True

    return files_deleted, total_size


# Function to read the last server and its IP address
def get_last_server_info():
    user = os.getlogin()  # Gets the username of the user
    profile_path = os.path.join(os.path.expanduser('~'), 'Documents', 'DayZ', f'{user}_settings.DayZProfile')

    if not os.path.exists(profile_path):
        return "Server info not found", "IP not found"

    with open(profile_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expressions to find the server name and IP address
    server_name_regex = r'lastMPServerName="([^"]+)"'
    server_ip_regex = r'lastMPServer="([^"]+)"'

    # Find the server name and IP address in the file content
    server_name_match = re.search(server_name_regex, content)
    server_ip_match = re.search(server_ip_regex, content)

    # Extract the server name and IP address if found
    last_server_name = server_name_match.group(1) if server_name_match else "Not Found"
    last_server_ip = server_ip_match.group(1) if server_ip_match else "Not Found"

    return last_server_name, last_server_ip


# Function to launch DayZ
def launch_dayz():
    url = "steam://rungameid/221100"
    webbrowser.open(url)

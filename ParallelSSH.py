import paramiko
import concurrent.futures
import sys
import logging
import socket
import time
import os
import multiprocessing
import random
import hashlib

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def ssh_key_login(ip, username, key_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, key_filename=key_path)
        logging.info(f"Successful login with username: {username} and key: {key_path}")
        client.close()
        return (ip, username, key_path, True)
    except Exception as e:
        logging.error(f"Login failed for username: {username} and key: {key_path}. Error: {e}")
        client.close()
        return (ip, username, key_path, False)

def ssh_password_login(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password)
        logging.info(f"Successful login with username: {username} and password hash: {hashlib.sha256(password.encode()).hexdigest()}")
        client.close()
        return (ip, username, password, True)
    except Exception as e:
        logging.error(f"Login failed for username: {username} and password hash: {hashlib.sha256(password.encode()).hexdigest()}. Error: {e}")
        client.close()
        return (ip, username, password, False)

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
    except Exception as e:
        logging.error(f"Error while checking open port on host: {host}. Error: {e}")
        return False

def check_ping(host):
    try:
        response = os.system("ping -c 1 " + host)
        if response == 0:
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"Error while checking ping on host: {host}. Error: {e}")
        return False

def try_login(ip, username, login, login_type, results_list):
    if not check_ping(ip):
        logging.error(f"Host {ip} is down")
        return
    if not check_open_port(ip, 22):
        logging.error(f"SSH port on host {ip} is closed")
        return

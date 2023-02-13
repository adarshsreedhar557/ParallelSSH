ParallelSSH

ParallelSSH is a Python script that uses the Paramiko library to perform parallel SSH login attempts on a given list of hosts, usernames and login credentials.
Requirements

    paramiko
    concurrent.futures
    sys
    logging
    socket
    time
    os
    multiprocessing
    random
    hashlib

Usage

The script requires three inputs: a list of IP addresses, a list of usernames and a list of login credentials (either passwords or key files).

python

python parallel_ssh.py <ip_list.txt> <username_list.txt> <login_list.txt>

The IP addresses, usernames and login credentials must be in separate text files, with one item per line. The number of IP addresses, usernames and login credentials must be the same.
Features

    Parallel processing of SSH login attempts
    Support for both password and key-based authentication
    Logging of successful and failed login attempts
    Error handling for hosts that are down or have closed SSH ports

Contributing

Contributions are welcome. Please fork the repository and make changes as you see fit.
License

The code in this repository is licensed under the Apache License 2.0.

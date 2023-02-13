ParallelSSH

ParallelSSH is a high-performance Python script that leverages the Paramiko library to perform parallel SSH login attempts on a list of specified hosts, usernames and login credentials. The script is designed to run efficiently even on large-scale environments and can handle thousands of login attempts concurrently.
Requirements

The following packages must be installed for the script to run:

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

Features

    Support for parallel processing of SSH login attempts for increased speed
    Authentication options for both password-based and key-based authentication
    Detailed logging of successful and failed login attempts with error handling for hosts that are down or have closed SSH ports
    Support for the Apache 2.0 open-source license

Usage

The script requires three inputs to run: a list of IP addresses, a list of usernames and a list of login credentials (either passwords or key files). The IP addresses, usernames, and login credentials must be in separate text files, with one item per line. The number of IP addresses, usernames, and login credentials must be the same.

python

python parallel_ssh.py <ip_list.txt> <username_list.txt> <login_list.txt>

Advanced Features

    Ability to customize the number of concurrent worker threads to adjust the performance based on the environment and the system resources.
    Dynamic timeout handling for each worker thread to handle the responsiveness of the target systems.
    Hashing of the password credentials for increased security and to avoid storing the passwords in clear text.
    Graceful error handling and logging to capture the unexpected errors and exceptions.

Contributing

This project welcomes contributions from the community. Whether you are fixing bugs, adding new features, or improving the documentation, your contributions are highly appreciated. To contribute, please fork the repository and submit a pull request.
License

This project is licensed under the Apache 2.0 open-source license. This means that you are free to use, modify and distribute the code, as long as you comply with the license terms and conditions.

import os
import getpass
import socket

def get_site():
    """
    Retrieves the site name from the environment variable 'TB_SITE'.

    Returns: str
    """
    return os.environ.get('TB_SITE', None)

def get_user():
    """
    Retrieves the user name based on the farm / interactive user scenario.

    Returns: str
    """
    farm = int(os.getenv('TB_FARM', None))
    if farm == 0:
        return getpass.getuser()
    return os.getenv('TB_FARM_USER', None)


def get_hostname():
    """
    Retrieves the hostname of the current machine.

    Returns: str
    """
    return socket.gethostname()

def get_ipv4_address():
    """
    Retrieves the IPv4 address of the current machine.

    This function creates a UDP socket, connects it to Google's public DNS server (8.8.8.8),
    and retrieves the IP address of the local machine from the socket's name.

    Returns: str

    Raises:
    Exception: If an error occurs while connecting to the DNS server or retrieving the IP address.
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        soc.connect(('8.8.8.8', 80))
        ip_addr = soc.getsockname()[0]
        soc.close()
        return ip_addr
    except Exception as e:
        raise e
    

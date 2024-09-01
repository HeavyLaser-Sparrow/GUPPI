import socket
import struct

def ip_to_binary(ip_address):
    """
    Convert an IPv4 address to its binary representation.
    
    Args:
        ip_address (str): The IPv4 address in dot-decimal notation.
    
    Returns:
        str: The binary representation of the IPv4 address.
    """
    try:
        # Convert IP address to 32-bit packed binary format
        packed_ip = socket.inet_aton(ip_address)
        # Unpack the binary data into a 32-bit integer
        binary_ip = struct.unpack("!I", packed_ip)[0]
        # Convert integer to binary string and pad it to 32 bits
        return f'{binary_ip:032b}'
    except socket.error:
        raise ValueError("Invalid IP address")

def binary_to_ip(binary_str):
    """
    Convert a binary representation to its IPv4 address.
    
    Args:
        binary_str (str): The binary representation of the IPv4 address (32 bits).
    
    Returns:
        str: The IPv4 address in dot-decimal notation.
    """
    if len(binary_str) != 32 or not all(b in '01' for b in binary_str):
        raise ValueError("Binary string must be 32 bits long and contain only '0' and '1' characters")
    
    # Convert binary string to integer
    binary_ip = int(binary_str, 2)
    # Pack integer into 32-bit binary format
    packed_ip = struct.pack("!I", binary_ip)
    # Convert packed binary data to dot-decimal notation
    return socket.inet_ntoa(packed_ip)

def mainIP():
    while True:
        print("Choose an option:")
        print("1. Convert IP address to binary")
        print("2. Convert binary to IP address")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            ip_address = input("Enter the IPv4 address (e.g., 192.168.1.1): ")
            try:
                binary_str = ip_to_binary(ip_address)
                print(f"Binary representation: {binary_str}")
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            binary_str = input("Enter the 32-bit binary string: ")
            try:
                ip_address = binary_to_ip(binary_str)
                print(f"IPv4 address: {ip_address}")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    mainIP()

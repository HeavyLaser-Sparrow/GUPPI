import ipaddress

def ipv6_to_bits(ipv6_addr):
    """Convert an IPv6 address to its binary representation."""
    try:
        # Create an IPv6 address object
        ipv6 = ipaddress.IPv6Address(ipv6_addr)
        # Convert the IPv6 address to its integer form
        ipv6_int = int(ipv6)
        # Format the integer as a binary string with leading zeros
        ipv6_bits = format(ipv6_int, '0128b')
        return ipv6_bits
    except ipaddress.AddressValueError:
        return "Invalid IPv6 address"

def bits_to_ipv6(bits):
    """Convert a binary string to an IPv6 address."""
    if len(bits) != 128 or not all(bit in '01' for bit in bits):
        return "Invalid binary string"
    
    # Convert the binary string to an integer
    ipv6_int = int(bits, 2)
    # Create an IPv6 address object from the integer
    ipv6 = ipaddress.IPv6Address(ipv6_int)
    return str(ipv6)
    
def mainIPv6():
	 # Test with an example IPv6 address
    #ipv6_example = "2001:db8::ff00:42:8329"
    choice = int(input("Do you want to got bits to ip[1] or ip to bits[2]?: "))
    if(choice == 2):
        ipv6_example = input("Choose an IPv6 address to convert to bits: ")
        # Convert IPv6 to bits
        bits = ipv6_to_bits(ipv6_example)
        print(f"IPv6 address {ipv6_example} in bits is: {bits}")
    # Convert bits back to IPv6
    elif(choice == 1):
        bits2 = input("Put in the bits: ")
        ipv6_reconstructed = bits_to_ipv6(bits2)
        print(f"Binary string {bits} back to IPv6 is: {ipv6_reconstructed}")

# Example usage:
if __name__ == "__main__":
	mainIPv6()
   

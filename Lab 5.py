def is_valid_part(part):
    try:
        number = int(part)
    except ValueError:
        return False

    if number < 0 or number > 255:
        return False

    if len(part) > 1 and part[0] == "0":
        return False

    return True


def is_valid_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not is_valid_part(part):
            return False

    return True

def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    if b == "":
        return 0

    return int(b[0]) * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"

    parts = ip.split(".")
    binary_parts = []

    for part in parts:
        binary = decimal_to_binary(int(part))
        binary = binary.zfill(8)
        binary_parts.append(binary)

    return ".".join(binary_parts)


print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))   # False
print(is_valid_part("0"))    # True

print(is_valid_ip("192.168.1.1"))      # True
print(is_valid_ip("192.168.256.1"))    # False
print(is_valid_ip("192.168.1"))        # False
print(is_valid_ip("192.168.01.1"))     # False

print(decimal_to_binary(10))   # 1010
print(decimal_to_binary(255))  # 11111111
print(decimal_to_binary(1))    # 1

print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1

print(ip_to_binary("192.168.1.1"))
print(ip_to_binary("255.255.255.0"))
print(ip_to_binary("256.1.1.1"))
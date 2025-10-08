def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

def count_ips(first, last):
    first_int = ip_to_int(first)
    last_int = ip_to_int(last)
    return last_int - first_int

if __name__ == "__main__":
    first = input()
    last = input()
    out_ = count_ips(first, last)
    print(out_)

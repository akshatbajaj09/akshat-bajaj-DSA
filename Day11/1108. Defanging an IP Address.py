def defangIPaddr(address):
    return address.replace(".", "[.]")


def defangIPaddr2(address):
    splitted_address = address.split(".")
    joined_address = "[.]".join(splitted_address)
    return joined_address


def solve():
    address = "1.1.1.1"
    print(defangIPaddr(address))
    print(defangIPaddr2(address))


if __name__ == "__main__":
    solve()

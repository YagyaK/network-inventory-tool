import csv

def load_devices(filename):
    devices = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            devices.append(row)

    return devices


def show_inventory(devices):
    print("NETWORK DEVICE INVENTORY")
    print("-" * 60)

    for device in devices:
        print("Hostname:", device["hostname"])
        print("IP Address:", device["ip"])
        print("Device Type:", device["device_type"])
        print("Location:", device["location"])
        print("Status:", device["status"])
        print("-" * 60)


def count_online_devices(devices):
    online_count = 0

    for device in devices:
        if device["status"].lower() == "online":
            online_count += 1

    return online_count


def main():
    devices = load_devices("devices.csv")
    show_inventory(devices)

    online = count_online_devices(devices)
    total = len(devices)

    print("SUMMARY")
    print("Total devices:", total)
    print("Online devices:", online)
    print("Offline devices:", total - online)


main()
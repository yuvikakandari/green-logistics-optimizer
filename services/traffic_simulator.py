import random


def get_live_traffic():

    return {
        ("Warehouse", "Hub_A"): random.randint(1, 10),
        ("Warehouse", "Hub_C"): random.randint(1, 10),
        ("Hub_A", "Hub_B"): random.randint(1, 10),
        ("Hub_C", "Hub_B"): random.randint(1, 10),
        ("Hub_B", "Customer"): random.randint(1, 10)
    }
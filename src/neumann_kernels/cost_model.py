import math


_KERNELS = (
    {
        "kernel_id": "radix5",
        "display_name": "Radix-5",
        "radix": 5,
        "num_products": 2,
        "status": "exact",
    },
    {
        "kernel_id": "radix9",
        "display_name": "Radix-9",
        "radix": 9,
        "num_products": 3,
        "status": "exact",
    },
    {
        "kernel_id": "radix15",
        "display_name": "Radix-15",
        "radix": 15,
        "num_products": 4,
        "status": "certified approximate",
    },
    {
        "kernel_id": "radix24",
        "display_name": "Radix-24",
        "radix": 24,
        "num_products": 5,
        "status": "certified approximate",
    },
)


def update_cost(num_products):
    return num_products + 2


def asymptotic_coefficient(radix, num_products):
    return update_cost(num_products) / math.log2(radix)


def iteration_count(radix, target_degree):
    if target_degree <= 1:
        return 0
    return math.ceil(math.log(target_degree, radix))


def multiply_count(radix, num_products, target_degree):
    return update_cost(num_products) * iteration_count(radix, target_degree)


def kernel_catalog():
    catalog = []
    for entry in _KERNELS:
        enriched = dict(entry)
        enriched["update_cost"] = update_cost(entry["num_products"])
        enriched["asymptotic_coefficient"] = asymptotic_coefficient(
            entry["radix"], entry["num_products"]
        )
        catalog.append(enriched)
    return catalog

import json
import os

WAREHOUSE_FILE = "data/warehouse.json"



def load_warehouse():

    if not os.path.exists(WAREHOUSE_FILE):
        return {}

    with open(WAREHOUSE_FILE, "r") as f:
        return json.load(f)



def save_warehouse(data):

    with open(WAREHOUSE_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- ALLOCATE RESOURCES ----------------
def allocate_resources(needs):

    warehouse_data = load_warehouse()

    allocated_resources = {}

    shortage = False

    for resource, required_quantity in needs.items():

        remaining_need = required_quantity

        allocated_quantity = 0

        allocated_warehouse = "NOT ALLOCATED"

        for warehouse_name, stock in warehouse_data.items():

            available = stock.get(resource, 0)

            if available <= 0:
                continue

            take = min(available, remaining_need)

            if take > 0:

                stock[resource] -= take

                allocated_quantity += take

                remaining_need -= take

                allocated_warehouse = warehouse_name

            if remaining_need <= 0:
                break

        allocated_resources[resource] = {

            "quantity": allocated_quantity,

            "warehouse": allocated_warehouse
        }

        # ✅ correct shortage logic
        if remaining_need > 0:
            shortage = True

    save_warehouse(warehouse_data)

    return allocated_resources, shortage


# ---------------- RESTOCK WAREHOUSE ----------------
def restock_warehouse():

    warehouse_data = load_warehouse()

    default_stock = {
        "blankets": 1000,
        "food": 2000,
        "medical_kits": 500
    }

    for warehouse_name in warehouse_data:

        for item, value in default_stock.items():

            warehouse_data[warehouse_name][item] = value

    save_warehouse(warehouse_data)

    return {
        "message": "Warehouse restocked successfully"
    }

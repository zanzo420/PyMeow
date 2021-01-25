from pymeow import enumerate_processes

for proc in enumerate_processes():
    print(f"[{proc['name']}]")
    for module, module_data in proc["modules"].items():
        print(f"\t{module}: {hex(module_data['baseaddr'])}")
from pymeow import enumerate_processes

for proc in enumerate_processes():
    modules = ", ".join(list(proc["modules"].keys()))
    print(f"[{proc['name']}] Modules: {modules}")
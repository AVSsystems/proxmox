import subprocess
import json

def get_vm_status():
    # Execute Proxmox cluster status command
    status = subprocess.check_output(["pvesh", "get", "/cluster/resources", "--output-format", "json"])
    data = json.loads(status)
    for item in data:
        if item.get('type') == 'vm':
            print(f"VMID: {item['vmid']} | Name: {item['name']} | Status: {item['status']}")

if __name__ == "__main__":
    get_vm_status()

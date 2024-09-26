import subprocess
import json

def get_lsblk_output():
    result = subprocess.run(['lsblk', '--json'], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"lsblk command failed with error: {result.stderr}")
    return json.loads(result.stdout)
def list_storage():
    lsblk_output = get_lsblk_output()
    block_device_names = [f"/dev/{device['name']}" for device in lsblk_output['blockdevices']]
    block_device_sizes = [f"{device['size']}" for device in lsblk_output['blockdevices']]
    headers = f"{'Device':<20}{'Size':>10}"
    combined_info = [headers] + [f"{name:<20}{size:>10}" for name, size in zip(block_device_names, block_device_sizes)]
    return combined_info

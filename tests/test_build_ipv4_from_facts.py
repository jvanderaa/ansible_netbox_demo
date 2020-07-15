"""
Unit test for building ipv4 from facts
"""
from plugins.filter.filter import FilterModule

def test_build_ipv4_from_facts():
    """
    Unit test of building ipv4 facts
    """
    null = None
    nxos_data = {
        "discovered_interpreter_python": "/usr/local/bin/python3.7",
        "net__hostname": "nxos01",
        "net__os": "7.3(0)D1(1)",
        "net__platform": "NX-OSv Chassis",
        "net_all_ipv4_addresses": [
            "172.31.1.101"
        ],
        "net_all_ipv6_addresses": [],
        "net_api": "cliconf",
        "net_fan_info": [
            {
                "hw_ver": "0.0",
                "model": null,
                "name": "ChassisFan1",
                "status": "Ok"
            },
            {
                "hw_ver": "0.0",
                "model": null,
                "name": "ChassisFan2",
                "status": "None"
            },
            {
                "hw_ver": "--",
                "model": "--",
                "name": "Fan_in_PS1",
                "status": "Ok"
            },
            {
                "hw_ver": "--",
                "model": "--",
                "name": "Fan_in_PS2",
                "status": "Failure"
            }
        ],
        "net_features_enabled": [
            "privilege"
        ],
        "net_filesystems": [
            "bootflash:"
        ],
        "net_gather_network_resources": [],
        "net_gather_subset": [
            "hardware",
            "default",
            "legacy",
            "interfaces",
            "features"
        ],
        "net_hostname": "nxos01",
        "net_image": "bootflash:///titanium-d1.7.3.0.D1.1.bin",
        "net_interfaces": {
            "Ethernet2/1": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/10": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/11": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/12": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/13": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/14": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/15": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/16": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/17": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/18": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/19": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/2": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/20": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/21": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/22": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/23": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/24": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/25": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/26": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/27": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/28": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/29": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/3": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/30": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/31": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/32": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/33": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/34": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/35": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/36": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/37": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/38": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/39": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/4": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/40": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/41": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/42": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/43": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/44": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/45": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/46": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/47": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/48": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/5": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/6": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/7": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/8": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet2/9": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/1": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/10": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/11": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/12": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/13": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/14": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/15": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/16": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/17": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/18": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/19": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/2": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/20": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/21": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/22": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/23": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/24": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/25": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/26": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/27": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/28": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/29": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/3": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/30": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/31": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/32": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/33": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/34": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/35": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/36": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/37": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/38": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/39": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/4": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/40": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/41": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/42": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/43": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/44": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/45": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/46": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/47": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/48": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/5": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/6": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/7": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/8": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet3/9": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/1": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/10": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/11": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/12": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/13": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/14": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/15": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/16": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/17": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/18": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/19": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/2": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/20": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/21": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/22": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/23": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/24": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/25": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/26": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/27": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/28": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/29": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/3": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/30": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/31": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/32": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/33": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/34": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/35": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/36": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/37": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/38": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/39": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/4": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/40": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/41": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/42": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/43": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/44": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/45": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/46": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/47": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/48": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/5": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/6": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/7": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/8": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "Ethernet4/9": {
                "bandwidth": 1000000,
                "duplex": "auto",
                "macaddress": "0000.0000.002f",
                "mode": "routed",
                "mtu": "1500",
                "speed": "auto-speed",
                "state": "down",
                "type": "Ethernet"
            },
            "mgmt0": {
                "bandwidth": 1000000,
                "duplex": "full",
                "ipv4": {
                    "address": "172.31.1.101",
                    "masklen": 24
                },
                "macaddress": "0c25.ea9d.9000",
                "mode": "routed",
                "mtu": "1500",
                "speed": "1000 Mb/s",
                "state": "up",
                "type": "Ethernet"
            }
        },
        "net_interfaces_list": [
            "mgmt0",
            "Ethernet2/1",
            "Ethernet2/2",
            "Ethernet2/3",
            "Ethernet2/4",
            "Ethernet2/5",
            "Ethernet2/6",
            "Ethernet2/7",
            "Ethernet2/8",
            "Ethernet2/9",
            "Ethernet2/10",
            "Ethernet2/11",
            "Ethernet2/12",
            "Ethernet2/13",
            "Ethernet2/14",
            "Ethernet2/15",
            "Ethernet2/16",
            "Ethernet2/17",
            "Ethernet2/18",
            "Ethernet2/19",
            "Ethernet2/20",
            "Ethernet2/21",
            "Ethernet2/22",
            "Ethernet2/23",
            "Ethernet2/24",
            "Ethernet2/25",
            "Ethernet2/26",
            "Ethernet2/27",
            "Ethernet2/28",
            "Ethernet2/29",
            "Ethernet2/30",
            "Ethernet2/31",
            "Ethernet2/32",
            "Ethernet2/33",
            "Ethernet2/34",
            "Ethernet2/35",
            "Ethernet2/36",
            "Ethernet2/37",
            "Ethernet2/38",
            "Ethernet2/39",
            "Ethernet2/40",
            "Ethernet2/41",
            "Ethernet2/42",
            "Ethernet2/43",
            "Ethernet2/44",
            "Ethernet2/45",
            "Ethernet2/46",
            "Ethernet2/47",
            "Ethernet2/48",
            "Ethernet3/1",
            "Ethernet3/2",
            "Ethernet3/3",
            "Ethernet3/4",
            "Ethernet3/5",
            "Ethernet3/6",
            "Ethernet3/7",
            "Ethernet3/8",
            "Ethernet3/9",
            "Ethernet3/10",
            "Ethernet3/11",
            "Ethernet3/12",
            "Ethernet3/13",
            "Ethernet3/14",
            "Ethernet3/15",
            "Ethernet3/16",
            "Ethernet3/17",
            "Ethernet3/18",
            "Ethernet3/19",
            "Ethernet3/20",
            "Ethernet3/21",
            "Ethernet3/22",
            "Ethernet3/23",
            "Ethernet3/24",
            "Ethernet3/25",
            "Ethernet3/26",
            "Ethernet3/27",
            "Ethernet3/28",
            "Ethernet3/29",
            "Ethernet3/30",
            "Ethernet3/31",
            "Ethernet3/32",
            "Ethernet3/33",
            "Ethernet3/34",
            "Ethernet3/35",
            "Ethernet3/36",
            "Ethernet3/37",
            "Ethernet3/38",
            "Ethernet3/39",
            "Ethernet3/40",
            "Ethernet3/41",
            "Ethernet3/42",
            "Ethernet3/43",
            "Ethernet3/44",
            "Ethernet3/45",
            "Ethernet3/46",
            "Ethernet3/47",
            "Ethernet3/48",
            "Ethernet4/1",
            "Ethernet4/2",
            "Ethernet4/3",
            "Ethernet4/4",
            "Ethernet4/5",
            "Ethernet4/6",
            "Ethernet4/7",
            "Ethernet4/8",
            "Ethernet4/9",
            "Ethernet4/10",
            "Ethernet4/11",
            "Ethernet4/12",
            "Ethernet4/13",
            "Ethernet4/14",
            "Ethernet4/15",
            "Ethernet4/16",
            "Ethernet4/17",
            "Ethernet4/18",
            "Ethernet4/19",
            "Ethernet4/20",
            "Ethernet4/21",
            "Ethernet4/22",
            "Ethernet4/23",
            "Ethernet4/24",
            "Ethernet4/25",
            "Ethernet4/26",
            "Ethernet4/27",
            "Ethernet4/28",
            "Ethernet4/29",
            "Ethernet4/30",
            "Ethernet4/31",
            "Ethernet4/32",
            "Ethernet4/33",
            "Ethernet4/34",
            "Ethernet4/35",
            "Ethernet4/36",
            "Ethernet4/37",
            "Ethernet4/38",
            "Ethernet4/39",
            "Ethernet4/40",
            "Ethernet4/41",
            "Ethernet4/42",
            "Ethernet4/43",
            "Ethernet4/44",
            "Ethernet4/45",
            "Ethernet4/46",
            "Ethernet4/47",
            "Ethernet4/48"
        ],
        "net_license_hostid": "TBEA9D9000B",
        "net_memfree_mb": 982.23046875,
        "net_memtotal_mb": 2992.91015625,
        "net_model": "NX-OSv Chassis (\"NX-OSv Supervisor Module\")",
        "net_module": [
            {
                "model": "N7K-SUP1",
                "ports": 0,
                "status": "active *",
                "type": "NX-OSv Supervisor Module"
            },
            {
                "model": "N7K-F248XP-25",
                "ports": 48,
                "status": "ok",
                "type": "NX-OSv Ethernet Module"
            },
            {
                "model": "N7K-F248XP-25",
                "ports": 48,
                "status": "ok",
                "type": "NX-OSv Ethernet Module"
            },
            {
                "model": "N7K-F248XP-25",
                "ports": 48,
                "status": "ok",
                "type": "NX-OSv Ethernet Module"
            }
        ],
        "net_neighbors": {
            "mgmt0": [
                {
                    "host": "rtr-1.josh-v.com",
                    "port": "GigabitEthernet0/1",
                    "sysname": "rtr-1.josh-v.com"
                }
            ]
        },
        "net_platform": "N7K-C7018",
        "net_power_supply_info": [
            {
                "amps": "77.96",
                "model": "DS-CAC-845W",
                "number": 1,
                "status": "Ok",
                "watts": "3274.32"
            },
            {
                "amps": "0.00",
                "model": "------------",
                "number": 2,
                "status": "Absent",
                "watts": "0.00"
            }
        ],
        "net_python_version": "3.7.7",
        "net_serialnum": "TMEA9D9000B",
        "net_system": "nxos",
        "net_version": "7.3(0)D1(1)",
        "net_vlan_list": [
            1
        ],
        "network_resources": {}
    }

    test_data = {
        "discovered_interpreter_python": "/usr/local/bin/python3.7",
        "net_all_ipv4_addresses": [
            "192.168.0.167",
            "172.31.1.1",
            "10.100.1.1",
            "10.50.50.1"
        ],
        "net_all_ipv6_addresses": [],
        "net_api": "cliconf",
        "net_filesystems": [
            "flash0:"
        ],
        "net_filesystems_info": {
            "flash0:": {
                "spacefree_kb": 1948176.0,
                "spacetotal_kb": 2092496.0
            }
        },
        "net_gather_network_resources": [],
        "net_gather_subset": [
            "interfaces",
            "default",
            "hardware"
        ],
        "net_hostname": "rtr-1",
        "net_image": "flash0:/vios-adventerprisek9-m",
        "net_interfaces": {
            "GigabitEthernet0/0": {
                "bandwidth": 1000000,
                "description": null,
                "duplex": "Auto",
                "ipv4": [
                    {
                        "address": "192.168.0.167",
                        "subnet": "24"
                    }
                ],
                "lineprotocol": "up",
                "macaddress": "0c25.ea08.4900",
                "mediatype": "RJ45",
                "mtu": 1500,
                "operstatus": "up",
                "type": "iGbE"
            },
            "GigabitEthernet0/1": {
                "bandwidth": 1000000,
                "description": null,
                "duplex": "Auto",
                "ipv4": [
                    {
                        "address": "172.31.1.1",
                        "subnet": "24"
                    }
                ],
                "lineprotocol": "up",
                "macaddress": "0c25.ea08.4901",
                "mediatype": "RJ45",
                "mtu": 1500,
                "operstatus": "up",
                "type": "iGbE"
            },
            "GigabitEthernet0/2": {
                "bandwidth": 1000000,
                "description": null,
                "duplex": "Auto",
                "ipv4": [
                    {
                        "address": "10.100.1.1",
                        "subnet": "24"
                    }
                ],
                "lineprotocol": "up",
                "macaddress": "0c25.ea08.4902",
                "mediatype": "RJ45",
                "mtu": 1500,
                "operstatus": "up",
                "type": "iGbE"
            },
            "GigabitEthernet0/3": {
                "bandwidth": 1000000,
                "description": null,
                "duplex": "Auto",
                "ipv4": [],
                "lineprotocol": "down",
                "macaddress": "0c25.ea08.4903",
                "mediatype": "RJ45",
                "mtu": 1500,
                "operstatus": "down",
                "type": "iGbE"
            },
            "Loopback0": {
                "bandwidth": 8000000,
                "description": null,
                "duplex": null,
                "ipv4": [
                    {
                        "address": "10.50.50.1",
                        "subnet": "32"
                    }
                ],
                "lineprotocol": "up",
                "macaddress": null,
                "mediatype": null,
                "mtu": 1514,
                "operstatus": "up",
                "type": null
            }
        },
        "net_iostype": "IOS",
        "net_memfree_mb": 253007.0703125,
        "net_memtotal_mb": 315455.65625,
        "net_model": "IOSv",
        "net_neighbors": {
            "GigabitEthernet0/0": [
                {
                    "host": "joshv-sw01.josh-v.com",
                    "port": "GigabitEthernet1/0/47"
                }
            ],
            "GigabitEthernet0/1": [
                {
                    "host": "nxos01(TBEA9D9000B)",
                    "port": "mgmt0"
                },
                {
                    "host": "nxos03(TBEAD8A300B)",
                    "port": "mgmt0"
                },
                {
                    "host": "nxos04(TBEA22BA00B)",
                    "port": "mgmt0"
                },
                {
                    "host": "nxos02(TBEA761700B)",
                    "port": "mgmt0"
                }
            ],
            "GigabitEthernet0/2": [
                {
                    "host": "rtr-4.josh-v.com",
                    "port": "GigabitEthernet0/0"
                }
            ]
        },
        "net_python_version": "3.7.7",
        "net_serialnum": "9GRLJCPTN0VYA3VWS0V15",
        "net_system": "ios",
        "net_version": "15.6(1)T",
        "network_resources": {}
    }

    expected_result = [
        {"interface": "GigabitEthernet0/0", "address": "192.168.0.167/24"},
        {"interface": "GigabitEthernet0/1", "address": "172.31.1.1/24"},
        {"interface": "GigabitEthernet0/2", "address": "10.100.1.1/24"},
        {"interface": "Loopback0", "address": "10.50.50.1/32"}
    ]

    nxos_result = [
        {"interface": "mgmt0", "address": "172.31.1.101/24"}
    ]
    assert FilterModule.build_ipv4_from_facts(test_data) == expected_result
    assert FilterModule.build_ipv4_from_facts(nxos_data) == nxos_result

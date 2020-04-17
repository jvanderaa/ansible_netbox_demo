#!/usr/bin/python
"""
Author: Josh VanDeraa

Filters related to the Ansible Config testing Playbooks
"""
import requests


class FilterModule:
    """
    Defines a filter module object.
    """

    @staticmethod
    def filters():
        """
        Return a list of hashes where the key is the filter
        name exposed to playbooks and the value is the function.
        """
        return {
            "get_ciscoios_serial_list": FilterModule.get_ciscoios_serial_list,
            "compare_lists": FilterModule.compare_lists,
            "convert_mac_address": FilterModule.convert_mac_address,
            "get_role_from_hostname": FilterModule.get_role_from_hostname,
            "get_interface_type": FilterModule.get_interface_type,
            "get_interface_by_bandwidth": FilterModule.get_interface_by_bandwidth,
            "build_ipv4_from_facts": FilterModule.build_ipv4_from_facts,
            "get_interface_id": FilterModule.get_interface_id,
        }

    @staticmethod
    def get_ciscoios_serial_list(ansible_facts):
        """
        Goal: Take information in Ansible Facts and return a list of serial numbers for the logical
        device. If it is a stack of switches with a single management, this should return multiple
        serial numbers. If it is a single unit then it should return the single serial number within
        a list.

        ansible_net_serialnum (string)         The serial number of the remote device

        ansible_net_stacked_serialnums (list)  when multiple devices are configured in a stack
                                                The serial numbers of each device in the stack

        """
        # Check if net_stacked_serialnums exists, then return it
        if ansible_facts.get("net_stacked_serialnums") is not None:
            return ansible_facts.get("net_stacked_serialnums")

        # Check that net_serialnum exists, returning the string back as a list of one
        if ansible_facts.get("net_serialnum") is not None:
            return [ansible_facts.get("net_serialnum")]

        return None

    @staticmethod
    def convert_mac_address(mac_address):
        """
        Goal: Return all MAC addresses sent in as a type of EAU-48 Address type
        Default: If None or 'None' is sent in as the Mac address, then all 0s are returned
        A method to verify that the MAC address is in a valid format for Netbox
        and returns a 00:00:00:00:00:00 if the MAC address is of type None

        EUI48      : AB:CD:EF:01:23:45
        "Cisco"    : abcd.ef01.2345
        "Microsoft": AB-CD-EF-01-23-45
        """
        if mac_address in ("None", None):
            mac_address = "0000.0000.0000"

        mac_address = mac_address.upper()
        mac_address = mac_address.replace(".", "")
        mac_address = mac_address.replace("-", "")
        mac_address = mac_address.replace(":", "")
        mac_address = ":".join(
            [mac_address[i : i + 2] for i, j in enumerate(mac_address) if not i % 2]
        )

        return mac_address

    @staticmethod
    def compare_lists(device_serial_numbers, netbox_serial_numbers):
        """
        A method to verify that the serial number(s) of a device/virtual chassis
        are in fact the same
        """
        device_serials_set = set(device_serial_numbers)
        netbox_serials_set = set(netbox_serial_numbers)

        return device_serials_set == netbox_serials_set

    @staticmethod
    def get_role_from_hostname(hostname):
        """
        Method to get a role from the hostname

        Args:
            hostname (string): String representation of the hostname
        """
        if "sw" in hostname:
            return "Switch"

        if "rtr" in hostname:
            return "Router"

        if "fw" in hostname:
            return "Firewall"

        if "nxos" in hostname:
            return "Switch"

        if "veos" in hostname:
            return "Switch"

        return None

    @staticmethod
    def get_interface_by_bandwidth(bandwidth_value):
        """
        Method to get the interface type based on the bandwidth value

        Args:
            bandwidth_value (int): Integer of the bandwith speed
        """
        if bandwidth_value == 8000000:
            return "Virtual"

        if bandwidth_value == 1000000:
            return "1000base-t"

        if bandwidth_value == 10000000:
            return "10gbase-t"

    @staticmethod
    def build_ipv4_from_facts(ansible_facts):
        """
        Method to build IPv4 CIDR address from the Ansible Facts output:

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

        ========================================================================

        Returns: [
            {"interface": "GigabitEthernet0/0", "address": "192.168.0.167/24"},
            {"interface": "GigabitEthernet0/1", "address": "172.31.1.1/24"}
        ]

        [summary]
        Args:
            ipv4_dict (dict): Dictionary from Ansible Facts representing addresses
        """
        return_list = []
        interface_facts = ansible_facts.get("net_interfaces")

        if interface_facts is not None:
            for interface, data in interface_facts.items():
                ipv4 = data.get("ipv4", None)
                if ipv4 is None:
                    continue

                # IOS Switch Output
                if isinstance(ipv4, list):
                    for prefix in ipv4:
                        prefix_len = prefix.get("subnet", None)
                        if prefix_len is None:
                            prefix_len = prefix.get("masklen")
                        cidr = f"{prefix['address']}/{prefix_len}"
                        return_list.append({"interface": interface, "address": cidr})

                # NXOS Switch output
                if isinstance(ipv4, dict):
                    if ipv4 == {}:
                        continue
                    cidr = f"{ipv4['address']}/{ipv4['masklen']}"
                    return_list.append({"interface": interface, "address": cidr})

        return return_list

    @staticmethod
    def get_interface_id(vm_name, netbox_headers):
        """
        Get an Interface ID from Netbox

        Args:
            vm_name (string): Name of the VM
        """
        url = (
            "http://netbox03/api/virtualization/interfaces/?virtual_machine=%s"
            % vm_name
        )
        result = requests.get(url, headers=netbox_headers)
        return result.json()["results"][0]["id"]

    @staticmethod
    def get_interface_type(interface_name):
        """
        Method to return the interface type (Physical, Virtual, speed) based on the name of the
        interface

        Args:
            interface_name (string): Interface Name
        """
        if "eth" in interface_name:
            return "1000base-t"

        if "Gigabit" in interface_name:
            return "1000base-t"

        if "Ethernet" in interface_name:
            return "1000base-t"

        if "switch0" in interface_name:
            return "Virtual"

        if "lo" in interface_name:
            return "Virtual"

        if "Loopback" in interface_name:
            return "Virtual"

        if "vlan" in interface_name.lower():
            return "Virtual"

        if "Port-channel" in interface_name:
            return "LAG"

        if "mgmt0" in interface_name:
            return "1000base-t"

        if "Management1" in interface_name:
            return "1000base-t"

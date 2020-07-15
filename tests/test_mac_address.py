"""
Test of Ansible Filters - MAC Address conversion
"""
from plugins.filter.filter import FilterModule


def test_filtermodule_convert_mac_address():
    """
    Function to test mac address filter
    """
    mac_address = "123a.124a.2387"
    mac_address2 = "12-3A-12-4A-23-87"
    assert FilterModule.convert_mac_address(mac_address) == "12:3A:12:4A:23:87"
    assert FilterModule.convert_mac_address(mac_address2) == "12:3A:12:4A:23:87"

"""
Test of Ansible Filters
"""
from plugins.filter.filter import FilterModule


def test_get_role_from_hostname():
    """
    Functional test of getting a role from the device name
    """
    device_test_mapping = {
        "sw": "Switch",
        "rtr": "Router",
        "fw": "Firewall",
        "nxos": "Switch",
        "veos": "Switch"
    }
    for text_in_name, device_role in device_test_mapping.items():
        assert FilterModule.get_role_from_hostname(text_in_name) == device_role  # nosec

    device_name_mapping = {
        "218-sw01": "Switch",
        "rtr-1": "Router",
        "14-fw1": "Firewall",
        "dc01-nxos-02": "Switch",
        "dc04-veos-14": "Switch"
    }

    for text_in_name, device_role in device_name_mapping.items():
        assert FilterModule.get_role_from_hostname(text_in_name) == device_role  # nosec

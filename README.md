# Ansible NetBox Demo

![](https://github.com/jvanderaa/ansible_netbox_demo/workflows/CI/badge.svg)

## Link to recording

Thanks to the Red Hat team that had the recording done of this. You can find it on YouTube at
[https://www.youtube.com/watch?v=GyQf5F0gr3w](https://www.youtube.com/watch?v=GyQf5F0gr3w).  

## Most Recent Updates

I have moved all of the data that was previously configured to be added to NetBox within the 00_setup_netbox_devices.yml
file to be configured in the all.yml. If looking to bootstrap your NetBox environment, this is the
main information that will need to get updated.  

**Important Note**
> This is **NOT** meant to be run constantly in your environment. Please do not use as such. This is
> a bootstrapping setup, to get you running. The intent of NetBox is to become the Source of Truth
> for your environment. If all you are doing is constantly updating NetBox from your devices, then
> the source of truth is the network device, not NetBox. Please be working to get your environment
> to the state that you have a Source of Truth that is NOT your device.

## Docker Container

To get access to the docker container follow the process outlined here:
https://docs.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages#:~:text=You%20can%20use%20the%20docker,TAG_NAME%20with%20tag%20for%20the


## Start

To setup NetBox, checkout https://netbox.readthedocs.io
Setup an API Key in the upper right admin panel
Generate an environment of devices to use

## Requirements

1. NetBox Installation
2. Docker Desktop on system
3. If running on Windows, you do not have `make`. The Makefile is just shortcuts to be used. Take a
look at the Makefile for the exact commands that replace the specific make commands.

## How to

1. Setup NetBox (see the beginning)
2. Setup a new file named .env that contains information about your NetBox environment for the container. See below for example config
3. Update your `group_vars/all.yml`,  `group_vars/` and `host_vars/` accordingly with credentials to connect to the devices, see below for example config
4. Create a container - `make build`
5. Enter the container - `make cli`
6. Setup NetBox with executing `ansible-playbook 00_setup_netbox_devices.yml`
7. Setup Devices Into Netbox `ansible-playbook 01_setup_devices.yml -i start_inventory` replace `start_inventory` with whatever your static inventory file is
8. Setup Interfaces using dynamic inventory `ansible-playbook 02_setup_interfaces.yml -i netbox_inventory.yml`
9. Run the audit `ansible-playbook 03_audit_netbox.yml -i netbox_inventory.yml` where you have updated the information in the netbox_inventory.yml file


### ENV File setup

```
NETBOX_API_KEY=<NetBox Key>
NETBOX_URL=<URL of NetBox>
```

### Group Vars, Host Vars

```yaml
---
ansible_user: <username>
ansible_password: <password>
ansible_network_os: <corresponding Ansible OS>
```

hostvars will only contain information overriding data points. In the example, the only thing set in the host vars
section is:

```yaml
---
rack_location: 41
```

## URLs

Helpful [URLs](./urls.md) have a few other links that may be helpful.

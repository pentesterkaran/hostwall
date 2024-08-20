![firewall_logo](https://github.com/pentesterkaran/hostwall/blob/main/logo/Hostwall.png)

## Overview

The hostWall is a Python-based tool designed to manage, and apply firewall rules from JSON files. This project aims to simplify the process of managing firewall configurations and provide a robust interface for rule management.

## Features

- Load firewall rules from JSON files
- Add, remove, and update firewall rules
- Save and export rules to JSON format
- Easy-to-use command-line interface

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pentesterkaran/hostwall.git
    ```

2. **Navigate to the hostwall directory:**

    ```bash
    cd hostwall
    ```

3. **Install the required dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. **Prepare your JSON rules file:**

    Add firewall rules in JSON file. For example:

    ```json
        {
    "BannedIpAddress" : ["10.0.0.1","192.23.121.2"],
    "BannedPorts" : [8443],
    "BannedSubnet" : ["127."],
    "Timethreshold" : 10,
    "BlockPingAttack" : "True"

    }
    ```

2. **Start firewall**

    ```bash
    sudo python3 fw.py

    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.




# hostwall

# Firewall Rules Manager

## Overview

The Firewall Rules Manager is a Python-based tool designed to load, manage, and apply firewall rules from JSON files. This project aims to simplify the process of managing firewall configurations and provide a robust interface for rule management.

## Features

- Load firewall rules from JSON files
- Add, remove, and update firewall rules
- Save and export rules to JSON format
- Easy-to-use command-line interface

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/firewall-rules-manager.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd firewall-rules-manager
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your JSON rules file:**

    Create a JSON file with your firewall rules. For example:

    ```json
    {
        "rules": [
            {
                "action": "allow",
                "protocol": "tcp",
                "port": 80,
                "source": "0.0.0.0/0"
            },
            {
                "action": "deny",
                "protocol": "tcp",
                "port": 22,
                "source": "192.168.1.1/32"
            }
        ]
    }
    ```

2. **Run the Firewall Rules Manager:**

    ```bash
    python firewall_manager.py --load path/to/your/rules.json
    ```

    Use `--add`, `--remove`, and `--update` options to manage rules as needed.

3. **Export rules to JSON format:**

    ```bash
    python firewall_manager.py --export path/to/save/rules.json
    ```

## Command-line Options

- `--load <file>`: Load rules from a JSON file.
- `--add <rule>`: Add a new rule.
- `--remove <rule_id>`: Remove an existing rule by ID.
- `--update <rule_id> <rule>`: Update an existing rule by ID.
- `--export <file>`: Export the current rules to a JSON file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out to [your-email@example.com](mailto:your-email@example.com).


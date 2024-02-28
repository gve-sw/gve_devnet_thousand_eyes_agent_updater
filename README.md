# gve_devnet_thousand_eyes_agent_updater
This project automates the process of updating ThousandEyes endpoint agents by reading hostnames from a CSV file, mapping them to their respective agent IDs, updating their license type, and then logging the results in both JSON and CSV formats.

## Contacts
* Jorge Banegas

## Solution Components
* ThousandEyes API

## Installation/Configuration

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed. This project is tested with Python 3.8+.
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Update the `config.py` file with your ThousandEyes API access token:
   ```python
   access_token = 'YOUR_ACCESS_TOKEN_HERE'
   ```
5. Prepare a CSV file named `data.csv` in the project's root directory with the following format, where each line contains the hostname of an endpoint agent you wish to update:
   ```
   Hostname
   agent1.example.com
   agent2.example.com
   ```
   A template CSV file is provided in the repository for reference.

## Usage

To update your ThousandEyes endpoint agents, follow these steps:

1. Ensure you have completed the installation/configuration steps.
2. Run the script from the terminal:
   ```
   $ python main.py
   ```
3. The script will read the hostnames from `data.csv`, match them to agent IDs via the ThousandEyes API, update the license type for each agent, and log the results in `update_results.json` and `update_results.csv` files in the project directory.

## Screenshots

![/IMAGES/output.png](/IMAGES/output.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

This project is provided under the Cisco Sample Code License. For details, see [LICENSE](LICENSE.md).

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md).

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md).

#### DISCLAIMER:
**Please note:** This script is meant for demo purposes only. All tools/scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. We are not responsible for any damage or data loss incurred with their use. You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
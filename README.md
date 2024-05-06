# NFC Enabled Toll Gate Wireless Payment System

## Overview

This project is a dashboard designed to be utilized by toll gate attendants for managing customer transactions. The system employs Near Field Communication (NFC) technology, allowing customers to make payments by tapping their NFC-enabled smartphones on the hardware. Payments are deducted from the linked cards or accounts of the customers.

## Technologies Used

- **Python**: Utilized for interfacing with the NFC hardware.
- **JavaScript**: Employed to dump information to a JSON file and manage transactions in the transaction listener file, as well as to write transaction history to a file.

## Installation

To ensure the proper functioning of the NFC Enabled Toll Gate Wireless Payment System, follow these installation steps:

1. **Install Node.js and npm**:
   - Visit [Node.js website](https://nodejs.org/) to download and install Node.js and npm, if you haven't already done so.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/nfc-tollgate-payment.git
   cd nfc-tollgate-payment
   ```

3. **Install Dependencies**:
   - Navigate to the project directory and install the required dependencies using npm:
   ```bash
   npm install
   ```

## Usage

1. **Run the Python Interface**:
   - Start the Python script responsible for interfacing with the NFC hardware:
   ```bash
   python nfc_interface.py
   ```

2. **Start the Dashboard**:
   - Launch the dashboard application by running the following command in the project directory:
   ```bash
   npm start
   ```

3. **Customer Transactions**:
   - Customers can approach the toll gate and tap their NFC-enabled smartphones on the hardware.
   - The dashboard will display transaction details and deduct payments from the linked cards or accounts of the customers.

## Contributing

This project is open-source, and contributions are welcome. You can clone the repository, build upon it, and submit pull requests for any enhancements or fixes.

## License

This project is licensed under the [MIT License](LICENSE).

For any further inquiries or support, please contact anesu@infinitylinesofcode.com .

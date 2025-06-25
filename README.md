ATM Interface with PIN Verification

This project is a simple command-line ATM system built using Python. It simulates basic banking operations like deposit, withdrawal, and balance inquiry. All transactions are protected by a PIN, which is read from an external file (pin.txt) for authentication.

Features

- Deposit and withdraw money with proper input checks
- Check current account balance
- PIN-based access for all operations
- Error handling for invalid inputs and insufficient balance

 How to Run

1. Make sure Python 3 is installed on your system.
2. Create a file named pin.txt in the same directory as the script.
3. Add your desired PIN to that file (e.g., 123456).
4. Run the program using:

```bash
python bank_atm.py

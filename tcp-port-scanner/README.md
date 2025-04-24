# ScanTCP
This project aims to develop a basic tool to identify open ports on remote hosts.

Este projeto tem como objetivo de desenvolver uma ferramenta básica para identificar portas abertas em hosts remotos.
## Project structure
```
📁 tcp-port-scanner
├── scanner_gui.py
├── 📁 scanner
│   └── tcp_scanner.py
├── requirements.txt
└── README.md
```
## Features
- Accepts a host (IP or domain).
- Scans a range of TCP ports (e.g., 1 to 100).
- Attempts to connect to each port.
- Displays whether the port is open or closed.

## Tecnologies used
- Python

## How to run the project

Before running the project, make sure you have Python installed on your machine. The recommended version is Python 3.10 or higher.

1. Clone the repository
```bash
git clone https://github.com/IsabellaPassarelli/ScanTCP.git
```
2. Navigate into the project folder
```bash
cd tcp-port-scanner
```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Run the file 
```bash
python tcp_scanner.py
```
5. Fill in the Host/IP, Starting Port, and Ending Port fields.
6. Click the "Scan" button to start scanning.
7. The results will appear at the bottom of the screen, showing the open ports.

## Educational purpose
This project is intended for educational purposes. It was developed as a practical exercise for learning the fundamentals of networking, Python programming, and basic techniques of footprinting and vulnerability analysis.
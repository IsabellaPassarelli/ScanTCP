# ScanTCP
This project is a TCP port scanner tool with a graphical interface, developed in Python using the pygame library. It allows scanning a range of ports on an IP or host and displaying the results interactively.

## Project structure
```
📁 tcp-port-scanner
├── main.py
├── scanner_gui.py
├── 📁 scanner
│   └── tcp_scanner.py
├── requirements.txt
└── README.md
```

## Features
1. Data Input:
    - The user can enter the host (IP or domain name).
    - The user can set the start port and end port for the scan.

2. Port Scanning:
    - When clicking the "Scan" button, the program scans the ports in the defined range.
    - The program shows the scan result: whether there are open ports or if no open ports were found.

3. Results:
    - The scan result is displayed on the screen, showing the open ports.
    - If no open ports are found, a message is displayed informing the user of that.

4. Graphical Interface:
    - The project uses the pygame library to create a simple and interactive graphical interface.

## Tecnologies used
- Python
- Pygame
- Sockets (TCP network)

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
or
```bash
py -m pip install -r requirements.txt
```
4. Run the file 
```bash
python main.py
```
or
```bash
py main.py
```

## How does it work?
1. In the Host/IP field, enter the IP or domain you want to scan (e.g., 127.0.0.1 or google.com).
2. In the Start Port field, enter the number of the first port you want to test (e.g., 20).
3. In the End Port field, enter the number of the last port you want to test (e.g., 80).
4. Click the "Scan" button to start the scan.
5. The scan results will be displayed below the filled fields, showing whether or not there are open ports.

## Educational purpose
This project is intended for educational purposes. It was developed as a practical exercise for learning the fundamentals of networking, Python programming, and basic techniques of footprinting and vulnerability analysis.

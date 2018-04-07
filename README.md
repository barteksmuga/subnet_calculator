# subnet_calculator

Calculator can both get an IP address with CIDR as an argument or run with IP address got from machine it runs on. Firstly it checks if an address is valid (suppose to consist of decimals and dots, all parts are between 0 to 255 and CIDR is between 0 to 32.)

### Output data:

* network address
* network class
* transforms CIDR to netmask
* broadcast address
* first host address
* last host address
* maximum hosts amount

All addresses are shown in both decimal and binary format. They are also written to `data.json` file.

Created by Bartłomiej Smuga.


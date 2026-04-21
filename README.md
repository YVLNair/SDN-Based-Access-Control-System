# SDN-Based Access Control System using POX

## Problem Statement

Design and implement a Software Defined Networking (SDN) based access control system that allows only authorized hosts to communicate within a network using OpenFlow rules.

---

## Tools & Technologies

* Mininet (network emulation)
* POX Controller (SDN controller)
* OpenFlow protocol
* iperf (performance testing)
* Ping (connectivity testing)
* ovs-ofctl (flow table verification)

---

## Installation

### 1. Update system
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install required packages
```bash
sudo apt install -y build-essential gcc make linux-headers-$(uname -r)
```

### 3. Install Mininet (for SDN simulation)
```bash
sudo apt install -y mininet
```

### 4. Install POX Controller
```bash
git clone https://github.com/noxrepo/pox.git
```

### 5. Clone the repository
```bash
git clone https://github.com/YVLNair/SDN-Based-Access-Control-System.git
```

### 6. Navigate to project directory
```bash
cd SDN-Based-Access-Control-System
```
---

## System Overview

The system uses a centralized SDN controller (POX) to enforce access control policies.
When a packet arrives at the switch, it is forwarded to the controller via a PacketIn event.
The controller checks the source MAC address against a whitelist and installs flow rules only for authorized hosts.

Unauthorized hosts are blocked since no forwarding rules are installed.

---

## Setup & Execution

### 1. Copy Controller File to POX Directory

```bash
cp access_control.py ~/pox/pox/
```

### 2. Start POX Controller

```bash
cd ~/pox
./pox.py access_control
```

### 3. Start Mininet Topology

```bash
sudo mn --topo single,3 --mac --controller=remote
```

---

## Testing & Demonstration

### Allowed Hosts

```bash
h1 ping h2
h1 iperf -s &
h2 iperf -c h1
```

### Blocked Hosts

```bash
h3 ping h1
h3 iperf -c h1
```

---

## Expected Output

* Authorized hosts communicate successfully
* Unauthorized hosts show:

  * "Destination Host Unreachable"
  * "No route to host"
* iperf shows high throughput for allowed hosts and failure for blocked hosts

---

## Flow Table Verification

```bash
sudo ovs-ofctl dump-flows s1
```

Only authorized MAC addresses appear in the flow table.

---

## Test Scenarios

### Scenario 1: Allowed vs Blocked

* h1 ↔ h2 communication succeeds
* h3 communication fails

### Scenario 2: Normal vs Failure

* iperf succeeds for authorized hosts
* iperf fails for unauthorized hosts

---

## Validation & Regression Testing

### Validation

System behavior is verified using:

* Ping (connectivity)
* iperf (performance)
* Flow table inspection (rule verification)

### Regression Testing

When the whitelist is modified, the system updates behavior accordingly without affecting valid rules.

---

## Proof of Execution

Screenshots/logs included in the repository:

* Ping results
* iperf results
* Flow table output

---

## Project Structure

```
sdn-access-control/
├── access_control.py
├── README.md
└── screenshots/
```

---

## References

* Mininet Documentation
* POX Controller Documentation
* OpenFlow Specification

---

## Conclusion

The project successfully demonstrates centralized access control in an SDN environment.
Flow rules are dynamically installed based on a whitelist policy, ensuring that only authorized hosts can communicate while unauthorized hosts are blocked.

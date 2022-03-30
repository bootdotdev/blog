---
title: "Quantum Programming 101: Backend Monitor"
author: Macauley Coggins
date: "2020-05-12"
categories: 
  - "misc"
images:
  - /img/QvKyBb3LzY7gFPBxE8FFse-scaled.jpeg
---

# Introduction

In a previous tutorial we showed how you can get basic information on all quantum devices using backend\_overview().

While this function is great to get information on all quantum devices at a glance it is not detailed on specific information such as qubit and gate errors. To get more detailed information on a quantum device (such as configuration and individual qubits and gates) you can use backend\_monitor().

# Implementation

Unlike backend\_overview() this is for getting information on a specific device so you have to pass the device name in to the function as an argument.

For example to get real time information on the IBMQ Burlngton device you enter the following:

```py
backend_monitor(provider.backends.ibmq_burlington)
```

and for another device like IBMQ Vigo:

```py
backend_monitor(provider.backends.ibmq_vigo)
```

# Steps

1. Copy and paste the code below in to a python file
2. Enter your API token in the IBMQ.enable\_account('Insert API token here') part
3. Save and run

# Code

```py
from qiskit import IBMQ
from qiskit.tools.monitor import backend_monitor

IBMQ.enable_account('ENTER API KEY HERE') # Insert your API token in to here
provider = IBMQ.get_provider(hub='ibm-q')

backend_monitor(provider.backends.ibmq_burlington) # Function to get all information back about a quantum  device  

print('\nPress any key to close')
input()
```

# Output

After the code is ran you will be given a list of information about the device including the configuration and specific information on individual qubits and gates.

![Screenshot showing the device information for the IBMQ Burlington quantum device.](https://images.squarespace-cdn.com/content/v1/5d52f7bd9d7b3e0001819015/1589211299682-JRAP2BQJ68X9626WMYFM/ke17ZwdGBToddI8pDm48kMKX0W--EDmH4ALtrb_P3jhZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyjFp1amORK2t8xjWd9mAMK3AXF3CMzEIgdjV21ENu1Md21upyglknm2oG7PZ4SNRg/2020-05-11+16_23_59-Window.png?format=750w)

Screenshot showing the device information for the IBMQ Burlington quantum device.

Want to learn about Quantum Programming? Head over to [Quantum Computing UK](https://quantumcomputinguk.org/).

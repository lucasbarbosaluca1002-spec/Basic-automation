# Log Processing Script


This repository contains **two versions of a log analysis program** created as part of my learning process with Python and basic security automation.

The first program is a **simpler script** that simulates a log file using a dictionary inside the code.  
It was created to practice logic, loops, dictionaries, and basic detection techniques such as brute force and port scan detection.

The second version, located inside the **Project/** folder, is a more complete implementation that **reads logs from a real file (`logs.json`)** and processes them automatically.

This structure demonstrates the progression from a **simple simulated environment** to a **script capable of reading and analyzing real log files**.

Hello! I created a small script to read a file where the dictionary **`logs`** represents the use of the following command:

```python
with open("path") as file:
```

The script reads the file content and processes the information contained in the logs.

<img width="100%" src="https://user-images.githubusercontent.com/8989346/136876224-bac0a91f-63a8-45ea-b5fc-6618bddf2335.gif" />

## Dictionaries Used


We created these dictionaries to store the results obtained while iterating through the **logs dictionary/file**.  
This allows the script to organize the information and later manipulate the data to generate warnings or alerts inside the system.

The dictionaries used are:

```python
portscan = {}
bruteforce = {}
users = {}
```

### Description

- **portscan** → Stores possible port scanning activities detected in the logs.  
- **bruteforce** → Stores possible brute force attempts detected in the logs.  
- **users** → Stores user-related information extracted from the logs.

These structures help keep the data organized and make it easier to analyze suspicious activity.

<img width="100%" src="https://user-images.githubusercontent.com/8989346/136876224-bac0a91f-63a8-45ea-b5fc-6618bddf2335.gif" />

### Temporary Variables

During the processing of the logs, we store data in temporary variables to maintain control of the file structure, its indexes, and its keys.

While the script iterates through the `logs` dictionary/file, the values are temporarily stored depending on the value of **X** at the moment the iteration occurs.

This allows the script to correctly identify the context of the data being processed and store the information in the appropriate dictionari

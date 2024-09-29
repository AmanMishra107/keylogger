# Keylogger Project

## Overview
This project is a sophisticated keylogger designed for **educational purposes only**. It showcases advanced techniques such as persistence, data exfiltration, encryption, and stealth. This project is not intended for malicious use and should be utilized responsibly.This code will only run on **Linux**

## Features
- **Persistence**: Automatically starts when the system reboots.
- **Data Exfiltration**: Sends logs to a remote server or email.
- **Encryption**: Encrypts the keystroke logs before storage or transmission.
- **Stealth**: Hides the process to avoid detection.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Modular Design**: Easily extendable with additional features.

## Requirements
- Python 3.x
- Libraries: `pynput`, `cryptography`, `requests`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NikhilMessa/keylogger.git
   cd keylogger

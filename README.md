# Vendramel-Projects — Python Sandbox

A collection of small, standalone Python scripts I built while learning the
language. Each file is self-contained and demonstrates a specific concept —
from algorithms and automation to scraping and a tiny game.

> 💡 For my production-grade, full-stack work see my pinned repositories:
> [mini-crm](https://github.com/Jeipocalo/mini-crm) ·
> [task-manager](https://github.com/Jeipocalo/task-manager) ·
> [api-receitas](https://github.com/Jeipocalo/api-receitas)

## Scripts

| Script | What it does | Key libraries |
|--------|--------------|---------------|
| `WebScraping.py` | Scrapes the latest headlines from BBC News and prints them with a count | `requests`, `beautifulsoup4` |
| `Database.py` | Connects to a MySQL database, runs a user-provided query and exports the results to an Excel file | `mysql-connector`, `pandas` |
| `SendMessage.py` | Bulk messaging from Excel contact lists — sends emails over SMTP (Office 365) and WhatsApp messages | `pandas`, `pywhatkit`, `smtplib` |
| `PCConfig.py` | Collects OS, network and hardware info (CPU, RAM, disks) and writes a `systeminfo.txt` report (Windows) | `psutil`, `py-cpuinfo`, `wmi`, `getmac` |
| `Conway.py` | Conway's Game of Life with a NumPy grid and an animated Matplotlib visualization | `numpy`, `matplotlib` |
| `GameProject.py` | A Pygame prototype: move a sprite with the arrow keys, switching background "stages" at the screen edge | `pygame` |
| `PasswordManager.py` | A CLI password vault that stores site/username/password entries in a JSON file (masked input) | stdlib (`json`, `getpass`) |
| `PasswordCreator.py` | Generates a random 16-character password from letters, digits and symbols | stdlib (`random`) |
| `FizzBuzz.py` | A configurable FizzBuzz where the user chooses the two words and their divisors | stdlib |
| `MergeFiles.py` | Concatenates two text files into a single output file | stdlib |
| `ChatBot.py` | A rule-based CLI chatbot that matches keywords to fixed responses | stdlib |

## Running

Each script runs on its own with Python 3:

```bash
python WebScraping.py
```

Scripts that use third-party libraries need them installed first, e.g.:

```bash
pip install requests beautifulsoup4 pandas numpy matplotlib pygame psutil py-cpuinfo wmi getmac pywhatkit mysql-connector-python
```

## Note

This repository is a **learning sandbox** — small experiments, not production
software. It documents my hands-on path with Python: algorithms, file and
database handling, automation, scraping and a bit of game programming.

## Author

João Pedro Vergopolan Vendramel · [LinkedIn](https://www.linkedin.com/in/joao-vendramel) · [GitHub](https://github.com/Jeipocalo)

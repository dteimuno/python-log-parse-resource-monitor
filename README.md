

```markdown
# 🧠 System Resource Monitor & Log Parser

This project contains two Python scripts designed for basic system monitoring and log analysis:

- `log_scanner.py`: Parses the system log file to search for specific keywords.
- `system_stats.py`: Displays real-time CPU and memory usage using `psutil`.

---

## 📁 Project Structure

```

.
├── log\_scanner.py        # Scans system.log for 'dead\_process' entries
├── system\_stats.py       # Prints CPU and memory usage stats
├── README.md             # Project documentation

````

---

## 📜 Description

### 🔍 `project.py`

A lightweight script to read and analyze lines from `/var/log/system.log`.

**Features:**
- Changes working directory to `/var/log` using a relative path.
- Streams and prints each line of `system.log`.
- Checks for the presence of the keyword `dead_process` (case-insensitive).
- Handles file access errors gracefully.

> ✅ Note: You may need elevated permissions (`sudo`) to access `/var/log/system.log`.

### 🖥️ `system_stats.py`

Uses the `psutil` library to display system hardware information and runtime usage statistics.

**Features:**
- Detects the number of logical and physical CPU cores.
- Measures CPU usage over a 1-second interval.
- Displays total available system memory.
- Includes a reusable function `get_memory_usage()` that returns memory stats as a dictionary.

---

## 🔧 Requirements

Ensure Python 3 and `psutil` are installed:

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install required package
pip install psutil
````

---

## 🚀 How to Run

### Run the log scanner:

```bash
python3 log_scanner.py
```

### Run the system resource monitor:

```bash
python3 system_stats.py
```

---

## 🧩 Sample Output

### `system_stats.py`

```
Logical CPUs : 8
Physical CPUs: 4
CPU Usage    : 12.3%
Memory Total : 16.00 GB
```

### `log_scanner.py`

```
line from system.log
line from system.log
...
Found 'dead_process' in log file.
```

---

## 📘 Future Improvements

* [ ] Add argparse support to specify log file paths dynamically.
* [ ] Export CPU and memory usage as JSON for integration with other tools.
* [ ] Extend `log_scanner.py` to support compressed logs (`.log.gz`) and time-based filtering.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Dennis Tei-Muno
[GitHub](https://github.com/dteimuno) • [LinkedIn](https://www.linkedin.com/in/dteimuno)


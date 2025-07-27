<!-- markdownlint-disable descriptive-link-text -->
<!-- markdownlint-disable no-duplicate-heading -->
<!-- markdownlint-disable no-bare-urls -->

# Access DB Export Scripts

This repository contains two scripts for exporting all tables from an Access Database (AccDB) to CSV files: `accdb-export-all.py` for Python environments and `accdb-export-all.sh` for Linux/macOS shells.

## Requirements

### Python Script

To run the Python script, make sure you have the following libraries installed:

- `mdbtools` - a library to work with Access databases (AccDB) in Python. Install it in your local machine using Homebrew or any other package manager.

```bash
brew install mdbtools
```

- The packages included inside [requirements.txt](./requirements.txt)

```bash
pip install -r requirements.txt
```

### Shell Script

The shell script assumes that the `mdb-tables` and `mdb-export` commands are available in your system's PATH. If they are not, please install the `mdbtools` package for your platform:

- For Windows: Download the mdbtools-0.43.zip from [here](https://github.com/mdbtools/mdbtools/releases) and extract it to a directory in your PATH.
- For Linux/macOS: Install it via Homebrew (preferred):

```bash
brew install mdbtools
```

or install it from source: https://github.com/mdbtools/mdbtools/

## Usage

### Python Script

To use the Python script, run:

```bash
pip install -r requirements.txt
cd scripts/
python accdb_export.py full-path-to-db
```

Replace full-path-to-db with the path to your Access database (AccDB). The script will export all tables from the database as CSV files in a new directory named after the database, under `result/`.

### Shell Script

To use the shell script, run:

```bash
cd scripts/
chmod +x accdb-export-all.sh
./accdb-export-all.sh full-path-to-db
```

Replace full-path-to-db with the path to your Access database (AccDB). The script will export all tables from the database as CSV files in a new directory named after the database, under `result/`.

## Example output

The scripts produce output similar to this:

```text
Tables found: [table1, table2]
Exporting table table1
Exported: result/dbname/table1.csv
Exporting table table2
Exported: result/dbname/table2.csv
All tables exported to result/dbname
```

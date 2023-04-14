## CSV to JSON Converter

This is a Python script that converts CSV files to JSON format.

### Requirements

- Python 3.x
- `csv` module (built-in)
- `json` module (built-in)

### Setup

1. Clone or download the repository to your computer.
2. Install Python 3.x if it is not already installed.
3. Create a virtual environment for the project by running the following command in your terminal: 

```python -m venv env```

4. Activate the virtual environment by running the following command in your terminal:

```source env/bin/activate```

### Usage

1. Place the CSV files you want to convert into the `input` directory.
2. Run the `import.py` script to convert the CSV files to JSON format.
3. The output JSON files will be placed in the `output` directory.

To run the script, open a terminal or command prompt and navigate to the directory where the script is located. Then run the following command:

```python3 csv_to_json.py```


The script will process all CSV files in the `input` directory and write the output JSON files to the `output` directory.

Note: You may need to modify the script to match the column headers in your CSV files, as well as the paths to your input and output directories.


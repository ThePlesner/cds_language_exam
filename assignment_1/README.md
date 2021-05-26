# Assignment 1 - Sentiment analysis

## Prerequisites

Bash and python 3 is needed to be able to run the shell-script and the python-scripts within this assignment. The python script has been tested on python 3.9.4, but this may not be required and older versions will most likely suffice.

## Setup

- Change into the assignment_1 directory if this has not already been done.
- Run the following command to create the virtual environment:

```
./create_venv_win.sh
```

If on a windows-system, or

```
./create_venv_unix.sh
```

If on a unix-system.

**NOTE:** If on a unix-system, permissions might have to be changed. This can be done by running the following command:

```
chmod +x create_venv_unix.sh
```

To run the script the virtual environment needs to be activated. This can be done by running the following command:

```
source venv/Scripts/activate
```

If on a windows-system, or

```
source venv/bin/activate
```

If on a unix-system.
To run the script use the following command:

```
python word_counts.py
```

For using default arguments, or

```
python word_counts.py [-d --data_dir_path] [-o --output_csv_path]
```

Where

- data_dir_path is the path to a directory containing a text-corpus. The script will find all txt-files within the data-folder by itself.
- output_csv_path is the path to an output csv. It will be created if it does not exist already.

**NOTE:** This repository already comes with a populated data-folder and output-folder.

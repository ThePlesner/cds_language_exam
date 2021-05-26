# Assignment 3 - Sentiment analysis

## Prerequisites

Bash and python 3 is needed to be able to run the shell-script and the python-scripts within this assignment. The python script has been tested on python 3.9.4, but this may not be required and older versions will most likely suffice.

## Setup

- Change into the assignment_3 directory if this has not already been done.
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

If on a unix-system. This repository already comes with an edgelist but if needed, you can create a new one by running the following command:

```
python create_edgelist.py
```

This will generate a new edgelist from the fake_or_real_news.csv dataset. Beware that this can take some time.
To create the network, run the following command:

```
python network.py
```

For using default arguments, or

```
python network.py [-e --edgelist_path] [-mw --min_weight]
```

Where

- edgelist_path is the path to an edgelist.csv. Default is edgelist.csv within the edgelists-folder.
- min_weight is the minimum weight an edge needs to be allowed to join the network. Default is 300.

**NOTE:** This repository already comes with an edgelist and a populated output/ and viz/ folder.

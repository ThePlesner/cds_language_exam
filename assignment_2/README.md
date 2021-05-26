# Assignment 2 - Sentiment analysis

## Prerequisites

Bash and python 3 is needed to be able to run the shell-script and the python-scripts within this assignment. The python script has been tested on python 3.9.4, but this may not be required and older versions will most likely suffice.

## Setup

- Change into the assignment_2 directory if this has not already been done.
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

If on a unix-system. To run the script, use the following command:

```
python sentiment.py
```

For using default arguments, or

```
python sentiment.py [-d --data_path] [-s --is_sample]
```

Where

- data_path is the path to the abcnews-date-text.csv. Default is abcnews-date-text.csv within the data-folder.
- is_sample is either true or false. If true, the script will run on 5000 headlines instead of the full dataset. This saves alot of time but the quality of the output-graph decreases dramatically.

**NOTE:** This repository already comes with a poplulated data and output folder, that has been run on the full dataset.

## Results

### What (if any) are the general trends?

We can see that something happens around 2008 and 2019. Both of these years take a dive in terms of their sentiment score and it is very clearly a trends of sorts.

### What (if any) inferences might you draw from them?

We can only guess, but around both of these years significant event happened. In 2008 and throughout 2009 we had the financial crisis which might've had a great impact on the headlines of the time. In 2019 Donald Trump was elected. Whether this event was good or bad is not up the author to judge, but certainly it stirret the waters and created a lot of headlines, most of which where voiced negatively.

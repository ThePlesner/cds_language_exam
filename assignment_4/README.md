# Assignment 4 - Sentiment analysis

## Prerequisites

Bash and python 3 is needed to be able to run the shell-script and the python-scripts within this assignment. The python script has been tested on python 3.9.4, but this may not be required and older versions will most likely suffice.

## Setup

- Change into the assignment_4 directory if this has not already been done.
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
To run the LDA-model run the following command:

```
python star_trek_lda.py
```

For using default arguments, or

```
python star_trek_lda.py [-d --data_path] [-t --topic_num]
```

Where

- data_path is the path to all_series_lines.json. Default is all_series_lines.json within the data-folder.
- topic_num is the number of topics to be identified. Default is 12.

**NOTE:** This repository already comes with a populated output-folder.

## Results

First of all, it has to be noted that there are some errors in the dataset due to the fact that in some cases newline has been substituted with nothing instead of a whitespace. This causes some words to concatenate. It is, however, not at big problem for this demonstration.

Looking at the output, we can see from the graph that there is a clear shift in the topics presented in the episodes. The biggest change happens around episode 300. Knowing very little about star trek (shame on me) it seems to indicate some sort of introduction of a new character or perhaps species within the universe. At least something that brings along a whole new set of topics within the episodes. It is rather difficult to backtract each episode from the graph but it does give an overall idea of how the topics change within the universe as the episodes progresses. Further work would include mapping each episode to the topics and get a more granular picture of the topics used but this is outside the scope of this assignment for now.

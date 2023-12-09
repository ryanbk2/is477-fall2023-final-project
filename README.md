# IS477 Fall 2023 Final Project

## Overview
This repository is intended to reproduce a subset of results based on a section of the paper titled above.
To be more specific, this repository will reproduce numeric results from the paper using data analysis techniques,
primarily simple logistic regression. 
The repository also intends to be used for understanding the importance of transparency and reproducibility of a prior analysis
and to ensure the integrity and trustworthiness of the results of said prior analysis.
The repository also serves as a tool to help others understand the role of privacy and intellectual laws in data curation, such as
copyright and licensing of data and software along with automation of data science worlflows and pipelines; preservation of such data is key learning points for parts of this repository.
This repository intends to use tools such as Git, Github, and Python for completing various assignments; every assignment will
be created via the creation of a new GitHub repository release and submitting them for grading.

## Analysis
The visualizations suggest that in the dataset, there are as many four-door sedans as there are two-door coupes. However, there are slightly more cars that can hold up to four people than two people, suggesting that some coupes are able to hold up to four people at a time.

## Workflow


## Reproducing
In order to prepare for the usage of the script prepare_data.py, it is recommended that Docker is set up, if possible (Commandplaette -->  Docker Images: Build Image). Ensure a virtual environment is set up, after going to the Command Palette --> Python: Create Environment --> Venv --> Recreate.
Do not worry if you do not have the "data" directory, as the once the script is ran after clicking "Run Python File", the script should create the directory along with all of the necessary files, and will automatically verify the integrity of said files created.

You will also need to have the environment and Docker (if possible) set up in order to use the other scripts in the "scripts" folder in the directory. If you do not have the Python libraries scikit-learn, numpy or pandas, install them using pip. Running the scripts will create files stored in the results directory. The script should create the directory if it doesn't exist already.
If you choose to run the scripts using Docker, then you can run each script like this: docker run --rm -v ${PWD}:/is477
username/is477-fall2023-final-project:scripts python < script > (without spaces after '<' and '>')

Otherwise, you can manually run each individual script. If they ran properly, then they should generate files in the results directory. If for whatever reason, the Python compiler outputs any "syntax" errors, try reopening this directory.

## License
This data will use the MIT License, which will permit re-distribution of a work given the creator is properly credited, and also makes this work open source; given it is necessary for others to be provided the opportunity to create something unique out of the data or improve on this current version of the work, the aformentioned license was specifically selected for that goal.

## Citations
Bohanec, Marko. (1997). Car Evaluation. UCI Machine Learning Repository. https://doi.org/10.24432/C5JP48.

Bohanec, Marko and Vladislav Rajkovič. “KNOWLEDGE ACQUISITION AND EXPLANATION FOR MULTI-ATTRIBUTE DECISION MAKING ∗.” (1988).
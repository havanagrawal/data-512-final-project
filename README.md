# Data 512: Analyzing 19th Century Literature w.r.t. the Bechdel Test

Assignment repository for DATA 512: Final Project

## Introduction

This repository contains a set of notebooks and reports regarding the analysis of popular 19th century literature in the context of the [Bechdel test](https://en.wikipedia.org/wiki/Bechdel_test). The results of the analyses are summarized [below](). It also showcases the gaps present in state-of-the-art NLP that hinder us from performing such analyses at scale.

## Reproducibility

While each independent notebook is completely reproducible, due to the qualitative nature of the analyses, it is not possible to replicate the research as is for any arbitrary novel. Instead, it is advisable to use the template notebook in the repository and modify it iteratively and interactively, to suit the novel at hand.


## Data

Since Project Gutenberg does not restrict its data under a license, a few novels are distributed along with this repository, along with their processed versions (required for analysis). 

## How To Run

### Prerequisites

1. Python 3.5 or later
2. pip3
3. A machine with at least 8G of RAM
4. Java 7 or above

### Steps

1. Clone this repository:
```
git clone https://github.com/havanagrawal/data-512-final-project.git
```
2. Install the required libraries:
```
pip3 install pandas numpy nltk matplotlib unidecode 
```

3. Download and unzip the latest version of Stanford NER from [here]()

## Data Schema

The original data is taken as free-form text files from Project Gutenberg. Since the files are fixed column width, we use a short script to convert them into a readable format.

After running the StanfordNER script, we get a JSON file that contains various analyzed linguistic forms. We use the relevant portions of this JSON file for our analysis.

## License

1. This repository and its contents are distributed under an open MIT License
2. Project Gutenberg opens its data to any form of commercial and non-commercial use, which is summarized [here](https://www.gutenberg.org/wiki/Gutenberg:Permission_How-To)
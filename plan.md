# Final Project Plan

## Table of Contents

1. [Why](#why)
    1. [Research Questions](#research-questions)
2. [The Plan](#the-plan)
    1. [Collection](#collection)
    2. [Processing](#processing)
    3. [Analysis](#analysis)
    4. [Deliverables](#deliverables)
3. [Unknowns/Limitations](#unknownslimitations)
4. [Motivation](#motivation)
5. [References](#references)

> “What an astonishing thing a book is. It's a flat object made from a tree with flexible parts on which are imprinted lots of funny dark squiggles. But one glance at it and you're inside the mind of another person, maybe somebody dead for thousands of years. Across the millennia, an author is speaking clearly and silently inside your head, directly to you. Writing is perhaps the greatest of human inventions, binding together people who never knew each other, citizens of distant epochs. Books break the shackles of time. A book is proof that humans are capable of working magic."  
 -- [*Carl Sagan, Cosmos, Part 11: The Persistence of Memory (1980)*](https://www.goodreads.com/quotes/460806-what-an-astonishing-thing-a-book-is-it-s-a-flat)

### Why

I have been an avid and voracious reader ever since the age of 12. I find books to be a fantastic source of knowledge, information and personal growth. Whether it is fictional, biographical or historical, a good novel captivates you, pulls you from the physical realm into itself. As the above quote so beautifully captures, a book allows you to listen to an author speak to you, directly, across time and space. The following research is simply an attempt on my part to listen just a little bit harder.

#### Research Questions

More concretely, I wish to explore the following questions, recognizing that not all of them may be answerable:

1. Do the worlds that authors construct reflect their own homes and surroundings? For instance, if an author places their characters mostly around London, is this any indication of where the author might have grown up/visited?
2. What sort of gender ratios do novels tend to have? Does this change from author to author?
3. How do various emotional aspects of the novel change over time for a particular author? Does he tend to keep his characters mostly in a state of happiness, misery, confusion or anger?

For RQ1, I hypothesize that this must be true for most authors (> 50%).

I hope to understand these authors, their environments, mindsets and beliefs slightly better through this research.

[Back to Top](#table-of-contents)

### The Plan

#### Collection

The dataset that I will be using is from [Project Gutenberg](https://www.gutenberg.org), which offers over 57,000 free eBooks. They provide specific steps to retrieve specific data, which are described [here](https://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages).

Downloading the data is as straightforward as running a bash command:

```
# -w 2 waits for 2 seconds between requests
# -m turns on mirroring and enables infinite depth
# -H spans hosts when retrieving
wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt"
```

As per my understanding, the data are structured in nested directories, where the nesting is arbitrary. Each novel is a single text file, in free-form text. It is fairly simple to extract all the text novels into a single directory.

Some of the files are contained in zip/tar files. Once again, it is fairly simple to find all zip/tar files and unzip them into a top level directory, something along the lines of:

```
find -name "*zip" | xargs -n1 unzip
```

For information about the authors themselves, data collection will be slightly more free form, and may require me to visit multiple sites to aggregate the details that I need (Goodreads, SparkNotes, etc).

I will most likely handpick a few authors of personal interest to me, and analyze their works.

#### Processing

For each novel, the header content contains the name of the author and the title of the novel. A sample novel is [Agatha Christie's "A Mysterious Affair At Styles"](http://www.gutenberg.org/files/863/863-0.txt)

The header of this file looks like this:


>The Project Gutenberg EBook of The Mysterious Affair at Styles, by Agatha Christie
>
>This eBook is for the use of anyone anywhere in the United States and most
other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms of
the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you'll have
to check the laws of the country where you are located before using this ebook.
>
> Title: The Mysterious Affair at Styles
>
> Author: Agatha Christie
>
> Release Date: July 27, 2008 [EBook #863]
> Last Updated: February 22, 2018
>
> Language: English
>
> Character set encoding: UTF-8
>
> \*\*\* START OF THIS PROJECT GUTENBERG EBOOK THE MYSTERIOUS AFFAIR AT STYLES \*\*\*

Thus the author and title are easily extractable.

In order to extract the data necessary for analysis, I will be using tools made available by [Stanford NLP's Group](https://nlp.stanford.edu/software/), and the [NLTK Library](http://www.nltk.org/) in Python.

To be particular, I will be using the following techniques for each of my research questions:
1. **RQ1**: Named Entity Recognition (NER) for locations
2. **RQ2**: n-grams/bag-of-letters for analyzing sex of the characters
3. **RQ3**: Sentiment analysis using existing models/lexicons

#### Analysis

**RQ1**  

By using StanfordNER, I should be able to extract the locations, and scene descriptions that an author uses most frequently, and determine whether these locations reflect the home town of the author.

**RQ2**  

For sex ratios, I plan to use some ideas borrowed from [NLTK's Gender Identification](https://www.nltk.org/book/ch06.html) combined with other potential research. If these do not result in accurate results, then the sex of characters can be manually annotated.

Ideally, given that the nature of this analysis does not impact real-world individuals, making an error or two should not affect my analysis.

**RQ3**  

For sentiment analysis, there are several existing lexicons that are known to give good results, such as:
 * [AFINN lexicon](https://github.com/fnielsen/afinn)
 * [Bing Liu’s lexicon](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html)
 * [MPQA subjectivity lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/)
 * [SentiWordNet](http://sentiwordnet.isti.cnr.it/)
 * [VADER lexicon](https://github.com/cjhutto/vaderSentiment)
 * [TextBlob lexicon](https://github.com/sloria/TextBlob/blob/eb08c120d364e908646731d60b4e4c6c1712ff63/textblob/en/en-sentiment.xml)

Ideally I should be able to analyze emotion at a granular level (happy/sad/fear/etc), but even positive/negative sentiments can reveal a lot about the writing patterns of an author.

This question is, in part, inspired from [this article](http://www.bbc.com/culture/story/20180525-every-story-in-the-world-has-one-of-these-six-basic-plots)

#### Deliverables

For each research question, either a short writeup or a descriptive visualization that effectively answers the question will be presented.

[Back to Top](#table-of-contents)

### Data Licensing

Project Gutenberg makes the permissions on its data very explicit on [this page](https://www.gutenberg.org/wiki/Gutenberg:Permission_How-To)

> Most permission request are not needed. The vast majority of Project Gutenberg eBooks are in the public domain in the US. This means that nobody can grant, or withhold, permission to do with this item as you please.
>
> "As you please" includes any commercial use, republishing in any format, making derivative works or performances, etc.

While there are some copyrighted items in the data set, they are clearly marked as such:

> There are thousands of items in the Project Gutenberg collection which are still under copyright protection. Each copyrighted item is clearly indicated as copyrighted in the eBook's header.

I will explicitly be avoiding using these data at all.

### Unknowns/Limitations

For RQ2, I recognize that gender is separate from sex, and my intent is to purely infer and report the _sex_ ratio. Unfortunately, due to the nature of the data available to me, this is in fact a binary variable. Thus, if authors did have characters with other genders, this will be missed by my analysis.

A part of my research is contingent upon the quality of the algorithms used. While RQ1 and RQ2 will be fairly robust to algorithmic errors, RQ3 is not. Lack of granularity in identifying sentiment might result in less interesting results.

Finally, since the novels are primarily from the 18th and 19th centuries, it is possible that certain aspects reflect that era (for instance, having lower or higher sex ratios than today's norms). Care must be taken before drawing injudicious conclusions.

[Back to Top](#table-of-contents)

### Motivation

My most primary drive to pursue this project is my own proclivity for reading. The potential ability to understand a person through their writing fascinates me to no end.

In terms of the hypotheses that I'm trying to prove or disprove, there are several human-centered considerations. For one, adjusting for algorithmic bias, or even acknowledging it will be a significant portion of the analysis. For instance, it would be senseless to analyze novels written in French, especially since the tools and libraries I am using have been trained on English corpora.

As part of RQ2, it will be interesting to gauge various algorithms for social bias, and their maturity in terms of recognizing that gender is not in fact binary.

[Back to Top](#table-of-contents)

### References

A list of reference papers/articles that I might use, or have in some way inspired this project:

1. [Every Story In The World Has One Of These 6 Basic Plots](http://www.bbc.com/culture/story/20180525-every-story-in-the-world-has-one-of-these-six-basic-plots)
2. [Recognizing Emotion Presence in Natural Language Sentences](https://pdfs.semanticscholar.org/0607/e7b5967c909250b355e0cf8d945dc8592e1b.pdf)
3. [Emotion recognition for sentences with unknown expressions based on semantic similarity by using Bag of Concepts](https://ieeexplore.ieee.org/document/7382148)
4. [Personae - A Corpus for Author and Personality Prediction Using Text](http://www.lrec-conf.org/proceedings/lrec2008/pdf/759_paper.pdf)

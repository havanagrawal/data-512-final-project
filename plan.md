# Final Project Plan

## Table of Contents

1. [Why](#why)
2. [The Plan](#the-plan)
  1. [Collection](#collection)
  2. [Processing](#processing)
  3. [Analysis](#analysis)
  4. [Deliverables](#deliverables)
3. [Unknowns/Limitations](#unknownslimitations)
4. [Motivation](#motivation)

> “What an astonishing thing a book is. It's a flat object made from a tree with flexible parts on which are imprinted lots of funny dark squiggles. But one glance at it and you're inside the mind of another person, maybe somebody dead for thousands of years. Across the millennia, an author is speaking clearly and silently inside your head, directly to you. Writing is perhaps the greatest of human inventions, binding together people who never knew each other, citizens of distant epochs. Books break the shackles of time. A book is proof that humans are capable of working magic."  
 -- [*Carl Sagan, Cosmos, Part 11: The Persistence of Memory (1980)*](https://www.goodreads.com/quotes/460806-what-an-astonishing-thing-a-book-is-it-s-a-flat)

### Why

I have been an avid and voracious reader ever since the age of 12. I find books to be a fantastic source of knowledge, information and personal growth. Whether it is fictional, biographical or historical, a good novel captivates you, pulls you from the physical realm into itself. As the above quote so beautifully captures, a book allows you to listen to an author speak to you, directly, across time and space. The following research is simply an attempt on my part to listen just a little bit harder.

More concretely, I wish to explore the following hypotheses, recognizing that not all of them may be answerable:

1. Do the worlds that authors construct reflect their own homes and surroundings? For instance, if an author places their characters mostly around London, is this any indication of where the author might have grown up/visited?
2. What sort of gender ratios do novels tend to have? Does this change from author to author?
3. How do various emotional aspects of the novel change over time for a particular author? Does he tend to keep his characters mostly in a state of happiness, misery, confusion or anger?

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

As per my understanding, the data are structured in nested directories, where the nesting is arbitrary. It is fairly simple to extract all the text novels into a single directory.

Some of the files are contained in zip/tar files. Once again, it is fairly simple to find all zip/tar files and unzip them into a top level directory, something along the lines of:

```
find -name "*zip" | xargs -n1 unzip
```

For information about the authors themselves, data collection will be slightly more free form, and may require me to visit multiple sites to aggregate the details that I need (Goodreads, SparkNotes, etc).

I will most likely handpick a few authors of personal interest to me, and analyze their works.

#### Processing

For each novel, the header content contains the name of the author and the title of the novel. A sample novel is [Agatha Christie's "A Mysterious Affair At Styles"](http://www.gutenberg.org/files/863/863-0.txt)

In order to extract the data necessary for analysis, I will be using tools made available by [Stanford NLP's Group](https://nlp.stanford.edu/software/), and the [NLTK Library](http://www.nltk.org/) in Python.

#### Analysis

**RQ1**
By using StanfordNER, I should be able to extract the locations, and scene descriptions that an author uses most frequently, and determine whether these locations reflect the home town of the author.

**RQ2**
For gender ratios, I plan to use some ideas borrowed from [NLTK's Gender Identification](https://www.nltk.org/book/ch06.html) combined with other potential research. If these do not result in accurate results, then the genders of characters can be manually annotated.

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

I can hopefully draw from prior work like [this](https://pdfs.semanticscholar.org/0607/e7b5967c909250b355e0cf8d945dc8592e1b.pdf) or [this](https://ieeexplore.ieee.org/document/7382148)

This question is, in part, inspired from [this article](http://www.bbc.com/culture/story/20180525-every-story-in-the-world-has-one-of-these-six-basic-plots)

#### Deliverables

For each research question, either a short writeup or a descriptive visualization that effectively answers the question will be presented.

[Back to Top](#table-of-contents)

### Unknowns/Limitations

As mentioned above, a part of my research is contingent upon the quality of the algorithms used. While RQ1 and RQ2 will be fairly robust to algorithmic errors, RQ3 is not. Lack of granularity in sentiment might result in less interesting results.

[Back to Top](#table-of-contents)

### Motivation

My most primary drive to pursue this project is my own proclivity for reading. The potential ability to understand a person through their writing fascinates me to no end.

In terms of the hypotheses that I'm trying to prove or disprove, there are several human-centered considerations. For one, adjusting for algorithmic bias, or even acknowledging it will be a significant portion of the analysis. For instance, it would be senseless to analyze novels written in French, especially since the tools and libraries I am using have been trained on English corpora.

Similarly, since the novels are primarily from the 18th and 19th centuries, it is possible that certain aspects reflect that era (for instance, having lower or higher gender ratios than today's norms). Care must be taken before drawing injudicious conclusions.

[Back to Top](#table-of-contents)

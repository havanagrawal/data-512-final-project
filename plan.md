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

> It's in literature that true life can be found. It's under the mask of fiction that you can tell the truth.
-- [*Gao Xignjian](https://www.goodreads.com/quotes/7202226-it-s-in-literature-that-true-life-can-be-found-it-s)

### Why

I have been an avid and voracious reader ever since the age of 12. I find books to be a fantastic source of knowledge, information and personal growth. Whether it is fictional, biographical or historical, a good novel captivates you, pulls you from the physical realm into itself. As the above quote so beautifully captures, a book allows you to listen to an author speak to you, directly, across time and space.

Further still, I believe that works of fiction often captures the true nature of society. They either reflect on the world, as it is, or what it might become. Either consciously or subconsciously, the worlds created by a writer capture their perspective. It is this idea that I wish to explore in this project.

#### Research Questions

I intend to analyze a subset of popular works in the context of the [Bechdel Test](https://en.wikipedia.org/wiki/Bechdel_test).

> The Bechdel test is a measure of the representation of women in fiction. It asks whether a work features at least two women who talk to each other about something other than a man. The requirement that the two women must be named is sometimes added.

1. What fraction of these novels pass the Bechdel test, and to what extent?
2. Is it reasonable to attempt to automate such tests, that rely heavily on social cues that may not be discernible through algorithmic means? If not, then what are the limitations that prevent us from doing so? More concretely:
    1. I wish to build an interactive pipeline that can consume a piece of text, and allow one to analyze the snippets that directly concern themselves with the test,
    2. Yield a result w.r.t the algorithm's belief about the extent to which the text passes the Bechdel test, analyze how close (or far) this is from reality, and identify the gaps, either in the tools, the technologies or my own methodology.

I hope to understand these authors, their environments, mindsets and beliefs slightly better through this research. I also hope that this will allow me to critically analyze existing tools and techniques, as well as my own human-centered algorithmic skills.

[Back to Top](#table-of-contents)

### The Plan

I intend to take a ["thick data"](https://medium.com/ethnography-matters/why-big-data-needs-thick-data-b4b3e75e3d7) approach to this research, i.e. instead of collecting data at scale, and performing superficial analysis, I will instead select a few novels and work with them. This will allow me to dive into the nitty-gritty details of where and why certain pieces of my pipeline fail, and whether I can manually annotate data to correct them.

An implication of the above approach is that I cannot make generalizable claims about authors. However, what I can do is post a thorough report of a small subset of novels and authors, and explore the feasibility of doing this at scale.

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
1. [**Named Entity Recognition (NER)**](https://nlp.stanford.edu/software/CRF-NER.shtml) from StanfordNLP for identifying names of characters
2. **n-grams/bag-of-letters/coreferent analysis** for analyzing the gender of the characters
3. [**Quote Annotator**](https://stanfordnlp.github.io/CoreNLP/quote.html) from Stanford NLP to identify spoken dialogue.

#### Analysis

By using StanfordNER, I should be able to extract the names of various characters. Through some pre-processing, I can disambiguate references to the same person (Mr. Holmes, Sherlock Holmes and S. Holmes).

For identifying gender, I plan to take a many-fold approach that _should_ yield the lowest error rate:
  1. Using some ideas borrowed from [NLTK's Gender Identification](https://www.nltk.org/book/ch06.html).
  2. Leverage occurrences of [coreferents](https://en.wikipedia.org/wiki/Coreference) (he/she/his/her) to identify gender.
  3. Identify courtesy titles (Mr., Mrs., Miss) that very explicitly reveal the gender of the entity.

 * In cases where the gender is ambiguous (not discernible through context, even by a human), I will note it as such in my report.
 * In cases where the gender is neither man nor woman, or the entity is simply genderless (The Cheshire Cat from Alice in Wonderland for instance), I will note it as such in my report.

#### Deliverables

1. A report of the extent to which selected works pass the Bechdel test, both from manual as well as computational analysis.
2. One or more visualizations of the conversations between characters, clearly identifying snippets that relate to the test.
3. A reproducible, interactive approach to analyzing literary works in the context of the Bechdel test.

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

I recognize that gender is separate from sex. The Bechdel test is very explicit in its wording, using the terms "man" and "woman", which implies that it relies on the gender of the entity, and not sex. It does not specify the behaviour of the test w.r.t. non-binary genders.

Unfortunately, the tools and techniques at my disposal are limited in identifying even binary gender, let alone non-binary. Consequently, I recognize a potential challenge is that I may have to be skeptical about every computational/algorithmic result, and validate every item of interest manually.

As far as I understand, there was little to no representation of non-binary genders in 18th and 19th century classical works. As a result, I _expect_ that identifying the _biological sex_ of an entity should _typically_ be a strong indicator of their gender. However, this is only an assumption, and all ambiguities or errors in identifying the gender will be explicitly reported.

Finally, since the novels are primarily from the 18th and 19th centuries, it is possible that certain aspects reflect that era. Passing or failing the Bechdel test is an aspect of a single work, and (IMO) should not be generalized to either the author or the time-period. Care must be taken before drawing injudicious conclusions.

[Back to Top](#table-of-contents)

### Motivation

My most primary drive to pursue this project is my own proclivity for reading. The potential ability to understand a person through their writing fascinates me to no end.

As an individual with a rather strong computer-science oriented background, I have far too much faith in algorithms and pure computational research. My understanding of human-centered aspects has grown rather steeply with this course, and I hope that with this project, I can understand the nuances of human-centered algorithmic design, identify challenges in such design, and address them either through practice or future scope.

[Back to Top](#table-of-contents)

### References

A list of reference papers/articles that I might use, or have in some way inspired this project:
1. [Automating the Bechdel Test](http://www.aclweb.org/anthology/N15-1084)
2. [A Social Network Analysis of Alice in Wonderland](https://www.semanticscholar.org/paper/Social-Network-Analysis-of-Alice-in-Wonderland-Agarwal-Corvalan/76842360337ca07a63a27a75319f63236e8c9cfe)

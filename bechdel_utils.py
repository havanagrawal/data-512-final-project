from collections import Counter, defaultdict
from nltk import wordpunct_tokenize

def prettify(name):
    """Properly capitalize a name
    
        >>> prettify("edgar ATHELING")
        "Edgar Atheling"
    """
    clean = []
    for word in name.split():
        capitalized = word[0].upper() + word[1:].lower()
        clean.append(capitalized)
    return " ".join(clean)


def resolve(speakers, coreferents, who):
    """Resolve coreferents."""
    for i, s in enumerate(speakers):
        if s in coreferents:
            speakers[i] = who
                
                
MALE_INDICATORS = {"he", "him", "his", "man", "boy"}
FEMALE_INDICATORS = {"she", "her", "hers", "woman", "girl"}


def about_man(s, gender_dict):
    """Return a dictionary of gender to relative frequency of mention/reference"""
    words = [w.lower() for w in wordpunct_tokenize(s)]
    word_freq = Counter(words)
    
    total_word_count = len(words)
    total_ref_count = defaultdict(int)
    
    for m_indicator in MALE_INDICATORS:
        total_ref_count["MALE"] += word_freq[m_indicator]
        
    for f_indicator in FEMALE_INDICATORS:
        total_ref_count["FEMALE"] += word_freq[f_indicator]
        
    for name, gender in gender_dict.items():
        total_ref_count[gender] += s.count(name)
        
    if '' in total_ref_count:
        del total_ref_count['']
    
    return {k:v/total_word_count for k,v in total_ref_count.items()}


def compress(speakers, talks):
    """Reduce consecutive dialogue by the same person into single records"""
    i = 0

    current_text = ""
    current_speaker = ""

    compressed_speakers = []
    compressed_talks = []

    for speaker, text in zip(speakers, talks):
        if speaker == current_speaker:
            current_text = current_text + " " + text
        else:
            compressed_speakers.append(current_speaker)
            compressed_talks.append(current_text.replace('"', ''))

            current_speaker = speaker
            current_text = text
            
    compressed_speakers.append(current_speaker)
    compressed_talks.append(current_text.replace('"', ''))
    
    return compressed_speakers, compressed_talks
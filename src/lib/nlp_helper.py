import nltk
# from nltk.corpus import words

# lexical parameters
def type_token_ratio(phrase: str) -> float:
    tokenized = nltk.tokenize.word_tokenize(phrase)
    if len(tokenized) > 0:
        return len(set(tokenized))/len(tokenized)
    else:
        raise Exception("No tokens detected, input phrase is probably empy")
    
def lexical_density_halliday(phrase: str) -> float:
    LEXICAL_TAGS = {
        "NN", "NNS", "NNP", "NNPS",
        "VB", "VBD", "VBG", "VBN", "VBP", "VBZ",
        "JJ", "JJR", "JJS",
        "RB", "RBR", "RBS"
    }
    tokenized = nltk.tokenize.word_tokenize(phrase)
    tagged = nltk.tag.pos_tag(tokenized)

    if len(tokenized) > 0:
        return len([token for token, tag in tagged if tag in LEXICAL_TAGS])/len(tokenized)
    else:
        raise Exception("No tokens detected, input phrase is probably empy")
    
"""
Writer: Ranel Ben Simman Tov
"""


def count_words(text):
    """
    :param text: a string
    :return: a dictionary with the words and their length
    :rtype: dict
    """
    # remove all non-alphabetic characters with generator expression
    # alternatively, we could use re.sub
    text = ''.join(c.lower() for c in text if c.isalpha() or c.isspace())
    # create a dictionary with the words and their length
    words_len = {word: len(word) for word in text.split()}
    return words_len


if __name__ == "__main__":
    txt = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(count_words(txt))

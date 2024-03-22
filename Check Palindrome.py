from string import ascii_lowercase


def main():
    text = rem_nonletters("Go hang a salami, I'm a lasagna hog.")
    print(is_palindrome(text))


def rem_nonltrs(t):
    """Removes all the non-letter characters from a given strings.
    Args:
        t (str): String to remove non-letter characters from.
    Returns:
        str : String without non-letter characters.
    """
    t = t.lower()
    tf = ""
    for letter in t:
        if letter in ascii_lowercase:
            tf += letter
        else:
            continue
    return tf


def rem_nonletters(t):
    """Another way of removing the non-letters from a given string.
    Args:
        t (str): String to remove non-letter characters from.
    """
    tf = list(filter(lambda a: a in ascii_lowercase, t.lower()))
    return "".join(tf)


def is_palindrome(text):
    """Checks whether a given string (without non-letter characters) is a Palindrome.
    Args:
        text (str): String to check.
    Returns:
        bool : True or False
    """
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


if __name__ == "__main__":
    main()

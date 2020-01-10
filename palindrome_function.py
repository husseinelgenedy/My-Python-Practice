def reverse(s):
    """ (str) -> str

    Return reverse of s.

    >>> reverse('hello')
    olleh
    >>> reverse('cat')
    tac
    >>> reverse('oh no!')
    !on oh
    """
    rev = ''
    for chr in s:
        rev = chr + rev
    return rev

def is_palindrome_1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_1('noon')
    True
    >>> is_palindrome_1('racecar')
    True
    >>> is_palindrome_1('dented')
    False
    """
    if s == reverse(s):
        x= True
    else:
        x= False
    return x

def is_palindrome_2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_2('noon')
    True
    >>> is_palindrome_2('racecar')
    True
    >>> is_palindrome_2('dented')
    False
    """
    if s[0:(len(s)-(len(s)//2))] == reverse(s[(len(s)//2):len(s)]):
        x= True
    else:
        x= False
    return x

def is_palindrome_3(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_3('noon')
    True
    >>> is_palindrome_3('racecar')
    True
    >>> is_palindrome_3('dented')
    False
    """
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return j <= i

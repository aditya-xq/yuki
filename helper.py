import re


def cleanString(dirtyString):
    cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleanString = re.sub(cleaner, '', dirtyString)

    return cleanString
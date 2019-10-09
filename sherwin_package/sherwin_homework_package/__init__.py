from collections import defaultdict
name = "sherwin_homework_package"

#2: anagram

def anagram(first, second):
    if len(first) != len(second):
        return False

    firstDict = defaultdict(lambda: 0)
    secondDict = defaultdict(lambda: 0)

    for element in first:
        firstDict[element] += 1

    for element in second:
        secondDict[element] += 1

    return firstDict == secondDict

#########################################


def anagram_2(first, second):
    if len(first) != len(second):
        return False

    return sorted(first) == sorted(second)

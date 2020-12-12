import re


def is_stressful(subj):
    """
        recognize stressful subject
    """
    str1 = re.search("[hH]+[!?.-]*e+[!?.-]*l+[!?.-]*p+[!?.-]*", subj, re.I)
    str2 = re.search("a+[!?.-]*s+[!?.-]*a+[!?.-]*p+[!?.-]*", subj, re.I)
    str3 = re.search("u+[!?.-]*r+[!?.-]*g+[!?.-]*e+[!?.-]*n+[!?.-]*t+[!?.-]*", subj, re.I)
    str4 = re.search("[?]+", subj, re.I)

    if str1 or str2 or str3 or str4:
        return True

    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed H-ELP") == True, "Second"
    assert is_stressful("asap help") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True, "Second"
    print('Done! Go Check it!')

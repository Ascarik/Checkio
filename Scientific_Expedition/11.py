import unicodedata


def checkio(in_string):
    "remove accents"
    return unicodedata.normalize('NFD', in_string) \
               .encode('ascii', 'ignore') \
               .decode("utf-8") or in_string


if __name__ == '__main__':
    print(checkio(u"loài trăn lớn"))
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')

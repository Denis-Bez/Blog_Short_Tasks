
# Search middle of string
def search_middle():
    word = 'woerd'
    print((s := word)[-(len(s) + 1) // 2])


if __name__ == '__main__':
    search_middle()

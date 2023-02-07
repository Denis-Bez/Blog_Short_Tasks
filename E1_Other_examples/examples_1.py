
# Search middle of string
def search_middle():
    word = 'woerd'
    print((s := word)[-(len(s) + 1) // 2])


# How abort current cicle iteration
def abort_cicle_iteration():
    array = [1, 2, 3, 4, 5]
    for i in array:
        if i == 3:
            continue
        print(i)

def test_commit_not_push():
    pass


if __name__ == '__main__':
    abort_cicle_iteration()

# coding=utf-8
linkses = {"title":"www", "kkk":"www"}
views = []


def create_view_for_links():
    view=""
    for key,value in linkses.items():
        view += "{}\n{}\n".format(key, value)
    return view


def main():
    print(create_view_for_links())


if __name__ == '__main__':
    main()

def file_write(item, tasks):
    with open('item.txt', "w") as fp:
        for x in tasks:
            fp.write("%s\n" % x)


def file_read(item):
    tasks = []
    with open('item.txt', "r") as fp:
        t1 = fp.readlines()
        for x in t1:
            tasks.append(x.rstrip('\n'))
            tasks.sort()
    return tasks
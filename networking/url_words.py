import urllib.request, urllib.parse, urllib.error

def sort_dic(dic):
    '''Assumes dic is dictionary (key:value).
    Returns dic sorted by value'''
    ord_dic = {}
    for value in sorted(dic.values(), reverse = True):
        for key in dic:
            if dic[key] == value:
                ord_dic[key] = value
    return ord_dic

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

ord_counts = sort_dic(counts)
print(ord_counts)
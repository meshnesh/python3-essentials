# import re
#
# def main():
#     fh = open("raven.txt")
#     for line in fh:
#         print (re.sub('(Len|Neverm)ore','###',line))
#
# if __name__ == "__main__": main()


import re

def main():
    fh = open('raven.txt')
    for line in fh:
    	match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line)

if __name__ == "__main__": main()
# import re

# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         if re.search('(Len|Neverm)ore', line):
#             print(line)

# if __name__ == "__main__": main()



import re

def main():
    fh = open('raven.txt')
    for line in fh:
    	match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

if __name__ == "__main__": main()
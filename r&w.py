from aetypes import end


def main():
    buffersize = 50
    # infile = open('lines.txt', 'r')
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.')
    buffer = infile.read(buffersize)
    print()
    print("Done.")


if __name__ == "__main__": main()

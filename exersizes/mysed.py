def mysed(patterns, repls, infile, outfile):
    with open(infile) as reader:
        with open(outfile, 'w') as writer:
            for line in reader.readlines():
                newline = line.replace(patterns, repls)
                writer.write(newline)


orig = 'greengold'
dest = 'greengreen'

mysed('gold', 'green', 'greengold', 'greengreen')

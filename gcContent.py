from __future__ import division

### file being examined

filename = "test.fa"

### variables initialized
longest = 0
shortest = None
numA = 0
numT = 0
numC = 0
numG = 0
numLen = 0
numSeq = 0
sequence = None


### read in file
try:
    f = file(filename)      #cast as a file object if not valid throw exception
except IOError:
    print "The file, %s, does not exist" % filename

for line in f:
    if line == "":
        continue
    if line.startswith(">",):
        numSeq += 1
        if sequence:
            seqLen = len(sequence)
            if seqLen > longest:
                longest = seqLen
            if not shortest:
                shortest = seqLen
            else:
                if seqLen < shortest:
                    shortest = seqLen
            numLen += seqLen
            position = 0
            while position < len(sequence):
                nuc = sequence[position]
                if nuc == "A":
                    numA += 1
                elif nuc == "T":
                    numT += 1
                elif nuc == "G":
                    numG += 1
                else:
                    numC += 1
                position += 1
        sequence = None
        continue
    else:
        if sequence:
            sequence += line.rstrip()
        else:
            sequence = line.rstrip()


#must run one more time
if sequence:
    seqLen = len(sequence)
    if seqLen > longest:
        longest = seqLen
    if not shortest:
        shortest = seqLen
    else:
        if seqLen < shortest:
            shortest = seqLen
    numLen += seqLen
    position = 0
    while position < len(sequence):
        nuc = sequence[position]
        if nuc == "A":
            numA += 1
        elif nuc == "T":
            numT += 1
        elif nuc == "G":
            numG += 1
        else:
            numC += 1
        position += 1
### do calculations
avg = numLen / numSeq
gc = ((numG + numC) / (numLen)) * 100


print "Total number of sequences in the file was: ", numSeq
print "Shortest sequence length was: ", shortest
print "Longest sequence length was: ", longest
print "Average sequence length was: ", avg
print "Percent gc content of the file was: ", gc
print "Total number of nucleotides was: ", numLen

import subprocess
import sys
import os
import re

### program as arguments accepts the directory with flagstat files and a filename to be written to
SEARCH = 'D\w+L006\w+'

try:
    if len(sys.argv)<2:
        print "USAGE: python sys.argv[0] input-dir output-dir index \n",
        print "Attempting default value test parameters...."
        Source = '/Users/Owner/PycharmProjects/Homework/'
        Results_to = '/Users/Owner/PycharmProjects/Homework/flag_outfile'
    else:
        Source = sys.argv[1]
        Results_to = sys.argv[2]
except IOError:
    print "Error in input"


def fileProcess(Source):
    print "Parse Begin..."
    parse = []
    for filename in os.listdir(Source):
        if filename[-3:len(filename)]=="txt":
            look = re.compile(SEARCH)
            target = look.match(filename)
            if target:
                print "Process file:", filename
                page = fileParse(filename)
                parse.append(page)
    output = outfileProcess(parse)
    outfile(output)
    return "Parse Complete"

def fileParse(file):
    f =open(file)
    list = []
    temp = file.split("_")
    seqID = str(temp[0] + "_" + temp[1] + "_" + temp[2])
    software = str(temp[len(temp)-2])
    passed = ""
    dups = ""
    mapped = ""
    paired = ""
    read1 = ""
    read2 = ""
    prop = ""
    selfMate = ""
    single = ""
    matechr = ""
    matechrQ = ""
    mapPercent = ""
    propPer = ""
    singlePer = ""
    counter = 0
    for line in f:
        p = re.compile('\w+')
        temp = p.findall(line)
        if counter == 0:
            passed = str(temp[0])
        if counter == 1:
            dups = str(temp[0])
        if counter == 2:
            mapped = str(temp[0])
            mapPercent = str(temp[3])+"."+str(temp[4])
        if counter == 3:
            paired = str(temp[0])
        if counter == 4:
            read1 = str(temp[0])
        if counter == 5:
            read2 = str(temp[0])
        if counter == 6:
            prop = str(temp[0])
            propPer = str(temp[5])+"."+str(temp[5])
        if counter == 7:
            selfMate = temp[0]
        if counter == 8:
            single = str(temp[0])
            singlePer = str(temp[3])+"."+str(temp[4])
        if counter == 9:
            matechr = str(temp[0])
        if counter == 10:
            matechrQ = str(temp[0])
        counter += 1
    list = [seqID, software, passed, dups, mapped, paired, read1, read2, prop, selfMate, single, matechr, matechrQ, mapPercent, propPer, singlePer]
    return list

def outfileProcess(list):
    toString = ""
    for num in xrange(len(list)):
        seqID = list[num][0]
        software = list[num][1]
        passed = list[num][2]
        dups = list[num][3]
        mapped = list[num][4]
        mapPercent = list[num][13]
        paired = list[num][5]
        read1 = list[num][6]
        read2 = list[num][7]
        prop = list[num][8]
        propPer = list[num][14]
        selfMate = list[num][9]
        single = list[num][10]
        singlePer = list[num][15]
        matechr = list[num][11]
        matechrQ = list[num][12]



        toString += str(seqID +":"+ software +"\t" + passed +"\t"+dups+"\t"+mapped+"\t"+mapPercent+"\t"+paired+"\t"+read1+"\t"+read2+"\t"+prop+"\t"+propPer+"\t"+selfMate + "\t"+single+"\t"+singlePer+"\t"+matechr+"\t"+matechrQ+"\n")
    return toString

def outfile(string):
    header = "File: \tPassed Reads: \tDuplicates: \tMapped: \tMapped%: \tPaired in Seq: \tRead1: \tRead2: \tProperly Paired: \tProperly Paired%: \tWith self and mate: \tSingletons: \tSingletons%: \tMate Diff Chr: \tMate Diff Chr Q >=5\n"
    toString = header + string
    outFile = open(Results_to,'w')
    outFile.write(toString)
    outFile.close()


fileProcess(Source)


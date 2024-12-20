from optparse import OptionParser
import sys, gzip
#option parser
parser = OptionParser(usage="""Run annotation.py \n Usage: %prog [options]""")
parser.add_option("-1","--read1",action = 'store',type = 'string',dest = 'READ1',help = "")
parser.add_option("-2","--read2",action = 'store',type = 'string',dest = 'READ2',help = "")
parser.add_option("-o","--out",action = 'store',type = 'string',dest = 'OUT',help = "")
(opt, args) = parser.parse_args()
if opt.READ1 == None or opt.READ2 == None or opt.OUT == None:
    print('Basic usage')
    print('')
    print('     python statistics_read.py -t 24 -i test.fastq(.gz)')
    print('')
    sys.exit()

fin_1 = gzip.open(opt.READ1, 'rt')
fin_2 = gzip.open(opt.READ2, 'rt')
fout = open(opt.OUT, 'w')

for readIDX, (read1, read2) in enumerate(zip(fin_1, fin_2)):
    if readIDX%4 == 0:
        read1ID = read1
        read2ID = read2
    if readIDX%4 == 1:
        read1Seq = read1
        read2Seq = read2
        fout.write(read1ID)
        fout.write(read1Seq)
        fout.write(read2ID)
        fout.write(read2Seq)

fout.close()
fin_1.close()
fin_2.close()
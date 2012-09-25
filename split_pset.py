from optparse import OptionParser
from pyPdf import PdfFileWriter, PdfFileReader
import sys

usage = """
Run this script in the directory that contains a pdf of your pset. 
You can run the command as follows to split your pset into multiple documents: 
    
    python split_pset.py -pset 1 -probs "1-2, 3"

This will result with 4 new files being creating in the format:
    
    pset1-1_answers.pdf
    pset1-2_answers.pdf

Where the the first file is pages 1-2 of the first pdf. The second file will contain only page 3. 

Your original pdf is expected to have a file name as follows (as generated by the startpset script):
    
    pset1_answers.pdf

This script should live with startpset.py since the file will be looked for at latex/pset1_answers.pdf
"""

parser = OptionParser(usage=usage)

parser.add_option("-p", "--problem-set", dest="pset",
              type="int", action="store", help="Specify the pset number to name the files with")
parser.add_option("-q", "--problems", dest="probs", type="string", action="store", help="Enter a comma separated value string of page numbers for the document to be split on.")

(options, args) = parser.parse_args()


def print_err_and_die(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)

def split_pset():
    if (not options.pset or not options.probs):
        print_err_and_die("You must enter both arguements! run with -h for help")

    try:
        filename = "latex/pset%s_answers.pdf"%options.pset
        inp = PdfFileReader(file(filename, "rb"))
    except IOError:
        print_err_and_die("Error! File, %s was not found." % filename)
    
    ##loop over user input and break up pdf
    questionNum = 1
    probs = options.probs.split(",")
    for prob in probs:
        print "Processing question", questionNum

        prob = prob.strip() #kill whitespace

        out = PdfFileWriter()
        pages = prob.split('-')

        for page in pages:
            out.addPage(inp.getPage(int(page)-1))

        outStream = file("latex/pset%s-%s_answer.pdf"%(options.pset, questionNum), "wb")
        out.write(outStream)
        outStream.close()
        questionNum +=1

    print "Done!"


if __name__ == "__main__":
    split_pset()

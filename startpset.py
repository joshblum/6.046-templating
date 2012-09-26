import jinja2
import sys
import os

TEMPLATE_TEMPLATE = 'problem_set_template.tex.jinja'

USAGE = """USAGE:
python startpset.py psetnumber [question count]

will create the following directory strucutre in the current working directory:

pset{{pset number}}
    \
     latex
        \
         pset{{pset number}}_answers.tex
         
if the folder pset{{pset number}} already exists, will abort.

question count is an optional paramter to make the templates for that many questions.
will default to 1
"""

def err(what):
    sys.stderr.write(what)

def print_usage_and_die():
    err(USAGE+"\n")
    sys.exit(1)

def parseargs(argslist):
    """
    Does the handling of args,
    returns a tuple of pset number and problem count.
    pset number is mandatory. problem count defaults to 1.
    """
    if len(argslist) < 1:
        print_usage_and_die()
    
    # ok, so we have at least on argument.
    first_arg = argslist[0]
    
    if first_arg == "help":
        print_usage_and_die()
    
    try:
        psetnumber = int(first_arg)
    except ValueError:
        err("First argument (pset number) must be an integer!\n")
        print_usage_and_die()
        
    if len(argslist) > 1:
        second_arg = argslist[1]
        try:
            problemcount = int(second_arg)
        except ValueError:
            err("Problem count must be an integer!\n")
            print_usage_and_die()  
    else:
        problemcount = 1
        
    return psetnumber, problemcount

def get_pset_template(psetnumber, problemcount):
    try:
        template_template_handle = open(TEMPLATE_TEMPLATE, 'r')
    except IOError:
        err("ERROR: Unable to open template template file: %s\n" % TEMPLATE_TEMPLATE)
        sys.exit(1)
    
    jinja_template = jinja2.Template(template_template_handle.read())
    return jinja_template.render(psetnumber=psetnumber, problems=range(1, problemcount+1))
    
def main():
    args = sys.argv[1:]
    psetnumber, problemcount = parseargs(args)
    
    pset_folder = "pset%d" % psetnumber
    
    if os.path.exists(pset_folder):
        err("%s already exists! aborting\n" % pset_folder)
        sys.exit(1)
        
    # if we are here the folder non-atomically does not exist
    # raceconditionracecondition heheheheh
    os.makedirs(pset_folder)
    
    latex_folder_path = "%s/latex" % pset_folder
    os.makedirs(latex_folder_path)
    
    answers_template_path = "%s/latex/pset%d_answers.tex" % (pset_folder, psetnumber)
    answers_template_handle = open(answers_template_path, 'w')
    answers_template_handle.write(get_pset_template(psetnumber, problemcount))
    answers_template_handle.close()
    
    print "done!"    
    

if __name__ == "__main__":
    main()
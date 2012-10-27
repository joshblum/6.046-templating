#6.046-templating

Create latex templates with your name and split final pset into separate files to upload.

## Usage

### startpset.py

    python startpset.py psetnumber [question count]

This command will create the following directory structure in the current working directory:

    pset{{pset number}}
        \
        latex
            \
            pset{{pset number}}_answers.tex
         
If the folder 

    pset{{pset number}}

already exists, the script will abort.

Question count is an optional paramter to make the templates for that many questions and will default to 1.

### split_pset.py
Run this script in the directory that contains a pdf of your pset. 
You can run the command as follows to split your pset into multiple documents: 

    python split_pset.py -p 1 -q "1-2, 3"

This will result with 2 new files being creating in the format:

    pset1-1_answers.pdf
    pset1-2_answers.pdf

The first file is pages 1-2 of the original pdf. The second file will contain only page 3. 

Your original pdf is expected to have a file name as follows (as generated by the `startpset.py` script):

    pset1_answers.pdf

This script should live with startpset.py since the file will be looked for at `pset%d/latex/pset1_answers.pdf`

#Requirements: 

    Jinja2==2.6

    pyPdf==1.13

Run the following to get started: 
  
    sudo pip install -r requirements.txt

#Authors
**Josh Blum**
+ joshblum@mit.edu

**Louis Sobel**
+ sobel@mit.edu
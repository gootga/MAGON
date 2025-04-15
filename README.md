# MAGON
This is a pyhton script that filters eigenstart by population.
Given a list in plain text format (one column) with names of populations
the script will search the input.ind and filter the input.geno accordingly.
It will output an new output.ind and output.geno with only the individuals 
that belong to the populations in the list provided.
In the default script example the extension for the population list is .dict 
but any .txt file is valid.
The script is a work in progress. Hopefully it will be made less rudimenaty in 
future updates.

INSTRUCTIONS for MAGON v1:
-Name your files and add the paths to the dedicated line in the script.
-Create a dictionary file (pop list, eg. "magon-dictionary.dat") with the names of the populations you want to keep.
-Run the script. 

EXAMPLE USAGE:
python3 magon_v1.py

TYPICAL SUCCESFUL OUTPUT:
Reading dictionary...
Reading individual metadata...
Individuals scanned: 25
Individuals selected: 10
Writing filtered .ind file...
Filtering .geno file...
Done!



# final_project_be434

I decided to make a script for my greenhouse at the CEAC, where I have to download files off of the campbell scientific server, and then modify them to be CSVs or excel files in order to use them. So I want to speed this process up by making it so I don't need to open excel in order to reformat the file to where I can use it in my R script. I would have written it in R like I am doing with my other data analysis stuff for my research, but I specifically wrote it in python for this class.

The idea behind this script is for it to take a positional input of a text file, as well as an optional output filename. Then the script will take the input file and using pandas import it into a dataframe. After this the data frame is saved as a csv with the outfile as its name, defaulting to "currentday_formatted.csv", where it will by default create the output file with the current day.Finally the script will also show a brief summary of the dataframe before letting the user know what the name of the output file is.

The script is called swgh_auto_formatter.py

It takes a an optional -o or --outfile argument where you can specify the filename as well as a positional filename input to tell it which file to format.



## Required Libraries:
-argparse

-pandas

-datetime 

## Added test.py

To use test suite run $ pytest test.py


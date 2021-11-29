#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-22
Purpose: Autoformat Files from campbell scientific for SWGH
"""

import argparse
import pandas as pd
from datetime import date


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='str',
                        default=str(date.today().strftime("%B_%d_%Y")) + '_'  + 'formatted.csv')

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Makes Soup"""
    args = get_args()
    df = imp_csv(args.file) # imports the file as a dataframe from pandas using the imp_csv() function.
    exp_csv(df,args.outfile) #Exports the dataframe as a csv with an optional file to specify it as.
    
# --------------------------------------------------


def imp_csv(fh):
    """imports the indicated csv file as a series of lists"""
    
    df = pd.read_csv(fh.name, delimiter = ",", skiprows=1)
    df = df.drop(labels=[0,1],axis=0)
    df.columns = ['datetime','record','battery','panel_t','avg_RH1','avg_AirT1','avg_PAR','total_PAR','irri_duration','avg_ATT_C','avg_CTT_C','avg_incoming_SW','avg_outgoing_SW','avg_incoming_LW','avg_outgoing_LW','avg_RH2','avg_AirT2','avg_CO2','avg_VPD']

    return df

def exp_csv(df,outfile):
    """exports the CSV to the name specified."""
    df.to_csv(outfile, index=False)
    pretty_print(df,outfile)

    

    
# --------------------------------------------------

def pretty_print(df,outfile):
    """prints a nice output to summarise CSV contents"""
    title = "Formatted and relabled CSV:"
    print("="*len(title) + "\n" + title + "\n" + "="*len(title))
    print(df)
    print("="*(len(outfile)+13))
    print('Exported to: ' + outfile)
    print("="*(len(outfile)+13))


if __name__ == '__main__':
    main()
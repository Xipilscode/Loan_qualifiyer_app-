# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

 
def save_csv(output_path, qualifying_loans): 
    """ Uses the csv library to save the qualifying data as a file.

    Args:
        csvpath (Path): The csv file path.
        qualifying_loans (Data): The data for qualifying loans
    """ 
    # Create a header
    header = ["The qualified bank loans"]

    # Use the csv library and `csv.writer` to write the header row
    # and  row of `qualifying_loans`
    # Open the output CSv file parth using 'with open'
    with open (str(output_path), 'w') as csvfile :
        # Create a csvwriter
        csvwriter = csv.writer(csvfile, delimiter=",")
        # Write the header to the CSV file
        csvwriter.writerow(header)
        # Write the values of each `qualifying_loans`
        # as a row in the CSV file
        for loan in qualifying_loans:
            csvwriter.writerow(loan)    

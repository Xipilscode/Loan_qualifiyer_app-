# Project Title

This loan qualifier application is designed to help a lender determine their borrowers eligibility for various bank loans. It utilizes a CSV file containing information on the loans offered by different banks. When the user runs the application, they will be prompted to enter their own personal and financial information. The application will then analyze this information and compare it to the criteria for the loans in the CSV file. Any loans for which the borrower qualifies will be saved in a separate CSV file for the user to review. This tool is intended to make it easier for borrowers to compare their options and find the loan that best fits their needs.

---

## Technologies

This application is written with Python 3.7 and uses:
   * sys module
   * pathlib module
   * fire library
   * questionary library
   

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

1. Create a new development environment called **loan_qualifier_app** and install the libraries contained in in Technologies description.
* From your terminal instance, create a nev virtual environment called **loan_qualifier_app** using the following code:

```python
conda create -n loan_qualifier_app python=3.7 anaconda 
```
* Activate the new **loan_qualifier_app** environment as follows:

```python
conda activate loan_qualifier_app  
```
2. Open **app.py** and review Python scripts.  
3. You'll be asked to enter a file path to a rate-sheet CSV file that contains data with a list of banks that offer loans.
4. After you'll enter the path you'll be asked a series of questions to determine eligible loans.
5. You'll be prompted if you want to save the list of data with eligible loans :
   * If you want to save the data, you'll be prompted to ented the path for saving data in a separate SCV file.
   * If not the system exits.  
---

## Usage

### User Story
* As a user, I need the ability to save the qualifying loans to a CSV file so    that I can share the results as a spreadsheet.

### Acceptance Criteria
* Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.

* Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

* Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

* Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

* Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

---

## Contributors
Brought to you by Alex Likhachev

---

## License

MIT

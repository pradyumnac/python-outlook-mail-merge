# python-outlook-mail-merge
This project allows you send mass emails with rich HTML formatting through Microsoft Outlook via an Excel workbook and Python.

# Getting Started
## Excel Method
You will need to install the libaries pypiwin32 (win32com.client) and pandas libraries to get this project running on your local machine.
```
pip install pypiwin32
```
```
pip install pandas
```

## Mail to method
You will need to install the libaries webbrowser libraries to get this project running on your local machine. The script mailto.py triggers a mailto to send a new mail open event to default email client
```
pip install webbrowser
```

# Running the Script
## Excel method
1. Rename it as "Excel Workbook Template.xlsx"
2. Create an Excel workbook with the column headers 'Email Address', 'Subject', and 'HTML Email Body'. Insert the email addresses, subject lines,
and HTML email bodies in the respective cells under the column headers.

3. Replace the code in the following line of the python script with the file directory to your Excel workbook:
```
file = pd.ExcelFile('Insert directory of Excel file containing list of email addresses you plan to send') 
```

## Mail to method
1. Rename `template.md.sample` to `template.md`
2. Replace the subject line keeping the starting character : **subject:**
3. Enter the body from 3rd line onwards
# License
See the LICENSE file for license rights and limitations (MIT).

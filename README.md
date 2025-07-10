# simplethread-project-reimbursement
This repo contains the solution and notes for my (J Weiss) interview assignment submission for SimpleThread. The problem is centered around a reimbursement amount for sets of project dates.

This program can run directly in console or IDE using a Python3 compiler. The test sets have been input manually to the main function, so will be utilizied when ran, and solution items will print sequentially to the console.
# Dependencies
- Python 3

# Input datasets
Set 1:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/4/24

Set 2:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
  Project 2: High Cost City Start Date: 10/2/24 End Date: 10/6/24
  Project 3: Low Cost City Start Date: 10/6/24 End Date: 10/9/24

Set 3:
  Project 1: Low Cost City Start Date: 9/30/24 End Date: 10/3/24
  Project 2: High Cost City Start Date: 10/5/24 End Date: 10/7/24
  Project 3: High Cost City Start Date: 10/8/24 End Date: 10/8/24

Set 4:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
  Project 2: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
  Project 3: High Cost City Start Date: 10/2/24 End Date: 10/3/24
  Project 4: High Cost City Start Date: 10/2/24 End Date: 10/6/24

# Output
$ amount for reimbursment per project set

# Rules
  - Travel days are start and end of project
  - Each project is either high cost or low cost
  - Contiguous or overlapping projects can be considered one project
  - Low cost travel reimbursement = 45
  - High cost travel reimbursement = 55
  - Low cost full day reimbursement = 75
  - High cost travel reimbursement = 85

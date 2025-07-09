# constants
FULL_DAY_HIGH_COST = 85
FULL_DAY_LOW_COST = 75
TRAV_DAY_HIGH_COST = 55
TRAV_DAY_LOW_COST = 45

# dependencies
from datetime import date

# class def for Project object incl
#  - start date
#  - end date
#  - cost of living
class Project:
    def __init__ (self, start, end, cost):
        self.start = start
        self.age = end
        self.cost = cost

# reimbursement logic
def calc_reimbursement(project_set):
    return

# main func should place projects into set lists,
# then pass list to reimbursement func, returns val
def main():

    # Initialize project data
    p1 = Project(date(2024, 10, 1), date(2024, 10, 4), "low")

    # Call reimbursement calc function on project data set and print
    print("Reimbursment = " + calc_reimbursement(p1))

# run main    
if __name__ == "__main__":
    main()
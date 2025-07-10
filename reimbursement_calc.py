# Constants
FULL_DAY_HIGH_COST = 85
FULL_DAY_LOW_COST = 75
TRAV_DAY_HIGH_COST = 55
TRAV_DAY_LOW_COST = 45

# Dependencies
from datetime import date, timedelta

# Class def for Project object incl
#  - start date
#  - end date
#  - cost of living
class Project:
    def __init__ (self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
    
    # Define printing method for debug
    def __repr__(self):
        return f"Project(start={self.start}, end={self.end}, cost='{self.cost}')"

# Reimbursement logic, input: set of projects; output: reimbursement amount
def calc_reimbursement(set):

    # Make sure set is sorted so we update correctly incrementaly... maybe
    sorted_set = sorted(set, key=lambda p: p.start)

    # Initialze dictionary for each date present in set; key = date, val = reimbursement
    reimburse_dict = {}

    # Iterate through each project in set
    for project in sorted_set:
        curr_date = project.start

        # Iterate through the project dates
        while project.start <= curr_date <= project.end:

            # Specific case for single day projects
            if curr_date == project.start == project.end:
                    if curr_date not in reimburse_dict:
                        reimburse_dict[curr_date] = TRAV_DAY_HIGH_COST if project.cost == "high" else TRAV_DAY_LOW_COST
                    else: 
                        if reimburse_dict[curr_date] == TRAV_DAY_HIGH_COST or reimburse_dict[curr_date] == TRAV_DAY_LOW_COST:
                            reimburse_dict[curr_date] = reimburse_dict[curr_date]
                        else:
                            reimburse_dict[curr_date] = FULL_DAY_HIGH_COST if project.cost == "high" else reimburse_dict[curr_date]         
            
            # Project start date
            elif curr_date == project.start:

                # Extra conditional for edge case of two projects starting on same day, and one ending the day another starts
                if (curr_date - timedelta(days=1)) in reimburse_dict:
                    prev_day_cost = reimburse_dict[curr_date-timedelta(days=1)]
                else: 
                    prev_day_cost = 0

                # If date is not in dict, add as travel; else if its a travel already, take higher full day
                if (curr_date not in reimburse_dict) or (prev_day_cost == TRAV_DAY_HIGH_COST or prev_day_cost == TRAV_DAY_LOW_COST) :
                    reimburse_dict[curr_date] = TRAV_DAY_HIGH_COST if project.cost == "high" else TRAV_DAY_LOW_COST
                else:
                    if reimburse_dict[curr_date] == TRAV_DAY_HIGH_COST: 
                        reimburse_dict[curr_date] = FULL_DAY_HIGH_COST 
                    else:
                        reimburse_dict[curr_date] = FULL_DAY_LOW_COST
            
            # Project full days
            elif project.start < curr_date < project.end:

                # If date is not in dict, add as full; change to high cost if overlap w/high cost
                if curr_date not in reimburse_dict:
                    reimburse_dict[curr_date] = FULL_DAY_HIGH_COST if project.cost == "high" else FULL_DAY_LOW_COST
                else: 
                    reimburse_dict[curr_date] = FULL_DAY_HIGH_COST if project.cost == "high" else reimburse_dict[curr_date]
            
            # Project end date
            else:

                # If date is not in dict, add as travel; else check if its already a travel and take the higher, or full accordingly
                if curr_date not in reimburse_dict:
                    reimburse_dict[curr_date] = TRAV_DAY_HIGH_COST if project.cost == "high" else TRAV_DAY_LOW_COST
                else:
                    if reimburse_dict[curr_date] == TRAV_DAY_LOW_COST and project.cost == "high":
                        reimburse_dict[curr_date] = TRAV_DAY_HIGH_COST
                    else:
                        reimburse_dict[curr_date] = FULL_DAY_HIGH_COST if project.cost == "high" else reimburse_dict[curr_date]
            
            # Increment current date counter
            curr_date += timedelta(days=1) 

    return sum(reimburse_dict.values())
        

# Main func should place projects into set lists,
# then passes list to reimbursement func, returns reimbursement total
def main():

    # Initialize project data s1p1 = set 1 project 1
    s1p1 = Project(date(2024, 10, 1), date(2024, 10, 4), "low")

    s2p1 = Project(date(2024, 10, 1), date(2024, 10, 1), "low")
    s2p2 = Project(date(2024, 10, 2), date(2024, 10, 6), "high")
    s2p3 = Project(date(2024, 10, 6), date(2024, 10, 9), "low")

    s3p1 = Project(date(2024, 9, 30), date(2024, 10, 3), "low")
    s3p2 = Project(date(2024, 10, 5), date(2024, 10, 7), "high")
    s3p3 = Project(date(2024, 10, 8), date(2024, 10, 8), "high")

    s4p1 = Project(date(2024, 10, 1), date(2024, 10, 1), "low")
    s4p2 = Project(date(2024, 10, 1), date(2024, 10, 1), "low")
    s4p3 = Project(date(2024, 10, 2), date(2024, 10, 3), "high")
    s4p4 = Project(date(2024, 10, 2), date(2024, 10, 6), "high")

    set1 = [s1p1]
    set2 = [s2p1, s2p2, s2p3]
    set3 = [s3p1, s3p2, s3p3]
    set4 = [s4p1, s4p2, s4p3, s4p4]

    # Call reimbursement calc function on project data set and print
    print(calc_reimbursement(set1))
    print(calc_reimbursement(set2))
    print(calc_reimbursement(set3))
    print(calc_reimbursement(set4))

# run main    
if __name__ == "__main__":
    main()
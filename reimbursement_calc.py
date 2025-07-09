# constants
FULL_DAY_HIGH_COST = 85
FULL_DAY_LOW_COST = 75
TRAV_DAY_HIGH_COST = 55
TRAV_DAY_LOW_COST = 45

# dependencies

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

            # Project start date
            if curr_date == project.start:

                # If date is not in dict, add as travel; else if its a travel already, take higher full day
                if curr_date not in reimburse_dict:
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

    for element in reimburse_dict:
        print(element)
        print(reimburse_dict[element])
        

# main func should place projects into set lists,
# then pass list to reimbursement func, returns val
def main():

    # Initialize project data
    s1p1 = Project(date(2024, 10, 1), date(2024, 10, 4), "low")

    s2p1 = Project(date(2024, 10, 1), date(2024, 10, 1), "low")
    s2p2 = Project(date(2024, 10, 2), date(2024, 10, 6), "high")
    s2p3 = Project(date(2024, 10, 6), date(2024, 10, 9), "low")

    set1 = [s1p1]
    set2 = [s2p1, s2p2, s2p3]
    #print(set1)
    # Call reimbursement calc function on project data set and print
    calc_reimbursement(set2)

# run main    
if __name__ == "__main__":
    main()
# constants
FULL_DAY_HIGH_COST = 85
FULL_DAY_LOW_COST = 75
TRAV_DAY_HIGH_COST = 55
TRAV_DAY_LOW_COST = 45

# dependencies
import numpy as np
from datetime import date

# class def for Project object incl
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

# reimbursement logic
def calc_reimbursement(set):
    num_low_trav = 0
    num_high_trav = 0
    num_low_full = 0
    num_high_full = 0

    reimburse = 0

    # for list of single val
    sorted_set = sorted(set, key=lambda p: p.start)

    #iterate from start date of first item to last date of last project, decide from there
    set_start_date = sorted_set[0].start 
    set_end_date = sorted_set[len(sorted_set)-1].end

    curr_date = set_start_date
    while curr_date <= set_end_date:

        # check if date exists in any project,
        # each day gets val of none, full high, full low, trav high, or trav low
        for project in sorted_set:
            if not (project.start <= curr_date <= project.end):
                reimburse += 0
            elif 
    

    # new idea just use a hash map
    reimburse_dict = {}
    for project in sorted_set:
        curr_date = project.start
        while project.start <= curr_date <= project.end:
            if curr_date in reimburse_dict:
                if project.cost == "low":
                    reimburse_dict

    print(sorted_set)
        

# main func should place projects into set lists,
# then pass list to reimbursement func, returns val
def main():

    # Initialize project data
    s1p1 = Project(date(2024, 10, 1), date(2024, 10, 4), "low")

    s2p1 = Project(date(2024, 10, 1), date(2024, 10, 1), "high")
    s2p2 = Project(date(2024, 10, 2), date(2024, 10, 6), "high")
    s2p3 = Project(date(2024, 10, 6), date(2024, 10, 9), "low")

    set1 = [s1p1]
    set2 = [s2p1, s2p2, s2p3]
    print(set1)
    # Call reimbursement calc function on project data set and print
    print(calc_reimbursement(set1))
    print(calc_reimbursement(set2))

# run main    
if __name__ == "__main__":
    main()
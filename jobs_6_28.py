class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Sort jobs by profit (high to low)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [False] * max_deadline
    result = [None] * max_deadline

    total_profit = 0

    for job in jobs:
        # Try to schedule job at the latest possible slot before deadline
        for i in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                result[i] = job.id
                total_profit += job.profit
                break

    print("Scheduled Jobs:", [j for j in result if j])
    print("Total Profit:", total_profit)

# Example usage
jobs = [
    Job('J1', 2, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

job_scheduling(jobs)

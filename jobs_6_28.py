def job_scheduling(jobs):
    jobs.sort(key=lambda x: -x[2])  # Sort by profit descending
    n = max(job[1] for job in jobs)
    slots = [None] * n

    for job in jobs:
        for i in range(min(n, job[1]) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job
                break

    scheduled = [j[0] for j in slots if j]
    profit = sum(j[2] for j in slots if j)
    print("Jobs:", scheduled)
    print("Profit:", profit)

# Each job = (Job ID, Deadline, Profit)
jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
job_scheduling(jobs)

Job = (input("enter the job value: "))
Job = Job.split()

Job = [(x) for x in Job]

Profit = (input("enter the profit value: "))
Profit = Profit.split()

Profit = [int(y) for y in Profit]

deadline = (input("enter the deadline value: "))
deadline = deadline.split()

deadline = [int(z) for z in deadline]


arr = [(Job[i], Profit[i], deadline[i]) for i in range(0,len(Profit))]

max_deadline = sorted(arr, key=lambda i: i[2],reverse=True)
n = max_deadline[0][2]
print(arr)

# arr = sorted(sorted_array, key=lambda i: i[2], reverse=True)

def job_seq(max_deadline,arr):
    d = []
    for i in range(max_deadline):
        max_item = arr[0]
        for item in arr:
            if item[2] == i+1: 
                if item[1] > max_item[1]:
                    max_item = item

        d.append(max_item)
    return d
print(job_seq(n,arr))














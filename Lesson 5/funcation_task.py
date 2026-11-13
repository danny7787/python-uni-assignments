# My functions task using an IT help desk example


# Takes a name, problem and priority and returns a ticket summary.
# If no priority is given, it uses "normal".
def create_ticket(name, problem, priority="normal"):
    ticket = name + ": " + problem + " - Priority: " + priority
    return ticket


# Takes the hours worked and rate in CHF and returns the cost.
# The default rate is 60 CHF per hour.
def calculate_cost(hours, hourly_rate=60):
    cost = hours * hourly_rate
    return cost


# Takes a list of ticket statuses and returns how many are open.
def count_open_tickets(statuses):
    count = 0
    for status in statuses:
        if status == "open":
            count = count + 1
    return count


# Main program
print("IT Help Desk")

# Positional arguments: the order of the values matters.
ticket1 = create_ticket("Daniel", "Printer offline", "high")
print(ticket1)

# Keyword arguments: use the parameter names.
ticket2 = create_ticket(problem="Email not working", name="Alex", priority="high")
print(ticket2)

# Default argument: priority will be normal.
ticket3 = create_ticket("Sam", "Mouse not working")
print(ticket3)

# Use the default hourly rate.
cost1 = calculate_cost(2)
print("Cost with default rate:", cost1, "CHF")

# Give a different rate using keyword arguments.
cost2 = calculate_cost(hours=3, hourly_rate=80)
print("Cost with different rate:", cost2, "CHF")

# Give the list to the function and print the result.
statuses = ["open", "closed", "open", "open"]
open_tickets = count_open_tickets(statuses)
print("Number of open tickets:", open_tickets)


        
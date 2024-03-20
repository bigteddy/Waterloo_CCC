P = int(input())
N = int(input())
R = int(input())

infected = N
infected_total = N
days = 0

while True:
    infected = infected * R
    infected_total = infected_total + infected
    days = days + 1

    # print(infected_total)
    if infected_total > P:
        break

print(days)

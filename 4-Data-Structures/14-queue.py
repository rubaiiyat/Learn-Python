from collections import deque

ticket = deque([])
ticket.append(5)
ticket.append(6)
ticket.append(7)
ticket.append(8)
ticket.append(9)

print(ticket)

for i in range(len(ticket) + 5):
    if not ticket:
        print("No Ticket Availabe now")
        break
    else:
        ticket.popleft()
        print(ticket)

#input phase
ticker = input("Enter stock ticker symbol:")
shares = float(input("Enter number of shares:"))
cost = float(input("Enter cost per share:"))

#process phase
invested = shares * cost 

#output phase 
print("Ticker:", ticker)
print("Total amount invested:", invested)
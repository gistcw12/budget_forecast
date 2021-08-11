import pandas as pd
budget_data = pd.read_csv('data.csv')
df = pd.DataFrame(budget_data) 
# print("Sum of Data is:",df.Amount.sum()) 

from datetime import datetime 
enter_date = str(input('Enter date(yyyy-mm-dd): ')) 
current_account_balance = input("Enter current balance on account:") 
forecast_date = datetime.strptime(enter_date, "%Y-%m-%d") 
forecast_balance = current_account_balance + df.Amount.sum()
# print(forecast_date)
# print(current_account_balance) 
# Check Read CSV
# print("Forecast Balance on the given date is:",df.Amount.sum())
print("Forecast Balance on the given date is:",forecast_balance)

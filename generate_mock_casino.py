import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Define the start and end date for the date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 4, 30)

# Sample data parameters
num_entries = 1000  # number of data entries
players = range(1, 101)  # 100 players
games = ['Blackjack', 'Roulette', 'Slots', 'Poker', 'Baccarat', 'Craps']
bet_min, bet_max = 10, 500  # min and max bet amount

# Generate mock data
data = {
    'PlayerID': [random.choice(players) for _ in range(num_entries)],
    'GameType': [random.choice(games) for _ in range(num_entries)],
    'BetAmount': [random.randint(bet_min, bet_max) for _ in range(num_entries)],
    'WinLossAmount': [random.randint(-bet_max, bet_max) for _ in range(num_entries)],
    'DateTime': [random_date(start_date, end_date) for _ in range(num_entries)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
df.head()
# Save the DataFrame to a CSV file
df.to_csv('mock_casino_data.csv', index=False)

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

def generate_betting_data(rows=10000):
    data = []
    current_date = datetime(2026, 1, 2)
    
    for i in range(rows):
        player_id = 1000 + i
        # Random signup date in the last 2 years
        signup_date = current_date - timedelta(days=random.randint(30, 730))
        
        # Features that influence churn
        total_deposits = round(random.uniform(10, 5000), 2)
        total_wagered = round(total_deposits * random.uniform(0.8, 1.2), 2)
        
        # Logic: If they lose a lot, they are more likely to have a high 'days_since_last_bet'
        win_loss_ratio = random.uniform(0.4, 1.1) 
        
        # Creating a 'churn' correlation
        if win_loss_ratio < 0.6 or total_wagered < 50:
            days_since_last_bet = random.randint(20, 60) # Likely churned
        else:
            days_since_last_bet = random.randint(1, 15)  # Active player
            
        preferred_sport = random.choice(['Football', 'Horse Racing', 'Tennis', 'Greyhounds', 'Cricket'])
        avg_odds = round(random.uniform(1.1, 10.0), 2)
        
        # Label for Churn (1 = Churned/Inactive, 0 = Active)
        churn_label = 1 if days_since_last_bet > 30 else 0
        
        data.append([
            player_id, signup_date.strftime('%Y-%m-%d'), total_deposits, 
            total_wagered, win_loss_ratio, days_since_last_bet, 
            preferred_sport, avg_odds, churn_label
        ])

    columns = [
        'player_id', 'signup_date', 'total_deposits', 'total_wagered', 
        'win_loss_ratio', 'days_since_last_bet', 'preferred_sport', 
        'avg_odds', 'churn_label'
    ]
    return pd.DataFrame(data, columns=columns)

# Generate and Save
df = generate_betting_data(10000)
df.to_csv('betting_project_data.csv', index=False)
print("Dataset created: 10,000 rows of player data saved to 'bet365_project_data.csv'")
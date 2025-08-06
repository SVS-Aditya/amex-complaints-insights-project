import pandas as pd
import random
from faker import Faker
from datetime import timedelta
import numpy as np

def generate_ticket_data(n_tickets=5000, seed=42):
    fake = Faker()
    random.seed(seed)
    np.random.seed(seed)

    categories = ['Billing', 'Fraud', 'Card Reissue', 'Travel Booking', 'Dispute']
    data = []

    for _ in range(n_tickets):
        created_at = fake.date_between(start_date='-1y', end_date='-10d')
        resolution_days = random.randint(1, 15)
        resolved_at = created_at + timedelta(days=resolution_days)

        entry = {
            'ticket_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'agent_id': f"AGENT{random.randint(100, 150)}",
            'created_at': created_at,
            'resolved_at': resolved_at,
            'resolution_days': resolution_days,
            'category': random.choice(categories),
            'satisfaction_score': random.randint(1, 10),
        }
        data.append(entry)

    df = pd.DataFrame(data)

    # Add computed fields
    df['sla_breached'] = df['resolution_days'] > 7
    df['incentive_eligible'] = df.apply(
        lambda row: row['resolution_days'] <= 7 and row['satisfaction_score'] >= 8, axis=1
    )

    return df

if __name__ == "__main__":
    df = generate_ticket_data(5000)
    df.to_csv("../data/agent_performance.csv", index=False)
    print("Generated and saved 5000 synthetic support tickets to ../data/agent_performance.csv")

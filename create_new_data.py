import pandas as pd
import numpy as np

# Create a dictionary with sample data
data = {
    'tenure': np.random.randint(1, 100, size=10),
    'age': np.random.randint(18, 70, size=10),
    'address': np.random.randint(1, 10, size=10),
    'income': np.random.randint(30000, 100000, size=10),
    'ed': np.random.randint(1, 5, size=10),
    'employ': np.random.randint(1, 30, size=10),
    'equip': np.random.randint(0, 2, size=10),
    'callcard': np.random.randint(0, 2, size=10),
    'wireless': np.random.randint(0, 2, size=10),
    'longmon': np.random.random(size=10) * 100,
    'tollmon': np.random.random(size=10) * 100,
    'equipmon': np.random.random(size=10) * 100,
    'cardmon': np.random.random(size=10) * 100,
    'wiremon': np.random.random(size=10) * 100,
    'longten': np.random.random(size=10) * 100,
    'tollten': np.random.random(size=10) * 100,
    'cardten': np.random.random(size=10) * 100,
    'voice': np.random.randint(0, 2, size=10),
    'pager': np.random.randint(0, 2, size=10),
    'internet': np.random.randint(0, 2, size=10),
    'callwait': np.random.randint(0, 2, size=10),
    'confer': np.random.randint(0, 2, size=10),
    'ebill': np.random.randint(0, 2, size=10),
    'loglong': np.random.random(size=10) * 10,
    'logtoll': np.random.random(size=10) * 10,
    'lninc': np.random.random(size=10) * 10,
    'custcat': np.random.randint(1, 5, size=10),
    'churn': np.random.randint(0, 2, size=10)  # Assuming 'churn' is the target variable
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('./data/raw/new_data.csv', index=False)

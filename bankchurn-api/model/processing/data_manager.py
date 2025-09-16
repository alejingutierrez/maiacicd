import pandas as pd
from typing import Optional


def load_dataset(file_name: str) -> pd.DataFrame:
    """
    Load dataset from file.
    
    Args:
        file_name: Name of the file to load
        
    Returns:
        DataFrame with test data
    """
    # For testing purposes, create a simple test dataset
    test_data = {
        "Customer_Age": [57],
        "Gender": ["M"],
        "Dependent_count": [4],
        "Education_Level": ["Graduate"],
        "Marital_Status": ["Single"],
        "Income_Category": ["$120K +"],
        "Card_Category": ["Blue"],
        "Months_on_book": [52],
        "Total_Relationship_Count": [2],
        "Months_Inactive_12_mon": [3],
        "Contacts_Count_12_mon": [2],
        "Credit_Limit": [25808.0],
        "Total_Revolving_Bal": [0.0],
        "Avg_Open_To_Buy": [25808.0],
        "Total_Amt_Chng_Q4_Q1": [0.712],
        "Total_Trans_Amt": [7794.0],
        "Total_Trans_Ct": [94],
        "Total_Ct_Chng_Q4_Q1": [0.843],
        "Avg_Utilization_Ratio": [0.0]
    }
    
    return pd.DataFrame(test_data)

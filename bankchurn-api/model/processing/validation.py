from typing import Optional
from pydantic import BaseModel


class DataInputSchema(BaseModel):
    """
    Schema for data input validation
    """
    Customer_Age: Optional[int] = None
    Gender: Optional[str] = None
    Dependent_count: Optional[int] = None
    Education_Level: Optional[str] = None
    Marital_Status: Optional[str] = None
    Income_Category: Optional[str] = None
    Card_Category: Optional[str] = None
    Months_on_book: Optional[int] = None
    Total_Relationship_Count: Optional[int] = None
    Months_Inactive_12_mon: Optional[int] = None
    Contacts_Count_12_mon: Optional[int] = None
    Credit_Limit: Optional[float] = None
    Total_Revolving_Bal: Optional[float] = None
    Avg_Open_To_Buy: Optional[float] = None
    Total_Amt_Chng_Q4_Q1: Optional[float] = None
    Total_Trans_Amt: Optional[float] = None
    Total_Trans_Ct: Optional[int] = None
    Total_Ct_Chng_Q4_Q1: Optional[float] = None
    Avg_Utilization_Ratio: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "Customer_Age": 57,
                "Gender": "M",
                "Dependent_count": 4,
                "Education_Level": "Graduate",
                "Marital_Status": "Single",
                "Income_Category": "$120K +",
                "Card_Category": "Blue",
                "Months_on_book": 52,
                "Total_Relationship_Count": 2,
                "Months_Inactive_12_mon": 3,
                "Contacts_Count_12_mon": 2,
                "Credit_Limit": 25808,
                "Total_Revolving_Bal": 0,
                "Avg_Open_To_Buy": 25808,
                "Total_Amt_Chng_Q4_Q1": 0.712,
                "Total_Trans_Amt": 7794,
                "Total_Trans_Ct": 94,
                "Total_Ct_Chng_Q4_Q1": 0.843,
                "Avg_Utilization_Ratio": 0
            }
        }

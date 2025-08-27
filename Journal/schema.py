from pydantic import BaseModel, Field
from datetime import date,datetime
from typing import Optional

class JournalEntrySchema(BaseModel):
    entryDate:date = Field(default=datetime.date(datetime.now()),description="date of the record entry")
    debit_account: str
    credit_account: str
    amount:float = Field(ge=0)
    narration:Optional[str]= None




from sqlalchemy import Integer, String, Date, Column,DECIMAL
from database import Base
from datetime import datetime



class JournalEntryModel(Base):
    __tablename__ = "JournalEntry"
    entryId = Column(Integer, primary_key=True,autoincrement=True)
    entryDate = Column(Date,nullable=False,default=datetime.date(datetime.now()))
    debit_account = Column(String,nullable=False)
    credit_account = Column(String,nullable=False)
    amount = Column(DECIMAL(precision=10,scale=2))
    narration = Column(String(100),nullable=True)
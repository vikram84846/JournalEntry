from fastapi import APIRouter, Depends, status, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
from .models import JournalEntryModel
from .schema import JournalEntrySchema



journalRouter = APIRouter(prefix="/journal",tags=["Journal"])




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@journalRouter.get("/",status_code=200)
async def all_entries(db:Session = Depends(get_db) ):
    records = db.query(JournalEntryModel).all()
    if not records :
        return {"message": "no entries to show"}
    return records
    

@journalRouter.post("/create-entry",status_code=status.HTTP_201_CREATED)
async def create_entry(entry:JournalEntrySchema,db:Session= Depends(get_db)):
    
    entry_model = JournalEntryModel(**entry.model_dump())
    db.add(entry_model)
    db.commit()
    db.refresh(entry_model)
    return {"data posted successfully":entry_model}

@journalRouter.delete("/delete-entry/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(id:int,db:Session= Depends(get_db)):
    required_entry = db.query(JournalEntryModel).filter(JournalEntryModel.entryId==id).first()
    if not required_entry:
        raise HTTPException(status_code=404,detail=f"no record found with this {id}")
    db.delete(required_entry)
    db.commit()
    
@journalRouter.put("/update_entry/{id}")
async def update_entry(id:int,updated_entry:JournalEntrySchema,db:Session= Depends(get_db)):
    required_entry = db.query(JournalEntryModel).filter(JournalEntryModel.entryId==id).first()
    if not required_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no record with this {id}")
    for key,value in updated_entry.model_dump().items():
        setattr(required_entry,key,value)
    db.commit()
    db.refresh(required_entry)
    return {"updated data successfully":required_entry}
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from database import Base,engine
from Journal.routes import journalRouter
#loading enviornment
load_dotenv()

#loading app and database
app = FastAPI()
Base.metadata.create_all(bind=engine)


#general routes
@app.get("/")
async def read_root():
    return {"status": "Grocery Shop API is running"}

#adding app specific routes 
app.include_router(journalRouter)

#starting the server
if __name__ == "__main__":
    uvicorn.run("main:app",port= int(os.getenv("PORT")),host=os.getenv("HOST"),reload=True)
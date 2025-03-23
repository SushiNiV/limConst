"""from backend.logic import limConst

def main():
    userInput = input("Enter a constant: ")  
    result = limConst(userInput)
    print(f"The limit is: {result}")

if __name__ == "__main__":
    main()
"""

from fastapi import FastAPI
from pydantic import BaseModel
from logic import limConst

app = FastAPI()

class InputData(BaseModel):
    input: str

@app.post("/compute")
def compute(data: InputData):
    result = limConst(data.input)
    return {"limit": result}

# Run with: uvicorn main:app --reload
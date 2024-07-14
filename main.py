from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id: int
    content: str

memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return "메모 추가 성공"


# @app.get("/memos")
# def read_memo():
#     return memos

@app.get("/memos")
def read_desc_memo(sorted_standard:str="", sorted_command:str=""):
    memo_desc = []
    memo_asc = []
    memo_key = {}
    if sorted_standard == "regis" and sorted_command == "desc":
        for memo in memos:
            memo_desc.append(memo.content)
        memo_desc.sort()
        return memo_desc
    elif sorted_standard == "detail" and sorted_command == "asc":
        for memo in memos:
            memo_key[memo.id] = memo.content
        memo_asc = sorted(memo_key.items(), reverse=True)
        return memo_asc
    else:
        return memos


@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return "석세스"
    return "메모가 존재하지 않습니다."

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == int(memo_id):
            memos.pop(index)
            return "석세스"
    return "메모가 존재하지 않습니다."

app.mount("/", StaticFiles(directory="static",html=True), name="static")
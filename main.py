import uvicorn
from fastapi import FastAPI
from rat_app.config import settings
from rat_app.rat import route as rat_routes
from fastapi_sqlalchemy import DBSessionMiddleware


app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)


"""
########################################################################################################################
                                             IMPORT ROUTES
########################################################################################################################
"""

app.include_router(rat_routes.router, prefix="/rat", tags=["Rat"])

print(
    """Welcome to:\n
  ██████╗  █████╗ ████████╗███████╗
  ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
  ██████╔╝███████║   ██║   ███████╗
  ██╔══██╗██╔══██║   ██║   ╚════██║
  ██║  ██║██║  ██║   ██║   ███████║
  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
"""
)


@app.get("/")
async def root():
    return {"message": "Welcome to Rats backend"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

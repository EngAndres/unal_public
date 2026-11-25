"""Execution point of the backend."""

from applications import router_stadiums, router_teams, router_players

from fastapi import FastAPI

app = FastAPI(title="UNAL World Cup", version="0.3", 
              description="Simple example of web services in python to handle information about the schedule of the soccer world cup 2026")

app.include_router(router_stadiums)
app.include_router(router_teams)
app.include_router(router_players)

@app.get("/")
def home():
    return {"message": "Welcome to UN!"}
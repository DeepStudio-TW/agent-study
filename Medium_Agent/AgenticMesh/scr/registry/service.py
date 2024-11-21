# src/registry/service.py
from fastapi import FastAPI, HTTPException
from .models import AgentRegistration, AgentMetadata
from datetime import datetime
import uuid

app = FastAPI()
registry = {}

@app.post("/register")
async def register_agent(registration: AgentRegistration):
    agent_id = str(uuid.uuid4())
    metadata = AgentMetadata(
        **registration.dict(),
        agent_id=agent_id,
        status="active",
        registered_at=datetime.now(),
        last_active=datetime.now()
    )
    registry[agent_id] = metadata
    return {"agent_id": agent_id}

@app.get("/agents/{agent_id}")
async def get_agent(agent_id: str):
    if agent_id not in registry:
        raise HTTPException(status_code=404, detail="Agent not found")
    return registry[agent_id]
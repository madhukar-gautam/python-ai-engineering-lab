from fastapi import APIRouter, Depends

from app.agents.models.agent import AgentRequest, AgentResponse
from app.agents.services.rca_agent import RCAAgent
from app.dependencies import get_rca_agent


router = APIRouter(
    prefix="/api/v1/agents",
    tags=["Agents"]
)


@router.post("/rca", response_model=AgentResponse)
async def investigate(
    request: AgentRequest,
    agent: RCAAgent = Depends(get_rca_agent)
) -> AgentResponse:

    answer = await agent.investigate(
        request.question
    )

    return AgentResponse(answer=answer)
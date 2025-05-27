from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServerSse, MCPServer
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
import asyncio

PEARL_API_KEY = "" # https://www.pearl.com/contact

async def run_agent(mcp_server: MCPServer):
    
    agent_legal_expert = Agent(
        name="LegalExpertAgent",
        handoff_description="Answer a legal question and check with an expert that the answer is correct.",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
            Answer the question as best as you can, and then use the askExpert (not askPearlExpert) tool to get a second 
            opinion from an expert. Make sure that you let the expert know that you are a virtual assistant operating on
            behalf of the customer and that you are looking for feedback on the accuracy and completeness of your answer.
            Create a two paragraph report for the user. The first paragraph summarized your answer to the 
            question briefly. The second paragraph summarizes the expert's review of the answer, re-written if necessary
            to make sense in the context of the conversation.""",
        mcp_servers=[mcp_server],
        
    )

    result = await Runner.run(
        agent_legal_expert, 
        "As a naturalized US citizen can I run for president?"
    )
    
    print(result.final_output)


async def main():

    print("Running Legal Agent...")

    async with MCPServerSse(
        name="Pearl API",
        params={
            "url": "https://mcp.pearl.com/mcp",
            "headers": {
                "X-API-KEY": PEARL_API_KEY
            }
        },
        client_session_timeout_seconds=600
    ) as mcp_server:
        tools = await mcp_server.list_tools()
        trace_id = gen_trace_id()
        with trace(workflow_name="Legal Agent", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run_agent(mcp_server)
    
if __name__ == "__main__":
    asyncio.run(main())

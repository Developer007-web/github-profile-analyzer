from fastmcp import FastMCP

from tools.profile_tools import analyze_profile as profile_tool
from tools.language_tools import analyze_languages as language_tool
from tools.repo_tools import repo_insights as repo_tool
from tools.activity_tools import (
    activity_score as activity_tool,
    learning_rate as learning_tool
)
from tools.ai_tools import (
    generate_summary as summary_tool,
    github_roast as roast_tool,
    project_recommendations as recommendation_tool
)

mcp = FastMCP("GitHub Profile Analyzer")


@mcp.tool(description="Analyze a GitHub user's profile")
async def analyze_profile(username: str):

    print("PROFILE TOOL CALLED:", username)

    return await profile_tool(username)


@mcp.tool(description="Analyze programming languages")
async def analyze_languages(username: str):

    print("LANGUAGE TOOL CALLED:", username)

    return await language_tool(username)


@mcp.tool(description="Get repository insights")
async def repo_insights(username: str):

    print("REPO TOOL CALLED:", username)

    return await repo_tool(username)


@mcp.tool(description="Calculate developer activity score")
async def activity_score(username: str):

    print("ACTIVITY TOOL CALLED:", username)

    return await activity_tool(username)


@mcp.tool(description="Analyze learning trend")
async def learning_rate(username: str):

    print("LEARNING TOOL CALLED:", username)

    return await learning_tool(username)


@mcp.tool(description="Generate developer summary")
async def generate_summary(username: str):

    print("SUMMARY TOOL CALLED:", username)

    return await summary_tool(username)


@mcp.tool(description="Roast a GitHub profile")
async def github_roast(username: str):

    print("ROAST TOOL CALLED:", username)

    return await roast_tool(username)


@mcp.tool(description="Recommend project ideas")
async def project_recommendations(username: str):

    print("PROJECT TOOL CALLED:", username)

    return await recommendation_tool(username)


if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=8000
    )
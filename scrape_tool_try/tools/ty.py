
from crewai_tools import BaseTool
from crewai import Agent, Task, Crew

class MyCustomTool(BaseTool):
    name: str = "calculate tool"
    description: str = "this tool calculates the sum of two numbers"

    def _run(self, a: int, b: int) -> int:
        return a + b

agent = Agent(
    role="Calculator",
    goal="Calculate the sum of two numbers",
    verbose=True,
    tools=[MyCustomTool()]
)

task = Task(
    description="Calculate the sum of two numbers",
    expected_output="The sum of two numbers",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2,
    memory=True
)



if __name__ == "__main__":
    result = crew.kickoff(inputs={"query": "calculate 3 and 4"})
    print(result)



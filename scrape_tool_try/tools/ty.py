import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from crewai_tools import BaseTool
from crewai import Agent, Task, Crew

class MyCustomTool(BaseTool):
    name: str = "calculate tool"
    description: str = "this tool calculates the sum of two numbers"

    def _run(self, a: int, b: int) -> int:
        return a + b
    def _set_args_schema(self):
        self.args_schema = {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        }

agent = Agent(
    role="Calculator",
    goal="Calculate the sum of two numbers, about the {query}",
    backstory="The agent should be able to calculate the sum of two numbers",
    verbose=True,
    tools=[MyCustomTool()]
)

task = Task(
    description="Calculate the sum of two numbers about {query}",
    expected_output="The sum of two numbers about {query}",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=2,
    memory=True
)



if __name__ == "__main__":
    result = crew.kickoff(inputs={"query": "calculate 1 and 4"})
    print(result)



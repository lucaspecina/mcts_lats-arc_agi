from __future__ import annotations  # noqa: F404
import sys
import os
from dotenv import load_dotenv
import getpass


# Define the path to your project
project_path = os.path.expanduser('~/Desktop/dev/ai/lucaspecina/arc-agi/ARC-AGI-solution')

# Add the project path to the PYTHONPATH
if project_path not in sys.path:
    sys.path.append(project_path)
os.chdir(project_path)

# Load the .env file
dotenv_path = os.path.join(project_path, '.env')
load_dotenv(dotenv_path)
# Now you can access the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
tavily_api_key = os.getenv('TAVILY_API_KEY')

def _set_if_undefined(var: str) -> None:
    if os.environ.get(var):
        return
    os.environ[var] = getpass.getpass(var)


init_prompt = """You are a VERY SMART AI who is very good at solving puzzles. Below is a list of input and output pairs with a pattern." 
Identify the patterns."
Hint: imagine the problem as a grid. Each number represents a different color. Imagine it visually and identify the pattern. Be very careful with the shape of the grids and identify the patterns for the inputs and outputs."
The pattern should be consistent to all the examples so if you apply it to the example inputs, you get the corresponding example outputs."
The result should be the output for the test input case."""
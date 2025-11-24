from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import json
from datetime import datetime
import re

load_dotenv()

@tool
def calculate(expression: str) -> str:
    """
    Calculate a mathematical expression. 
    Supports basic arithmetic: +, -, *, /, **, (), and common functions like sqrt, abs, round.
    Example: "2 + 2", "sqrt(16)", "10 ** 2"
    """
    try:
        # Remove any potentially dangerous operations
        if any(keyword in expression.lower() for keyword in ['import', 'exec', 'eval', '__']):
            return "Error: Invalid expression"
        
        # Safe mathematical evaluation
        import math
        allowed_names = {
            'abs': abs, 'round': round, 'min': min, 'max': max,
            'sqrt': math.sqrt, 'pow': math.pow, 'pi': math.pi, 'e': math.e,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'log': math.log, 'log10': math.log10, 'ceil': math.ceil, 'floor': math.floor
        }
        
        # Evaluate the expression
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error calculating expression: {str(e)}"


@tool
def analyze_text(text: str) -> str:
    """
    Analyze text and return statistics including word count, character count, 
    sentence count, and reading time estimate.
    """
    try:
        # Basic text analysis
        char_count = len(text)
        char_count_no_spaces = len(text.replace(" ", ""))
        word_count = len(text.split())
        
        # Count sentences (rough estimate)
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        # Estimate reading time (average 200 words per minute)
        reading_time_minutes = round(word_count / 200, 1)
        
        analysis = f"""Text Analysis:
- Characters (with spaces): {char_count}
- Characters (without spaces): {char_count_no_spaces}
- Words: {word_count}
- Sentences: {sentence_count}
- Estimated reading time: {reading_time_minutes} minutes
- Average words per sentence: {round(word_count / max(sentence_count, 1), 1)}"""
        
        return analysis
    except Exception as e:
        return f"Error analyzing text: {str(e)}"


@tool
def format_json(json_string: str) -> str:
    """
    Format and validate a JSON string. Returns prettified JSON or error message.
    """
    try:
        # Parse and re-format JSON
        parsed = json.loads(json_string)
        formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
        return f"Formatted JSON:\n{formatted}"
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON - {str(e)}"
    except Exception as e:
        return f"Error formatting JSON: {str(e)}"


@tool
def get_current_datetime(timezone: str = "UTC") -> str:
    """
    Get the current date and time. 
    Timezone parameter is optional (currently only UTC is supported in this version).
    """
    try:
        now = datetime.utcnow()
        return f"Current date and time (UTC): {now.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error getting datetime: {str(e)}"


@tool
def convert_case(text: str, case_type: str) -> str:
    """
    Convert text case. 
    case_type options: 'upper', 'lower', 'title', 'capitalize', 'snake', 'camel', 'kebab'
    """
    try:
        case_type = case_type.lower()
        
        if case_type == 'upper':
            return text.upper()
        elif case_type == 'lower':
            return text.lower()
        elif case_type == 'title':
            return text.title()
        elif case_type == 'capitalize':
            return text.capitalize()
        elif case_type == 'snake':
            # Convert to snake_case
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace(' ', '_')
        elif case_type == 'camel':
            # Convert to camelCase
            words = re.sub(r'[^a-zA-Z0-9]', ' ', text).split()
            return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        elif case_type == 'kebab':
            # Convert to kebab-case
            return re.sub(r'[^a-zA-Z0-9]', '-', text).lower()
        else:
            return f"Error: Unknown case type '{case_type}'. Use: upper, lower, title, capitalize, snake, camel, or kebab"
    except Exception as e:
        return f"Error converting case: {str(e)}"


TOOLS = [calculate, analyze_text, format_json, get_current_datetime, convert_case]

SYSTEM_MESSAGE = (
    "You are a helpful AI assistant with various utility tools. "
    "You can perform calculations, analyze text, format JSON, get current time, and convert text cases. "
    "Be concise, accurate, and helpful in your responses."
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
agent = create_react_agent(llm, TOOLS, prompt=SYSTEM_MESSAGE)


def run_agent(user_input: str) -> str:
    """Run the agent with a user query and return the response."""
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"recursion_limit": 50}
        )
        return result["messages"][-1].content
    except Exception as e:
        return f"Error: {str(e)}" 
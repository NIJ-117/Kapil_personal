from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
import subprocess
import requests  # Import requests to make the API call


class Pipeline:
    def __init__(self):
        self.name = "Python Code Pipeline"
        # FastAPI endpoint URL
        self.api_url = "http://127.0.0.1:8081/determine-task"

    async def on_startup(self):
        print(f"on_startup:{__name__}")
    
    async def on_shutdown(self):
        print(f"on_shutdown:{__name__}")

    def execute_python_code(self, code):
        try:
            result = subprocess.run(
                ["python", "-c", code], capture_output=True, text=True, check=True
            )
            stdout = result.stdout.strip()
            return stdout, result.returncode
        except subprocess.CalledProcessError as e:
            return e.output.strip(), e.returncode

    def determine_task(self, user_input: str) -> str:
        # Define the input data for the API call
        data = {"user_input": user_input}
        
        # Send the POST request to the FastAPI endpoint
        try:
            response = requests.post(self.api_url, json=data)
            response.raise_for_status()  # Raise an error for unsuccessful status codes
            result = response.json()
            return result["task"]  # Extract the task from the response
        except requests.RequestException as e:
            print("Failed to call API:", e)
            return "unknown"  # Default to "unknown" in case of an error

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        print(f"pipe:{__name__}")
        print(messages)
        print(user_message)

        # Determine the task using the API call
        task = self.determine_task(user_message)
        print("Task determined:", task)

        if task == "code_generation":
            
            return "preforming code generation"
        elif task == "compliance_check":
            return "Performing compliance check (not implemented)"
        elif task == "code_edit":
            return "Performing code edit (not implemented)"
        else:
            return task

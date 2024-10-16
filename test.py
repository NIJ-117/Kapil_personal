import requests

class Pipeline:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.name = "Wikipedia Pipeline"
        
        self.api_url = "http://127.0.0.1:8081/determine-task"  # FastAPI endpoint for determining the task

    async def on_startup(self):
        print(f"on_startup:{__name__}")
    
    async def on_shutdown(self):
        print(f"on_shutdown:{__name__}")

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

        return task

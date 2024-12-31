from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
from schemas import OpenAIChatMessage
import requests
import os


class Pipeline:
    class Valves(BaseModel):
        pass

    def __init__(self):
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "wiki_pipeline"
        self.name = "llama_code_agent"

        # Initialize rate limits
        self.valves = self.Valves(**{"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "")})

    async def on_startup(self):
        # This function is called when the server is started.
        print(f"on_startup:{__name__}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        print(f"on_shutdown:{__name__}")
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print(f"pipe:{__name__}")

        if body.get("title", False):
            print("Title Generation")
            return "llama_code_agent"
        else:
            titles = []
            for query in [user_message]:
                query = query.replace(" ", "_")

                

                # Define the URL of the FastAPI server
                url = "http://localhost:8083/code"  # Update the port if needed

                # Define the data to send in the POST request
                data = {
                    "user_input": query
                }

                # Send the POST request
                response = requests.post(url, json=data)

                # Check if the request was successful
                if response.status_code == 200:
                    # Print the translated text from the response
                    translated_text = response.json().get("Final_code_generated")
                    # print("Translated Text:", translated_text)
                    return translated_text
                else:
                    # Print an error message if the request failed
                    print(f"Failed to get a response: {response.status_code}")
                    print(response.text)
                    return "not able generate"

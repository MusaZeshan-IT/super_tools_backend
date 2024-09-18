"""
The views for the super_tools app
"""

import os
import cohere
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Loading the environment variables
load_dotenv()

# Cohere API key from settings
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize the Cohere client
co = cohere.Client(cohere_api_key)


class WritingToolsAPIView(APIView):
    """A class-based view for handling AI generation tasks via Cohere API."""

    def post(self, request, *args, **kwargs):
        """The post method for the Cohere API"""

        # Extract task and input text from the request body
        text = request.data.get("text")
        task = request.data.get("task")

        # Set the model
        model = "command-xlarge-20210901"

        if not text:
            return Response(
                {"error": "Text field is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        prompt = (
            f"Perform the following task: {task}. On this provided input text: {text}"
        )

        try:
            # Make the API request to Cohere
            response = co.generate(
                model=model,
                prompt=prompt,
                max_tokens=1000,
                temperature=0.7,  # Adjust as needed
            )

            generated_text = response.generations[0].text.strip()

            return Response({"output": generated_text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

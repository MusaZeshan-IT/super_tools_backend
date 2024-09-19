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
        model = "command-xlarge"

        if not text:
            return Response(
                {"error": "Text field is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Construct the prompt with specific task instructions
        prompt = (
            f"Perform the following task exactly as described: {task}. "
            f"Given the text: {text}, do not deviate from this task. "
            f"Your response should strictly be a direct result of the task without any extra content. "
            f"Do not generate any additional content, comments, follow-ups, or introductory phrases. "
            f"If you include anything beyond the requested result, it will not meet the required specifications."
            f"Strictly adhere to these instructions and avoid any deviations."
        )

        try:
            # Make the API request to Cohere
            response = co.generate(
                model=model,
                prompt=prompt,
                max_tokens=700,
                temperature=0.3,  # Adjusted temperature for stricter adherence
            )

            generated_text = response.generations[0].text.strip()

            return Response({"output": generated_text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

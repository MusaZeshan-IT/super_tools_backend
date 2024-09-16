"""
The views for the super_tools app
"""

import openai
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# Set your OpenAI API key (best practice is to use environment variables)
openai.api_key = settings.OPENAI_API_KEY


class SummarizeTextView(APIView):
    """Function for summarizing text"""

    def post(self, request):
        """The post method for summarizing text"""

        try:
            # Get the text from the request
            text = request.data.get("text", "")

            # Call OpenAI to summarize the text
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Summarize the following text in a way that is easy to understand, engaging, and professional. The summary should be clear and compelling, as if written by the best content writer, and suitable for readers of all ages, including non-native English speakers or a 10-year-old child. The tone should feel natural, like a knowledgeable and friendly teacher explaining the topic. Summarize the following text: {text}",
                max_tokens=150,
                temperature=0.7,
            )

            # Extract the summary from the response
            summary = response.choices[0].text.strip()

            return Response({"summary": summary}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

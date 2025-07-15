# Beyondchat-assignment
Reddit Persona Report Generator
This Python script automates the creation of detailed user personas based on Reddit data. It scrapes a user's recent posts and comments using the PRAW library, then employs Google's Gemini 1.5 Flash model to generate a structured persona report. The report infers characteristics like interests, behaviors, frustrations, and goals, with citations linking back to specific Reddit content. This tool is useful for market research, content strategy, or user analysis, providing insights into online personas without manual data review.

Key Features
-Interactive command-line interface for inputting Reddit user profile URLs.

-Generates reports in a readable Markdown-like text format, saved as individual files.

-Supports multiple report generations in one session, with an option to exit.

-Includes error handling for invalid URLs, empty data, or API issues.

-Adheres to PEP-8 coding standards for maintainability.

Prerequisites
-Python 3.6+ installed on your system.

-Valid Reddit API credentials (client ID, client secret, user agent) obtained from reddit.com/prefs/apps. (here i have hardcoded my credentials as it was with a spare account and a free API key for gemini.)

-A free Google API key from ai.google.dev for Gemini access.

-Basic familiarity with running Python scripts in a terminal.

-Create a virutal environmentif you wish to.
Installation Guide

- To get started, install the required libraries. Open your terminal and run:

|____ pip install praw google-generativeai
- If you have a requirements.txt file with these dependencies, use: (which i have provided)

|____ pip install -r requirements.txt
- Update the script with your API credentials (hardcoded for testing; switch to environment variables for security):

|____ export REDDIT_CLIENT_ID=your_client_id

|____ export REDDIT_CLIENT_SECRET=your_client_secret

|____ export REDDIT_USER_AGENT="your_user_agent"

|____ export GOOGLE_API_KEY=your_google_api_key

Usage Guide
- Run the script in your terminal with:

|____ python reddit_persona_report_generator.py

Step-by-Step Instructions

-When prompted, paste a Reddit user profile URL (e.g., https://www.reddit.com/user/exampleuser/).

-The script will scrape data, generate the report, and save it as a text file (e.g., exampleuser_persona_report.txt).

-You'll be prompted again for another URL.

-Type -1 to exit the program. 



Limitations

-Works only with user profiles (not subreddits or posts).

-AI-generated inferences may not be 100% accurate; always verify.

-Dependent on API availability and your credentials' validity.

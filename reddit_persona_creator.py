import praw
import google.generativeai as genai
import re

# Hardcoded credentials (for testing only - not secure for sharing; use environment variables in production)
# This is a spare ID so I hardcoded the credentials here and api key i used here was free of cost so I shared it here too
REDDIT_CLIENT_ID = 'mSK43zqD-HZzy-0KuIX6TQ'
REDDIT_CLIENT_SECRET = 'h8QkaghhMKHnrdakkItQOfPfxMUaYA'
REDDIT_USER_AGENT = 'script:callisto-mimas:v1.0 (by u/Available-Carrot1899)'
GOOGLE_API_KEY = 'AIzaSyDQ5nUmvwWPsAXlaDb-iY5r7dTrEVhb24M'

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_username_from_url(url):
    """Extract username from Reddit profile URL."""
    match = re.search(r'reddit\.com/user/([^/]+)/?', url)
    if match:
        return match.group(1)
    raise ValueError("Invalid Reddit profile URL. Use format: https://www.reddit.com/user/username/")

def scrape_user_data(username):
    """Scrape posts and comments from the user."""
    user = reddit.redditor(username)
    posts = []
    comments = []
    
    # Get user's submissions (posts)
    for submission in user.submissions.new(limit=50):
        posts.append({
            'id': submission.id,
            'title': submission.title,
            'body': submission.selftext,
            'url': f"https://www.reddit.com{submission.permalink}"
        })
    
    # Get user's comments
    for comment in user.comments.new(limit=50):
        comments.append({
            'id': comment.id,
            'body': comment.body,
            'url': f"https://www.reddit.com{comment.permalink}"
        })
    
    return posts, comments

def build_persona_report(posts, comments):
    """Use Gemini to generate a structured user persona report with citations."""
    # Prepare data for the model
    data_text = "Posts:\n" + "\n".join([f"ID: {p['id']} - {p['title']}: {p['body']}" for p in posts]) + "\n\nComments:\n" + "\n".join([f"ID: {c['id']} - {c['body']}" for c in comments])
    
    # Enhanced prompt for structured report format
    prompt = f"""
    Based on the following Reddit posts and comments, create a detailed user persona report in text format.
    Structure it with these sections: Profile Overview, Behavior & Habits, Frustrations, Motivations, Preferences, Personality Needs, Goals & Needs.
    Include inferred details like name, role, location, age, and bio where possible.
    For each point, cite specific post or comment IDs (e.g., [Post ID: abc123] or [Comment ID: def456]).
    
    Data:
    {data_text}
    
    Output as plain text with Markdown headings and bullet points for readability.
    Start with a title like 'User Persona Report: [Inferred Name]'.
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    print("Welcome to the Reddit Persona Report Generator!")
    while True:
        url = input("Paste Reddit user profile URL (or type -1 to exit): ").strip()
        if url == '-1':
            print("Exiting the program. Goodbye!")
            break
        try:
            username = get_username_from_url(url)
            posts, comments = scrape_user_data(username)
            
            if not posts and not comments:
                print("No data found for this user. Try another URL.")
                continue
            
            report = build_persona_report(posts, comments)
            
            # Output to text file
            output_file = f"{username}_persona_report.txt"
            with open(output_file, 'w') as f:
                f.write(report)
            
            print(f"Persona report saved to {output_file}")
        except ValueError as ve:
            print(f"Error: {ve} Please try a valid user profile URL.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

if __name__ == "__main__":
    main()

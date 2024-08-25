from creds import gemini_key
import google.generativeai as genai

genai.configure(api_key=gemini_key)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Make me a playlist for a rainy summer day with songs by the artists Kendrick Lamar, Jcole, Kanye West. You can include songs from other artists that are similar to the ones provided, but make about 80% of the playlist songs from these artists")

print(response.text)

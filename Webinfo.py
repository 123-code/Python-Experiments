from openai import OpenAI
import subprocess
import base64
import os 
from dotenv import load_dotenv

load_dotenv()

model = OpenAI(api_key=api_key)
model.timeout = 10

def image_b64(image):
    with open(image, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def url2screenshot(url):
    print(f"crawling: {url}...")

    if os.path.exists('screenshot.png'):
        os.remove('screenshot.png')

    result = subprocess.run(
        ["node", "screenshottest.js", url],
        capture_output=True,
        text=True
    )
    
    exitcode = result.returncode
    output = result.stdout

    if not os.path.exists('screenshot.png'):
        print("ERROR")
        return "Failed to scrape the website"
    
    b64_image = image_b64("screenshot.png")
    return b64_image

def visionExtract(b64_image, prompt):
    response = model.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You a web scraper, your job is to extract information based on a screenshot of a website & user's instruction",
            }
        ] + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{b64_image}",
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
            }
        ],
        max_tokens=1024,
    )

    message = response.choices[0].message
    message_text = message.content

    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        return "I was unable to find the answer on that website. Please pick another one"
    else:
        print(f"GPT: {message_text}")
        return message_text


def visionCrawl(url, prompt):
    b64_image = url2screenshot(url)
    if b64_image:
        return visionExtract(b64_image, prompt)
    else:
        return "Failed to get image"

response = visionCrawl('https://mail.google.com/mail/u/0/#inbox', 'what are my 5 first emails?')
print(response)

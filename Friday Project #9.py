import tkinter as tk
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("key")

def send_prompt():
  prompt = prompt_entry.get()
  if prompt:
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=prompt,
      max_tokens=150
    )
    response_text.config(state=tk.NORMAL)
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, response.choices[0].text)
    response_text.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("OpenAI Prompt Sender")

# Prompt entry
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

# Send button
send_button = tk.Button(root, text="Send", command=send_prompt)
send_button.pack()

# Response display
response_label = tk.Label(root, text="OpenAI Response:")
response_label.pack()
response_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
response_text.pack()

root.mainloop()
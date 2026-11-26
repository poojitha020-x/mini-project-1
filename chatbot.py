import gradio as gr
import requests

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:1b"

def chat(message, history):
    url = "http://localhost:11434/api/chat"

    # Convert Gradio history into Ollama message format
    messages = []
    for item in history:
        # Handles both Gradio dict format and older tuple/list format safely
        if isinstance(item, dict):
            messages.append({"role": item["role"], "content": item["content"]})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            messages.append({"role": "user", "content": item[0]})
            if item[1]:
                messages.append({"role": "assistant", "content": item[1]})

    # Add current user message
    messages.append({"role": "user", "content": message})

    try:
        response = requests.post(
            url,
            json={
                "model": "llama3.2:1b",
                "messages": messages,
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running (`ollama serve`)."
    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.ChatInterface(
    fn=chat,
    title="Llama 3.2 Chatbot",
    description="Chat with your local Ollama LLM",
)

if __name__ == "__main__":
    demo.launch()

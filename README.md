# 🤖 Triple AI Chatbot

A simple AI-powered chatbot built with **Streamlit** and **LangChain**, using **Groq LLMs** for fast and accurate responses.
This project demonstrates a **basic chatbot setup** with structured outputs using Pydantic, without conversation memory.

---

## 🚀 Features

- Interactive chat interface using **Streamlit**
- Powered by **Groq (LLaMA 3.1)** models
- Uses **LangChain LCEL** for prompt chaining
- **Structured JSON output** with `PydanticOutputParser`
- Domain-restricted responses (e.g. Machine Learning)
- Confidence level returned with each answer
- No conversation memory (each question is handled independently)

---

## 🧠 How It Works

1. The user enters a question in the Streamlit UI.
2. The question is sent to a LangChain pipeline:
   - Prompt Template
   - Groq LLM
   - Pydantic Output Parser
3. The model returns a structured response:
   - `answer`
   - `confidence` (low / medium / high)
4. The answer is displayed in the chat interface.

---

## 📁 Project Structure

Chatbot/

│

├── app.py              # Streamlit app (UI)

├── chatbot.py          # LangChain model pipeline

├── requirements.txt    # Python dependencies

├── .env                # Environment variables (GROQ_API_KEY)

└── README.md           # Project documentation

## 🛠️ Requirements

---
- Python **3.10 or 3.11** (recommended)
- Groq API Key

### Python Libraries
- streamlit
- langchain
- langchain-core
- langchain-groq
- pydantic
- python-dotenv
---
## ⚙️ Installation

### 1️⃣ Create a virtual environment

```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ Install dependencies

<pre class="overflow-visible! px-0!" data-start="1680" data-end="1723"><div class="w-full"><div class=""><div class=""><div class="min-h-0 min-w-0"><div class="border-token-border-light bg-token-bg-elevated-secondary corner-superellipse/1.1 rounded-3xl border my-4"><div class="pointer-events-none sticky z-40 shrink-0 mx-4 transition-opacity duration-300"><div class="sticky bg-token-border-light"></div></div><div class="relative z-0 flex max-w-full"><div id="b2a93627-99ab-4702-be44-5a8316517f0e:2:editor" class="Rx43rG_codemirror z-10 flex h-full w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼy"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell" aria-placeholder=""><div class="cm-line">pip install <span class="ͼr">-r</span> requirements.txt</div></div></div></div></div></div></div></div></div></div></div></pre>

## 🔑 Environment Variables

Create a `.env` file in the project root:

<pre class="overflow-visible! px-0!" data-start="1802" data-end="1848"><div class="w-full"><div class=""><div class=""><div class="min-h-0 min-w-0"><div class="border-token-border-light bg-token-bg-elevated-secondary corner-superellipse/1.1 rounded-3xl border my-4"><div class="pointer-events-none sticky z-40 shrink-0 mx-4 transition-opacity duration-300 opacity-0"><div class="sticky bg-token-border-light"></div></div><div class="relative z-0 flex max-w-full"><div id="b2a93627-99ab-4702-be44-5a8316517f0e:3:editor" class="Rx43rG_codemirror z-10 flex h-full w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼy"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" aria-placeholder=""><div class="cm-line">GROQ_API_KEY=your_groq_api_key_here</div></div></div></div></div></div></div></div></div></div></div></pre>

> ⚠️ Keep `.env` private. Do not commit to GitHub.

---

## ▶️ Running the Application

<pre class="overflow-visible! px-0!" data-start="1938" data-end="1970"><div class="w-full"><div class=""><div class=""><div class="min-h-0 min-w-0"><div class="border-token-border-light bg-token-bg-elevated-secondary corner-superellipse/1.1 rounded-3xl border my-4"><div class="pointer-events-none sticky z-40 shrink-0 mx-4 transition-opacity duration-300 opacity-0"><div class="sticky bg-token-border-light"></div></div><div class="relative z-0 flex max-w-full"><div id="b2a93627-99ab-4702-be44-5a8316517f0e:4:editor" class="Rx43rG_codemirror z-10 flex h-full w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼy"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell" aria-placeholder=""><div class="cm-line">streamlit run app.py</div></div></div></div></div></div></div></div></div></div></div></pre>

The app will open in your browser.

---

## 🧪 Example Output

<pre class="overflow-visible! px-0!" data-start="2035" data-end="2179"><div class="w-full"><div class=""><div class=""><div class="min-h-0 min-w-0"><div class="border-token-border-light bg-token-bg-elevated-secondary corner-superellipse/1.1 rounded-3xl border my-4"><div class="pointer-events-none sticky z-40 shrink-0 mx-4 transition-opacity duration-300 opacity-0"><div class="sticky bg-token-border-light"></div></div><div class="relative z-0 flex max-w-full"><div id="b2a93627-99ab-4702-be44-5a8316517f0e:5:editor" class="Rx43rG_codemirror z-10 flex h-full w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼy"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="json" aria-placeholder=""><div class="cm-line"><span class="cm-matchingBracket">{</span></div><div class="cm-line">  <span class="ͼj">"answer"</span>: <span class="ͼm">"Deep Learning frameworks are software libraries used to build and train neural networks..."</span>,</div><div class="cm-line">  <span class="ͼj">"confidence"</span>: <span class="ͼm">"high"</span></div><div class="cm-line"><span class="cm-matchingBracket">}</span></div></div></div></div></div></div></div></div></div></div></div></pre>

---

## 📌 Notes

* The chatbot  **does not store chat history** .
* Each question is processed independently.
* Designed for **learning and experimentation** with LangChain and structured LLM outputs.

---

## 📈 Possible Extensions

* Add conversation memory
* Enable streaming responses
* Add multiple domains
* Save chat history in a database
* Deploy using Docker or Streamlit Cloud

---

## 📜 License

MIT License

For educational purposes and personal use.

Copyright (c) 2026 Ahmed Akram Amer | The Triple AI

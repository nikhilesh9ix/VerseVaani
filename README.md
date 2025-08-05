# 📜 VerseVaani – Sanskrit Shloka Explainer (Multilingual AI Assistant)

**VerseVaani** is an open-source AI assistant that explains Sanskrit shlokas in a poetic, respectful, and spiritually rich way. It uses an open large language model (LLM) via OpenRouter to interpret and break down any Sanskrit verse.

🧘 Ideal for:  
- Students learning Sanskrit  
- Spiritual seekers  
- Indian language enthusiasts

---

## ✨ Features

- 🔤 Input any Sanskrit verse (e.g. from Gita or Vedas)
- 💬 Get an English poetic translation
- 🔍 Word-by-word meaning
- 🧠 Cultural/spiritual interpretation
- 🌐 Multilingual-ready: English (✅), Hindi & Telugu (coming soon)
- 🚀 Hosted on Hugging Face Spaces (Streamlit)

---

## 🔗 Try It Live

👉 https://huggingface.co/spaces/Nikhilesh9ix/VerseVaani

---

## 🛠️ Tech Stack

| Component     | Tech                                |
|---------------|--------------------------------------|
| Model         | mistralai/mistral-7b-instruct-v0.3  |
| API Provider  | [OpenRouter.ai](https://openrouter.ai) |
| UI Framework  | Streamlit (chat-based interface)    |
| Hosting       | Hugging Face Spaces                 |
| Secrets       | Hugging Face Environment Variables  |

---

## 🧠 How It Works

- Uses a carefully crafted **system prompt** to act as a devotional, Sanskrit-savvy assistant.
- On every message:
  - Sends current chat history and prompt to OpenRouter API.
  - Displays formatted response in the chat UI.

---

## ▶️ Example Input

योगः कर्मसु कौशलम्


### Output
- **Translation**: “Yoga is skill in action.”
- **Word-by-word**:
  - योगः = yoga / discipline
  - कर्मसु = in actions
  - कौशलम् = excellence / skill
- **Explanation**: This verse from the Bhagavad Gita teaches that acting with awareness, without attachment to outcomes, is true spiritual discipline.

---

## 🛡️ API Key Management

- The app uses a secure environment variable `OPENROUTER_API_KEY`
- To run this Space, go to **Settings → Secrets** and add:
  - **Name:** `OPENROUTER_API_KEY`
  - **Value:** your OpenRouter API key (e.g. `sk-or-...`)

---

## 🛤 Roadmap

- [x] Deploy core functionality with English responses
- [ ] Add dropdown for Hindi and Telugu output
- [ ] Add voice (text-to-speech) option
- [ ] Integrate Bhagavad Gita lookup (RAG)

---

## 📣 Feedback & Contribution

- 🧪 Try the app and submit your favorite shlokas
- 🗳 Leave feedback via Google Form (coming soon)
- 🧑‍💻 Pull requests welcome! Prompt tuning, UI, language support, etc.

---

## 🪪 License

- **Code:** GNU AFFERO GENERAL PUBLIC LICENSE
- **Model:** Hosted via OpenRouter (open-access)

---

🙏 *VerseVaani brings ancient Sanskrit wisdom to the modern world using respectful AI interpretation.*

# 📜 VerseVaani – Interpreting Sanskrit Wisdom Through AI

## 1. Why We Built It

While studying shlokas in our curriculum and spiritual practices, we realized how often their beauty is lost in rigid word-by-word translations. VerseVaani was created to solve this exact gap: to bring clarity, poetry, and spiritual meaning back into Sanskrit interpretation—while keeping it simple and accessible.

This project is personal for us. Whether it’s helping someone understand a Bhagavad Gita verse, or a parent revisiting prayers from their childhood, we wanted to build something that explains not just the meaning—but the feeling behind Sanskrit.

---

## 2. What VerseVaani Does

Paste in any Sanskrit verse—whether from scripture, class notes, or a devotional—and VerseVaani:

* Translates it into **poetic English**
* Breaks down each word and its **individual meaning**
* Explains the **spiritual and cultural context**

Currently, it responds in English, but we’re actively developing support for **Hindi** and **Telugu** so the tool can speak to users in the languages closest to their hearts.

---

## 3. The Heart of the System Prompt

To shape the assistant’s personality, we wrote a system prompt that mimics the style of a **humble Sanskrit teacher**—respectful, wise, and thoughtful.

### English Prompt

```
You are ShlokaSevak, a wise and devotional assistant who explains Sanskrit shlokas in English.

For each Sanskrit verse:
1. Provide a poetic and clear English translation.
2. Break down the verse word-by-word with meanings.
3. Explain the deeper spiritual or cultural context.

Respond respectfully, and ask for clarification if the input is unclear.
```

We went through multiple revisions. Early prompts were too literal—lacking warmth or poetry. After feedback and testing, we tuned it to feel more human, more like a teacher, less like a chatbot.

---

## 4. Lessons From Real Users

To avoid building in a vacuum, we shared VerseVaani early with a small group—friends, family, and peers who understood Sanskrit or were spiritually inclined. Here are 3 voices that shaped the direction:

### 🔹 Feedback Snapshot:

**📖 User 1 – English-Sanskrit Student**

* “I’ve heard this verse a hundred times but never really *understood* it. This explanation made it personal. It made sense.”

**🪔 User 2 – Hindi Speaker testing with family**

* “My mom couldn’t follow the English easily. If the bot could respond in Hindi, she'd use it every day.”

**🎓 User 3 – Telugu Learner**

* “I loved how the meanings were simple. I showed it to my teacher. She asked for a Telugu version!”

### 💡 Key Takeaways:

1. Add multilingual support with properly tuned prompts
2. Users appreciate *poetic tone* more than literal accuracy
3. Audio output (TTS) is a frequent feature request

---

## 5. Roadmap (What’s Next)

To keep things lean but ambitious, we split our roadmap into three stages:

### 🛠️ Setup Stage (Week 1)

* Add multilingual dropdown (EN active, HI & TE placeholders)
* Connect OpenRouter API securely with Hugging Face Secrets
* Begin structured user feedback collection

### 🚧 Growth Stage (Weeks 2–4)

* Enable **Text-to-Speech** for pronunciation and accessibility
* Integrate **RAG** to detect if input is from Gita/Vedas
* Start prompt testing for **Hindi and Telugu** replies
* Outreach to college Sanskrit clubs

### 🚀 Launch-Ready Stage (Month 2–3)

* Launch mobile-optimized version
* Detect scripture source & verse number
* Collaborate with teachers to tune tone
* Explore offline version for rural users

---

## 6. How We'll Grow It

We’re a small team, but we want VerseVaani to reach real users. Here’s how:

### 👥 Outreach

* Reddit (r/Sanskrit, r/Hinduism)
* WhatsApp/Telegram spiritual groups
* Devpost & GitHub showcase

### 🎯 Who It’s For

* Students studying Sanskrit
* Elderly who remember verses but seek clarity
* Gita readers & bhajan listeners who want depth

### 💬 Feedback Loop

* Embedded Google Form in UI
* Reach out to professors for suggestions
* Enable GitHub Discussions for open feedback

---

## 7. Stack + Deployment

* **LLM:** mistralai/mistral-7b-instruct-v0.3 via OpenRouter
* **Frontend:** Streamlit (chat interface)
* **API Integration:** Python + `requests`
* **Hosting:** Hugging Face Spaces
* **Secrets:** Hugging Face Secrets tab for API key

🔗 **Live App:** [https://huggingface.co/spaces/Nikhilesh9ix/VerseVaani](https://huggingface.co/spaces/Nikhilesh9ix/VerseVaani)

---

## 8. License

* Code: MIT
* Model: Open access via OpenRouter (Mistral-7B)

---

🙏 *To us, VerseVaani is more than a tool — it's a digital prayer. A way to carry the soul of Sanskrit into the future, one verse at a time.*
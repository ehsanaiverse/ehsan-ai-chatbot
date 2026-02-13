# 🤖 Ehsan AI ChatBot

> A sleek, modern AI-powered chatbot built with Streamlit and LangChain, featuring a beautiful glassmorphism UI and powered by Groq's lightning-fast LLM API.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.30+-red.svg)
![LangChain](https://img.shields.io/badge/langchain-0.1+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 💬 **Real-time Chat Interface** - Smooth, responsive conversation experience with streaming responses
- 🎨 **Modern Glassmorphism UI** - Beautiful dark theme with gradient accents
- 🤖 **Multiple AI Models** - Choose between Llama 3.1 8B (fast) and Llama 3.3 70B (smart)
- ⚙️ **Customizable Settings** - Adjust temperature and AI personality on the fly
- 💾 **Export Conversations** - Download your chat history as JSON
- 🎯 **Clean Code Architecture** - Well-organized, modular, and maintainable
- ⚡ **Streaming Responses** - See AI responses appear in real-time

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one free here](https://console.groq.com/keys))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ehsanaiverse/ehsan-ai-chatbot.git
cd ehsan-ai-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
cp .env.example .env

# Edit .env and add your API key
# GROQ_API_KEY=gsk_your_actual_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

The chatbot will open automatically in your browser at `http://localhost:8501`

## 📦 Dependencies

Create a `requirements.txt` file with:

```txt
streamlit>=1.30.0
langchain-groq>=0.1.0
langchain-core>=0.1.0
python-dotenv>=1.0.0
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

### Customization

You can customize the chatbot by editing the configuration constants in `app.py`:

```python
# Theme Colors
THEME_COLORS = {
    "primary": "#4F46E5",      # Primary gradient color
    "secondary": "#818CF8",     # Secondary gradient color
    "background": "#0F172A",    # Background color
    "text": "#F8FAFC"          # Text color
}

# Available Models
MODELS = {
    'llama-3.1-8b-instant': 'Llama 3.1 8B (Fast)',
    'llama-3.3-70b-versatile': 'Llama 3.3 70B (Smart)'
}
```

## 📖 Usage Guide

### Getting Started

1. **Launch the application** using `streamlit run app.py`
2. **Select your model** from the sidebar:
   - **Llama 3.1 8B** - Fast responses, great for quick questions
   - **Llama 3.3 70B** - More intelligent, better for complex tasks

3. **Adjust creativity** using the temperature slider:
   - **0.0-0.3** - Focused and deterministic
   - **0.4-0.7** - Balanced (recommended)
   - **0.8-1.0** - Creative and varied

4. **Customize AI personality** in the "Persona" section
5. **Start chatting!**

### Features Overview

#### Model Selection
- **Llama 3.1 8B (Fast)** - Optimized for speed, perfect for:
  - Quick questions
  - Code snippets
  - Simple tasks
  
- **Llama 3.3 70B (Smart)** - More powerful, ideal for:
  - Complex reasoning
  - Detailed explanations
  - Creative writing
  - In-depth analysis

#### Temperature Control
Controls the randomness of AI responses:
- **Low (0.0-0.3)** - Precise, focused, factual
- **Medium (0.4-0.7)** - Balanced creativity and accuracy
- **High (0.8-1.0)** - More creative and varied responses

#### System Prompt
Customize the AI's personality and behavior:
- Professional assistant
- Creative writer
- Code expert
- Research helper
- Or create your own!

#### Export Chat
- Click **Export** to save your conversation
- Downloads as JSON with timestamp
- Easy to import or analyze later

## 🎨 UI Features

### Modern Design
- **Glassmorphism effects** - Translucent elements with blur
- **Gradient accents** - Beautiful purple-to-indigo gradients
- **Dark theme** - Easy on the eyes for long sessions
- **Smooth animations** - Polished hover and transition effects

### Chat Interface
- **User messages** - Displayed with gradient background on the right
- **AI responses** - Shown with glassmorphic cards on the left
- **Avatars** - User (👤) and AI (🤖) icons for clarity
- **Streaming** - Watch responses appear in real-time

### Sidebar
- **Compact settings** - All controls in one place
- **Quick actions** - Clear and Export buttons
- **Live configuration** - Changes apply immediately

## 🏗️ Project Structure

```
ehsan-ai-chatbot/
├── chatbot_app.py           # Main application file
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── .env                   # Your API keys (create this)
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## 🔐 Security Best Practices

1. **Never commit your `.env` file** - Add it to `.gitignore`
2. **Keep your API key private** - Don't share or expose it
3. **Rotate keys regularly** - Update API keys every few months
4. **Use environment variables** - Never hardcode sensitive data

Add to your `.gitignore`:
```
.env
__pycache__/
*.pyc
.streamlit/
```

## 🐛 Troubleshooting

### Common Issues

**Problem: "API Key not found"**
```bash
# Solution: Make sure .env file exists with your API key
echo "GROQ_API_KEY=gsk_your_key_here" > .env
```

**Problem: Module not found errors**
```bash
# Solution: Install all dependencies
pip install -r requirements.txt
```

**Problem: Port already in use**
```bash
# Solution: Use a different port
streamlit run app.py --server.port 8502
```

**Problem: Slow responses**
- Try the faster model: Llama 3.1 8B
- Check your internet connection
- Verify API key is valid

### Getting Help

If you encounter issues:
1. Check the [Groq Documentation](https://console.groq.com/docs)
2. Review [Streamlit Documentation](https://docs.streamlit.io/)
3. Open an issue on GitHub

## 📊 Performance

- **Response Time**: 1-3 seconds (model dependent)
- **Memory Usage**: ~200-300 MB
- **Streaming**: Real-time token generation
- **API Calls**: Efficient conversation management

## 🛠️ Advanced Usage

### Custom Models

Add more models by editing the `MODELS` dictionary:

```python
MODELS = {
    'llama-3.1-8b-instant': 'Llama 3.1 8B (Fast)',
    'llama-3.3-70b-versatile': 'Llama 3.3 70B (Smart)',
    'mixtral-8x7b-32768': 'Mixtral 8x7B (Versatile)',
    # Add your model here
}
```

### Modify System Prompt

Change the default AI behavior:

```python
if 'system_prompt' not in st.session_state:
    st.session_state.system_prompt = "Your custom instructions here"
```

### Styling Customization

Edit the `load_css()` function to change colors, fonts, and layout.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- [ ] Add more AI models
- [ ] Implement conversation search
- [ ] Add voice input/output
- [ ] Create different UI themes
- [ ] Add image generation capability
- [ ] Implement user authentication
- [ ] Add conversation analytics

## 📝 Code Overview

### Main Components

**SessionState** - Manages application state
```python
class SessionState:
    @staticmethod
    def initialize():
        # Initializes chat history, model settings, etc.
```

**ChatBot** - Handles LLM interactions
```python
class ChatBot:
    def get_llm(self):
        # Returns configured ChatGroq instance
```

**render_sidebar()** - Creates settings panel
- Model selection
- Temperature control
- System prompt editor
- Clear/Export actions

**render_chat_interface()** - Main chat UI
- Displays message history
- Handles user input
- Streams AI responses

## 🌟 Features in Detail

### Real-time Streaming
Responses appear token-by-token for better UX:
```python
stream = llm.stream(messages)
response = st.write_stream(stream)
```

### Conversation Management
Chat history is maintained with proper message types:
```python
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=user_input),
    AIMessage(content=ai_response)
]
```

### Export Functionality
Save conversations as structured JSON:
```json
[
  {
    "role": "user",
    "content": "Hello!"
  },
  {
    "role": "assistant", 
    "content": "Hi! How can I help?"
  }
]
```

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 Ehsan Ullah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Groq** - For providing ultra-fast LLM inference
- **LangChain** - For the excellent conversation framework
- **Streamlit** - For making beautiful web apps easy
- **Meta AI** - For the Llama models

## 📞 Contact & Support

- **Author**: Ehsan Ullah
- **GitHub**: [@ehsanaiverse](https://github.com/ehsanaiverse)
- **Issues**: [GitHub Issues](https://github.com/ehsanaiverse/ehsan-ai-chatbot/issues)

## 🗺️ Roadmap

- [x] Basic chat interface
- [x] Multiple model support
- [x] Streaming responses
- [x] Export conversations
- [ ] Conversation search
- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Image generation
- [ ] Document analysis
- [ ] API endpoint

---

<div align="center">

**Made with ❤️ by Ehsan Ullah**

*Star ⭐ this repository if you find it helpful!*

[Report Bug](https://github.com/ehsanaiverse/ehsan-ai-chatbot/issues) · [Request Feature](https://github.com/ehsanaiverse/ehsan-ai-chatbot/issues)

</div>
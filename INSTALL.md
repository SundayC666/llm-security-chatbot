# Security Chatbot - Installation Instructions

## Quick Installation (Windows 11)

### 1. Extract the Project
```bash
# Extract the downloaded file
tar -xzf security_chatbot.tar.gz
cd security_chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
copy .env.example .env
# Edit .env with your API key or Ollama settings
```

### 5. Run the Application
```bash
streamlit run app.py
```

## Detailed Instructions
See the following files for more information:
- `快速開始指南_中文.md` - Complete Chinese guide
- `README.md` - Full English documentation
- `PRESENTATION_GUIDE.md` - Presentation preparation guide

## Quick Start with Ollama (Free)
1. Install Ollama from https://ollama.ai
2. Run: `ollama pull llama2`
3. Run: `ollama serve` (keep running)
4. In .env: Set `USE_OLLAMA=true`
5. Run: `streamlit run app.py`

## Quick Start with OpenAI
1. Get API key from https://platform.openai.com/api-keys
2. In .env: Set `OPENAI_API_KEY=sk-your-key-here`
3. Run: `streamlit run app.py`

## Testing
```bash
python test_chatbot.py
```

## Support
If you encounter issues, check the troubleshooting section in:
- `快速開始指南_中文.md` (Chinese)
- `README.md` (English)

# Security Chatbot - File List and Description

## 📁 Complete File Structure

```
security_chatbot/
├── Core Application Files
│   ├── app.py                      # Main Streamlit web interface
│   ├── chatbot.py                  # Chatbot logic and LLM integration
│   ├── rag_pipeline.py             # RAG implementation with FAISS
│   └── cve_collector.py            # CVE data collection from NIST NVD
│
├── Configuration Files
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Environment variables template
│   └── .env                        # Your configuration (create this)
│
├── Documentation (English)
│   ├── README.md                   # Complete project documentation
│   ├── INSTALL.md                  # Quick installation guide
│   ├── PRESENTATION_GUIDE.md       # 15-minute presentation structure
│   ├── ARCHITECTURE.md             # System architecture diagrams
│   └── FILE_LIST.md                # This file
│
├── Documentation (Chinese)
│   ├── 快速開始指南_中文.md          # Quick start guide in Chinese
│   └── 專案總結_中文.md              # Project summary in Chinese
│
├── Testing
│   └── test_chatbot.py             # Comprehensive test suite
│
└── Data Directories (created at runtime)
    ├── data/
    │   └── cve_data.json           # Fetched CVE records
    └── vector_store/
        ├── faiss_index.bin         # FAISS vector index
        └── documents.pkl           # Document metadata
```

## 📄 File Descriptions

### Core Application Files

#### `app.py` (Streamlit Web Interface)
- **Purpose**: Main user interface
- **Features**:
  - Chat interface
  - LLM configuration (OpenAI/Ollama)
  - Knowledge base management
  - Conversation history
  - Real-time updates
- **Entry Point**: Run with `streamlit run app.py`

#### `chatbot.py` (Chatbot Logic)
- **Purpose**: Core chatbot implementation
- **Components**:
  - LLMInterface: Handles OpenAI and Ollama
  - SecurityChatbot: Main chatbot class
  - create_chatbot(): Initialization function
- **Key Functions**:
  - chat(): Process queries and generate responses
  - _build_prompt(): Create LLM prompts with context
  - _extract_sources(): Extract CVE citations

#### `rag_pipeline.py` (RAG Implementation)
- **Purpose**: Retrieval-Augmented Generation pipeline
- **Components**:
  - SecurityRAGPipeline: Main RAG class
  - create_sample_infrastructure(): Sample data
- **Key Functions**:
  - build_knowledge_base(): Create vector store
  - retrieve(): Search for relevant documents
  - save_index() / load_index(): Persistence
  - add_custom_document(): Add new documents

#### `cve_collector.py` (CVE Data Collection)
- **Purpose**: Fetch and parse CVE data from NIST NVD
- **Features**:
  - Automatic rate limiting
  - API key support
  - Data parsing and formatting
- **Key Functions**:
  - fetch_recent_cves(): Get CVEs from last N days
  - fetch_specific_cve(): Get specific CVE by ID
  - save_to_file() / load_from_file(): Data persistence

### Configuration Files

#### `requirements.txt`
- **Purpose**: Python package dependencies
- **Key Packages**:
  - streamlit: Web interface
  - langchain: LLM framework
  - sentence-transformers: Embeddings
  - faiss-cpu: Vector search
  - openai: OpenAI API
  - requests: HTTP requests

#### `.env.example`
- **Purpose**: Template for environment variables
- **Variables**:
  - OPENAI_API_KEY: OpenAI API key
  - USE_OLLAMA: Enable Ollama (true/false)
  - OLLAMA_MODEL: Ollama model name
  - NVD_API_KEY: NIST NVD API key (optional)

### Documentation Files

#### `README.md` (English)
- **Contents**:
  - Project overview
  - Installation instructions
  - Usage guide
  - Architecture details
  - Troubleshooting
  - ~300 lines

#### `INSTALL.md`
- **Contents**:
  - Quick installation steps
  - Platform-specific instructions
  - Common issues
  - ~50 lines

#### `PRESENTATION_GUIDE.md`
- **Contents**:
  - 15-minute presentation structure
  - Slide-by-slide content
  - Demo preparation
  - Q&A preparation
  - ~400 lines

#### `ARCHITECTURE.md`
- **Contents**:
  - System architecture diagrams
  - Data flow diagrams
  - Component interactions
  - ASCII art visualizations
  - ~200 lines

#### `快速開始指南_中文.md` (Chinese Quick Start)
- **Contents**:
  - 安裝步驟（中文）
  - 設定說明
  - 使用方法
  - 問題排除
  - ~300 行

#### `專案總結_中文.md` (Chinese Project Summary)
- **Contents**:
  - 專案完成清單
  - 技術規格
  - 效能指標
  - 成果總結
  - ~200 行

### Testing Files

#### `test_chatbot.py`
- **Purpose**: Comprehensive testing suite
- **Tests**:
  1. CVE data collection
  2. RAG pipeline functionality
  3. LLM integration
  4. End-to-end chatbot
  5. Evaluation metrics
- **Usage**: `python test_chatbot.py`

## 📊 File Statistics

| Category | Files | Lines of Code | Size |
|----------|-------|---------------|------|
| Core Python | 4 | ~1,500 | ~50 KB |
| Documentation | 7 | ~2,000 | ~100 KB |
| Configuration | 2 | ~50 | ~2 KB |
| Tests | 1 | ~400 | ~15 KB |
| **Total** | **14** | **~3,950** | **~167 KB** |

## 🔍 File Dependencies

### Import Chain
```
app.py
  ├─→ chatbot.py
  │   ├─→ rag_pipeline.py
  │   │   ├─→ sentence_transformers
  │   │   ├─→ faiss
  │   │   └─→ langchain
  │   ├─→ cve_collector.py
  │   │   └─→ requests
  │   └─→ openai
  └─→ streamlit

test_chatbot.py
  ├─→ cve_collector.py
  ├─→ rag_pipeline.py
  └─→ chatbot.py
```

## 📝 Usage Priority

### Must Read First
1. `README.md` or `快速開始指南_中文.md`
2. `INSTALL.md`
3. `.env.example` → Create `.env`

### For Development
1. `chatbot.py` - Understand core logic
2. `rag_pipeline.py` - Understand RAG
3. `cve_collector.py` - Understand data collection

### For Presentation
1. `PRESENTATION_GUIDE.md`
2. `ARCHITECTURE.md`
3. `專案總結_中文.md`

### For Testing
1. `test_chatbot.py`

## 🎯 File Usage Scenarios

### Scenario 1: First-Time Setup
```
1. Read: README.md or 快速開始指南_中文.md
2. Create: .env (from .env.example)
3. Run: pip install -r requirements.txt
4. Run: streamlit run app.py
```

### Scenario 2: Development
```
1. Modify: chatbot.py, rag_pipeline.py, or cve_collector.py
2. Test: python test_chatbot.py
3. Run: streamlit run app.py
```

### Scenario 3: Presentation Preparation
```
1. Read: PRESENTATION_GUIDE.md
2. Review: ARCHITECTURE.md
3. Practice: Demo with app.py
4. Prepare: Screenshots and examples
```

### Scenario 4: Troubleshooting
```
1. Check: README.md troubleshooting section
2. Check: 快速開始指南_中文.md 常見問題
3. Run: python test_chatbot.py
4. Review: Error logs
```

## 🔧 Modifying Files

### To Change LLM Provider
- **File**: `chatbot.py`
- **Section**: `LLMInterface` class
- **What**: Add new provider in generate_response()

### To Add Data Source
- **File**: `cve_collector.py`
- **Section**: Create new collector class
- **Also**: Update `rag_pipeline.py` to use it

### To Customize UI
- **File**: `app.py`
- **Section**: Streamlit components
- **What**: Modify layout, add features

### To Change Embedding Model
- **File**: `rag_pipeline.py`
- **Section**: `__init__` in SecurityRAGPipeline
- **What**: Change model name

### To Add Infrastructure
- **File**: `rag_pipeline.py`
- **Function**: `create_sample_infrastructure()`
- **What**: Add your server details

## 🎓 Learning Path

### Beginner (Understand Usage)
1. `README.md` or `快速開始指南_中文.md`
2. `INSTALL.md`
3. Run `streamlit run app.py`

### Intermediate (Understand Implementation)
1. `ARCHITECTURE.md`
2. `chatbot.py` - Main logic
3. `rag_pipeline.py` - RAG implementation
4. `cve_collector.py` - Data collection

### Advanced (Modify and Extend)
1. All Python files
2. `test_chatbot.py` - Testing patterns
3. Experiment with modifications
4. Add new features

## 📦 Distribution

### What to Share
- All files in the project
- Pre-built vector store (optional)
- Sample CVE data (optional)

### What NOT to Share
- `.env` file (contains API keys)
- `data/` directory (can be regenerated)
- `vector_store/` directory (can be regenerated)
- `__pycache__/` directories

## 🔒 Security Notes

### Sensitive Files
- `.env` - Contains API keys, never commit
- API keys in code - Never hardcode

### Safe to Share
- All `.py` files
- All `.md` files
- `.env.example` (no actual keys)
- `requirements.txt`

## ✅ Checklist Before Submission

- [ ] All Python files present
- [ ] All documentation files present
- [ ] `requirements.txt` complete
- [ ] `.env.example` provided
- [ ] Test script works
- [ ] README is clear
- [ ] Chinese guide is complete
- [ ] Presentation guide ready
- [ ] No API keys in code
- [ ] No sensitive data included

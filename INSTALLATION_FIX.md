# 安裝問題修正指南 / Installation Fix Guide

## ⚠️ Python 3.13.7 套件版本問題

如果你在安裝時遇到 `faiss-cpu==1.7.4` 的錯誤，這是因為舊版本不支援 Python 3.13。

### 解決方案 1: 使用更新的 requirements.txt（推薦）

專案中的 `requirements.txt` 已經更新為相容版本。直接執行：

```bash
pip install -r requirements.txt
```

### 解決方案 2: 手動安裝正確版本

```bash
# 安裝相容的套件版本
pip install streamlit>=1.31.0
pip install langchain>=0.1.0
pip install langchain-community>=0.0.20
pip install langchain-openai>=0.0.5
pip install openai>=1.12.0
pip install faiss-cpu>=1.9.0
pip install sentence-transformers>=2.3.0
pip install requests>=2.31.0
pip install python-dotenv>=1.0.0
pip install pandas>=2.0.0
pip install numpy>=1.24.0
pip install tiktoken>=0.6.0
```

### 解決方案 3: 使用 Python 3.11 或 3.12（如果問題持續）

如果 Python 3.13 仍有問題，建議降級到 Python 3.11 或 3.12：

**選項 A: 使用 Python 3.11**
```bash
# 下載並安裝 Python 3.11
# https://www.python.org/downloads/

# 使用 Python 3.11 建立虛擬環境
python3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**選項 B: 使用 Python 3.12**
```bash
# 使用 Python 3.12
python3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🔧 常見套件安裝問題

### 問題 1: NumPy 版本衝突
```
ERROR: Could not find a version that satisfies the requirement numpy==1.26.4
```

**解決方法：**
```bash
pip install numpy>=1.24.0
```

### 問題 2: LangChain 模組結構問題
```
❌ LangChain text splitter failed: No module named 'langchain.text_splitter'
```

**解決方法：**
```bash
# Install additional langchain packages
pip install langchain-text-splitters langchain-core
```

The code has been updated to handle both old and new langchain structures automatically.

### 問題 3: sentence-transformers 依賴問題
```
ERROR: Failed building wheel for sentence-transformers
```

**解決方法：**
```bash
# 先安裝依賴
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install sentence-transformers
```

### 問題 4: faiss-cpu 安裝失敗
```
ERROR: No matching distribution found for faiss-cpu
```

**解決方法 A（推薦）：**
```bash
pip install faiss-cpu
```

**解決方法 B（如果 A 失敗）：**
```bash
# 使用 conda 安裝（如果你有 conda）
conda install -c conda-forge faiss-cpu
```

### 問題 5: Microsoft Visual C++ 錯誤（Windows）
```
error: Microsoft Visual C++ 14.0 or greater is required
```

**解決方法：**
1. 下載並安裝 Microsoft C++ Build Tools
2. 網址：https://visualstudio.microsoft.com/visual-cpp-build-tools/
3. 選擇「Desktop development with C++」
4. 安裝後重新執行 `pip install -r requirements.txt`

## ✅ 驗證安裝

執行以下命令確認所有套件都正確安裝：

```python
# test_imports.py
try:
    import streamlit
    print("✅ streamlit:", streamlit.__version__)
except ImportError as e:
    print("❌ streamlit:", e)

try:
    import langchain
    print("✅ langchain:", langchain.__version__)
except ImportError as e:
    print("❌ langchain:", e)

try:
    import faiss
    print("✅ faiss-cpu: installed")
except ImportError as e:
    print("❌ faiss-cpu:", e)

try:
    from sentence_transformers import SentenceTransformer
    print("✅ sentence-transformers: installed")
except ImportError as e:
    print("❌ sentence-transformers:", e)

try:
    import openai
    print("✅ openai:", openai.__version__)
except ImportError as e:
    print("❌ openai:", e)

print("\n如果所有套件都顯示 ✅，表示安裝成功！")
```

執行驗證：
```bash
python test_imports.py
```

## 🚀 最簡安裝流程（Windows 11）

**步驟 1: 確認 Python 版本**
```bash
python --version
# 應該顯示 Python 3.11.x, 3.12.x 或 3.13.x
```

**步驟 2: 建立乾淨的虛擬環境**
```bash
# 如果之前安裝失敗，先刪除舊的虛擬環境
rmdir /s venv

# 建立新的虛擬環境
python -m venv venv

# 啟動虛擬環境
venv\Scripts\activate
```

**步驟 3: 更新 pip**
```bash
python -m pip install --upgrade pip
```

**步驟 4: 安裝套件（使用更新的 requirements.txt）**
```bash
pip install -r requirements.txt
```

**步驟 5: 驗證安裝**
```bash
python test_chatbot.py
```

## 📦 替代安裝方法：使用 Conda

如果 pip 安裝一直有問題，可以使用 Conda：

```bash
# 安裝 Miniconda（如果還沒有）
# https://docs.conda.io/en/latest/miniconda.html

# 建立 conda 環境
conda create -n security_chatbot python=3.11
conda activate security_chatbot

# 安裝套件
conda install -c conda-forge faiss-cpu
pip install streamlit langchain langchain-community langchain-openai
pip install sentence-transformers openai python-dotenv requests pandas numpy tiktoken
```

## 🔍 檢查套件版本相容性

```bash
# 列出已安裝的套件
pip list

# 檢查特定套件
pip show faiss-cpu
pip show numpy
pip show streamlit
```

## 💡 最小安裝（如果完整安裝失敗）

如果你只想先測試基本功能，可以只安裝核心套件：

```bash
# 核心套件
pip install streamlit
pip install openai
pip install requests
pip install python-dotenv

# 然後逐一測試添加其他套件
pip install langchain
pip install sentence-transformers
pip install faiss-cpu
```

## 📞 仍有問題？

1. **檢查 Python 版本**：確保是 3.11、3.12 或 3.13
2. **更新 pip**：`python -m pip install --upgrade pip`
3. **清除快取**：`pip cache purge`
4. **使用虛擬環境**：避免全域安裝衝突
5. **查看錯誤訊息**：複製完整的錯誤訊息查詢解決方案

## ✨ 成功安裝的標誌

安裝成功後，你應該能夠：

```bash
# 1. 執行測試
python test_chatbot.py

# 2. 啟動應用
streamlit run app.py

# 3. 導入模組不會報錯
python -c "import faiss; import streamlit; import langchain; print('All good!')"
```

## 📝 更新日誌

- **2025-10-22**: 更新 requirements.txt 以支援 Python 3.13
- 主要更改：faiss-cpu 從 1.7.4 → >=1.9.0
- 所有套件改用 >= 而非 == 以提高相容性

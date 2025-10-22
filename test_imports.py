"""
Test Script to Verify All Required Packages are Installed
Run this after installing requirements.txt
"""

import sys

print("="*70)
print("  Security Chatbot - Package Installation Test")
print("="*70)
print()

# Track success
all_good = True

# Test Python version
print(f"Python Version: {sys.version}")
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 11:
    print("✅ Python version is compatible (3.11+)")
else:
    print("⚠️  Python version might have compatibility issues")
    print("   Recommended: Python 3.11, 3.12, or 3.13")
print()

# Test core packages
packages_to_test = [
    ("streamlit", "Streamlit"),
    ("langchain", "LangChain"),
    ("langchain_community", "LangChain Community"),
    ("langchain_openai", "LangChain OpenAI"),
    ("openai", "OpenAI"),
    ("faiss", "FAISS (faiss-cpu)"),
    ("sentence_transformers", "Sentence Transformers"),
    ("requests", "Requests"),
    ("dotenv", "Python Dotenv"),
    ("pandas", "Pandas"),
    ("numpy", "NumPy"),
    ("tiktoken", "Tiktoken"),
]

print("Testing Package Imports:")
print("-" * 70)

for module_name, display_name in packages_to_test:
    try:
        module = __import__(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"✅ {display_name:.<45} v{version}")
    except ImportError as e:
        print(f"❌ {display_name:.<45} NOT INSTALLED")
        print(f"   Error: {e}")
        all_good = False

print()
print("="*70)

# Test specific functionality
print("Testing Key Functionality:")
print("-" * 70)

# Test SentenceTransformer
try:
    from sentence_transformers import SentenceTransformer
    print("✅ SentenceTransformer class available")
except Exception as e:
    print(f"❌ SentenceTransformer import failed: {e}")
    all_good = False

# Test FAISS
try:
    import faiss
    # Try to create a simple index
    index = faiss.IndexFlatL2(128)
    print("✅ FAISS can create index")
except Exception as e:
    print(f"❌ FAISS functionality test failed: {e}")
    all_good = False

# Test OpenAI client
try:
    from openai import OpenAI
    print("✅ OpenAI client available")
except Exception as e:
    print(f"❌ OpenAI client import failed: {e}")
    all_good = False

# Test LangChain text splitter
try:
    try:
        from langchain.text_splitter import RecursiveCharacterTextSplitter
    except ImportError:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("✅ LangChain text splitter available")
except Exception as e:
    print(f"❌ LangChain text splitter failed: {e}")
    all_good = False

# Test Streamlit
try:
    import streamlit as st
    print("✅ Streamlit module available")
except Exception as e:
    print(f"❌ Streamlit import failed: {e}")
    all_good = False

print()
print("="*70)

# Final result
if all_good:
    print("🎉 SUCCESS! All packages are installed correctly!")
    print()
    print("You can now run:")
    print("  - python test_chatbot.py      (Run tests)")
    print("  - streamlit run app.py        (Start the application)")
else:
    print("⚠️  WARNING: Some packages are missing or have issues.")
    print()
    print("Please install missing packages:")
    print("  pip install -r requirements.txt")
    print()
    print("If you continue to have issues, see INSTALLATION_FIX.md")

print("="*70)

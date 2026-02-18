import sys
import os

# Ensure the project root is in sys.path
sys.path.append(os.getcwd())

from backend.main_engine import rag_system

print("Testing RAG System...")
try:
    response = rag_system.process_query("demo_user", "Public", "What is PSLV?")
    print(f"Response: {response}")
except Exception as e:
    import traceback
    traceback.print_exc()

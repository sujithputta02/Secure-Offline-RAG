import os
import sys

# Add the project root to the python path
sys.path.append(os.getcwd())

from backend.validator import Validator

print("Initializing Validator...")
validator = Validator()

if validator.graph_store is None:
    print("SUCCESS: GraphStore is None (Validation disabled) as expected for offline mode.")
    
    # Test validate_answer returns safe default
    is_valid, msg = validator.validate_answer("test query", [])
    print(f"Validation Result: {is_valid}, Message: {msg}")
    
    if is_valid and "Skipped" in msg:
        print("SUCCESS: validation skipped correctly.")
    else:
        print("FAILURE: validation did not skip correctly.")

else:
    print("WARNING: GraphStore initialized successfully. Is Neo4j actually running?")

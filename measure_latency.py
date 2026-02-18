import time
import os
import sys

# Add the current directory to sys.path
sys.path.append(os.getcwd())

from backend.retriever import retrieve_context

def main():
    with open("latency_results_final.txt", "w", encoding="utf-8") as f:
        query = "What is the specific impulse of the engine?"
        
        f.write("--- Starting Latency Test ---\n")
        
        # Cold Start
        f.write("\n1. Cold Start (Loading Model & Index)...\n")
        start_time = time.time()
        results = retrieve_context(query)
        end_time = time.time()
        f.write(f"   Time taken: {end_time - start_time:.4f} seconds\n")
        f.write(f"   Results found: {len(results)}\n")
    
        # Warm Start
        f.write("\n2. Warm Start (Cached)...\n")
        latencies = []
        for i in range(5):
            start_time = time.time()
            results = retrieve_context(query)
            end_time = time.time()
            duration = end_time - start_time
            latencies.append(duration)
            f.write(f"   Run {i+1}: {duration:.4f} seconds\n")
    
        avg_latency = sum(latencies) / len(latencies)
        f.write(f"\nAverage Warm Latency: {avg_latency:.4f} seconds\n")
    
        if avg_latency < 0.1:
            f.write("\n[SUCCESS]: Caching is working! Response is instant.\n")
        else:
            f.write("\n[FAILURE]: Response is still slow.\n")

if __name__ == "__main__":
    main()

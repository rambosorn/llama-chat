from rag_pipeline import ask_techcorp_ai
import time

import sys

def run_test():
    with open("executive_report.md", "w", encoding="utf-8") as f:
        # Redirect stdout to file
        sys.stdout = f
        
        print("# 🎩 EXECUTIVE AGENT TEST REPORT\n")
        
        # 1. Level 3 Challenge (Cross-Department)
        q1 = "Does our monthly net profit cover the total budget for Project Pegasus?"
        print(f"## [TEST 1] Complex Query\n**Q:** '{q1}'\n")
        ask_techcorp_ai(q1)
        
        print("\n" + "="*50 + "\n")
        
        # 2. Level 1 Control (Specific)
        q2 = "List all sales transactions for Widget A"
        print(f"## [TEST 2] Specific Query\n**Q:** '{q2}'\n")
        ask_techcorp_ai(q2)
        
        sys.stdout = sys.__stdout__ # Reset

if __name__ == "__main__":
    run_test()

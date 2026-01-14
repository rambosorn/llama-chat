from rag_pipeline import ask_techcorp_ai
import sys

def run_test():
    # Capture output
    
    print("# 🧠 CONSULTATIVE REASONING TEST\n")
    
    # Test 1: Finance (Budget vs Spending)
    # Context: User asks about profit/budget.
    q1 = "Does our current profit cover the budget for Project Pegasus?"
    
    print(f"## [TEST 1] Complex Reasoning\n**Q:** '{q1}'\n")
    result = ask_techcorp_ai(q1)
    
    # We expect the output to have "Answer:", "Recommendation:", "Reasoning:" sections.
    # The function prints to stdout already, so we just run it.

if __name__ == "__main__":
    run_test()

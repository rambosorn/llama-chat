from rag_pipeline import ask_techcorp_ai
import sys

def run_test():
    with open("sales_report.md", "w", encoding="utf-8") as f:
        sys.stdout = f
        
        print("# 📊 SALES PERFORMANCE PROMPT TEST\n")
        
        # Test 1: Aggregation/Comparison (Logic)
        q1 = "Which region sold the most units of Widget B?"
        print(f"## [TEST 1] Comparison\n**Q:** '{q1}'\n")
        ask_techcorp_ai(q1)
        print("\n" + "="*50 + "\n")
        
        # Test 2: Revenue Summation (Math)
        # Note: LLMs are bad at math, but let's see if it can retrieve the right rows first.
        q2 = "What was the total revenue in February 2023?"
        print(f"## [TEST 2] Date Filtering & Sum\n**Q:** '{q2}'\n")
        ask_techcorp_ai(q2)
        print("\n" + "="*50 + "\n")

        # Test 3: Product Comparison
        q3 = "Compare the sales of Widget A and Widget C."
        print(f"## [TEST 3] Product Comparison\n**Q:** '{q3}'\n")
        ask_techcorp_ai(q3)
        
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    run_test()

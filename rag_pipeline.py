import ollama
from query_db import search_documents
import time

def classify_intent(question):
    """
    Decides which department handles the request.
    Returns: 'HR_Law', 'Sales_Marketing', 'Account_Finance', 'IT', 'Executive', or 'General'
    """
    print("🤔 ROUTER: Analyzing intent...")
    prompt = f"""
    You are the Receptionist Bot for a large Distribution & Retail Company.
    Classify the following USER QUESTION into one of these departments:
    
    - HR_Law: Policies, leave, contracts, legal compliance, code of conduct.
    - Sales_Marketing: Product prices, sales data, returns, promotions, customer service.
    - Account_Finance: Budgets, expenses, payments, financial reports, payroll.
    - IT: Technical projects, software help, access rights, logins, hardware.
    - Executive: Questions that require comparing data from TWO or more departments (e.g. "Profit vs Budget"), strategic analysis, or broad company overviews.
    
    If unsure, choose 'General'.
    
    Return ONLY the exact category name. Do not add punctuation or explanation.
    
    QUESTION: "{question}"
    CATEGORY:
    """
    try:
        response = ollama.chat(model="llama3.2", messages=[{'role': 'user', 'content': prompt}])
        category = response['message']['content'].strip()
        
        # Cleanup potential extra text
        valid_depts = ['HR_Law', 'Sales_Marketing', 'Account_Finance', 'IT', 'Executive', 'General']
        for dept in valid_depts:
            if dept in category:
                return dept
                
        return "General"
    except:
        return "General"

def ask_techcorp_ai(question):
    try:
        print(f"\n🤖 USER ASKS: '{question}'")
        print("------------------------------------------------")
        
        start_time = time.time()
        
        # 1. ROUTE
        department = classify_intent(question)
        print(f"👉 ROUTED TO: {department}")
        
        # 2. RETRIEVE (Scoped by Department)
        # Executive searches EVERYTHING. General searches EVERYTHING (or just general folder? let's say everything for general fallback)
        # Others are Scoped.
        
        if department in ["Executive", "General"]:
            print(f"🔍 Retrieving context from 'GLOBAL' Cabinet (Access Level: {department})...")
            results = search_documents(question, n_results=15) # Fetch more for complex queries
        else:
            print(f"🔍 Retrieving context from '{department}' Cabinet...")
            results = search_documents(question, n_results=3, where={"department": department})
            
        retrieval_time = time.time() - start_time
        
        # Filter results by relevance score (Anti-Hallucination)
        # Adjustment: Temporarily disabled strict filtering (threshold -10.0)
        # to ensure results are returned until distance metric is calibrated.
        
        valid_results = [r for r in results if r['score'] >= -10.0]
        
        if not valid_results:
            print("⚠️ No relevant documents found.")
            return {
                "answer": f"I checked the available records for {department}, but couldn't find information relevant enough to your query. (Confidence too low)",
                "sources": [],
                "metrics": {"retrieval_time": retrieval_time, "generation_time": 0}
            }
    
        # 3. AUGMENT
        context_text = "\n\n".join([f"doc: {r['source']} (Dept: {r.get('source_dept', 'Unknown')}) \n content: {r['content']}" for r in valid_results])
        
        # Custom System Prompts per Persona
        personas = {
            "HR_Law": "You are a rigid but helpful HR & Legal Officer. Cite specific policies.",
            "Sales_Marketing": "You are an energetic Sales Director. Focus on growth, numbers, and customer satisfaction.",
            "Account_Finance": "You are a precise Accountant. Be exact with numbers and budget details.",
            "IT": "You are a helpful IT Support Specialist. Explain technical concepts simply.",
            "Executive": "You are the Chief Strategy Officer. You have access to ALL files. Synthesize information from different departments.",
            "General": "You are a helpful Corporate Assistant."
        }
        
        system_persona = personas.get(department, personas['General'])
        
        prompt = f"""
        {system_persona}
        
        You are an intelligent consultant. Your goal is not just to answer, but to GUIDE the user.
        
        STRICT RULE: Answer ONLY using the provided CONTEXT. Do not use outside knowledge.
        
        Use the following CONTEXT to answer the QUESTION.
        
        Format your response exactly like this:
        
        **🎯 Answer:**
        [Direct, factual answer to the question based on the documents.]
        
        **💡 Recommendation:**
        [Provide 1-2 actionable steps the user should take. Be proactive.]
        
        **⚖️ Logical Reasoning:**
        [Explain WHY you recommend this. Cite best practices, logic, or specific constraints from the documents.]
        
        If the answer is not in the documents, say "I don't know based on the available records."
        
        CONTEXT:
        {context_text}
        
        QUESTION: 
        {question}
        
        ANSWER:
        """
        
        print("\n🧠 GENERATING ANSWER...")
        
        # 4. GENERATE
        start_gen = time.time()
        model_name = "llama3.2" 
        
        # TEMPERATURE 0.1 = Deterministic / Factual
        response = ollama.chat(
            model=model_name, 
            messages=[{'role': 'user', 'content': prompt}],
            options={'temperature': 0.1} 
        )
        
        answer = response['message']['content']
        gen_time = time.time() - start_gen
        
        print("\n✨ AI ANSWER:")
        print(answer)
        print("------------------------------------------------")
        
        return {
            "answer": answer,
            "sources": [r['source'] for r in valid_results],
            "metrics": {
                "department": department,
                "retrieval_time": round(retrieval_time, 2), 
                "generation_time": round(gen_time, 2),
                "total_time": round(retrieval_time + gen_time, 2)
            }
        }
            
    except Exception as e:
        import traceback
        print(f"Error: {e}")
        traceback.print_exc()
        return {
            "answer": f"Error generating response: {str(e)}",
            "sources": [],
            "metrics": {"error": str(e)}
        }

if __name__ == "__main__":
    # Test Questions
    ask_techcorp_ai("What is the project pegasus budget?")
    ask_techcorp_ai("Can I use ChatGPT for work?")

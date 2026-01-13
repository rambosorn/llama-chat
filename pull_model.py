import ollama
import sys

def setup_model():
    model_name = "llama3.2"
    print(f"⬇️  Pulling model '{model_name}' via Python client...")
    print("    (This may take a while depending on internet speed...)")
    
    try:
        # stream=True allows us to see progress ideally, but for simple script we just wait
        progress = ollama.pull(model_name, stream=True)
        
        for p in progress:
            status = p.get('status', '')
            # Safe get with defaults
            completed = p.get('completed')
            total = p.get('total')
            
            if completed is not None and total is not None and total > 0:
                percent = (completed / total) * 100
                print(f"\r    {status}: {percent:.1f}%", end="")
            else:
                # Just print status if numbers aren't valid
                print(f"\r    {status}", end="")
        
        print(f"\n✅ Model '{model_name}' ready!")
        
    except Exception as e:
        print(f"\n❌ Error pulling model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_model()

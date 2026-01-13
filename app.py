from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from rag_pipeline import ask_techcorp_ai
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_key_fallback') # Secure key

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mock Login Logic (Now Secure-ish)
        username = request.form.get('username')
        password = request.form.get('password')
        
        env_user = os.getenv('ADMIN_USER', 'admin')
        env_pass = os.getenv('ADMIN_PASS', 'admin')
        
        if username == env_user and password == env_pass: 
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials. Try again.")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['user'])

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    start_time = time.time()
    result = ask_techcorp_ai(question) # Returns dict now
    end_time = time.time()
    
    # Unwrap if it's a dict (which it is now)
    answer_text = result['answer'] if isinstance(result, dict) else result
    metrics = result['metrics'] if isinstance(result, dict) and 'metrics' in result else {}
    
    return jsonify({
        'answer': answer_text,
        'time_taken': f"{end_time - start_time:.2f}s",
        'metrics': metrics
    })

if __name__ == '__main__':
    # Default to False for production safety
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=5000)

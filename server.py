import os
import subprocess
from datetime import datetime
from flask import Flask
import pytz  

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Naman Vinay Singh"
    
    try:
        username = os.getlogin()
    except:
        username = os.environ.get("USER", "unknown")
    
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    
    return f"""
<pre>
name: {name}
user: {username}
server time (IST): {server_time}

----- top output -----
{top_output}
</pre>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

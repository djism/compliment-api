from flask import Flask, request, jsonify, send_from_directory
import html
from pathlib import Path

app = Flask(__name__)

@app.route('/static/<path:filename>')
def serve_media(filename):
    """Serve the background image"""
    return send_from_directory('static', filename)

@app.get("/")
def home():
    name = request.args.get("n") or request.args.get("name")
    name_text = f"{html.escape(name.strip())}, " if name else ""
    
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>💝 For You</title>
<style>
  * {{box-sizing:border-box;margin:0;padding:0}}
  html,body{{height:100%;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;}}
  
  body{{
    background:#000;
    overflow:hidden;
    position:relative;
  }}
  
  /* NYC Christmas background image */
  .bg{{
    position:fixed;
    top:0;left:0;right:0;bottom:0;
    background-image:url('/static/nyc_christmas.jpg');
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    z-index:0;
  }}
  
  /* Overlay for better text readability */
  .overlay{{
    position:fixed;
    top:0;left:0;right:0;bottom:0;
    background:linear-gradient(to bottom, rgba(10,17,40,.3) 0%, rgba(10,17,40,.5) 100%);
    z-index:1;
  }}
  
  /* Christmas string lights at top */
  .string-lights{{
    position:fixed;
    top:0;
    left:0;
    right:0;
    height:100px;
    z-index:4;
    pointer-events:none;
  }}
  
  .string-light{{
    position:absolute;
    width:12px;
    height:12px;
    border-radius:50%;
    box-shadow:0 0 25px currentColor, 0 0 10px #fff;
    animation:bulbTwinkle 2s ease-in-out infinite;
  }}
  
  .string-light:nth-child(1){{left:5%;top:20px;color:#ff6b6b;animation-delay:0s}}
  .string-light:nth-child(2){{left:15%;top:30px;color:#4ecdc4;animation-delay:0.3s}}
  .string-light:nth-child(3){{left:25%;top:20px;color:#ffd700;animation-delay:0.6s}}
  .string-light:nth-child(4){{left:35%;top:35px;color:#ff6b6b;animation-delay:0.9s}}
  .string-light:nth-child(5){{left:45%;top:25px;color:#95e1d3;animation-delay:0.2s}}
  .string-light:nth-child(6){{left:55%;top:30px;color:#ffd700;animation-delay:0.5s}}
  .string-light:nth-child(7){{left:65%;top:20px;color:#ff6b6b;animation-delay:0.8s}}
  .string-light:nth-child(8){{left:75%;top:35px;color:#4ecdc4;animation-delay:0.1s}}
  .string-light:nth-child(9){{left:85%;top:25px;color:#ffd700;animation-delay:0.4s}}
  .string-light:nth-child(10){{left:95%;top:30px;color:#ff6b6b;animation-delay:0.7s}}
  
  /* Snowflakes */
  .snow-container{{
    position:fixed;
    top:0;left:0;right:0;bottom:0;
    overflow:hidden;
    z-index:2;
    pointer-events:none;
  }}
  
  .snowflake{{
    position:absolute;
    top:-10px;
    color:#fff;
    font-size:1em;
    opacity:0.9;
    animation:snowfall linear infinite;
    text-shadow:0 0 8px rgba(255,255,255,.8);
  }}
  
  .snowflake:nth-child(1){{left:10%;animation-duration:8s;animation-delay:0s;font-size:1.4em}}
  .snowflake:nth-child(2){{left:20%;animation-duration:10s;animation-delay:1s;font-size:1em}}
  .snowflake:nth-child(3){{left:30%;animation-duration:12s;animation-delay:2s;font-size:1.2em}}
  .snowflake:nth-child(4){{left:40%;animation-duration:9s;animation-delay:0.5s;font-size:1.5em}}
  .snowflake:nth-child(5){{left:50%;animation-duration:11s;animation-delay:1.5s;font-size:1.1em}}
  .snowflake:nth-child(6){{left:60%;animation-duration:10s;animation-delay:3s;font-size:1.3em}}
  .snowflake:nth-child(7){{left:70%;animation-duration:13s;animation-delay:2.5s;font-size:1em}}
  .snowflake:nth-child(8){{left:80%;animation-duration:9s;animation-delay:1s;font-size:1.4em}}
  .snowflake:nth-child(9){{left:90%;animation-duration:11s;animation-delay:0.5s;font-size:1.2em}}
  .snowflake:nth-child(10){{left:15%;animation-duration:10s;animation-delay:2.5s;font-size:1.1em}}
  .snowflake:nth-child(11){{left:25%;animation-duration:12s;animation-delay:1.5s;font-size:1.3em}}
  .snowflake:nth-child(12){{left:35%;animation-duration:8s;animation-delay:3s;font-size:1em}}
  .snowflake:nth-child(13){{left:45%;animation-duration:11s;animation-delay:0.5s;font-size:1.5em}}
  .snowflake:nth-child(14){{left:55%;animation-duration:9s;animation-delay:2s;font-size:1.2em}}
  .snowflake:nth-child(15){{left:65%;animation-duration:10s;animation-delay:1s;font-size:1.1em}}
  .snowflake:nth-child(16){{left:75%;animation-duration:13s;animation-delay:0.5s;font-size:1.4em}}
  .snowflake:nth-child(17){{left:85%;animation-duration:11s;animation-delay:2.5s;font-size:1em}}
  .snowflake:nth-child(18){{left:95%;animation-duration:9s;animation-delay:1.5s;font-size:1.3em}}
  .snowflake:nth-child(19){{left:5%;animation-duration:12s;animation-delay:3s;font-size:1.2em}}
  .snowflake:nth-child(20){{left:8%;animation-duration:10s;animation-delay:0.5s;font-size:1.1em}}
  .snowflake:nth-child(21){{left:12%;animation-duration:11s;animation-delay:1.8s;font-size:1.3em}}
  .snowflake:nth-child(22){{left:18%;animation-duration:9s;animation-delay:2.8s;font-size:1em}}
  .snowflake:nth-child(23){{left:22%;animation-duration:13s;animation-delay:1.2s;font-size:1.4em}}
  .snowflake:nth-child(24){{left:28%;animation-duration:10s;animation-delay:3.5s;font-size:1.2em}}
  .snowflake:nth-child(25){{left:32%;animation-duration:12s;animation-delay:0.8s;font-size:1.1em}}
  
  /* Main container */
  .container{{
    position:relative;
    z-index:3;
    height:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:2rem;
  }}
  
  .card{{
    max-width:800px;
    width:100%;
    text-align:center;
    animation:fadeInScale 1.5s ease-out;
  }}
  
  /* Heart decoration */
  .heart-decoration{{
    font-size:5rem;
    margin-bottom:2rem;
    animation:heartBeat 1.5s ease-in-out infinite;
    filter:drop-shadow(0 0 30px rgba(255,107,107,.9)) drop-shadow(0 0 60px rgba(255,107,107,.6));
  }}
  
  /* Main message */
  .message{{
    background:rgba(255,255,255,.97);
    backdrop-filter:blur(30px);
    border-radius:40px;
    padding:4rem 3rem;
    box-shadow:0 30px 90px rgba(255,215,0,.4), 0 0 0 2px rgba(255,255,255,.95), 0 0 80px rgba(255,107,107,.3);
    position:relative;
    overflow:hidden;
  }}
  
  .message::before{{
    content:'';
    position:absolute;
    top:-50%;
    left:-50%;
    width:200%;
    height:200%;
    background:conic-gradient(from 0deg, transparent, rgba(255,215,0,.15), transparent 30%);
    animation:rotate 8s linear infinite;
  }}
  
  .message-content{{
    position:relative;
    z-index:1;
  }}
  
  .line{{
    font-size:2.5rem;
    font-weight:700;
    line-height:1.6;
    margin:1rem 0;
    opacity:0;
    animation:fadeInUp 1s ease-out forwards;
  }}
  
  .line:nth-child(1){{
    animation-delay:0.5s;
    background:linear-gradient(135deg, #c94b4b 0%, #4b134f 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  
  .line:nth-child(2){{
    animation-delay:1s;
    background:linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  
  .line:nth-child(3){{
    animation-delay:1.5s;
    background:linear-gradient(135deg, #0575e6 0%, #021b79 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  
  .line:nth-child(4){{
    animation-delay:2s;
    background:linear-gradient(135deg, #f37335 0%, #fdc830 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  
  .line:nth-child(5){{
    animation-delay:2.5s;
    font-size:3rem;
    background:linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  
  /* Sparkles */
  .sparkles{{
    margin-top:3rem;
    font-size:2rem;
    opacity:0;
    animation:fadeIn 1s ease-out 3s forwards, sparkleAnim 2s ease-in-out 3s infinite;
  }}
  
  /* Floating hearts */
  .floating-hearts{{
    position:fixed;
    top:0;left:0;right:0;bottom:0;
    pointer-events:none;
    z-index:4;
  }}
  
  .floating-heart{{
    position:absolute;
    font-size:2rem;
    animation:floatUp 8s ease-in infinite;
    opacity:0;
    filter:drop-shadow(0 0 15px rgba(255,107,107,.8));
  }}
  
  .floating-heart:nth-child(1){{left:10%;animation-delay:0s}}
  .floating-heart:nth-child(2){{left:25%;animation-delay:1.5s}}
  .floating-heart:nth-child(3){{left:40%;animation-delay:3s}}
  .floating-heart:nth-child(4){{left:55%;animation-delay:4.5s}}
  .floating-heart:nth-child(5){{left:70%;animation-delay:6s}}
  .floating-heart:nth-child(6){{left:85%;animation-delay:7.5s}}
  
  @keyframes snowfall{{
    0%{{top:-10%;transform:translateX(0) rotate(0deg);opacity:0}}
    10%{{opacity:0.9}}
    90%{{opacity:0.9}}
    100%{{top:110%;transform:translateX(100px) rotate(360deg);opacity:0}}
  }}
  
  @keyframes bulbTwinkle{{
    0%,100%{{opacity:0.6;transform:scale(1)}}
    50%{{opacity:1;transform:scale(1.3)}}
  }}
  
  @keyframes fadeInScale{{
    from{{opacity:0;transform:scale(0.8)}}
    to{{opacity:1;transform:scale(1)}}
  }}
  
  @keyframes heartBeat{{
    0%,100%{{transform:scale(1)}}
    10%{{transform:scale(1.1)}}
    20%{{transform:scale(1)}}
    30%{{transform:scale(1.15)}}
    40%{{transform:scale(1)}}
  }}
  
  @keyframes fadeInUp{{
    from{{opacity:0;transform:translateY(30px)}}
    to{{opacity:1;transform:translateY(0)}}
  }}
  
  @keyframes rotate{{
    from{{transform:rotate(0deg)}}
    to{{transform:rotate(360deg)}}
  }}
  
  @keyframes fadeIn{{
    to{{opacity:1}}
  }}
  
  @keyframes sparkleAnim{{
    0%,100%{{transform:scale(1)}}
    50%{{transform:scale(1.2);filter:brightness(1.5)}}
  }}
  
  @keyframes floatUp{{
    0%{{bottom:-10%;opacity:0;transform:translateX(0)}}
    10%{{opacity:.8}}
    90%{{opacity:.8}}
    100%{{bottom:110%;opacity:0;transform:translateX(50px)}}
  }}
  
  @media(max-width:768px){{
    .line{{font-size:1.8rem}}
    .line:nth-child(5){{font-size:2.2rem}}
    .message{{padding:2.5rem 2rem}}
    .heart-decoration{{font-size:3.5rem}}
  }}
  
  @media(max-width:480px){{
    .line{{font-size:1.4rem}}
    .line:nth-child(5){{font-size:1.8rem}}
    .message{{padding:2rem 1.5rem}}
  }}
</style>
</head>
<body>
  <div class="bg"></div>
  <div class="overlay"></div>
  
  <div class="string-lights">
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
    <div class="string-light"></div>
  </div>
  
  <div class="snow-container">
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄</div>
  </div>
  
  <div class="floating-hearts">
    <div class="floating-heart">💖</div>
    <div class="floating-heart">💕</div>
    <div class="floating-heart">💗</div>
    <div class="floating-heart">💝</div>
    <div class="floating-heart">💓</div>
    <div class="floating-heart">💞</div>
  </div>
  
  <div class="container">
    <div class="card">
      <div class="heart-decoration">💝</div>
      
      <div class="message">
        <div class="message-content">
          <div class="line">{name_text}Get well soon,</div>
          <div class="line">and finish all your work</div>
          <div class="line">and meet me,</div>
          <div class="line">I miss</div>
          <div class="line">those tiny hands to hold</div>
          <div class="sparkles">✨ 💕 ✨</div>
        </div>
      </div>
    </div>
  </div>
</body></html>"""

@app.get("/api")
def api():
    name = request.args.get("n") or request.args.get("name")
    name_text = f"{html.escape(name.strip())}, " if name else ""
    return jsonify({{"message": f"{name_text}Get well soon, and finish all your work, I miss those tiny hands to hold"}})

if __name__ == "__main__":
    # Create static folder if it doesn't exist
    Path("static").mkdir(exist_ok=True)
    print("\n💝 NYC Christmas magic page ready!")
    print("\n📸 IMPORTANT: Save the uploaded image as 'nyc_christmas.jpg' in the 'static' folder")
    print("🌸 Visit: http://localhost:5001")
    print("🎀 Add ?name=HerName to personalize\n")
    
    app.run(host="0.0.0.0", port=5001, debug=True)
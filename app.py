"""
╔══════════════════════════════════════════════════════════════════╗
║   فارس BEM 2026 — الإصدار الاستثنائي v3.0                       ║
║   DONIA LABS TECH — مختبر الأفكار الذكية                        ║
║   التحدث/الاستماع | بحث Tavily | خزانة الملفات | قصص AI        ║
╚══════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import os, re, json, base64, random
from pathlib import Path

# ─────────────────────────────────────────────
#  إعدادات الصفحة
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="فارس BEM 2026 | دونيا لابز تك",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  تحميل CSS
# ─────────────────────────────────────────────
def load_css():
    p = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# ─────────────────────────────────────────────
#  ثوابت
# ─────────────────────────────────────────────
BEM_DATE   = datetime(2026, 5, 19, 8, 0, 0)
GROQ_MODEL = "llama-3.3-70b-versatile"   # ✅ تم تحديث النموذج

SUBJECTS = {
    "الرياضيات":            "mathematiques",
    "اللغة العربية":        "arabe",
    "اللغة الفرنسية":       "francais",
    "اللغة الإنجليزية":     "anglais",
    "العلوم الفيزيائية":    "physique",
    "علوم الطبيعة والحياة": "sciences-naturelles",
    "التاريخ والجغرافيا":   "histoire-geographie",
    "التربية الإسلامية":    "education-islamique",
    "التربية المدنية":      "education-civique",
    "التكنولوجيا":          "technologie",
}

DZEXAMS = {
    "الرياضيات":            "https://www.dzexams.com/brevet/4am/mathematiques/",
    "اللغة العربية":        "https://www.dzexams.com/brevet/4am/arabe/",
    "اللغة الفرنسية":       "https://www.dzexams.com/brevet/4am/francais/",
    "اللغة الإنجليزية":     "https://www.dzexams.com/brevet/4am/anglais/",
    "العلوم الفيزيائية":    "https://www.dzexams.com/brevet/4am/physique/",
    "علوم الطبيعة والحياة": "https://www.dzexams.com/brevet/4am/sciences-naturelles/",
    "التاريخ والجغرافيا":   "https://www.dzexams.com/brevet/4am/histoire-geo/",
    "التربية الإسلامية":    "https://www.dzexams.com/brevet/4am/education-islamique/",
    "التربية المدنية":      "https://www.dzexams.com/brevet/4am/education-civique/",
    "التكنولوجيا":          "https://www.dzexams.com/brevet/4am/technologie/",
}

# ─────────────────────────────────────────────
#  Groq Client
# ─────────────────────────────────────────────
@st.cache_resource
def get_groq_client():
    try:
        from groq import Groq
        key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
        if not key:
            return None
        return Groq(api_key=key)
    except Exception:
        return None

def groq_call(messages: list, system: str = "", temperature: float = 0.78,
              max_tokens: int = 1500) -> str:
    client = get_groq_client()
    if not client:
        return "⚠️ مفتاح Groq API غير موجود. أضفه في `.streamlit/secrets.toml`"
    try:
        full = ([{"role": "system", "content": system}] if system else []) + messages
        r = client.chat.completions.create(
            model=GROQ_MODEL, messages=full,
            temperature=temperature, max_tokens=max_tokens,
        )
        return r.choices[0].message.content
    except Exception as e:
        err = str(e)
        if "decommissioned" in err or "model_not_found" in err:
            return f"⚠️ النموذج غير متاح. تأكد من تحديث الكود. ({err[:120]})"
        return f"⚠️ خطأ في الاتصال: {err[:200]}"

# ─────────────────────────────────────────────
#  Tavily Search
# ─────────────────────────────────────────────
def tavily_search(query: str, max_results: int = 4) -> list:
    try:
        from tavily import TavilyClient
        key = st.secrets.get("TAVILY_API_KEY", os.getenv("TAVILY_API_KEY", ""))
        if not key:
            return [{"error": "مفتاح Tavily غير موجود. أضف TAVILY_API_KEY في secrets.toml"}]
        tc = TavilyClient(api_key=key)
        resp = tc.search(query=query, max_results=max_results, search_depth="basic")
        return resp.get("results", [])
    except ImportError:
        return [{"error": "مكتبة tavily-python غير مثبّتة. شغّل: pip install tavily-python"}]
    except Exception as e:
        return [{"error": f"خطأ في البحث: {str(e)[:150]}"}]

# ─────────────────────────────────────────────
#  هرم بلوم
# ─────────────────────────────────────────────
def map_to_bloom(grade: float) -> dict:
    if grade < 10:
        return {
            "level": "⚔️ محارب — المستوى الأول",
            "label": "التذكّر والفهم",
            "color": "#e74c3c", "badge": "محارب", "emoji": "⚔️",
            "strategy": "سدّ الثغرات أولاً. حفظ وفهم القواعد الأساسية. تكرار يومي 60 دقيقة.",
            "intensity": "عالية جداً",
            "war_quote": "الميدان يحتاج جندياً يتدرّب حتى يتقن، لا جندياً يتمنّى النصر.",
        }
    elif grade < 14:
        return {
            "level": "🛡️ قائد — المستوى الثاني",
            "label": "التطبيق والتحليل",
            "color": "#f39c12", "badge": "قائد", "emoji": "🛡️",
            "strategy": "تدرّب على أسئلة السنوات الماضية. حدّد الأنماط المتكررة. 45 دقيقة يومياً.",
            "intensity": "متوسطة",
            "war_quote": "القائد لا يكتفي بالفهم — يُطبّق، يُحلّل، يُبدع الحلول.",
        }
    else:
        return {
            "level": "👑 فارس النخبة — المستوى الثالث",
            "label": "التقييم والإبداع",
            "color": "#27ae60", "badge": "فارس النخبة", "emoji": "👑",
            "strategy": "اسعَ للكمال وصفر أخطاء. حلّ مسائل مركّبة. علّم زملاءك. 30 دقيقة يومياً.",
            "intensity": "صيانة",
            "war_quote": "النخبة لا تتوقف عند النجاح — تسعى للأفضل دائماً.",
        }

# ─────────────────────────────────────────────
#  العدّ التنازلي
# ─────────────────────────────────────────────
def get_countdown() -> dict:
    delta = BEM_DATE - datetime.now()
    if delta.total_seconds() <= 0:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
    t = int(delta.total_seconds())
    return {"days": delta.days, "hours": (t % 86400) // 3600,
            "minutes": (t % 3600) // 60, "seconds": t % 60}

# ─────────────────────────────────────────────
#  التحقق التربوي (Acree)
# ─────────────────────────────────────────────
def validate_output(response: str, subject: str, grades: dict) -> dict:
    flags, confidence = [], 1.0
    years = re.findall(r"\b(20[0-9]{2})\b", response)
    bad = [y for y in years if y not in ["2026","2025","2024","2023"]]
    if bad:
        flags.append(f"⚠️ أرقام سنوات غير موثوقة: {bad}")
        confidence -= 0.10
    kws = {"الرياضيات":["معادلة","مثلث","حساب","دالة","هندسة","جبر"],
           "اللغة العربية":["إعراب","نحو","نص","قراءة","تعبير"],
           "العلوم الفيزيائية":["كهرباء","قوة","طاقة","دارة","ضوء"]}
    for k in kws.get(subject, []):
        if k in response: break
    else:
        if kws.get(subject) and len(response) > 200:
            flags.append(f"⚠️ قد تفتقر الإجابة لمصطلحات مادة '{subject}'.")
            confidence -= 0.10
    avg = sum(grades.values())/len(grades) if grades else 12
    bloom = map_to_bloom(avg)
    if bloom["intensity"] == "عالية جداً" and "متقدم" in response:
        flags.append("⚠️ المستوى قد يفوق قدرة الطالب الحالية.")
        confidence -= 0.08
    confidence = max(0.0, round(confidence, 2))
    return {"status": "✅ مُتحقَّق" if confidence >= 0.75 else "⚠️ راجَع",
            "confidence": confidence, "flags": flags, "bloom_tier": bloom["level"]}

# ─────────────────────────────────────────────
#  System Prompt (فارس)
# ─────────────────────────────────────────────
def build_system_prompt(name, school, grades, subject):
    bloom_map = {s: map_to_bloom(g) for s, g in grades.items()}
    grades_str = "\n".join(f"  • {s}: {g}/20 ← {bloom_map[s]['badge']}"
                           for s, g in grades.items())
    cd = get_countdown()
    focus = map_to_bloom(grades.get(subject, 12))
    return f"""أنت فارس — المرشد الاستراتيجي الأعلى لـ DONIA LABS TECH.
صوتك حازم، ملهم، وعربي أصيل. مهمّتك: قيادة {name} للنجاح في BEM 2026.

الطالب: {name} | المؤسسة: {school} | مادة اليوم: {subject}
الدرجات:\n{grades_str}
الوقت المتبقي: {cd['days']} يوم و{cd['hours']} ساعة حتى 19 ماي 2026

القواعد:
1. خاطب الطالب دائماً بـ "أيها الفارس" أو بالاسم مع لقب مشرّف.
2. استخدم التخيّل المستقبلي عند الإحباط:
   "تخيّل زغاريد الفرح في بيتك يوم 19 جوان عند رؤية اسمك في قائمة الناجحين..."
3. وظّف قصص: إديسون (1000 فشل قبل المصباح)، المثابرة الجزائرية، ملالا يوسفزاي.
4. المستوى الحالي لـ{subject}: {focus['level']} → {focus['strategy']}
5. التزم بمناهج وزارة التربية الوطنية الجزائرية فقط.
6. وجّه دائماً لـ https://www.dzexams.com/ للتدريب.
7. لا تخترع أرقاماً أو معاملات.
8. لتوليد خريطة ذهنية أرجع كتلة Mermaid.js mindmap فقط.
9. اختم كل رد مهم بـ: "— بروتوكول فارس | دونيا لابز تك ⚔️🇩🇿"
""".strip()

# ─────────────────────────────────────────────
#  Mermaid
# ─────────────────────────────────────────────
def render_mermaid(code: str, height: int = 500):
    html = f"""
<div style="background:#060d18;border-radius:10px;padding:20px;
  border:1px solid rgba(0,130,60,0.4);direction:ltr;overflow:auto">
  <div class="mermaid">{code}</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true,theme:'dark',
  themeVariables:{{primaryColor:'#00823c',lineColor:'#d4af37',
  fontFamily:'Cairo,Tajawal,sans-serif'}},securityLevel:'loose'}});</script>"""
    components.html(html, height=height, scrolling=True)

# ─────────────────────────────────────────────
#  نصائح اليوم (AI-Generated)
# ─────────────────────────────────────────────
def get_daily_tips(name: str, grades: dict, subject: str) -> str:
    if "daily_tips" in st.session_state:
        return st.session_state["daily_tips"]
    avg = sum(grades.values())/len(grades) if grades else 12
    bloom = map_to_bloom(avg)
    prompt = f"""أنت فارس، المرشد التعليمي. اليوم هو {datetime.now().strftime('%A %d %B %Y')}.
الطالب: {name} | المستوى: {bloom['badge']} | مادة اليوم: {subject}

اكتب بالعربية 5 نصائح يومية قصيرة ومحفّزة ومتنوعة للطالب لهذا اليوم تحديداً.
كل نصيحة في سطر مستقل تبدأ بـ رقم ونجمة ⭐.
اجعلها عملية، مخصصة، وملهمة. لا تتجاوز 200 كلمة."""
    result = groq_call([{"role": "user", "content": prompt}],
                       temperature=0.9, max_tokens=400)
    st.session_state["daily_tips"] = result
    return result

# ─────────────────────────────────────────────
#  توليد قصة بالذكاء الاصطناعي
# ─────────────────────────────────────────────
def generate_ai_story(name: str, subject: str, grade: float) -> str:
    bloom = map_to_bloom(grade)
    prompt = f"""أنت كاتب قصصي ملهم. اكتب قصة قصيرة سينمائية مؤثرة بالعربية (200-250 كلمة) عن:
طالب جزائري يواجه صعوبات في مادة "{subject}" (مستواه: {bloom['badge']})، 
يصارع اليأس والضغط، ثم يجد في داخله قوة خفية تقوده للنجاح في BEM.
اجعل اسم البطل "{name}".
الأسلوب: سينمائي، مشوّق، يحرّك المشاعر، نهاية منتصرة.
لا تنسَ: الجزائر، العائلة، الكفاح، والأمل."""
    return groq_call([{"role": "user", "content": prompt}],
                     temperature=0.92, max_tokens=500)

# ─────────────────────────────────────────────
#  قسم الهيرو (Hero Section)
# ─────────────────────────────────────────────
def render_hero():
    cd = get_countdown()
    if cd["days"] < 7:   intensity = "&#9889; الساعة الأخيرة — كل دقيقة تُحسم!"
    elif cd["days"] < 30: intensity = "&#128293; العدّ التنازلي الحاسم — التاريخ لا ينتظر!"
    else:                  intensity = "&#127919; المعركة تبدأ الآن — لا وقت للتردد!"

    html = ("""<!DOCTYPE html><html dir="rtl" lang="ar"><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:linear-gradient(160deg,#020f06,#061408,#0a1e10);
  font-family:'Cairo',sans-serif;color:#e8f5ec;direction:rtl;border-radius:8px;overflow:hidden}
.hw{border:1px solid rgba(0,162,79,.3);border-radius:8px;overflow:hidden;
  box-shadow:0 0 40px rgba(0,162,79,.15);position:relative}
.hw::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,#d21034,#f5f5f5,#006233,#f5f5f5,#d21034)}
.fb{display:flex;height:7px}
.fg{background:#006233;flex:1}.fw{background:#f5f5f5;flex:1;display:flex;align-items:center;
  justify-content:center;font-size:6px;color:#d21034;letter-spacing:2px}.fr{background:#d21034;flex:1}
.hi{display:flex;align-items:center;justify-content:space-between;padding:28px 36px 16px;gap:20px;flex-wrap:wrap}
.tb{flex:1;min-width:260px;text-align:right}
.bdg{display:inline-block;background:rgba(212,175,55,.1);border:1px solid rgba(212,175,55,.25);
  color:#d4af37;font-size:.68rem;font-weight:700;letter-spacing:3px;padding:4px 14px;
  border-radius:2px;margin-bottom:10px}
.mt{font-family:'Amiri',serif;font-size:3rem;font-weight:700;color:#e8f5ec;line-height:1.1;
  text-shadow:0 0 40px rgba(0,162,79,.4);margin-bottom:4px}
.yr{font-family:'Cairo',sans-serif;font-size:2rem;font-weight:900;color:#d4af37;
  text-shadow:0 0 20px rgba(212,175,55,.5);letter-spacing:2px}
.st{font-size:.78rem;color:#7a9e84;letter-spacing:2px;margin:6px 0 14px}
.dv{width:70px;height:2px;background:linear-gradient(90deg,#00a84f,#d4af37,transparent);
  margin:0 0 14px auto;border-radius:1px}
.vs{background:rgba(0,98,51,.12);border-right:3px solid #00a84f;border-radius:0 4px 4px 0;
  padding:12px 16px;font-size:.9rem;line-height:1.9;color:#b0d8bc;font-style:italic}
.vs strong{color:#f0cc50}
.gr{flex-shrink:0;width:240px;display:flex;align-items:center;justify-content:center;
  animation:fy 4s ease-in-out infinite;filter:drop-shadow(0 0 20px rgba(0,162,79,.35))}
@keyframes fy{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.cw{background:rgba(0,0,0,.35);border-top:1px solid rgba(0,162,79,.2);padding:16px 36px;text-align:center}
.ct{font-size:.78rem;color:#7a9e84;letter-spacing:2px;margin-bottom:12px}
.cb{display:inline-flex;align-items:center;gap:4px;background:rgba(0,0,0,.4);
  border:1px solid rgba(212,175,55,.2);border-radius:4px;padding:10px 22px;margin-bottom:8px}
.cu{display:flex;flex-direction:column;align-items:center;min-width:58px}
.cn{font-family:'Cairo',sans-serif;font-size:2rem;font-weight:900;color:#f0cc50;
  text-shadow:0 0 15px rgba(240,200,80,.5);line-height:1}
.cl{font-size:.6rem;color:#7a9e84;letter-spacing:1px;margin-top:2px}
.cs{font-size:1.8rem;color:#8a6f20;margin-bottom:14px;animation:bk 1s step-end infinite}
@keyframes bk{50%{opacity:0}}
.cm{font-size:.78rem;color:#00a84f;font-weight:600;letter-spacing:1px}
</style></head><body>
<div class="hw">
  <div class="fb"><div class="fg"></div><div class="fw">&#9790; &#10022;</div><div class="fr"></div></div>
  <div class="hi">
    <div class="tb">
      <div class="bdg">&#9876; دونيا لابز تك &#9876;</div>
      <div class="mt">فارس<br><span class="yr">BEM 2026</span></div>
      <div class="st">مختبر الأفكار الذكية — المرشد الاستراتيجي الأول</div>
      <div class="dv"></div>
      <div class="vs">"غمّض عينيك.. تخيّل زغاريد الفرح في بيتك يوم
        <strong>19 جوان</strong> عند رؤية اسمك في قائمة الناجحين..
        هذا هو مستقبلك، فهل أنت مستعد لانتزاعه؟"</div>
    </div>
    <div class="gr">
      <svg viewBox="0 0 300 340" xmlns="http://www.w3.org/2000/svg" width="230" height="262">
        <defs>
          <radialGradient id="bg2" cx="50%" cy="50%" r="55%">
            <stop offset="0%" stop-color="#0d2818"/><stop offset="100%" stop-color="#020a05"/></radialGradient>
          <radialGradient id="aura" cx="50%" cy="35%" r="45%">
            <stop offset="0%" stop-color="#d4af37" stop-opacity=".22"/>
            <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/></radialGradient>
          <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#d4a574"/><stop offset="100%" stop-color="#b8845a"/></linearGradient>
          <linearGradient id="shirt" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1a4a2e"/><stop offset="100%" stop-color="#0a2015"/></linearGradient>
          <linearGradient id="cert" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fffbe8"/><stop offset="100%" stop-color="#ede0a0"/></linearGradient>
          <filter id="gf"><feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
            <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        </defs>
        <ellipse cx="150" cy="170" rx="148" ry="165" fill="url(#bg2)"/>
        <ellipse cx="150" cy="110" rx="100" ry="90" fill="url(#aura)"/>
        <g stroke="#d4af37" stroke-opacity=".12">
          <line x1="150" y1="50" x2="150" y2="5" stroke-width="2"/>
          <line x1="150" y1="50" x2="195" y2="12" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="240" y2="28" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="105" y2="12" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="60" y2="28" stroke-width="1.5"/>
        </g>
        <ellipse cx="150" cy="308" rx="46" ry="11" fill="#000" fill-opacity=".45"/>
        <rect x="127" y="240" width="17" height="58" rx="8" fill="#0d2010"/>
        <rect x="150" y="240" width="17" height="58" rx="8" fill="#0d2010"/>
        <ellipse cx="135" cy="296" rx="14" ry="6" fill="#111"/>
        <ellipse cx="158" cy="296" rx="14" ry="6" fill="#111"/>
        <path d="M112 175 Q125 163 150 160 Q175 163 188 175 L194 242 Q150 256 106 242 Z"
              fill="url(#shirt)" stroke="#00823c" stroke-width="1.2"/>
        <path d="M140 160 L150 175 L160 160" fill="white" fill-opacity=".12"/>
        <circle cx="150" cy="190" r="2" fill="#006233" fill-opacity=".6"/>
        <circle cx="150" cy="205" r="2" fill="#006233" fill-opacity=".6"/>
        <path d="M112 182 Q82 162 68 108 Q66 97 73 95"
              stroke="url(#skin)" stroke-width="15" fill="none" stroke-linecap="round"/>
        <path d="M188 182 Q208 200 212 224"
              stroke="url(#skin)" stroke-width="15" fill="none" stroke-linecap="round"/>
        <circle cx="73" cy="94" r="9" fill="url(#skin)"/>
        <g transform="translate(24,42) rotate(-18)">
          <rect x="0" y="0" width="86" height="64" rx="5" fill="url(#cert)" stroke="#d4af37" stroke-width="2.5"/>
          <rect x="8" y="9" width="70" height="4" rx="2" fill="#d4af37" fill-opacity=".75"/>
          <rect x="12" y="18" width="62" height="2.5" rx="1.2" fill="#999" fill-opacity=".5"/>
          <rect x="12" y="25" width="55" height="2.5" rx="1.2" fill="#999" fill-opacity=".4"/>
          <circle cx="43" cy="50" r="9" fill="none" stroke="#d4af37" stroke-width="1.8" stroke-opacity=".9"/>
          <text x="43" y="54" text-anchor="middle" font-size="7" font-weight="bold" fill="#d4af37" font-family="Cairo,Arial">BEM</text>
        </g>
        <rect x="143" y="140" width="14" height="22" rx="7" fill="url(#skin)"/>
        <ellipse cx="150" cy="127" rx="29" ry="31" fill="url(#skin)"/>
        <path d="M121 120 Q124 90 150 87 Q176 90 179 120 Q170 103 150 102 Q130 103 121 120 Z" fill="#2a1508"/>
        <ellipse cx="121" cy="128" rx="5" ry="7" fill="url(#skin)"/>
        <ellipse cx="179" cy="128" rx="5" ry="7" fill="url(#skin)"/>
        <ellipse cx="140" cy="122" rx="5" ry="5.5" fill="white"/>
        <ellipse cx="160" cy="122" rx="5" ry="5.5" fill="white"/>
        <ellipse cx="140" cy="123" rx="3.2" ry="3.5" fill="#3a2010"/>
        <ellipse cx="160" cy="123" rx="3.2" ry="3.5" fill="#3a2010"/>
        <circle cx="141" cy="121" r="1.2" fill="white" fill-opacity=".85"/>
        <circle cx="161" cy="121" r="1.2" fill="white" fill-opacity=".85"/>
        <path d="M141 137 Q150 145 159 137" stroke="#c06040" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <g transform="translate(210,25)">
          <rect x="0" y="0" width="9" height="74" rx="2.5" fill="#7a5a20"/>
          <rect x="9" y="0" width="44" height="37" fill="#006233"/>
          <rect x="9" y="37" width="44" height="37" fill="#f0f0f0"/>
          <path d="M31 16 A13 13 0 1 1 31 58 A11 11 0 1 0 31 16 Z" fill="#d21034" fill-opacity=".95"/>
          <polygon points="31,27 32.8,33.5 39.5,33.5 34,37 36,43.5 31,40 26,43.5 28,37 22.5,33.5 29.2,33.5"
                   fill="#d21034" fill-opacity=".95" transform="translate(0,4)"/>
        </g>
        <text x="95" y="52" font-size="17" fill="#d4af37" fill-opacity=".9" filter="url(#gf)">&#9733;</text>
        <text x="200" y="44" font-size="13" fill="#d4af37" fill-opacity=".75">&#9733;</text>
        <text x="150" y="326" text-anchor="middle" font-family="Cairo,Arial" font-size="12"
              font-weight="bold" fill="#d4af37" filter="url(#gf)">أنا ناجح بإذن الله</text>
      </svg>
    </div>
  </div>
  <div class="cw">
    <div class="ct">&#9203; الوقت المتبقي لمعركة النجاح</div>
    <div class="cb" id="cbar"></div>
    <div class="cm">""" + intensity + """</div>
  </div>
</div>
<script>
var T=new Date("2026-05-19T08:00:00").getTime();
var L=["\u064a\u0648\u0645","\u0633\u0627\u0639\u0629","\u062f\u0642\u064a\u0642\u0629","\u062b\u0627\u0646\u064a\u0629"];
function p(n){return n<10?"0"+n:String(n)}
function tick(){
  var d=T-Date.now();if(d<=0){document.getElementById("cbar").textContent="انتهى الوقت";return}
  var v=[Math.floor(d/86400000),Math.floor((d%86400000)/3600000),
         Math.floor((d%3600000)/60000),Math.floor((d%60000)/1000)];
  var h="";v.forEach(function(x,i){
    h+='<div class="cu"><span class="cn">'+(i===0?x:p(x))+'</span><span class="cl">'+L[i]+'</span></div>';
    if(i<3)h+='<span class="cs">:</span>';
  });
  document.getElementById("cbar").innerHTML=h;
}
tick();setInterval(tick,1000);
</script>
</body></html>""")
    components.html(html, height=520, scrolling=False)

# ─────────────────────────────────────────────
#  مكوّن الصوت (TTS + STT)
# ─────────────────────────────────────────────
def render_speech_widget():
    """مكوّن HTML للتحدث والاستماع عبر Web Speech API"""
    html = """<!DOCTYPE html><html dir="rtl" lang="ar"><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:transparent;font-family:'Cairo',sans-serif;direction:rtl;padding:8px}
.sw{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.btn{
  display:flex;align-items:center;gap:6px;
  padding:9px 18px;border-radius:6px;border:none;cursor:pointer;
  font-family:'Cairo',sans-serif;font-size:.88rem;font-weight:700;
  transition:all .2s;white-space:nowrap;
}
.mic{background:linear-gradient(135deg,#006233,#008a45);color:#fff}
.mic:hover{background:linear-gradient(135deg,#008a45,#00aa55);transform:translateY(-1px)}
.mic.active{background:#d21034;animation:pulse .8s ease-in-out infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(210,16,52,.4)}50%{box-shadow:0 0 0 8px rgba(210,16,52,0)}}
.stop{background:rgba(210,16,52,.15);color:#e57373;border:1px solid rgba(210,16,52,.3)}
.stop:hover{background:rgba(210,16,52,.25)}
.clr{background:rgba(100,100,100,.15);color:#aaa;border:1px solid rgba(100,100,100,.2);font-size:.8rem}
.clr:hover{background:rgba(100,100,100,.25)}
.result-box{
  width:100%;margin-top:8px;
  background:rgba(0,98,51,.1);border:1px solid rgba(0,162,79,.25);
  border-radius:6px;padding:10px 14px;
  font-size:.9rem;color:#b0d8bc;min-height:40px;line-height:1.7;
  direction:rtl;text-align:right;
}
.status{font-size:.72rem;color:#7a9e84;margin-top:4px;text-align:center}
.send-btn{
  width:100%;margin-top:6px;
  background:linear-gradient(135deg,rgba(212,175,55,.15),rgba(212,175,55,.08));
  border:1px solid rgba(212,175,55,.3);color:#d4af37;
  padding:8px;border-radius:5px;font-family:'Cairo',sans-serif;
  font-weight:700;font-size:.85rem;cursor:pointer;transition:all .2s;
}
.send-btn:hover{background:rgba(212,175,55,.22);border-color:#d4af37}
.send-btn:disabled{opacity:.4;cursor:not-allowed}
.tts-input{
  width:100%;padding:8px 12px;margin-top:8px;
  background:rgba(0,20,10,.4);border:1px solid rgba(0,162,79,.25);
  color:#e8f5ec;border-radius:5px;font-family:'Cairo',sans-serif;
  font-size:.85rem;direction:rtl;
}
.tts-input::placeholder{color:#7a9e84}
.tts-btn{
  width:100%;margin-top:5px;
  background:linear-gradient(135deg,rgba(0,98,51,.2),rgba(0,130,60,.1));
  border:1px solid rgba(0,162,79,.3);color:#00a84f;
  padding:8px;border-radius:5px;font-family:'Cairo',sans-serif;
  font-weight:700;font-size:.85rem;cursor:pointer;transition:all .2s;
}
.tts-btn:hover{background:rgba(0,162,79,.22)}
.section-title{font-size:.78rem;font-weight:700;color:#7a9e84;
  letter-spacing:1px;margin:12px 0 6px;padding-bottom:3px;
  border-bottom:1px solid rgba(0,162,79,.15)}
</style></head><body>
<div class="section-title">🎤 الاستماع للطالب (إدخال صوتي)</div>
<div class="sw">
  <button class="btn mic" id="micBtn" onclick="startListening()">🎤 ابدأ التحدث</button>
  <button class="btn stop" id="stopBtn" onclick="stopListening()" disabled>⏹ إيقاف</button>
  <button class="btn clr" onclick="clearResult()">🗑 مسح</button>
</div>
<div class="result-box" id="result" dir="rtl">انقر على "ابدأ التحدث" وتكلّم...</div>
<div class="status" id="status">جاهز</div>
<button class="send-btn" id="sendBtn" onclick="sendToChat()" disabled>✅ أرسل هذا النص للدردشة</button>

<div class="section-title">🔊 قراءة النص بصوت عالٍ (TTS)</div>
<input class="tts-input" id="ttsInput" placeholder="اكتب أي نص لقراءته بصوت عالٍ..." dir="rtl">
<button class="tts-btn" onclick="speakText()">🔊 استمع</button>

<script>
var recog = null;
var finalText = "";

function initRecog(){
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SR){document.getElementById("status").textContent="⚠️ المتصفح لا يدعم التعرف على الكلام";return null;}
  var r = new SR();
  r.lang = "ar-DZ";
  r.continuous = true;
  r.interimResults = true;
  r.onresult = function(e){
    var interim = "";
    for(var i=e.resultIndex;i<e.results.length;i++){
      if(e.results[i].isFinal) finalText += e.results[i][0].transcript + " ";
      else interim += e.results[i][0].transcript;
    }
    document.getElementById("result").textContent = finalText + interim;
    document.getElementById("sendBtn").disabled = (finalText.trim() === "");
  };
  r.onerror = function(e){
    document.getElementById("status").textContent = "⚠️ خطأ: " + e.error;
    resetBtns();
  };
  r.onend = function(){
    document.getElementById("status").textContent = "توقّف التسجيل";
    resetBtns();
  };
  return r;
}

function startListening(){
  recog = initRecog();
  if(!recog) return;
  finalText = "";
  document.getElementById("result").textContent = "🔴 يستمع...";
  document.getElementById("micBtn").textContent = "🔴 يستمع...";
  document.getElementById("micBtn").classList.add("active");
  document.getElementById("micBtn").disabled = true;
  document.getElementById("stopBtn").disabled = false;
  document.getElementById("status").textContent = "جارٍ التسجيل — تحدّث الآن";
  recog.start();
}

function stopListening(){
  if(recog) recog.stop();
  resetBtns();
}

function resetBtns(){
  document.getElementById("micBtn").textContent = "🎤 ابدأ التحدث";
  document.getElementById("micBtn").classList.remove("active");
  document.getElementById("micBtn").disabled = false;
  document.getElementById("stopBtn").disabled = true;
}

function clearResult(){
  finalText = "";
  document.getElementById("result").textContent = "انقر على 'ابدأ التحدث' وتكلّم...";
  document.getElementById("sendBtn").disabled = true;
  document.getElementById("status").textContent = "تم المسح";
}

function sendToChat(){
  var txt = finalText.trim();
  if(!txt) return;
  // إرسال النص عبر query string ليلتقطه Streamlit
  var url = new URL(window.parent.location.href);
  url.searchParams.set("voice_input", txt);
  url.searchParams.set("voice_ts", Date.now());
  window.parent.history.replaceState(null,"",url.toString());
  document.getElementById("status").textContent = "✅ تم إرسال النص للدردشة!";
  // إعادة تحميل الصفحة الأم
  setTimeout(function(){ window.parent.location.reload(); }, 300);
}

function speakText(){
  var txt = document.getElementById("ttsInput").value.trim();
  if(!txt) return;
  window.speechSynthesis.cancel();
  var u = new SpeechSynthesisUtterance(txt);
  u.lang = "ar";
  u.rate = 0.88;
  u.pitch = 1.0;
  // اختر صوتاً عربياً إن وُجد
  var voices = window.speechSynthesis.getVoices();
  var arVoice = voices.find(v => v.lang.startsWith("ar"));
  if(arVoice) u.voice = arVoice;
  window.speechSynthesis.speak(u);
}

// تحميل الأصوات
window.speechSynthesis.onvoiceschanged = function(){};
</script>
</body></html>"""
    components.html(html, height=340, scrolling=False)


def inject_tts_button(text: str, btn_label: str = "🔊 استمع") -> str:
    """يُنشئ HTML لزر TTS مضمّن في الصفحة"""
    clean = text.replace("'","&#39;").replace('"','&quot;').replace('\n',' ')[:500]
    return (f'<button onclick="if(window.speechSynthesis){{window.speechSynthesis.cancel();'
            f'var u=new SpeechSynthesisUtterance(\'{clean}\');u.lang=\'ar\';u.rate=0.88;'
            f'window.speechSynthesis.speak(u);}}" '
            f'style="background:rgba(0,162,79,.1);border:1px solid rgba(0,162,79,.3);'
            f'color:#00a84f;padding:3px 10px;border-radius:4px;cursor:pointer;'
            f'font-family:Cairo,sans-serif;font-size:.78rem;">{btn_label}</button>')

# ─────────────────────────────────────────────
#  الشريط الجانبي
# ─────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("""<div class="sidebar-header">
  <div class="sb-icon">⚔️</div><h2>مركز القيادة</h2>
  <p>دونيا لابز تك — v3.0</p>
</div>""", unsafe_allow_html=True)

        st.markdown('<div class="sb-section-title">🪖 ملف الفارس</div>', unsafe_allow_html=True)
        name   = st.text_input("الاسم الكامل", key="student_name", placeholder="مثال: يوسف بن علي")
        school = st.text_input("المؤسسة التعليمية", key="school", placeholder="مثال: متوسطة ابن خلدون")

        st.divider()
        st.markdown('<div class="sb-section-title">📊 الدرجات / 20</div>', unsafe_allow_html=True)
        grades = {}
        for subj in SUBJECTS:
            bloom = map_to_bloom(st.session_state.get(f"g_{subj}", 12.0))
            c1, c2 = st.columns([3, 2])
            with c1:
                st.markdown(f'<div class="grade-label"><span style="color:{bloom["color"]}">'
                            f'{bloom["emoji"]}</span> {subj}</div>', unsafe_allow_html=True)
            with c2:
                grades[subj] = st.number_input(subj, 0.0, 20.0, 12.0, 0.5,
                                               key=f"g_{subj}", label_visibility="collapsed")

        st.divider()
        st.markdown('<div class="sb-section-title">🎯 معركة اليوم</div>', unsafe_allow_html=True)
        subject = st.selectbox("اختر المادة", list(SUBJECTS.keys()), key="selected_subject")

        st.divider()
        if grades:
            avg = sum(grades.values())/len(grades)
            ov  = map_to_bloom(avg)
            st.markdown(f"""<div class="bloom-summary">
  <div style="font-size:2rem;text-align:center">{ov['emoji']}</div>
  <div style="text-align:center;font-size:.85rem;font-weight:700;color:{ov['color']}">{ov['badge']}</div>
  <div style="text-align:center;font-size:.7rem;color:#8a9ab0">المعدل: {avg:.1f}/20</div>
</div>""", unsafe_allow_html=True)

        st.divider()
        if st.button("🔄 إعادة الجلسة", use_container_width=True):
            for k in ["messages","val_log","daily_tips","story_output"]:
                st.session_state.pop(k, None)
            st.rerun()

    return name, school, grades, subject

# ─────────────────────────────────────────────
#  لوحة الأداء
# ─────────────────────────────────────────────
def render_dashboard(grades, subject):
    if not grades: return
    avg = sum(grades.values())/len(grades)
    ov  = map_to_bloom(avg)
    wk  = min(grades, key=grades.get)
    st_ = max(grades, key=grades.get)
    fb  = map_to_bloom(grades.get(subject, 12))

    st.markdown('<h3 class="section-title">📊 خريطة المعركة الأكاديمية</h3>', unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    def sc(n,l,col="#d4af37",cls=""):
        return f'<div class="stat-card {cls}"><div class="stat-num" style="color:{col}">{n}</div><div class="stat-lbl">{l}</div></div>'
    with c1: st.markdown(sc(f"{avg:.1f}","المعدل / 20"), unsafe_allow_html=True)
    with c2: st.markdown(sc(ov["badge"],"مستواك العام",ov["color"]), unsafe_allow_html=True)
    with c3: st.markdown(sc(f"{grades[wk]:.1f}",f"⚔️ {wk[:12]}","#e74c3c","danger"), unsafe_allow_html=True)
    with c4: st.markdown(sc(f"{grades[st_]:.1f}",f"👑 {st_[:12]}","#27ae60","success"), unsafe_allow_html=True)

    st.markdown(f"""<div class="focus-card">
  <div class="focus-header">{fb['emoji']} مادة اليوم: <strong>{subject}</strong></div>
  <div class="focus-level" style="color:{fb['color']}">{fb['level']}</div>
  <div class="focus-quote">"{fb['war_quote']}"</div>
  <div class="focus-strategy">🎯 {fb['strategy']}</div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  واجهة الدردشة
# ─────────────────────────────────────────────
def render_chat(name, school, grades, subject):
    if "messages"  not in st.session_state: st.session_state.messages  = []
    if "val_log"   not in st.session_state: st.session_state.val_log   = []

    # استقبال النص الصوتي عبر query params
    qp = st.query_params
    voice_text = qp.get("voice_input", "")
    if voice_text and voice_text not in [m.get("content","") for m in st.session_state.messages]:
        st.session_state["pending_voice"] = voice_text
        st.query_params.clear()

    # رسالة الترحيب
    if not st.session_state.messages and name:
        cd = get_countdown()
        fb = map_to_bloom(grades.get(subject, 12))
        welcome = f"""⚔️ **{name.upper()} — أيها الفارس، بيانات مهمّتك:**

غمّض عينيك لحظة.. تخيّل **يوم 19 جوان** عند رؤية اسمك في قائمة الناجحين.
**هذا المشهد ينتظرك — لكنّه لن يأتيك بل أنت من ستنتزعه.**

📋 **بياناتك الميدانية:**
- 🎯 مادة اليوم: **{subject}** | مستواك: **{fb['level']}**
- ⏳ الوقت: **{cd['days']} يوماً و{cd['hours']} ساعة**

💡 **أوامر متاحة:** اسألني عن {subject} | **خريطة ذهنية** | **خطة دراسية** | **ألهمني**

— بروتوكول فارس | دونيا لابز تك ⚔️🇩🇿"""
        st.session_state.messages.append({"role":"assistant","content":welcome})

    # عرض المحادثة
    for i, msg in enumerate(st.session_state.messages):
        cls = "user-bubble" if msg["role"]=="user" else "ai-bubble"
        av  = "🪖" if msg["role"]=="user" else "⚔️"
        content = msg["content"]

        if msg["role"] == "assistant" and "```mermaid" in content:
            parts = content.split("```mermaid", 1)
            st.markdown(f'<div class="chat-msg {cls}"><span class="ch-avatar">{av}</span>'
                        f'<div class="ch-body">{parts[0]}</div></div>', unsafe_allow_html=True)
            mm = parts[1].split("```",1)[0].strip()
            render_mermaid(mm)
            rest = parts[1].split("```",1)[1] if "```" in parts[1] else ""
            if rest.strip():
                st.markdown(f'<div class="chat-msg {cls}"><div class="ch-body">{rest}</div></div>',
                            unsafe_allow_html=True)
        else:
            tts_btn = inject_tts_button(content) if msg["role"]=="assistant" else ""
            st.markdown(
                f'<div class="chat-msg {cls}">'
                f'<span class="ch-avatar">{av}</span>'
                f'<div class="ch-body">{content}<br>{tts_btn}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    # روابط dzexams
    lnk = DZEXAMS.get(subject,"https://www.dzexams.com/brevet/4am/")
    st.markdown(f"""<div class="resource-box">
  <div class="resource-title">📚 مصادر التدريب الرسمية — {subject}</div>
  <a href="{lnk}" target="_blank" class="dz-btn">📄 امتحانات — {subject}</a>
  <a href="https://www.dzexams.com/brevet/4am/" target="_blank" class="dz-btn">🏛️ مركز BEM</a>
</div>""", unsafe_allow_html=True)

    # سجل التحقق
    if st.session_state.val_log:
        with st.expander("🔬 سجل طبقة التحقق التربوي (Acree)", expanded=False):
            v = st.session_state.val_log[-1]
            c1,c2 = st.columns(2)
            with c1: st.metric("الحالة",v["status"]); st.metric("الثقة",f"{v['confidence']*100:.0f}٪")
            with c2: st.metric("مستوى بلوم",v["bloom_tier"][:18])
            for fl in v["flags"]: st.warning(fl)
            if not v["flags"]: st.success("✅ لا مشكلات تربوية.")

    st.markdown("---")

    # التحقق من API
    client = get_groq_client()
    if not client:
        st.error("🔑 أضف `GROQ_API_KEY` في `.streamlit/secrets.toml`")
        st.code("GROQ_API_KEY = \"gsk_...\"", language="toml")
        return
    if not name:
        st.info("👤 أدخل اسمك في الشريط الجانبي.")
        return

    # استخدام النص الصوتي المعلّق
    pending = st.session_state.pop("pending_voice", None)

    user_input = st.chat_input(f"⚔️ أرسل أمرك لفارس — {subject}...")
    if pending and not user_input:
        user_input = pending
        st.info(f"🎤 تم استقبال: **{user_input}**")

    if user_input:
        actual = user_input
        if any(x in user_input for x in ["قصة إديسون","اديسون"]):
            actual = "أريد قصة إديسون الملهمة بأسلوب سينمائي."
        elif "قصة جزائرية" in user_input:
            actual = "أريد قصة نجاح جزائرية ملهمة."
        elif any(x in user_input for x in ["ألهمني","محتاج تشجيع","أشعر بالإحباط"]):
            actual = "أنا محتاج جرعة إلهامية قوية الآن — أشعر باليأس."

        st.session_state.messages.append({"role":"user","content":user_input})
        with st.spinner("⚔️ فارس يضع استراتيجيته..."):
            sp = build_system_prompt(name, school, grades, subject)
            hist = [{"role":m["role"],"content":m["content"]}
                    for m in st.session_state.messages[-12:]]
            hist[-1]["content"] = actual
            resp = groq_call(hist, system=sp)

        vld = validate_output(resp, subject, grades)
        st.session_state.val_log.append(vld)
        st.session_state.messages.append({"role":"assistant","content":resp})
        st.rerun()

# ─────────────────────────────────────────────
#  تبويب البحث بـ Tavily
# ─────────────────────────────────────────────
def render_search_tab(name: str, subject: str):
    st.markdown('<h3 class="section-title">🔍 البحث الذكي عبر الإنترنت</h3>', unsafe_allow_html=True)
    st.info("ابحث عن أي مفهوم دراسي أو درس وسيجلب فارس أحدث المعلومات من الإنترنت.")

    preset_queries = [
        f"شرح درس {subject} للسنة الرابعة متوسط الجزائر",
        f"تمارين محلولة {subject} BEM الجزائر",
        f"ملخص منهج {subject} 4AM الجزائر",
        "أساليب المراجعة الفعّالة قبل الامتحانات",
        "كيفية إدارة الوقت في امتحان BEM",
    ]
    st.markdown("**اقتراحات سريعة:**")
    cols = st.columns(3)
    for i, q in enumerate(preset_queries[:3]):
        with cols[i]:
            if st.button(q[:35]+"...", key=f"pq_{i}", use_container_width=True):
                st.session_state["search_query"] = q

    query = st.text_input("🔍 أدخل استفسارك",
                          value=st.session_state.get("search_query",""),
                          key="search_input",
                          placeholder=f"مثال: شرح معادلات الدرجة الأولى 4AM...")

    c1, c2 = st.columns([3,1])
    with c1:
        do_search = st.button("🔍 ابحث الآن", use_container_width=True, type="primary")
    with c2:
        ai_summary = st.checkbox("تلخيص AI", value=True)

    if do_search and query.strip():
        with st.spinner("🌐 جارٍ البحث عبر الإنترنت..."):
            results = tavily_search(query)

        if results and "error" not in results[0]:
            st.success(f"✅ تم العثور على {len(results)} نتائج")
            for r in results:
                st.markdown(f"""<div class="res-card">
  <div class="res-header">
    <a href="{r.get('url','#')}" target="_blank" style="color:#00a84f;text-decoration:none">
      🔗 {r.get('title','نتيجة')}
    </a>
  </div>
  <div style="font-size:.82rem;color:#7a9e84;margin:6px 0">{r.get('url','')[:60]}</div>
  <div style="font-size:.88rem;color:#b0d8bc;line-height:1.7">{r.get('content','')[:300]}...</div>
</div>""", unsafe_allow_html=True)

            if ai_summary:
                st.markdown("---")
                st.markdown("### 🤖 ملخص فارس الذكي")
                combined = "\n\n".join([f"المصدر: {r.get('title','')}\n{r.get('content','')[:400]}"
                                        for r in results[:3]])
                summary_prompt = f"""أنت فارس المرشد التعليمي. الطالب {name} بحث عن: "{query}"

نتائج البحث:
{combined}

اكتب بالعربية ملخصاً تعليمياً واضحاً ومفيداً يناسب طالب متوسطة جزائري.
اجعله منظماً، مع نقاط رئيسية، ولا يتجاوز 250 كلمة."""
                with st.spinner("🤖 فارس يحلّل النتائج..."):
                    summary = groq_call([{"role":"user","content":summary_prompt}],
                                        temperature=0.7, max_tokens=500)
                st.markdown(f'<div class="story-card">{summary}</div>', unsafe_allow_html=True)
        else:
            err = results[0].get("error","خطأ غير معروف") if results else "لا نتائج"
            st.error(f"⚠️ {err}")
            st.info("أضف `TAVILY_API_KEY` في `.streamlit/secrets.toml`\n\n"
                    "احصل على مفتاح مجاني: https://tavily.com")

# ─────────────────────────────────────────────
#  خزانة الملفات
# ─────────────────────────────────────────────
def render_file_vault():
    st.markdown('<h3 class="section-title">📁 خزانة الملفات الدراسية</h3>', unsafe_allow_html=True)
    st.info("ارفع ملفاتك الدراسية (PDF، صور، ملاحظات) وأدِرها من هنا.")

    if "vault_files" not in st.session_state:
        st.session_state.vault_files = {}

    # رفع الملفات
    st.markdown("### 📤 رفع ملف جديد")
    uploaded = st.file_uploader(
        "اختر ملفاً",
        type=["pdf","png","jpg","jpeg","txt","docx","xlsx","mp3","mp4"],
        key="vault_upload",
        help="يدعم: PDF، صور، نصوص، Word، Excel"
    )
    col_subj, col_note = st.columns(2)
    with col_subj:
        file_subject = st.selectbox("المادة المرتبطة", ["عام"]+list(SUBJECTS.keys()), key="file_subj")
    with col_note:
        file_note = st.text_input("ملاحظة (اختياري)", key="file_note", placeholder="مثال: ملخص الفصل الثاني")

    if st.button("📥 حفظ في الخزانة", use_container_width=True) and uploaded:
        file_data = {
            "name":    uploaded.name,
            "type":    uploaded.type,
            "size":    uploaded.size,
            "subject": file_subject,
            "note":    file_note,
            "data":    base64.b64encode(uploaded.read()).decode(),
            "date":    datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        fid = f"{datetime.now().timestamp():.0f}"
        st.session_state.vault_files[fid] = file_data
        st.success(f"✅ تم حفظ '{uploaded.name}' في الخزانة!")

    st.markdown("---")

    # عرض الملفات المحفوظة
    if not st.session_state.vault_files:
        st.markdown('<div class="story-card" style="text-align:center;color:#7a9e84">'
                    '📂 الخزانة فارغة — ارفع ملفاتك الدراسية للبدء</div>', unsafe_allow_html=True)
        return

    st.markdown(f"### 📂 ملفاتك المحفوظة ({len(st.session_state.vault_files)} ملف)")

    # فلترة
    filter_subj = st.selectbox("فلترة حسب المادة", ["الكل"]+list(SUBJECTS.keys()), key="vault_filter")

    files = st.session_state.vault_files
    cols = st.columns(2)
    col_idx = 0

    for fid, f in list(files.items()):
        if filter_subj != "الكل" and f["subject"] != filter_subj:
            continue

        size_kb = f["size"] / 1024
        icon = ("📄" if "pdf" in f["type"] else
                "🖼️" if "image" in f["type"] else
                "📝" if "text" in f["type"] else "📎")

        # زر التحميل
        file_bytes = base64.b64decode(f["data"])
        b64 = base64.b64encode(file_bytes).decode()
        dl_link = (f'<a href="data:{f["type"]};base64,{b64}" download="{f["name"]}" '
                   f'class="res-link">⬇️ تحميل</a>')

        with cols[col_idx % 2]:
            st.markdown(f"""<div class="res-card">
  <div class="res-header">
    <span>{icon} {f['name'][:30]}</span>
    <span style="color:#7a9e84;font-size:.72rem">{size_kb:.1f} KB</span>
  </div>
  <div style="font-size:.75rem;color:#7a9e84;margin:4px 0">
    📚 {f['subject']} | 📅 {f['date']}
  </div>
  {f'<div style="font-size:.78rem;color:#b0d8bc">💬 {f["note"]}</div>' if f["note"] else ""}
  <div style="margin-top:8px">{dl_link}</div>
</div>""", unsafe_allow_html=True)

            if st.button("🗑 حذف", key=f"del_{fid}"):
                del st.session_state.vault_files[fid]
                st.rerun()

        col_idx += 1

# ─────────────────────────────────────────────
#  نصائح اليوم
# ─────────────────────────────────────────────
def render_daily_tips_tab(name, grades, subject):
    st.markdown('<h3 class="section-title">💡 نصائح ومحفّزات اليوم</h3>', unsafe_allow_html=True)
    st.caption(f"📅 {datetime.now().strftime('%A %d %B %Y')} — مولّدة بالذكاء الاصطناعي")

    if st.button("🔄 توليد نصائح جديدة", use_container_width=True):
        st.session_state.pop("daily_tips", None)

    client = get_groq_client()
    if not client:
        st.error("🔑 أضف مفتاح Groq API في secrets.toml")
        return

    with st.spinner("💡 فارس يعدّ نصائحك اليومية..."):
        tips = get_daily_tips(name or "الفارس", grades, subject)

    st.markdown(f'<div class="story-card">{tips}</div>', unsafe_allow_html=True)

    # ──  جدول الدراسة اليومي السريع ──
    st.markdown("---")
    st.markdown("### ⏰ جدول الدراسة المقترح لهذا اليوم")

    avg = sum(grades.values())/len(grades) if grades else 12
    bloom = map_to_bloom(avg)

    schedule = [
        ("🌅 الفجر — الصباح الباكر", "07:00–07:30", "مراجعة خفيفة وقراءة الملاحظات"),
        (f"📚 الجلسة الأولى — {subject}", "09:00–10:00", f"دراسة مركّزة | {bloom['strategy'][:60]}"),
        ("☕ راحة", "10:00–10:15", "استراحة قصيرة — ماء وتنفس عميق"),
        ("📝 الجلسة الثانية — تمارين", "10:15–11:15", f"تمارين من dzexams.com على {subject}"),
        ("🍽️ الظهيرة", "13:00–14:30", "راحة وصلاة وغداء — أجسامنا تحتاج وقوداً"),
        ("📖 الجلسة الثالثة — مراجعة", "15:00–16:00", "مراجعة ما درسته اليوم وتصحيح الأخطاء"),
        ("🌙 المراجعة الليلية", "20:00–21:00", "مراجعة نهائية وكتابة ملخص قصير"),
    ]

    for session in schedule:
        st.markdown(f"""<div class="res-card" style="margin-bottom:6px;padding:10px 14px">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <span style="font-weight:700;color:#e8f5ec">{session[0]}</span>
    <span style="color:#d4af37;font-size:.82rem;font-family:monospace">{session[1]}</span>
  </div>
  <div style="font-size:.8rem;color:#7a9e84;margin-top:4px">{session[2]}</div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  قصص AI
# ─────────────────────────────────────────────
def render_stories_tab(name, grades, subject):
    st.markdown('<h3 class="section-title">🎬 مكتبة الإلهام السينمائي</h3>', unsafe_allow_html=True)

    # القصص الثابتة
    stories = {
        "💡 إديسون — عندما يصبح الفشل وقوداً": """
في عام 1879، فشل توماس إديسون **أكثر من ألف مرة** قبل اختراع المصباح.

صحفي سأله: *"كيف تشعر بعد ألف فشل؟"*

فأجابه إديسون: **"لم أفشل ألف مرة. اكتشفت ألف طريقة لا تنجح."**

وفي الليلة الألف وواحد... أضاء العالم.

🎯 **لك أيها الفارس:** كل مسألة لا تحلّها اليوم هي خطوة نحو حلّها غداً.""",

        "🏆 الصمود — قصة المثابرة": """
رفضته عشرون مدرسة. قالوا: *"أنت لستَ للنجاح."*

لكنه كان يُكرّر كل صباح: **"ما دامت يدايَ تتحركان، القلم يكتب، والحلم لا يموت."**

في السنة التي يأس فيها الجميع... أثبت للعالم أنهم أخطأوا.

🎯 **لك:** من قال إن درجة الأمس تُحدّد مصير الغد؟ النتيجة ليست قراراً نهائياً.""",

        "🇩🇿 فارس جزائري — من الأوراس إلى القمة": """
في قرية صغيرة، بعيدة عن المدن، طالب لم يملك إلا دفتراً وقلماً وإرادة من فولاذ.

كهرباء متقطعة. لا إنترنت. لا دروس خصوصية.
كان يقرأ على ضوء الشمعة حتى تُسوّد الصفحات.

يوم النتائج... **اسمه كان الأول في الولاية.**

سُئل: "ما سرّك؟" فقال: **"لم أنافس أحداً سواي."**

🎯 **لك:** إن كان هو قادراً بلا وسائل... فما عذرك وأنت تملك كل الأدوات؟""",
    }

    for title, story in stories.items():
        with st.expander(title, expanded=(title == list(stories.keys())[2])):
            st.markdown(f'<div class="story-card">{story}</div>', unsafe_allow_html=True)

    # ── توليد قصة AI مخصصة ──
    st.markdown("---")
    st.markdown("### 🤖 توليد قصتك الخاصة بالذكاء الاصطناعي")
    st.caption("قصة سينمائية مخصصة لك أنت — بطلها يحمل اسمك.")

    client = get_groq_client()
    if not client:
        st.error("🔑 أضف مفتاح Groq API")
        return

    focus_grade = grades.get(subject, 12)
    c1, c2 = st.columns(2)
    with c1:
        story_subject = st.selectbox("المادة في القصة", list(SUBJECTS.keys()),
                                      index=list(SUBJECTS.keys()).index(subject),
                                      key="story_subj")
    with c2:
        story_style = st.selectbox("أسلوب القصة",
                                    ["سينمائي مشوّق","حماسي قصير","شعري وعاطفي","واقعي جزائري"],
                                    key="story_style")

    if st.button("✨ ولّد قصتي الآن", use_container_width=True, type="primary"):
        with st.spinner("🎬 فارس يكتب قصتك السينمائية..."):
            bloom = map_to_bloom(grades.get(story_subject, 12))
            prompt = (f"أنت كاتب قصصي. اكتب قصة {story_style} بالعربية (200-250 كلمة) عن "
                      f"طالب جزائري اسمه '{name or 'الفارس'}' يواجه صعوبات في '{story_subject}' "
                      f"(مستوى {bloom['badge']})، يصارع ثم ينتصر في BEM 2026. "
                      f"الأسلوب: {story_style}. النهاية: منتصرة ومؤثرة.")
            story = groq_call([{"role":"user","content":prompt}], temperature=0.93, max_tokens=550)
        st.session_state["story_output"] = story
        st.rerun()

    if "story_output" in st.session_state:
        st.markdown(f'<div class="story-card">{st.session_state["story_output"]}</div>',
                    unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  هرم بلوم + دليل الاستخدام
# ─────────────────────────────────────────────
def render_guide_tab():
    st.markdown('<h3 class="section-title">📖 دليل الاستخدام وهرم بلوم</h3>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔺 ما هو هرم بلوم؟", "📋 دليل الاستخدام"])

    with tab1:
        st.markdown("""<div class="story-card">
<h4 style="color:#d4af37;margin-bottom:12px">🔺 هرم بلوم التعليمي — تصنيف المهارات المعرفية</h4>
<p style="color:#b0d8bc;line-height:1.9;margin-bottom:14px">
هرم بلوم هو نموذج تربوي طوّره <strong>بنجامين بلوم</strong> عام 1956 لتصنيف مستويات التفكير
من البسيط إلى المعقد. يُستخدم عالمياً لتصميم المناهج وتقييم الطلاب.
</p>
</div>""", unsafe_allow_html=True)

        bloom_levels = [
            ("👑","الإبداع (Creating)","#27ae60","المستوى السادس — الأعلى",
             "توليد أفكار جديدة، تصميم، إنتاج، بناء حلول مبتكرة.",
             "مثال: ابتكار طريقة جديدة لحل معادلة، كتابة نص إبداعي أصيل."),
            ("🏅","التقييم (Evaluating)","#2ecc71","المستوى الخامس",
             "الحكم على الأفكار، تقييم الحلول، الدفاع عن الآراء بأدلة.",
             "مثال: تقييم صحة إجابة، المقارنة بين طريقتين لحل مسألة."),
            ("🔬","التحليل (Analyzing)","#f39c12","المستوى الرابع",
             "تفكيك المعلومات لفهم العلاقات والمبادئ الخفية.",
             "مثال: تحليل نص أدبي، تفسير نتائج تجربة علمية."),
            ("🔧","التطبيق (Applying)","#e67e22","المستوى الثالث",
             "استخدام المعلومات في مواقف جديدة وحل مسائل.",
             "مثال: تطبيق قانون رياضي على مسألة، كتابة جملة بقاعدة نحوية."),
            ("💡","الفهم (Understanding)","#e74c3c","المستوى الثاني",
             "شرح الأفكار وتفسيرها بأسلوب خاص.",
             "مثال: إعادة صياغة درس بكلماتك، شرح مفهوم لزميل."),
            ("📌","التذكّر (Remembering)","#c0392b","المستوى الأول — القاعدة",
             "استرجاع المعلومات الأساسية، الحفظ، التعرف.",
             "مثال: حفظ القواعد، تعريفات المصطلحات، الصيغ الرياضية."),
        ]

        for emoji, name_lvl, color, level_label, desc, ex in bloom_levels:
            st.markdown(f"""<div class="res-card" style="border-right:4px solid {color};margin-bottom:8px">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
    <span style="font-size:1.5rem">{emoji}</span>
    <div>
      <div style="font-size:1rem;font-weight:700;color:{color}">{name_lvl}</div>
      <div style="font-size:.72rem;color:#7a9e84">{level_label}</div>
    </div>
  </div>
  <div style="font-size:.85rem;color:#b0d8bc;line-height:1.7;margin-bottom:4px">{desc}</div>
  <div style="font-size:.78rem;color:#7a9e84;font-style:italic">{ex}</div>
</div>""", unsafe_allow_html=True)

        st.markdown("""<div class="story-card" style="margin-top:12px">
<h4 style="color:#d4af37">⚔️ كيف يستخدمها فارس؟</h4>
<p style="color:#b0d8bc;line-height:1.9;margin-top:8px">
يحلّل فارس تلقائياً درجاتك ويضعك في المستوى المناسب:
<br>• <strong style="color:#e74c3c">أقل من 10/20</strong> → محارب (التذكّر والفهم) — أولوية الأساسيات
<br>• <strong style="color:#f39c12">10 إلى 14/20</strong> → قائد (التطبيق والتحليل) — أولوية الممارسة
<br>• <strong style="color:#27ae60">14 وما فوق</strong> → فارس النخبة (التقييم والإبداع) — أولوية الكمال
<br><br>كلما ارتفع مستواك في هرم بلوم، كلما اقتربت من درجات الامتياز في BEM 2026.
</p>
</div>""", unsafe_allow_html=True)

        # مخطط Mermaid
        st.markdown("### المخطط البياني لهرم بلوم")
        render_mermaid("""mindmap
  root((هرم بلوم))
    المستوى السادس
      الإبداع
        توليد
        تصميم
    المستوى الخامس
      التقييم
        الحكم
        المقارنة
    المستوى الرابع
      التحليل
        التفكيك
        التفسير
    المستوى الثالث
      التطبيق
        الاستخدام
        التنفيذ
    المستوى الثاني
      الفهم
        الشرح
        الإعادة
    المستوى الأول
      التذكّر
        الحفظ
        التعرف""", height=420)

    with tab2:
        st.markdown("""<div class="story-card">
<h4 style="color:#d4af37;margin-bottom:16px">📋 دليل الاستخدام الشامل — فارس BEM 2026</h4>

<h5 style="color:#00a84f;margin:14px 0 8px">1️⃣ الإعداد الأولي</h5>
<ul style="color:#b0d8bc;line-height:2;padding-right:20px">
  <li>أدخل <strong>اسمك ومؤسستك</strong> في الشريط الجانبي الأيمن</li>
  <li>أدخل <strong>درجاتك في كل مادة</strong> (من 0 إلى 20)</li>
  <li>اختر <strong>مادة اليوم</strong> التي ستركّز عليها</li>
  <li>سيحلّل فارس مستواك تلقائياً بهرم بلوم</li>
</ul>

<h5 style="color:#00a84f;margin:14px 0 8px">2️⃣ غرفة المعارك (الدردشة)</h5>
<ul style="color:#b0d8bc;line-height:2;padding-right:20px">
  <li>اكتب سؤالك أو طلبك بالعربية</li>
  <li>اكتب <strong>"خريطة ذهنية"</strong> لتوليد مخطط بصري للدرس</li>
  <li>اكتب <strong>"خطة دراسية"</strong> لجدول يومي مُحكم</li>
  <li>اكتب <strong>"ألهمني"</strong> لجرعة حماسية</li>
  <li>انقر على <strong>🔊 استمع</strong> أسفل كل رد لسماعه صوتياً</li>
</ul>

<h5 style="color:#00a84f;margin:14px 0 8px">3️⃣ التحدث والاستماع (الصوت)</h5>
<ul style="color:#b0d8bc;line-height:2;padding-right:20px">
  <li>انقر <strong>🎤 ابدأ التحدث</strong> وتحدّث بالعربية</li>
  <li>سيتعرف التطبيق على كلامك ويحوّله لنص</li>
  <li>انقر <strong>✅ أرسل للدردشة</strong> لإرسال نصك</li>
  <li>يمكنك إدخال أي نص لقراءته بصوت عالٍ (TTS)</li>
  <li><strong>⚠️ ملاحظة:</strong> يتطلب متصفح Chrome أو Edge لأفضل تجربة</li>
</ul>

<h5 style="color:#00a84f;margin:14px 0 8px">4️⃣ البحث الذكي (Tavily)</h5>
<ul style="color:#b0d8bc;line-height:2;padding-right:20px">
  <li>ابحث عن أي درس أو مفهوم عبر الإنترنت</li>
  <li>فارس يلخّص النتائج تلقائياً بالعربية</li>
  <li>يتطلب مفتاح TAVILY_API_KEY في secrets.toml</li>
</ul>

<h5 style="color:#00a84f;margin:14px 0 8px">5️⃣ خزانة الملفات</h5>
<ul style="color:#b0d8bc;line-height:2;padding-right:20px">
  <li>ارفع ملفاتك الدراسية (PDF، صور، نصوص)</li>
  <li>نظّمها حسب المادة وأضف ملاحظات</li>
  <li>حمّلها متى شئت</li>
</ul>

<h5 style="color:#00a84f;margin:14px 0 8px">6️⃣ إعداد المفاتيح (secrets.toml)</h5>
<div style="background:#0a1a0d;border:1px solid rgba(0,162,79,.2);
  border-radius:4px;padding:12px;font-family:monospace;font-size:.82rem;
  color:#b0d8bc;margin-top:6px;direction:ltr;text-align:left">
# .streamlit/secrets.toml<br>
GROQ_API_KEY = "gsk_..."<br>
TAVILY_API_KEY = "tvly-..."
</div>
<ul style="color:#7a9e84;line-height:2;padding-right:20px;margin-top:8px;font-size:.82rem">
  <li>Groq مجاني: <a href="https://console.groq.com" style="color:#00a84f">console.groq.com</a></li>
  <li>Tavily مجاني: <a href="https://tavily.com" style="color:#00a84f">tavily.com</a></li>
</ul>

</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  خزينة الموارد
# ─────────────────────────────────────────────
def render_resources_tab(grades):
    st.markdown('<h3 class="section-title">📚 خزينة الموارد الرسمية</h3>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (subj, link) in enumerate(DZEXAMS.items()):
        bloom = map_to_bloom(grades.get(subj, 12))
        with cols[i % 2]:
            st.markdown(f"""<div class="res-card">
  <div class="res-header">
    <span>{subj}</span>
    <span style="color:{bloom['color']};font-size:.78rem">{bloom['badge']}</span>
  </div>
  <a href="{link}" target="_blank" class="res-link">📄 امتحانات وتمارين ←</a>
  <div class="res-grade">الدرجة: {grades.get(subj, 12):.1f}/20</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="footer-brand">
  <div class="footer-logo">⚔️🇩🇿⚔️</div>
  <h3>فارس BEM 2026 — v3.0</h3>
  <p>دونيا لابز تك — مختبر الأفكار الذكية</p>
  <div class="footer-tags">
    <span>llama-3.3-70b-versatile ✅</span>
    <span>Tavily Search</span>
    <span>Web Speech API</span>
    <span>خزانة الملفات</span>
    <span>هرم بلوم</span>
    <span>مناهج وزارة التربية الجزائرية</span>
  </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  التطبيق الرئيسي
# ─────────────────────────────────────────────
def main():
    render_hero()
    name, school, grades, subject = render_sidebar()

    tabs = st.tabs([
        "⚔️ غرفة المعارك",
        "🎤 التحدث والاستماع",
        "🔍 البحث الذكي",
        "📁 خزانة الملفات",
        "🗺️ الخرائط الذهنية",
        "🎬 الإلهام والقصص",
        "💡 نصائح اليوم",
        "📚 الموارد",
        "📖 الدليل وبلوم",
    ])

    with tabs[0]:
        render_dashboard(grades, subject)
        st.markdown("---")
        render_chat(name, school, grades, subject)

    with tabs[1]:
        st.markdown('<h3 class="section-title">🎤 التحدث والاستماع</h3>', unsafe_allow_html=True)
        st.info("تحدّث بالعربية وسيتعرف التطبيق على كلامك، أو أدخل نصاً لسماعه بصوت عالٍ.")
        render_speech_widget()
        st.markdown("---")
        st.markdown("### 🔊 قراءة آخر رد من فارس")
        if st.session_state.get("messages"):
            last_ai = next((m["content"] for m in reversed(st.session_state.messages)
                           if m["role"]=="assistant"), None)
            if last_ai:
                clean = last_ai[:400].replace("**","").replace("*","").replace("#","")
                st.markdown(f'<div class="story-card" style="font-size:.9rem">{clean[:300]}...</div>',
                            unsafe_allow_html=True)
                st.markdown(inject_tts_button(clean, "🔊 اقرأ الرد الأخير من فارس"),
                            unsafe_allow_html=True)

    with tabs[2]:
        render_search_tab(name, subject)

    with tabs[3]:
        render_file_vault()

    with tabs[4]:
        st.markdown('<h3 class="section-title">🗺️ مولّد الخرائط الذهنية</h3>', unsafe_allow_html=True)
        default = f"""mindmap
  root(({subject}))
    المحور الأول
      فرع 1
      فرع 2
    المحور الثاني
      فرع 3
      فرع 4
    المحور الثالث
      فرع 5"""
        mm = st.text_area("كود Mermaid", value=default, height=250)
        if st.button("🗺️ عرض الخريطة", use_container_width=True):
            render_mermaid(mm)
        if get_groq_client() and st.button("🤖 توليد خريطة بالذكاء الاصطناعي", use_container_width=True):
            topic = st.text_input("موضوع الخريطة", value=subject, key="mm_topic")
            with st.spinner("🗺️ فارس يرسم الخريطة..."):
                sp = build_system_prompt(name or "الفارس", school or "", grades, subject)
                resp = groq_call([{"role":"user",
                                   "content":f"ولّد خريطة ذهنية Mermaid mindmap لدرس: {topic}"}],
                                  system=sp, max_tokens=600)
            if "```mermaid" in resp:
                code = resp.split("```mermaid",1)[1].split("```",1)[0].strip()
                render_mermaid(code)

    with tabs[5]:
        render_stories_tab(name, grades, subject)

    with tabs[6]:
        render_daily_tips_tab(name, grades, subject)

    with tabs[7]:
        render_resources_tab(grades)

    with tabs[8]:
        render_guide_tab()


if __name__ == "__main__":
    main()

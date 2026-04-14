"""
╔══════════════════════════════════════════════════════════════════╗
║       فارس BEM 2026  —  الإصدار الاستثنائي                      ║
║       DONIA LABS TECH — مختبر الأفكار الذكية                    ║
║       النسخة الإلهامية الكاملة | اللغة العربية 100٪             ║
╚══════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import os
import re

# ─────────────────────────────────────────────
#  إعدادات الصفحة
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="فارس BEM 2026 | دونيا لابز تك",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_bar="expanded",
)

# ─────────────────────────────────────────────
#  تحميل CSS المخصص
# ─────────────────────────────────────────────
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ─────────────────────────────────────────────
#  ثوابت المنظومة
# ─────────────────────────────────────────────
BEM_DATE = datetime(2026, 5, 19, 8, 0, 0)

SUBJECTS = {
    "الرياضيات":           "mathematiques",
    "اللغة العربية":       "arabe",
    "اللغة الفرنسية":      "francais",
    "اللغة الإنجليزية":    "anglais",
    "العلوم الفيزيائية":   "physique",
    "علوم الطبيعة والحياة":"sciences-naturelles",
    "التاريخ والجغرافيا":  "histoire-geographie",
    "التربية الإسلامية":   "education-islamique",
    "التربية المدنية":     "education-civique",
    "التكنولوجيا":         "technologie",
}

DZEXAMS_LINKS = {
    "الرياضيات":           "https://www.dzexams.com/brevet/4am/mathematiques/",
    "اللغة العربية":       "https://www.dzexams.com/brevet/4am/arabe/",
    "اللغة الفرنسية":      "https://www.dzexams.com/brevet/4am/francais/",
    "اللغة الإنجليزية":    "https://www.dzexams.com/brevet/4am/anglais/",
    "العلوم الفيزيائية":   "https://www.dzexams.com/brevet/4am/physique/",
    "علوم الطبيعة والحياة":"https://www.dzexams.com/brevet/4am/sciences-naturelles/",
    "التاريخ والجغرافيا":  "https://www.dzexams.com/brevet/4am/histoire-geo/",
    "التربية الإسلامية":   "https://www.dzexams.com/brevet/4am/education-islamique/",
    "التربية المدنية":     "https://www.dzexams.com/brevet/4am/education-civique/",
    "التكنولوجيا":         "https://www.dzexams.com/brevet/4am/technologie/",
}

# ─────────────────────────────────────────────
#  مكتبة قصص النجاح الملهمة
# ─────────────────────────────────────────────
SUCCESS_STORIES = {
    "edison": {
        "title": "💡 توماس إديسون — عندما يصبح الفشل وقوداً",
        "story": """
في عام 1879، كانت مختبرات مينلو بارك تضجّ بالدخان والخيبات.
توماس إديسون فشل **أكثر من ألف مرة** في اختراع المصباح الكهربائي.

صحفي سأله ذات يوم بسخرية: *"كيف تشعر بعد ألف فشل؟"*

فأجابه إديسون بهدوء المنتصرين:
**"لم أفشل ألف مرة. اكتشفت ألف طريقة لا تنجح."**

وفي الليلة الألف وواحد... أضاء العالم.

🎯 **الرسالة لك أيها الفارس:**
كل مسألة لا تحلّها اليوم هي خطوة نحو حلّها غداً.
الفشل ليس نهاية الطريق — إنه منعطف يقودك للصواب.
        """,
    },
    "stewart": {
        "title": "🏆 الصمود — قصة المثابرة ضد المستحيل",
        "story": """
كان الطريق أمامه مسدوداً من كل الجهات.
رفضته عشرون مدرسة. قالوا له: *"أنت لستَ للنجاح."*

لكنه لم يسمع. كان يُكرّر لنفسه كل صباح:
**"ما دامت يدايَ تتحركان، فالقلم يكتب، والحلم لا يموت."**

في السنة التي يأس فيها الجميع... أثبت للعالم أنهم أخطأوا.

🎯 **الرسالة لك أيها الفارس:**
من قال لك إن درجة الأمس تُحدّد مصير الغد؟
النتيجة ليست قراراً نهائياً — إنها **نقطة انطلاق.**
        """,
    },
    "algerian_hero": {
        "title": "🇩🇿 فارس جزائري — من أعماق الأوراس إلى قمة النجاح",
        "story": """
في قرية صغيرة، بعيدة عن مراكز المدن،
طالب لم يكن يملك إلا دفتراً وقلماً وإرادة من فولاذ.

كهرباء متقطعة. لا إنترنت. لا دروس خصوصية.
لكنه كان يقرأ على ضوء الشمعة حتى تُسوّد الصفحات.

يوم النتائج... **اسمه كان الأول في الولاية.**

سُئل: "ما سرّك؟"
فقال: **"لم أنافس أحداً سواي. كنتُ كل يوم أتفوق على نفسي بالأمس."**

🎯 **الرسالة لك أيها الفارس:**
إن كان هو قادراً، وأنت في مدينة بها كل الأدوات...
**فما عذرك؟ الميدان أمامك. الشرف ينتظر.**
        """,
    },
}

# ─────────────────────────────────────────────
#  محرك بلوم التعليمي (عربي)
# ─────────────────────────────────────────────
def map_to_bloom(grade: float) -> dict:
    """تصنيف الدرجة حسب تصنيف بلوم بالمصطلحات العربية."""
    if grade < 10:
        return {
            "level":    "⚔️ محارب — المستوى الأول",
            "label":    "التذكّر والفهم",
            "color":    "#e74c3c",
            "badge":    "محارب",
            "emoji":    "⚔️",
            "strategy": (
                "الأولوية القصوى: سدّ الثغرات الأساسية فوراً. "
                "ركّز على الحفظ والفهم العميق للقواعد والتعريفات. "
                "استخدم تقنية التكرار المتباعد. "
                "خصّص 60 دقيقة يومياً على الأقل لهذه المادة."
            ),
            "bloom_ar": ["التذكّر", "الفهم"],
            "intensity": "عالية جداً",
            "war_quote": "الميدان يحتاج جندياً يتدرّب حتى يتقن، لا جندياً يتمنّى النصر.",
        }
    elif grade < 14:
        return {
            "level":    "🛡️ قائد — المستوى الثاني",
            "label":    "التطبيق والتحليل",
            "color":    "#f39c12",
            "badge":    "قائد",
            "emoji":    "🛡️",
            "strategy": (
                "الأولوية: إتقان حل المسائل وأنماط الامتحانات. "
                "تدرّب على أسئلة السنوات الماضية. "
                "حدّد الأنماط المتكررة في كل مادة. "
                "خصّص 45 دقيقة يومياً للتطبيق المركّز."
            ),
            "bloom_ar": ["التطبيق", "التحليل"],
            "intensity": "متوسطة",
            "war_quote": "القائد لا يكتفي بالفهم — يُطبّق، يُحلّل، يُبدع الحلول.",
        }
    else:
        return {
            "level":    "👑 فارس النخبة — المستوى الثالث",
            "label":    "التقييم والإبداع",
            "color":    "#27ae60",
            "badge":    "فارس النخبة",
            "emoji":    "👑",
            "strategy": (
                "الأولوية: الوصول للكمال وصفر الأخطاء. "
                "تحدّ نفسك بمسائل مركّبة وصعبة. "
                "علّم زملاءك لترسّخ معرفتك. "
                "30 دقيقة يومياً للصقل والتميّز."
            ),
            "bloom_ar": ["التقييم", "الإبداع"],
            "intensity": "صيانة",
            "war_quote": "النخبة لا تتوقف عند النجاح — تسعى للأفضل دائماً.",
        }

# ─────────────────────────────────────────────
#  محرك العدّ التنازلي
# ─────────────────────────────────────────────
def get_countdown() -> dict:
    """حساب الوقت المتبقي لامتحان BEM 2026 بدقة."""
    now = datetime.now()
    delta = BEM_DATE - now
    if delta.total_seconds() <= 0:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
    total_seconds = int(delta.total_seconds())
    return {
        "days":    delta.days,
        "hours":   (total_seconds % 86400) // 3600,
        "minutes": (total_seconds % 3600)  // 60,
        "seconds": total_seconds % 60,
    }

# ─────────────────────────────────────────────
#  طبقة التحقق التربوي (Acree)
# ─────────────────────────────────────────────
def validate_pedagogical_output(response: str, subject: str, grades: dict) -> dict:
    """
    طبقة التحقق الثانوية — تضمن جودة المخرجات التربوية
    وتوافقها مع مناهج وزارة التربية الوطنية الجزائرية.
    """
    flags = []
    confidence = 1.0

    # القاعدة 1: فحص الأرقام غير الموثقة
    if re.search(r"\b(20[0-9]{2})\b", response):
        years = re.findall(r"\b(20[0-9]{2})\b", response)
        suspicious = [y for y in years if y not in ["2026", "2025", "2024"]]
        if suspicious:
            flags.append(f"⚠️ أرقام سنوات غير موثقة: {suspicious}")
            confidence -= 0.10

    # القاعدة 2: التحقق من توافق المادة
    subject_keywords = {
        "الرياضيات":          ["معادلة", "مثلث", "حساب", "دالة", "هندسة", "جبر"],
        "اللغة العربية":      ["إعراب", "نحو", "صرف", "نص", "قراءة", "تعبير"],
        "اللغة الفرنسية":     ["conjugaison", "grammaire", "texte", "rédaction"],
        "العلوم الفيزيائية":  ["كهرباء", "قوة", "طاقة", "دارة", "ضوء", "صوت"],
        "علوم الطبيعة والحياة":["خلية", "تكاثر", "هضم", "تنفس", "نبات", "حيوان"],
        "التاريخ والجغرافيا": ["ثورة", "استقلال", "خريطة", "مناخ", "حضارة"],
    }
    kws = subject_keywords.get(subject, [])
    if kws:
        hits = sum(1 for k in kws if k in response)
        if hits == 0 and len(response) > 200:
            flags.append(f"⚠️ الإجابة قد لا تتضمن مفردات مادة '{subject}'.")
            confidence -= 0.12

    # القاعدة 3: تناسق مستوى بلوم
    avg = sum(grades.values()) / len(grades) if grades else 12
    bloom = map_to_bloom(avg)
    if bloom["intensity"] == "عالية جداً" and ("متقدم" in response or "صعب جداً" in response):
        flags.append("⚠️ مستوى صعوبة المحتوى قد يتجاوز المستوى الحالي للطالب.")
        confidence -= 0.08

    # القاعدة 4: التحقق من الحياد التربوي
    if any(w in response.lower() for w in ["لا يمكنك", "أنت ضعيف", "مستحيل"]):
        flags.append("⚠️ الرد قد يحتوي على أسلوب سلبي يضرّ بالدافعية.")
        confidence -= 0.15

    confidence = max(0.0, round(confidence, 2))
    status = "✅ مُتحقَّق منه" if confidence >= 0.75 else "⚠️ يستوجب المراجعة"

    return {
        "status":     status,
        "confidence": confidence,
        "flags":      flags,
        "bloom_tier": bloom["level"],
    }

# ─────────────────────────────────────────────
#  رسم خرائط ميرميد
# ─────────────────────────────────────────────
def render_mermaid(mermaid_code: str, height: int = 520):
    """عرض مخططات Mermaid.js بالسمة الجزائرية الداكنة."""
    html = f"""
<div style="
  background: #060d18;
  border-radius: 10px;
  padding: 20px;
  border: 1px solid rgba(0,130,60,0.4);
  box-shadow: 0 0 30px rgba(0,130,60,0.1);
  overflow: auto;
  direction: ltr;
">
  <div class="mermaid">{mermaid_code}</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'dark',
    themeVariables: {{
      primaryColor:        '#00823c',
      primaryTextColor:    '#f5f5f5',
      primaryBorderColor:  '#00823c',
      lineColor:           '#d4af37',
      secondaryColor:      '#0d2818',
      tertiaryColor:       '#060d18',
      background:          '#060d18',
      mainBkg:             '#0d2818',
      nodeBorder:          '#00823c',
      clusterBkg:          '#0d2818',
      titleColor:          '#d4af37',
      edgeLabelBackground: '#060d18',
      fontFamily:          'Cairo, Tajawal, sans-serif',
    }},
    mindmap: {{ padding: 18 }},
    securityLevel: 'loose',
  }});
</script>
"""
    components.html(html, height=height, scrolling=True)

# ─────────────────────────────────────────────
#  الـ SYSTEM PROMPT — بروتوكول فارس
# ─────────────────────────────────────────────
def build_system_prompt(name: str, school: str, grades: dict, subject: str) -> str:
    bloom_map = {s: map_to_bloom(g) for s, g in grades.items()}
    grades_str = "\n".join(
        f"  • {s}: {g}/20 ← {bloom_map[s]['badge']}"
        for s, g in grades.items()
    )
    cd = get_countdown()
    weakest = min(grades, key=grades.get) if grades else subject
    strongest = max(grades, key=grades.get) if grades else subject
    focus_grade = grades.get(subject, 12)
    focus_bloom = map_to_bloom(focus_grade)

    return f"""
أنت **فارس** — المرشد الاستراتيجي الأعلى لمنصة DONIA LABS TECH.
صوتك سينمائي، حازم، ملهم، وعربي أصيل.
مهمّتك: قيادة الطالب نحو النجاح في امتحان BEM 2026 بتاريخ 19 ماي 2026.

══════════════════════════════════════════
ملف الطالب
══════════════════════════════════════════
الاسم:       {name}
المؤسسة:     {school}
مادة اليوم:  {subject}
الدرجات الحالية:
{grades_str}

أقوى مادة:   {strongest} ({grades.get(strongest, 0):.1f}/20)
أضعف مادة:   {weakest} ({grades.get(weakest, 0):.1f}/20)
مستوى اليوم في {subject}: {focus_grade}/20 ← {focus_bloom['level']}

الوقت المتبقي: {cd['days']} يوم و {cd['hours']} ساعة و {cd['minutes']} دقيقة حتى BEM 2026

══════════════════════════════════════════
هويّتك ومنهجك
══════════════════════════════════════════
أنت لستَ روبوتاً — أنت مرشد ميداني ومحارب أفكار.
خاطب الطالب دائماً بـ: "أيها الفارس" أو "أيتها الفارسة".
اجعل كل رسالة تحمل ثلاثة عناصر:
  1. 🔥 شرارة إلهامية (جملة توقد الروح)
  2. 📚 محتوى أكاديمي دقيق وموثوق
  3. 🎯 أمر ميداني واضح (ما يجب فعله الآن)

══════════════════════════════════════════
الأدوات النفسية المدمجة
══════════════════════════════════════════
1. التخيّل المستقبلي — استخدم هذا الزناد عند بداية كل جلسة أو حين يشعر الطالب بالإحباط:
   "غمّض عينيك.. تخيّل زغاريد الفرح في بيتك يوم 19 جوان عند رؤية اسمك في قائمة الناجحين..
   أبوك يبكي من الفرح. أمّك تحضن الورقة. هذا هو مستقبلك، فهل أنت مستعد لانتزاعه؟"

2. قصص النجاح السينمائية — وظّفها بحكمة:
   • **إديسون**: "فشل أكثر من ألف مرة قبل أن يضيء العالم. كل مسألة صعبة أمامك هي فشل إديسون رقم 999."
   • **الصمود الجزائري**: "طلاب من الأوراس، بلا كهرباء، بلا إنترنت، نجحوا بإرادة فولاذية. ما عذرك؟"
   • **الإرادة**: "ليس الأذكى من يفوز. من يصمد أطول هو من يقف آخر الليل فوق منصة التتويج."

3. الأرقيتايب الحربي:
   "ميدان الشرف" = قاعة الامتحان
   "سلاحك" = القلم والمعرفة
   "انتصارك" = شهادة BEM
   "معسكر التدريب" = ساعات الدراسة

4. النقد البنّاء — عند الخطأ:
   لا تقل "أنت مخطئ". قل: "جيّد، هذا الخطأ يُعلّمنا درساً أعمق — إليك الصواب..."

══════════════════════════════════════════
المنطق الأكاديمي
══════════════════════════════════════════
• التزم بمناهج وزارة التربية الوطنية الجزائرية بدقة تامة.
• وجّه الطالب دائماً لـ https://www.dzexams.com/ للتدريب.
• لا تخترع أرقاماً أو معادلات أو معاملات غير موثّقة.
• المستوى {focus_bloom['badge']}: {focus_bloom['strategy']}

══════════════════════════════════════════
توليد خرائط المعرفة
══════════════════════════════════════════
عند طلب خريطة ذهنية أو "مخطط"، أرجع كتلة Mermaid.js فقط:
```mermaid
mindmap
  root((الموضوع))
    الفرع الأول
      عنصر 1
      عنصر 2
    الفرع الثاني
      عنصر 3
```
اجعل التسميات مختصرة. أقصى عمق: 3 مستويات.

══════════════════════════════════════════
هويّة العلامة التجارية
══════════════════════════════════════════
أنت تمثّل DONIA LABS TECH — مختبر الأفكار الذكية.
اختم كل رد مهم بـ: "— بروتوكول فارس | دونيا لابز تك ⚔️🇩🇿"
""".strip()

# ─────────────────────────────────────────────
#  الشعار والعنوان
# ─────────────────────────────────────────────
def render_hero():
    cd = get_countdown()
    intensity_msg = (
        "⚡ الساعة الأخيرة — كل دقيقة تُحسم!" if cd["days"] < 7
        else "🔥 العدّ التنازلي الحاسم — التاريخ لا ينتظر!"
        if cd["days"] < 30 else "🎯 المعركة تبدأ الآن — لا وقت للتردد!"
    )

    # SVG: طالب يرفع شهادة النجاح مع العلم الجزائري
    hero_svg = """
<svg viewBox="0 0 420 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:380px;filter:drop-shadow(0 0 20px rgba(0,160,70,0.4));">
  <!-- خلفية -->
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#0a2416"/>
      <stop offset="100%" style="stop-color:#050d0a"/>
    </radialGradient>
    <radialGradient id="glow1" cx="50%" cy="30%" r="40%">
      <stop offset="0%" style="stop-color:#d4af37;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:transparent;stop-opacity:0"/>
    </radialGradient>
    <linearGradient id="skinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#d4a574"/>
      <stop offset="100%" style="stop-color:#c49060"/>
    </linearGradient>
    <linearGradient id="clothGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#1a4a2e"/>
      <stop offset="100%" style="stop-color:#0d2818"/>
    </linearGradient>
    <linearGradient id="paperGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#fff9e6"/>
      <stop offset="100%" style="stop-color:#f0e8c0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- خلفية مضيئة -->
  <ellipse cx="210" cy="160" rx="200" ry="155" fill="url(#bgGrad)"/>
  <ellipse cx="210" cy="120" rx="120" ry="100" fill="url(#glow1)"/>

  <!-- أشعة النجاح الخلفية -->
  <g opacity="0.15">
    <line x1="210" y1="60" x2="210" y2="0" stroke="#d4af37" stroke-width="2"/>
    <line x1="210" y1="60" x2="260" y2="10" stroke="#d4af37" stroke-width="1.5"/>
    <line x1="210" y1="60" x2="310" y2="30" stroke="#d4af37" stroke-width="1.5"/>
    <line x1="210" y1="60" x2="160" y2="10" stroke="#d4af37" stroke-width="1.5"/>
    <line x1="210" y1="60" x2="110" y2="30" stroke="#d4af37" stroke-width="1.5"/>
    <line x1="210" y1="60" x2="350" y2="70" stroke="#d4af37" stroke-width="1"/>
    <line x1="210" y1="60" x2="70" y2="70" stroke="#d4af37" stroke-width="1"/>
  </g>

  <!-- الجسم - ملابس مدرسية -->
  <ellipse cx="210" cy="265" rx="52" ry="15" fill="#061208" opacity="0.5"/>
  <!-- ساقان -->
  <rect x="188" y="230" width="16" height="50" rx="8" fill="#0d2818"/>
  <rect x="210" y="230" width="16" height="50" rx="8" fill="#0d2818"/>
  <!-- قدمان -->
  <ellipse cx="196" cy="278" rx="12" ry="6" fill="#1a1a1a"/>
  <ellipse cx="218" cy="278" rx="12" ry="6" fill="#1a1a1a"/>

  <!-- الجذع -->
  <path d="M175 165 Q185 155 210 152 Q235 155 245 165 L252 230 Q210 245 168 230 Z"
        fill="url(#clothGrad)" stroke="#00823c" stroke-width="1"/>
  <!-- طوق القميص -->
  <path d="M198 152 L210 168 L222 152" fill="white" opacity="0.15"/>

  <!-- الذراع اليسرى (مرفوعة تحمل الشهادة) -->
  <path d="M175 175 Q145 155 130 100 Q128 90 135 88"
        stroke="url(#skinGrad)" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- الذراع اليمنى -->
  <path d="M245 175 Q265 190 268 210"
        stroke="url(#skinGrad)" stroke-width="14" fill="none" stroke-linecap="round"/>

  <!-- الشهادة (محمولة باليد اليسرى) -->
  <g transform="translate(90,50) rotate(-15)">
    <rect x="0" y="0" width="80" height="60" rx="4" fill="url(#paperGrad)"
          stroke="#d4af37" stroke-width="2" filter="url(#glow)"/>
    <!-- الخطوط الداخلية -->
    <rect x="8" y="10" width="64" height="3" rx="1.5" fill="#d4af37" opacity="0.7"/>
    <rect x="12" y="18" width="56" height="2" rx="1" fill="#888" opacity="0.5"/>
    <rect x="12" y="24" width="50" height="2" rx="1" fill="#888" opacity="0.4"/>
    <rect x="12" y="30" width="54" height="2" rx="1" fill="#888" opacity="0.3"/>
    <!-- ختم -->
    <circle cx="40" cy="46" r="8" fill="none" stroke="#d4af37" stroke-width="1.5" opacity="0.8"/>
    <text x="40" y="50" text-anchor="middle" font-size="8" fill="#d4af37" opacity="0.9">BEM</text>
    <!-- وميض -->
    <rect x="0" y="0" width="80" height="60" rx="4" fill="white" opacity="0.08"/>
  </g>

  <!-- الرقبة -->
  <rect x="203" y="130" width="14" height="22" rx="7" fill="url(#skinGrad)"/>

  <!-- الرأس -->
  <ellipse cx="210" cy="118" rx="28" ry="30" fill="url(#skinGrad)"/>
  <!-- شعر -->
  <path d="M182 110 Q185 82 210 80 Q235 82 238 110 Q230 95 210 93 Q190 95 182 110 Z"
        fill="#2c1a0e"/>
  <!-- ملامح الوجه -->
  <ellipse cx="200" cy="115" rx="4" ry="4.5" fill="white"/>
  <ellipse cx="220" cy="115" rx="4" ry="4.5" fill="white"/>
  <ellipse cx="200" cy="116" rx="2.5" ry="3" fill="#3a2010"/>
  <ellipse cx="220" cy="116" rx="2.5" ry="3" fill="#3a2010"/>
  <!-- بريق العيون (ابتسامة النصر) -->
  <circle cx="201" cy="114" r="1" fill="white" opacity="0.8"/>
  <circle cx="221" cy="114" r="1" fill="white" opacity="0.8"/>
  <!-- الابتسامة -->
  <path d="M202 126 Q210 133 218 126" stroke="#c07040" stroke-width="2" fill="none" stroke-linecap="round"/>

  <!-- العلم الجزائري (صغير خلفه) -->
  <g transform="translate(285, 30)">
    <rect x="0" y="0" width="10" height="70" rx="2" fill="#6b4c11"/>
    <rect x="10" y="0" width="40" height="35" fill="#006233"/>
    <rect x="10" y="35" width="40" height="35" fill="white"/>
    <!-- هلال ونجمة صغيرة -->
    <path d="M30 18 A12 12 0 1 1 30 52 A10 10 0 1 0 30 18 Z" fill="#d21034" opacity="0.9"/>
    <polygon points="30,28 31.5,33 37,33 32,36 34,41 30,38 26,41 28,36 23,33 28.5,33"
             fill="#d21034" transform="translate(0,5)" opacity="0.9"/>
  </g>

  <!-- نجوم المجد -->
  <text x="155" y="45" font-size="16" fill="#d4af37" opacity="0.9" filter="url(#glow)">★</text>
  <text x="260" y="38" font-size="12" fill="#d4af37" opacity="0.7">★</text>
  <text x="140" y="80" font-size="10" fill="#d4af37" opacity="0.5">✦</text>

  <!-- نص "نجحت!" -->
  <text x="210" y="308" text-anchor="middle"
        font-family="Cairo, Arial" font-size="13" font-weight="bold"
        fill="#d4af37" filter="url(#glow)">أنا ناجح بإذن الله</text>
</svg>"""

    st.markdown(f"""
<div class="hero-wrapper">

  <!-- شريط العلم -->
  <div class="flag-stripe-container">
    <div class="flag-stripe green"></div>
    <div class="flag-stripe white">
      <span class="flag-symbol">☽ ✦</span>
    </div>
    <div class="flag-stripe red"></div>
  </div>

  <div class="hero-content">
    <!-- النص الرئيسي -->
    <div class="hero-text-block">
      <div class="brand-badge">⚔️ دونيا لابز تك ⚔️</div>
      <h1 class="hero-title">فارس<br><span class="bem-year">BEM 2026</span></h1>
      <p class="hero-subtitle">مختبر الأفكار الذكية — المرشد الاستراتيجي الأول</p>
      <div class="hero-divider"></div>
      <p class="hero-vision">
        "غمّض عينيك.. تخيّل زغاريد الفرح في بيتك يوم<br>
        <strong>19 جوان</strong> عند رؤية اسمك في قائمة الناجحين..<br>
        هذا هو مستقبلك، فهل أنت مستعد لانتزاعه؟"
      </p>
    </div>

    <!-- رسمة الطالب -->
    <div class="hero-graphic">
      {hero_svg}
    </div>
  </div>

  <!-- العداد التنازلي -->
  <div class="countdown-section">
    <p class="countdown-title">⏳ الوقت المتبقي لمعركة النجاح</p>
    <div class="countdown-bar">
      <div class="cd-unit">
        <span class="cd-num">{cd['days']}</span>
        <span class="cd-lbl">يوم</span>
      </div>
      <span class="cd-sep">:</span>
      <div class="cd-unit">
        <span class="cd-num">{cd['hours']:02d}</span>
        <span class="cd-lbl">ساعة</span>
      </div>
      <span class="cd-sep">:</span>
      <div class="cd-unit">
        <span class="cd-num">{cd['minutes']:02d}</span>
        <span class="cd-lbl">دقيقة</span>
      </div>
      <span class="cd-sep">:</span>
      <div class="cd-unit">
        <span class="cd-num">{cd['seconds']:02d}</span>
        <span class="cd-lbl">ثانية</span>
      </div>
    </div>
    <p class="countdown-sub">{intensity_msg}</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  الشريط الجانبي — تسجيل الطالب
# ─────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("""
<div class="sidebar-header">
  <div class="sb-icon">⚔️</div>
  <h2>مركز القيادة</h2>
  <p>دونيا لابز تك</p>
</div>""", unsafe_allow_html=True)

        # ── ملف الطالب ──
        st.markdown('<div class="sb-section-title">🪖 ملف الفارس</div>', unsafe_allow_html=True)
        student_name = st.text_input(
            "الاسم الكامل",
            key="student_name",
            placeholder="مثال: يوسف بن علي",
        )
        school = st.text_input(
            "المؤسسة التعليمية",
            key="school",
            placeholder="مثال: متوسطة الأمير عبد القادر، سطيف",
        )

        st.divider()

        # ── الدرجات ──
        st.markdown('<div class="sb-section-title">📊 الدرجات / 20</div>', unsafe_allow_html=True)
        grades = {}
        for subject in SUBJECTS:
            bloom = map_to_bloom(st.session_state.get(f"g_{subject}", 12.0))
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(
                    f'<div class="grade-label">'
                    f'<span style="color:{bloom["color"]}">{bloom["emoji"]}</span> {subject}'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            with col2:
                grade = st.number_input(
                    subject,
                    min_value=0.0, max_value=20.0,
                    value=12.0, step=0.5,
                    key=f"g_{subject}",
                    label_visibility="collapsed",
                )
            grades[subject] = grade

        st.divider()

        # ── مادة اليوم ──
        st.markdown('<div class="sb-section-title">🎯 معركة اليوم</div>', unsafe_allow_html=True)
        selected_subject = st.selectbox(
            "اختر المادة",
            options=list(SUBJECTS.keys()),
            key="selected_subject",
        )

        st.divider()

        # ── ملخص بلوم ──
        if grades:
            avg = sum(grades.values()) / len(grades)
            overall = map_to_bloom(avg)
            st.markdown(f"""
<div class="bloom-summary">
  <div style="font-size:2rem;text-align:center">{overall['emoji']}</div>
  <div style="text-align:center;font-size:0.85rem;font-weight:700;
              color:{overall['color']}">{overall['badge']}</div>
  <div style="text-align:center;font-size:0.7rem;color:#8a9ab0">
    المعدل العام: {avg:.1f}/20
  </div>
</div>""", unsafe_allow_html=True)

        st.divider()
        if st.button("🔄 إعادة تعيين الجلسة", use_container_width=True):
            for k in ["messages", "val_log"]:
                st.session_state.pop(k, None)
            st.rerun()

    return student_name, school, grades, selected_subject

# ─────────────────────────────────────────────
#  لوحة الأداء الأكاديمي
# ─────────────────────────────────────────────
def render_dashboard(grades: dict, subject: str):
    if not grades:
        return
    avg = sum(grades.values()) / len(grades)
    overall = map_to_bloom(avg)
    weakest  = min(grades, key=grades.get)
    strongest= max(grades, key=grades.get)
    focus_bloom = map_to_bloom(grades.get(subject, 12))

    st.markdown('<h3 class="section-title">📊 خريطة المعركة الأكاديمية</h3>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)

    def stat_card(num, label, color="#d4af37", cls=""):
        return f"""
<div class="stat-card {cls}">
  <div class="stat-num" style="color:{color}">{num}</div>
  <div class="stat-lbl">{label}</div>
</div>"""

    with c1:
        st.markdown(stat_card(f"{avg:.1f}", "المعدل العام / 20"), unsafe_allow_html=True)
    with c2:
        st.markdown(stat_card(overall["badge"], "مستواك العام", overall["color"]), unsafe_allow_html=True)
    with c3:
        st.markdown(stat_card(f"{grades[weakest]:.1f}", f"⚔️ {weakest[:12]}", "#e74c3c", "danger"), unsafe_allow_html=True)
    with c4:
        st.markdown(stat_card(f"{grades[strongest]:.1f}", f"👑 {strongest[:12]}", "#27ae60", "success"), unsafe_allow_html=True)

    # بطاقة المادة المختارة
    st.markdown(f"""
<div class="focus-card">
  <div class="focus-header">
    {focus_bloom['emoji']} مادة اليوم: <strong>{subject}</strong>
  </div>
  <div class="focus-level" style="color:{focus_bloom['color']}">
    {focus_bloom['level']}
  </div>
  <div class="focus-quote">"{focus_bloom['war_quote']}"</div>
  <div class="focus-strategy">🎯 {focus_bloom['strategy']}</div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  روابط dzexams
# ─────────────────────────────────────────────
def get_dzexams_block(subject: str) -> str:
    link = DZEXAMS_LINKS.get(subject, "https://www.dzexams.com/brevet/4am/")
    return f"""
<div class="resource-box">
  <div class="resource-title">📚 مصادر التدريب الرسمية — {subject}</div>
  <a href="{link}" target="_blank" class="dz-btn">
    📄 امتحانات وتمارين — {subject}
  </a>
  <a href="https://www.dzexams.com/brevet/4am/" target="_blank" class="dz-btn">
    🏛️ مركز BEM الشامل
  </a>
  <a href="https://www.dzexams.com/brevet/" target="_blank" class="dz-btn">
    📂 مستودع BEM الكامل
  </a>
  <div class="resource-note">جميع الموارد من dzexams.com — المنصة الجزائرية الرسمية للتحضير</div>
</div>"""

# ─────────────────────────────────────────────
#  واجهة الدردشة
# ─────────────────────────────────────────────
def render_chat(student_name, school, grades, subject):
    # تهيئة الجلسة
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "val_log" not in st.session_state:
        st.session_state.val_log = []

    # رسالة الترحيب الافتتاحية
    if not st.session_state.messages and student_name:
        cd = get_countdown()
        focus_bloom = map_to_bloom(grades.get(subject, 12))
        welcome = f"""
⚔️ **{student_name.upper()} — أيها الفارس، بيانات مهمّتك:**

غمّض عينيك لحظة..
تخيّل **يوم 19 جوان** عند رؤية اسمك في قائمة الناجحين.
أبوك يبكي فرحاً. أمّك تضمّك. الجيران يهنّؤون.
**هذا المشهد ينتظرك — لكنّه لن يأتيك، بل أنت من ستنتزعه.**

---

📋 **بياناتك الميدانية:**
- 🎯 **مادة اليوم:** {subject}
- 📊 **مستواك الحالي:** {grades.get(subject, 12):.1f}/20 — **{focus_bloom['level']}**
- ⏳ **الوقت المتبقي:** {cd['days']} يوماً و {cd['hours']} ساعة

💡 **اختر أمرك الميداني:**
- 💬 اسألني أي شيء في مادة **{subject}**
- 🗺️ اكتب **"خريطة ذهنية"** لتوليد مخطط بصري
- 📅 اكتب **"خطة دراسية"** للحصول على جدول يومي مُحكم
- 💪 اكتب **"ألهمني"** لتلقّي جرعة إلهامية سينمائية
- 📖 اكتب **"قصة إديسون"** أو **"قصة جزائرية"** للشحن النفسي

— بروتوكول فارس | دونيا لابز تك ⚔️🇩🇿
"""
        st.session_state.messages.append({"role": "assistant", "content": welcome})

    # عرض المحادثة
    for msg in st.session_state.messages:
        role_cls = "user-bubble" if msg["role"] == "user" else "ai-bubble"
        avatar = "🪖" if msg["role"] == "user" else "⚔️"

        if msg["role"] == "assistant" and "```mermaid" in msg["content"]:
            parts = msg["content"].split("```mermaid", 1)
            if parts[0].strip():
                st.markdown(
                    f'<div class="chat-msg {role_cls}">'
                    f'<span class="ch-avatar">{avatar}</span>'
                    f'<div class="ch-body">{parts[0]}</div></div>',
                    unsafe_allow_html=True,
                )
            mermaid_raw = parts[1].split("```", 1)[0].strip()
            render_mermaid(mermaid_raw)
            remainder = parts[1].split("```", 1)[1] if "```" in parts[1] else ""
            if remainder.strip():
                st.markdown(
                    f'<div class="chat-msg {role_cls}">'
                    f'<div class="ch-body">{remainder}</div></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                f'<div class="chat-msg {role_cls}">'
                f'<span class="ch-avatar">{avatar}</span>'
                f'<div class="ch-body">{msg["content"]}</div></div>',
                unsafe_allow_html=True,
            )

    # روابط dzexams
    st.markdown(get_dzexams_block(subject), unsafe_allow_html=True)

    # سجل التحقق
    if st.session_state.val_log:
        with st.expander("🔬 سجل طبقة التحقق التربوي (Acree)", expanded=False):
            v = st.session_state.val_log[-1]
            c1, c2 = st.columns(2)
            with c1:
                st.metric("الحالة", v["status"])
                st.metric("نسبة الثقة", f"{v['confidence']*100:.0f}٪")
            with c2:
                st.metric("مستوى بلوم", v["bloom_tier"][:20])
            if v["flags"]:
                for f in v["flags"]:
                    st.warning(f)
            else:
                st.success("✅ لم تُرصد أي مشكلات تربوية في هذا الرد.")

    # صندوق الإدخال
    st.markdown("---")

    # التحقق من وجود API Key
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        st.error("🔑 مفتاح Groq API غير مُعرَّف. أضف `GROQ_API_KEY` في ملف `.streamlit/secrets.toml`")
        st.code('# .streamlit/secrets.toml\nGROQ_API_KEY = "gsk_..."', language="toml")
        return

    if not student_name:
        st.info("👤 أدخل اسمك في الشريط الجانبي لتفعيل بروتوكول فارس.")
        return

    user_input = st.chat_input(
        f"⚔️ أرسل أمرك لفارس — اسأل عن {subject}، أو اطلب خريطة ذهنية، أو خطة دراسية..."
    )

    if user_input:
        # إضافة رسائل مخصصة
        actual_input = user_input
        if any(x in user_input for x in ["قصة إديسون", "اديسون", "ادیسون"]):
            actual_input = "أريد سماع قصة إديسون الملهمة بأسلوب سينمائي."
        elif "قصة جزائرية" in user_input or "بطل جزائري" in user_input:
            actual_input = "أريد سماع قصة نجاح جزائري ملهمة بأسلوب سينمائي."
        elif "ألهمني" in user_input or "محتاج تشجيع" in user_input:
            actual_input = "أنا محتاج جرعة إلهامية قوية الآن. ألهمني بأسلوب مشعل."

        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("⚔️ فارس يضع استراتيجيته..."):
            try:
                from groq import Groq
                client = Groq(api_key=api_key)
                system_prompt = build_system_prompt(student_name, school, grades, subject)
                history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages[-12:]
                    if m["role"] != "assistant" or m["content"] != st.session_state.messages[0]["content"]
                ]
                history[-1]["content"] = actual_input

                response_obj = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[{"role": "system", "content": system_prompt}] + history,
                    temperature=0.8,
                    max_tokens=1600,
                )
                response = response_obj.choices[0].message.content
            except Exception as e:
                response = f"⚠️ خطأ في الاتصال: {str(e)}"

        # التحقق التربوي
        validation = validate_pedagogical_output(response, subject, grades)
        st.session_state.val_log.append(validation)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# ─────────────────────────────────────────────
#  تبويب الخرائط الذهنية
# ─────────────────────────────────────────────
def render_mindmap_tab():
    st.markdown('<h3 class="section-title">🗺️ مولّد الخرائط الذهنية</h3>', unsafe_allow_html=True)
    st.info(
        "في **غرفة المعارك**، اكتب **'خريطة ذهنية'** وسيولّد فارس مخططاً بصرياً للدرس تلقائياً. "
        "يمكنك أيضاً رسم مخطط يدوياً هنا."
    )

    default_map = """mindmap
  root((الرياضيات — BEM 2026))
    الجبر
      المعادلات
        الدرجة الأولى
        الدرجة الثانية
      المتباينات
      الأنظمة
    الهندسة
      مبرهنة فيثاغورس
      حساب المثلثات
      التحويلات الهندسية
    الإحصاء
      الوسط الحسابي
      الوسيط
      المنوال
    الحساب
      القاسم المشترك الأكبر
      المضاعف المشترك الأصغر
      الأعداد الأولية"""

    mermaid_input = st.text_area(
        "كتابة كود Mermaid",
        value=default_map,
        height=280,
        key="manual_mermaid",
    )
    if st.button("🗺️ عرض الخريطة الذهنية", use_container_width=True):
        render_mermaid(mermaid_input)

# ─────────────────────────────────────────────
#  تبويب المصادر
# ─────────────────────────────────────────────
def render_resources_tab(grades: dict):
    st.markdown('<h3 class="section-title">📚 خزينة الموارد الرسمية</h3>', unsafe_allow_html=True)
    st.markdown(
        "جميع الروابط موجّهة حصرياً إلى **dzexams.com** — "
        "المنصة الجزائرية الرسمية للتحضير لامتحان BEM."
    )

    cols = st.columns(2)
    for i, (subject, link) in enumerate(DZEXAMS_LINKS.items()):
        bloom = map_to_bloom(grades.get(subject, 12))
        with cols[i % 2]:
            st.markdown(f"""
<div class="res-card">
  <div class="res-header">
    <span>{subject}</span>
    <span style="color:{bloom['color']};font-size:0.78rem">{bloom['badge']}</span>
  </div>
  <a href="{link}" target="_blank" class="res-link">📄 امتحانات وتمارين ←</a>
  <div class="res-grade">الدرجة: {grades.get(subject, 12):.1f}/20</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div class="footer-brand">
  <div class="footer-logo">⚔️🇩🇿⚔️</div>
  <h3>فارس BEM 2026</h3>
  <p>دونيا لابز تك — مختبر الأفكار الذكية</p>
  <div class="footer-tags">
    <span>سياسة الصفر هلوسة</span>
    <span>محرك بلوم التعليمي</span>
    <span>متوافق مع مناهج وزارة التربية الوطنية</span>
    <span>Groq AI — LLaMA 3 70B</span>
  </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  قصص النجاح المدمجة
# ─────────────────────────────────────────────
def render_stories_tab():
    st.markdown('<h3 class="section-title">🎬 مكتبة الإلهام السينمائي</h3>', unsafe_allow_html=True)
    st.markdown("اقرأ قصة كل صباح — واستمدّ منها وقود المعركة اليومية.")

    for key, story_data in SUCCESS_STORIES.items():
        with st.expander(story_data["title"], expanded=(key == "algerian_hero")):
            st.markdown(
                f'<div class="story-card">{story_data["story"]}</div>',
                unsafe_allow_html=True,
            )

# ─────────────────────────────────────────────
#  التطبيق الرئيسي
# ─────────────────────────────────────────────
def main():
    render_hero()

    student_name, school, grades, selected_subject = render_sidebar()

    tab_chat, tab_map, tab_stories, tab_resources = st.tabs([
        "⚔️ غرفة المعارك",
        "🗺️ الخرائط الذهنية",
        "🎬 الإلهام السينمائي",
        "📚 خزينة الموارد",
    ])

    with tab_chat:
        render_dashboard(grades, selected_subject)
        st.markdown("---")
        render_chat(student_name, school, grades, selected_subject)

    with tab_map:
        render_mindmap_tab()

    with tab_stories:
        render_stories_tab()

    with tab_resources:
        render_resources_tab(grades)


if __name__ == "__main__":
    main()

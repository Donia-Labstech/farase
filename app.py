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
    initial_sidebar_state="expanded",
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
    if cd["days"] < 7:
        intensity_msg = "&#9889; الساعة الأخيرة — كل دقيقة تُحسم!"
    elif cd["days"] < 30:
        intensity_msg = "&#128293; العدّ التنازلي الحاسم — التاريخ لا ينتظر!"
    else:
        intensity_msg = "&#127919; المعركة تبدأ الآن — لا وقت للتردد!"

    hero_html = (
        """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{
  background:linear-gradient(160deg,#020f06 0%,#061408 40%,#0a1e10 100%);
  font-family:'Cairo',sans-serif;color:#e8f5ec;direction:rtl;
  border-radius:8px;overflow:hidden;
}
.hero-wrap{
  border:1px solid rgba(0,162,79,0.3);border-radius:8px;overflow:hidden;
  box-shadow:0 0 40px rgba(0,162,79,0.15);position:relative;
}
.hero-wrap::before{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,#d21034,#f5f5f5,#006233,#f5f5f5,#d21034);
}
.flag-bar{display:flex;height:7px}
.fg{background:#006233;flex:1}
.fw{background:#f5f5f5;flex:1;display:flex;align-items:center;justify-content:center;
    font-size:6px;color:#d21034;letter-spacing:2px}
.fr{background:#d21034;flex:1}
.hero-inner{
  display:flex;align-items:center;justify-content:space-between;
  padding:28px 36px 16px;gap:20px;flex-wrap:wrap;
}
.text-block{flex:1;min-width:260px;text-align:right}
.badge{
  display:inline-block;background:rgba(212,175,55,0.1);
  border:1px solid rgba(212,175,55,0.25);color:#d4af37;
  font-size:0.68rem;font-weight:700;letter-spacing:3px;
  padding:4px 14px;border-radius:2px;margin-bottom:10px;
}
.main-title{
  font-family:'Amiri',serif;font-size:3rem;font-weight:700;
  color:#e8f5ec;line-height:1.1;
  text-shadow:0 0 40px rgba(0,162,79,0.4);margin-bottom:4px;
}
.bem-yr{
  font-family:'Cairo',sans-serif;font-size:2rem;font-weight:900;
  color:#d4af37;text-shadow:0 0 20px rgba(212,175,55,0.5);letter-spacing:2px;
}
.sub-title{font-size:0.78rem;color:#7a9e84;letter-spacing:2px;margin:6px 0 14px}
.divider{width:70px;height:2px;
  background:linear-gradient(90deg,#00a84f,#d4af37,transparent);
  margin:0 0 14px auto;border-radius:1px}
.vision{
  background:rgba(0,98,51,0.12);border-right:3px solid #00a84f;
  border-radius:0 4px 4px 0;padding:12px 16px;
  font-size:0.9rem;line-height:1.9;color:#b0d8bc;font-style:italic;
}
.vision strong{color:#f0cc50}
.graphic{
  flex-shrink:0;width:240px;
  display:flex;align-items:center;justify-content:center;
  animation:floatY 4s ease-in-out infinite;
  filter:drop-shadow(0 0 20px rgba(0,162,79,0.35));
}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.cd-wrap{
  background:rgba(0,0,0,0.35);border-top:1px solid rgba(0,162,79,0.2);
  padding:16px 36px;text-align:center;
}
.cd-title{font-size:0.78rem;color:#7a9e84;letter-spacing:2px;margin-bottom:12px}
.cd-bar{
  display:inline-flex;align-items:center;gap:4px;
  background:rgba(0,0,0,0.4);border:1px solid rgba(212,175,55,0.2);
  border-radius:4px;padding:10px 22px;margin-bottom:8px;
}
.cd-unit{display:flex;flex-direction:column;align-items:center;min-width:58px}
.cd-num{
  font-family:'Cairo',sans-serif;font-size:2rem;font-weight:900;
  color:#f0cc50;text-shadow:0 0 15px rgba(240,200,80,0.5);line-height:1;
}
.cd-lbl{font-size:0.6rem;color:#7a9e84;letter-spacing:1px;margin-top:2px}
.cd-sep{font-size:1.8rem;color:#8a6f20;margin-bottom:14px;animation:blk 1s step-end infinite}
@keyframes blk{50%{opacity:0}}
.cd-msg{font-size:0.78rem;color:#00a84f;font-weight:600;letter-spacing:1px}
</style>
</head>
<body>
<div class="hero-wrap">
  <div class="flag-bar">
    <div class="fg"></div>
    <div class="fw">&#9790; &#10022;</div>
    <div class="fr"></div>
  </div>
  <div class="hero-inner">
    <div class="text-block">
      <div class="badge">&#9876; دونيا لابز تك &#9876;</div>
      <div class="main-title">فارس<br><span class="bem-yr">BEM 2026</span></div>
      <div class="sub-title">مختبر الأفكار الذكية — المرشد الاستراتيجي الأول</div>
      <div class="divider"></div>
      <div class="vision">
        "غمّض عينيك.. تخيّل زغاريد الفرح في بيتك يوم
        <strong>19 جوان</strong> عند رؤية اسمك في قائمة الناجحين..
        هذا هو مستقبلك، فهل أنت مستعد لانتزاعه؟"
      </div>
    </div>
    <div class="graphic">
      <svg viewBox="0 0 300 340" xmlns="http://www.w3.org/2000/svg" width="230" height="262">
        <defs>
          <radialGradient id="bg2" cx="50%" cy="50%" r="55%">
            <stop offset="0%" stop-color="#0d2818"/>
            <stop offset="100%" stop-color="#020a05"/>
          </radialGradient>
          <radialGradient id="aura" cx="50%" cy="35%" r="45%">
            <stop offset="0%" stop-color="#d4af37" stop-opacity="0.22"/>
            <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#d4a574"/>
            <stop offset="100%" stop-color="#b8845a"/>
          </linearGradient>
          <linearGradient id="shirt" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1a4a2e"/>
            <stop offset="100%" stop-color="#0a2015"/>
          </linearGradient>
          <linearGradient id="cert" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fffbe8"/>
            <stop offset="100%" stop-color="#ede0a0"/>
          </linearGradient>
          <filter id="gf">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
            <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>
        <ellipse cx="150" cy="170" rx="148" ry="165" fill="url(#bg2)"/>
        <ellipse cx="150" cy="110" rx="100" ry="90" fill="url(#aura)"/>
        <g stroke="#d4af37" stroke-opacity="0.12">
          <line x1="150" y1="50" x2="150" y2="5" stroke-width="2"/>
          <line x1="150" y1="50" x2="195" y2="12" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="240" y2="28" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="105" y2="12" stroke-width="1.5"/>
          <line x1="150" y1="50" x2="60" y2="28" stroke-width="1.5"/>
        </g>
        <ellipse cx="150" cy="308" rx="46" ry="11" fill="#000" fill-opacity="0.45"/>
        <rect x="127" y="240" width="17" height="58" rx="8" fill="#0d2010"/>
        <rect x="150" y="240" width="17" height="58" rx="8" fill="#0d2010"/>
        <ellipse cx="135" cy="296" rx="14" ry="6" fill="#111"/>
        <ellipse cx="158" cy="296" rx="14" ry="6" fill="#111"/>
        <path d="M112 175 Q125 163 150 160 Q175 163 188 175 L194 242 Q150 256 106 242 Z"
              fill="url(#shirt)" stroke="#00823c" stroke-width="1.2"/>
        <path d="M140 160 L150 175 L160 160" fill="white" fill-opacity="0.12"/>
        <circle cx="150" cy="190" r="2" fill="#006233" fill-opacity="0.6"/>
        <circle cx="150" cy="205" r="2" fill="#006233" fill-opacity="0.6"/>
        <circle cx="150" cy="220" r="2" fill="#006233" fill-opacity="0.6"/>
        <path d="M112 182 Q82 162 68 108 Q66 97 73 95"
              stroke="url(#skin)" stroke-width="15" fill="none" stroke-linecap="round"/>
        <path d="M188 182 Q208 200 212 224"
              stroke="url(#skin)" stroke-width="15" fill="none" stroke-linecap="round"/>
        <circle cx="73" cy="94" r="9" fill="url(#skin)"/>
        <g transform="translate(24,42) rotate(-18)">
          <rect x="0" y="0" width="86" height="64" rx="5"
                fill="url(#cert)" stroke="#d4af37" stroke-width="2.5"/>
          <rect x="8" y="9" width="70" height="4" rx="2" fill="#d4af37" fill-opacity="0.75"/>
          <rect x="12" y="18" width="62" height="2.5" rx="1.2" fill="#999" fill-opacity="0.5"/>
          <rect x="12" y="25" width="55" height="2.5" rx="1.2" fill="#999" fill-opacity="0.4"/>
          <rect x="12" y="32" width="60" height="2.5" rx="1.2" fill="#999" fill-opacity="0.35"/>
          <circle cx="43" cy="50" r="9" fill="none" stroke="#d4af37" stroke-width="1.8" stroke-opacity="0.9"/>
          <text x="43" y="54" text-anchor="middle" font-size="7" font-weight="bold"
                fill="#d4af37" font-family="Cairo,Arial">BEM</text>
          <rect x="0" y="0" width="86" height="64" rx="5" fill="white" fill-opacity="0.06"/>
        </g>
        <rect x="143" y="140" width="14" height="22" rx="7" fill="url(#skin)"/>
        <ellipse cx="150" cy="127" rx="29" ry="31" fill="url(#skin)"/>
        <path d="M121 120 Q124 90 150 87 Q176 90 179 120 Q170 103 150 102 Q130 103 121 120 Z"
              fill="#2a1508"/>
        <ellipse cx="121" cy="128" rx="5" ry="7" fill="url(#skin)"/>
        <ellipse cx="179" cy="128" rx="5" ry="7" fill="url(#skin)"/>
        <path d="M136 114 Q142 111 148 113" stroke="#5a3010" stroke-width="2"
              fill="none" stroke-linecap="round"/>
        <path d="M152 113 Q158 111 164 114" stroke="#5a3010" stroke-width="2"
              fill="none" stroke-linecap="round"/>
        <ellipse cx="140" cy="122" rx="5" ry="5.5" fill="white"/>
        <ellipse cx="160" cy="122" rx="5" ry="5.5" fill="white"/>
        <ellipse cx="140" cy="123" rx="3.2" ry="3.5" fill="#3a2010"/>
        <ellipse cx="160" cy="123" rx="3.2" ry="3.5" fill="#3a2010"/>
        <circle cx="141" cy="121" r="1.2" fill="white" fill-opacity="0.85"/>
        <circle cx="161" cy="121" r="1.2" fill="white" fill-opacity="0.85"/>
        <path d="M147 128 Q150 132 153 128" stroke="#b07040" stroke-width="1.2"
              fill="none" stroke-linecap="round"/>
        <path d="M141 137 Q150 145 159 137"
              stroke="#c06040" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <g transform="translate(210,25)">
          <rect x="0" y="0" width="9" height="74" rx="2.5" fill="#7a5a20"/>
          <rect x="9" y="0" width="44" height="37" fill="#006233"/>
          <rect x="9" y="37" width="44" height="37" fill="#f0f0f0"/>
          <path d="M31 16 A13 13 0 1 1 31 58 A11 11 0 1 0 31 16 Z"
                fill="#d21034" fill-opacity="0.95"/>
          <polygon
            points="31,27 32.8,33.5 39.5,33.5 34,37 36,43.5 31,40 26,43.5 28,37 22.5,33.5 29.2,33.5"
            fill="#d21034" fill-opacity="0.95" transform="translate(0,4)"/>
        </g>
        <text x="95" y="52" font-size="17" fill="#d4af37" fill-opacity="0.9"
              filter="url(#gf)">&#9733;</text>
        <text x="200" y="44" font-size="13" fill="#d4af37" fill-opacity="0.75">&#9733;</text>
        <text x="80" y="90" font-size="11" fill="#d4af37" fill-opacity="0.55">&#10022;</text>
        <text x="150" y="326" text-anchor="middle"
              font-family="Cairo,Arial" font-size="12" font-weight="bold"
              fill="#d4af37" filter="url(#gf)">&#x623;&#x646;&#x627; &#x646;&#x627;&#x62C;&#x62D; &#x628;&#x625;&#x630;&#x646; &#x627;&#x644;&#x644;&#x647;</text>
      </svg>
    </div>
  </div>
  <div class="cd-wrap">
    <div class="cd-title">&#9203; الوقت المتبقي لمعركة النجاح</div>
    <div class="cd-bar" id="cd-bar"></div>
    <div class="cd-msg" id="cd-msg">""" + intensity_msg + """</div>
  </div>
</div>
<script>
  var BEM_TS = new Date("2026-05-19T08:00:00").getTime();
  var LABELS = ["\u064a\u0648\u0645","\u0633\u0627\u0639\u0629","\u062f\u0642\u064a\u0642\u0629","\u062b\u0627\u0646\u064a\u0629"];
  function pad(n){return n<10?"0"+n:String(n);}
  function tick(){
    var diff = BEM_TS - Date.now();
    if(diff<=0){document.getElementById("cd-bar").textContent="\u0627\u0646\u062a\u0647\u0649 \u0627\u0644\u0648\u0642\u062a";return;}
    var vals=[
      Math.floor(diff/86400000),
      Math.floor((diff%86400000)/3600000),
      Math.floor((diff%3600000)/60000),
      Math.floor((diff%60000)/1000)
    ];
    var html="";
    vals.forEach(function(v,i){
      html+='<div class="cd-unit"><span class="cd-num">'+(i===0?v:pad(v))+'</span><span class="cd-lbl">'+LABELS[i]+'</span></div>';
      if(i<3) html+='<span class="cd-sep">:</span>';
    });
    document.getElementById("cd-bar").innerHTML=html;
  }
  tick();
  setInterval(tick,1000);
</script>
</body>
</html>"""
    )
    components.html(hero_html, height=520, scrolling=False)
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

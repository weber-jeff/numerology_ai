from typing import TypedDict, List, Optional

class NumerologyAnalysis(TypedDict, total=False):
    summary: str
    advice: str
    master: bool
    traits: List[str]
    strengths: List[str]
    weaknesses: List[str]
    business: Optional[str]
    relationships: Optional[str]
    purpose: Optional[str]
    element: Optional[str]
    color: Optional[str]
    vibration: Optional[str]

def build_report_string(
    number: int,
    title: str,
    emoji: str,
    analysis: NumerologyAnalysis,
    include_element: bool = False,
    include_color_vibrations: bool = False
) -> str:
    report = "=" * 60 + "\n"
    report += f"{emoji} {title} Number {number} Report {emoji}\n"
    report += "=" * 60 + "\n"
    report += f"🧾 Summary:\n{analysis.get('summary', 'No summary available.')}\n\n"
    report += f"💡 Advice:\n{analysis.get('advice', 'No advice available.')}\n\n"

    if analysis.get('master') is not None:
        master_status = "Yes" if analysis['master'] else "No"
        report += f"🌟 Master Number: {master_status}\n"

    if include_element and 'element' in analysis and analysis['element']:
        report += f"🌿 Element: {analysis['element']}\n"

    if include_color_vibrations:
        if 'color' in analysis and analysis['color']:
            report += f"🎨 Color: {analysis['color']}\n"
        if 'vibration' in analysis and analysis['vibration']:
            report += f"🎵 Vibration: {analysis['vibration']}\n"

    traits = analysis.get('traits') or []
    strengths = analysis.get('strengths') or []
    weaknesses = analysis.get('weaknesses') or []

    report += "\n🔑 Core Traits:\n"
    report += f" - {', '.join(traits) if traits else 'N/A'}\n"

    report += "✅ Strengths:\n"
    report += f" - {', '.join(strengths) if strengths else 'N/A'}\n"

    report += "⚠️ Weaknesses:\n"
    report += f" - {', '.join(weaknesses) if weaknesses else 'N/A'}\n"

    report += "\n💼 Business Outlook:\n"
    report += f" - {analysis.get('business', 'N/A')}\n"

    report += "\n❤️ Relationships:\n"
    report += f" - {analysis.get('relationships', 'N/A')}\n"

    report += "\n🎯 Life Purpose:\n"
    report += f" - {analysis.get('purpose', 'N/A')}\n"

    report += "=" * 60 + "\n"
    return report

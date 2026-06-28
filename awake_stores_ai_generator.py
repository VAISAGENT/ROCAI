import os
import anthropic

# CONFIGURATION - set ANTHROPIC_API_KEY env var or paste key below
API_KEY = os.getenv("ANTHROPIC_API_KEY", "sk-ant-api03-YOUR_NEW_KEY_HERE")

client = anthropic.Anthropic(api_key=API_KEY)


def generate_awake_audit_report() -> str:
    """Uses Claude to generate a detailed Awake Stores audit report as JSON."""

    audit_prompt = """
    You are a digital business strategist analyzing Awake Stores (cannabis dispensary, Brooklyn & Fort Lauderdale).

    Based on their current state:
    - Instagram: 64 followers on main account, 999 on secondary (@awakecanna) - split audience
    - Website: awakestores.com - clean design but no visitor tracking, manual chat only
    - Operating hours: 12 PM - 8 PM (closed 8 PM - 12 PM)
    - Products: Edibles, Drinks, Topicals, Concentrates, Flower, Vapes, Accessories
    - Locations: Brooklyn (Park Slope) & Fort Lauderdale
    - Current gaps: No 24/7 customer service, no voice AI, no automated social posting, no lead capture

    Generate a detailed audit report with:
    1. Executive Summary (overall score, key findings)
    2. Critical gaps (list 5-7 major conversion blockers)
    3. Revenue impact calculation (estimated lost monthly revenue)
    4. Immediate solutions (30-day roadmap)
    5. Pricing proposal (setup fee + monthly retainer)
    6. Next steps

    Format as JSON for easy parsing.
    """

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": audit_prompt}],
    )

    return message.content[0].text


def generate_outreach_email() -> str:
    """Uses Claude to generate a personalized outreach email for Awake Stores."""

    email_prompt = """
    Write a concise outreach email to the owner/partners of Awake Stores (cannabis dispensary in Brooklyn & Fort Lauderdale).

    Email should:
    - Acknowledge their strong brand and product
    - Identify the specific problem: losing customers outside 12 PM - 8 PM when closed
    - Quantify cost: estimate they're losing $3-5K/month in after-hours orders
    - Position solution: 24/7 AI agents, automated social posting, visitor tracking
    - Sound like a peer/strategist, NOT a salesperson
    - Include a soft CTA (discovery call)
    - Keep it under 150 words

    Send to: parkslope@awakestores.com
    From: Kyle Strand (Operations Specialist)
    """

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": email_prompt}],
    )

    return message.content[0].text


if __name__ == "__main__":
    print("=" * 80)
    print("AWAKE STORES - AUDIT & OUTREACH GENERATION")
    print("=" * 80)

    print("\n[1/2] Generating audit report...\n")
    audit = generate_awake_audit_report()
    print(audit)

    print("\n" + "=" * 80)
    print("\n[2/2] Generating outreach email...\n")
    email = generate_outreach_email()
    print(email)

    print("\n" + "=" * 80)
    print("COMPLETE - Ready to send to Awake Stores")
    print("=" * 80)

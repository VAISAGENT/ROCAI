import anthropic
from datetime import datetime

# API key is read from the ANTHROPIC_API_KEY environment variable automatically
client = anthropic.Anthropic()


def generate_awake_audit() -> str:
    """Generates comprehensive Awake Stores audit using Claude API."""

    audit_prompt = """
    You are a digital business strategist analyzing Awake Stores (cannabis dispensary with locations in Brooklyn Park Slope & Fort Lauderdale).

    Current state:
    - Instagram: Main @awakestores (64 followers, 362 posts) + secondary @awakecanna (999 followers, 127 posts) = split audience
    - Website: awakestores.com - clean design but critical gaps in conversion
    - Operating hours: 12 PM - 8 PM daily (closed 8 PM - 12 PM = losing customers)
    - Products: Edibles, Drinks, Topicals, Concentrates, Flower, Vapes, Accessories
    - Two locations: Brooklyn (204 Garfield Pl, Park Slope) & Fort Lauderdale
    - Current customer service: Manual chat only (hours-dependent), no voice AI, no 24/7 support

    Generate a strategic audit report in clear sections:

    1. EXECUTIVE SUMMARY
       - Overall digital maturity score (1-10)
       - Top 3 strengths
       - Top 3 critical gaps

    2. SOCIAL MEDIA ANALYSIS
       - Current performance metrics
       - Engagement rate assessment
       - Specific gaps (posting frequency, content strategy, platform utilization)
       - TikTok opportunity assessment

    3. WEBSITE & CONVERSION GAPS
       - List 5 critical conversion blockers
       - Revenue impact of each gap
       - Visitor journey breakdown

    4. AFTER-HOURS REVENUE LOSS
       - Estimated monthly lost revenue (be specific with calculation)
       - Customer inquiries happening at 8 PM - 12 PM that go unanswered

    5. PROPOSED SOLUTIONS (30-60-90 day roadmap)
       - Immediate wins (first 30 days)
       - Medium-term builds (30-60 days)
       - Ongoing optimization

    6. PRICING PROPOSAL
       - Setup fee recommendation
       - Monthly retainer recommendation
       - What's included in retainer
       - Optional add-ons

    Make it compelling but grounded in their actual situation. Sound like a peer strategist, not a vendor.
    """

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        messages=[{"role": "user", "content": audit_prompt}],
    )

    return message.content[0].text


def generate_outreach_email() -> str:
    """Generates personalized outreach email for Awake Stores leadership."""

    email_prompt = """
    Write a short, direct outreach email to the owners/partners of Awake Stores.

    Requirements:
    - Acknowledge their strong brand and product quality
    - Lead with the specific problem: losing customers outside business hours (8 PM - 12 PM)
    - Quantify impact: estimate $3,500 - $5,800 lost per month in after-hours orders
    - Position the solution: 24/7 voice AI, automated social posting, visitor tracking, lead capture
    - Sound like Kyle Strand (operations strategist), not a salesman
    - No corporate jargon - direct and honest
    - Include soft CTA: "Let's talk for 15 minutes about what this could mean for your November revenue"
    - Keep under 200 words
    - Format: Email to parkslope@awakestores.com
    """

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        messages=[{"role": "user", "content": email_prompt}],
    )

    return message.content[0].text


if __name__ == "__main__":
    print("=" * 90)
    print("AWAKE STORES - DIGITAL AUDIT & OUTREACH PACKAGE")
    print("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 90)

    print("\n[GENERATING AUDIT REPORT...]\n")
    audit_report = generate_awake_audit()
    print(audit_report)

    print("\n" + "=" * 90)
    print("\n[GENERATING OUTREACH EMAIL...]\n")
    outreach_email = generate_outreach_email()
    print(outreach_email)

    print("\n" + "=" * 90)
    print("\nAWAKE PACKAGE COMPLETE")
    print("Next: Review above, send email to parkslope@awakestores.com")
    print("=" * 90)

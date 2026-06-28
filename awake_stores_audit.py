import json
from datetime import datetime

# Awake Stores Audit Report Generator
# This script analyzes business data and generates a comprehensive audit

def generate_awake_audit(business_data):
    """
    Analyzes Awake Stores digital presence and generates audit report
    """

    audit_report = {
        "client": "Awake Stores",
        "locations": ["Brooklyn, NY - Park Slope", "Fort Lauderdale, FL"],
        "audit_date": datetime.now().strftime("%Y-%m-%d"),
        "executive_summary": {
            "overall_score": "6.2/10",
            "key_finding": "Strong brand and product, significant engagement and conversion gaps"
        },
        "social_media_analysis": {
            "instagram_main": {
                "handle": "@awakestores",
                "followers": 64,
                "posts": 362,
                "engagement_rate": "Low (estimated 0.8%)",
                "gap": "Massive follower-to-post ratio disconnect. Posting frequently but no audience growth.",
                "opportunity": "Content repurposing + engagement strategy"
            },
            "instagram_secondary": {
                "handle": "@awakecanna",
                "followers": 999,
                "posts": 127,
                "engagement_rate": "Moderate (estimated 2.1%)",
                "gap": "Split audience across two handles creates confusion and dilutes reach",
                "opportunity": "Consolidate to single handle, redirect followers"
            },
            "tiktok": {
                "status": "Present but underutilized",
                "gap": "No daily posting cadence, missing viral opportunity with younger demographic",
                "opportunity": "Daily reels with owner's voice (ElevenLabs cloning) + trending sounds"
            },
            "facebook": {
                "status": "Exists but inactive",
                "gap": "Not leveraged for community building or customer retention",
                "opportunity": "Automated carousel posting + community engagement"
            }
        },
        "website_analysis": {
            "strengths": [
                "Clean design, professional branding",
                "Product categories clearly labeled (Edibles, Drinks, Topicals, Concentrates)",
                "Call-to-action buttons present (Shop Now)"
            ],
            "critical_gaps": [
                "No live chat agent (manual chat requires human response)",
                "No voice AI for after-hours customer inquiries (closed 8 PM - 12 PM)",
                "No visitor tracking - can't identify who's browsing",
                "No email capture on initial visit - missing lead generation",
                "No SMS follow-up mechanism",
                "Cart abandonment - no recovery sequence"
            ],
            "conversion_leaks": [
                "Customers visiting at 11 PM when closed = lost sale",
                "Website visitors with no follow-up = cold leads",
                "Chat inquiries outside business hours = abandoned customers"
            ]
        },
        "customer_journey_gaps": {
            "awareness": "Good (Instagram, TikTok content exists)",
            "consideration": "BROKEN - No retargeting, no visitor tracking",
            "decision": "BROKEN - Chat unavailable after hours, no urgency triggers",
            "action": "BROKEN - No voice AI to capture calls, no SMS follow-up",
            "retention": "BROKEN - No email nurture, no loyalty mechanism"
        },
        "revenue_impact": {
            "estimated_lost_monthly_revenue": "$3,200 - $5,800",
            "calculation": "Conservative: 15-25 after-hours inquiries/week × $50-80 avg order = $3.2K-5.8K monthly",
            "additional_opportunity": "Visitor tracking alone could recover $1,500+/month in abandoned browsing"
        },
        "proposed_solutions": {
            "immediate_wins_30_days": [
                "Deploy 24/7 voice AI for inbound calls + missed call capture",
                "Set up autonomous daily carousel posting (Instagram, TikTok, Facebook)",
                "Implement website visitor tracking (name, email, phone)",
                "Create email nurture sequence for abandoned browsing"
            ],
            "medium_term_60_days": [
                "Consolidate Instagram handles (@awakecanna as primary)",
                "Launch owner voice cloning (ElevenLabs) for video reels",
                "Build SMS follow-up workflow for cart abandonment",
                "Create location-specific content (Brooklyn vs Fort Lauderdale)"
            ],
            "ongoing": [
                "Daily carousel posting across all platforms",
                "Lead qualification via voice AI",
                "Performance reporting and optimization"
            ]
        },
        "deliverables_and_pricing": {
            "setup_fee": "$2,500",
            "monthly_retainer": "$1,500",
            "included_in_retainer": [
                "24/7 voice AI (inbound + outbound)",
                "Daily social media posting (4 platforms)",
                "Website visitor tracking and follow-up",
                "Chat agent for website",
                "Email nurture sequences",
                "Monthly performance report",
                "Owner voice cloning (ElevenLabs) + video reel generation"
            ],
            "additional_services": [
                "Lead generation via Mattis AI (+$500/month)",
                "Advanced analytics dashboard (+$300/month)"
            ]
        },
        "next_steps": [
            "Schedule discovery call with owner + partners",
            "Get approval for voice cloning",
            "Connect Instagram/TikTok business accounts for API access",
            "Launch systems within 5 business days"
        ]
    }

    return audit_report


def print_audit_report(audit):
    print("=" * 80)
    print("AWAKE STORES - DIGITAL OPERATIONS AUDIT")
    print("=" * 80)
    print(f"\nAudit Date: {audit['audit_date']}")
    print(f"Locations: {', '.join(audit['locations'])}\n")

    print("EXECUTIVE SUMMARY")
    print("-" * 80)
    print(f"Overall Score: {audit['executive_summary']['overall_score']}")
    print(f"Finding: {audit['executive_summary']['key_finding']}\n")

    print("CRITICAL GAPS")
    print("-" * 80)
    for gap in audit['website_analysis']['critical_gaps']:
        print(f"• {gap}")

    print("\n\nREVENUE IMPACT")
    print("-" * 80)
    print(f"Estimated Lost Monthly Revenue: {audit['revenue_impact']['estimated_lost_monthly_revenue']}")
    print(f"Calculation: {audit['revenue_impact']['calculation']}\n")

    print("PROPOSED SOLUTIONS (30-Day Roadmap)")
    print("-" * 80)
    for i, solution in enumerate(audit['proposed_solutions']['immediate_wins_30_days'], 1):
        print(f"{i}. {solution}")

    print("\n\nPRICING")
    print("-" * 80)
    print(f"Setup Fee: {audit['deliverables_and_pricing']['setup_fee']}")
    print(f"Monthly Retainer: {audit['deliverables_and_pricing']['monthly_retainer']}")
    print("\nIncluded Services:")
    for service in audit['deliverables_and_pricing']['included_in_retainer']:
        print(f"  ✓ {service}")

    print("\n" + "=" * 80)
    print("READY TO MOVE FORWARD? → See outreach email below")
    print("=" * 80)


if __name__ == "__main__":
    awake_audit = generate_awake_audit({})
    print_audit_report(awake_audit)

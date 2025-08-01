import time

email_templates = {
    "high": [
        "Hi {name}, thanks for booking a demo! Want to revisit what we discussed?",
        "Hey {name}, still thinking about our product? Let’s talk next steps."
    ],
    "medium": [
        "Hi {name}, hope you liked our webinar — got any questions?",
        "Hey {name}, we noticed you downloaded our guide. Here’s a case study too!"
    ],
    "low": [
        "Hi {name}, just wanted to introduce ourselves — here's a quick overview.",
        "Hey {name}, check out this story from someone like you!"
    ]
}

def nurture_lead(name, intent_level):
    print(f"\n📨 Starting nurture track for: {name} (Intent: {intent_level})\n")
    sequence = email_templates.get(intent_level, [])
    for i, template in enumerate(sequence):
        message = template.format(name=name)
        print(f"Email {i+1}: {message}")
        time.sleep(0.5)

if __name__ == "__main__":
    test_leads = [
        {"name": "Ravi", "intent": "high"},
        {"name": "Priya", "intent": "medium"},
        {"name": "Amit", "intent": "low"}
    ]
    for lead in test_leads:
        nurture_lead(lead["name"], lead["intent"])

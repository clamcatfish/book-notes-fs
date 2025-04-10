import json
with open ('notes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)
# Sample input data (replace this with actual input)
data = [
    {
        "id": 1744217764151,
        "title": "Learning to Cope",
        "page": "17",
        "book": "The Beauty of Discomfort",
        "tags": ["Difficulty", "Perseverance"],
        "description": "...",
        "comments": "Get out of your comfort zone\r\n\r\nline break.",
        "helpfulness": 4,
        "createdAt": "2025-04-09T16:56:04.152Z",
        "updatedAt": "2025-04-09T16:56:04.152Z"
    },
    {
        "id": 1744219870914,
        "title": "What Would a ____ Person Do?",
        "page": "40",
        "book": "Atomic Habits",
        "tags": ["Focus", "Virtues"],
        "description": "...",
        "comments": "What would the perfect boyfriend do?",
        "helpfulness": 6,
        "createdAt": "2025-04-09T17:31:10.914Z",
        "updatedAt": "2025-04-09T17:31:10.916Z"
    }
]

# Tag mapping
tag_map = {
    "Achievement": ["Achievement", "Hard Work", "Talent", "Praise", "Success", "Working"],
    "Adaptation": ["Attachment", "Change", "Loss", "Death", "Control"],
    "Anxiety": ["Faith", "Cowardice", "Fear", "Worrying", "Anxiety"],
    "Challenge": ["Challenge", "Difficulty", "Discomfort", "Failure", "Hardship", "Pain", "Stress", "Struggle", "Suffering", "Sacrifice"],
    "Communication": ["Leadership", "Teamwork", "Arguing", "Body Language", "Communication", "Criticism", "Deceit", "Socializing"],
    "Ego": ["Ego", "Entitlement", "Pride"],
    "Focus": ["Productivity", "Mindset", "Attention", "Decision Making", "Discipline", "Focus", "Present", "Thinking", "Will", "Willpower", "Distraction", "Procrastination"],
    "Depression": ["Rumination", "Despair", "Hopelessness", "Depression", "Regret", "Boredom", "Sadness"],
    "Growth": ["Competition", "Complacency", "Growth", "Improvement", "Performance", "Strength"],
    "Hate": ["Anger", "Bitterness", "Jealousy", "Contempt", "Negativity", "Emotion", "Frustration", "Hatred", "Hope", "Nervosity", "Nervousness", "Revenge"],
    "Health": ["Age", "Sleep", "Well Being"],
    "Learning": ["Knowledge", "Learning", "Memory", "Perception", "Understanding"],
    "Mapping": ["Visualization", "Expectations", "Goal Setting", "Organization", "Planning", "Review", "Time"],
    "Mindfulness": ["Calmness", "Acceptance", "Awareness", "Clarity", "Control", "Meditation", "Mindfulness", "Gratitude"],
    "Motivation": ["Confidence", "Action", "Ambition", "Passion", "Purpose", "Motivation", "Belief"],
    "Positivity": ["Enjoyment", "Happiness", "Positivity"],
    "Relationships": ["Dating", "Intimacy", "Love", "Marriage", "Parenting", "Sex", "Masculinity", "Giving"],
    "Resilience": ["Dedication", "Determination", "Mental Fortitude", "Endurance", "Perseverance", "Persistance"],
    "Routine": ["Behaviour", "Consistency", "Habits", "Media", "Practice", "Routine", "Repetition"],
    "Vices": ["Procrastination", "Resistance", "Self Control", "Abstinence", "Addiction", "Desire", "Impulse", "Indulgence", "Pleasure", "Temptation"],
    "Virtues": ["Courage", "Attitude", "Character", "Identity", "Virtue", "Humility", "Kindness", "Patience", "Responsibility", "Honesty", "Masculinity", "Empathy", "Forgiveness"]
}

# Reverse mapping for quick lookup
tag_lookup = {}
for category, terms in tag_map.items():
    for tag in terms:
        tag_lookup[tag.lower()] = category

# Set to collect unmatched tags
unmatched_tags = set()

# Process each entry
for entry in data:
    new_tags = set()
    for tag in entry["tags"]:
        category = tag_lookup.get(tag.lower())
        if category:
            new_tags.add(category)
        else:
            unmatched_tags.add(tag)
            new_tags.add(tag)  # Still include for now, to avoid data loss
    entry["tags"] = sorted(new_tags)

# Output results
print(json.dumps(data, indent=2))
print("\nUnmatched tags for review:", sorted(unmatched_tags))

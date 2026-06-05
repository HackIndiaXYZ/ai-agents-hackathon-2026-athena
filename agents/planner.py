# agents/planner.py
def create_learning_plan(level, topic):

    if level == "Beginner":
        return [
            f"Study basics of {topic}",
            f"Practice introductory questions on {topic}",
            f"Take an easy quiz on {topic}"
        ]

    elif level == "Intermediate":
        return [
            f"Review core concepts of {topic}",
            f"Solve moderate problems",
            f"Take a medium difficulty quiz"
        ]

    else:
        return [
            f"Explore advanced concepts in {topic}",
            f"Solve challenging problems",
            f"Take an advanced quiz"
        ]
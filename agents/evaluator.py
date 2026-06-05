# agenst/evaluator.py
def evaluate_quiz(score, total):

    percentage = (score / total) * 100

    if percentage >= 80:
        level = "Advanced"
        recommendation = "Move to harder concepts"

    elif percentage >= 50:
        level = "Intermediate"
        recommendation = "Practice similar questions"

    else:
        level = "Beginner"
        recommendation = "Revise fundamentals"

    return {
        "score": score,
        "total": total,
        "percentage": round(percentage, 2),
        "level": level,
        "recommendation": recommendation
    }
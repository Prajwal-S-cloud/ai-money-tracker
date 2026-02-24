def analyze_spending(df):

    total = df["amount"].sum()
    summary = df.groupby("category")["amount"].sum()

    return total, summary


def financial_advice(summary):

    advice = []

    if "Food" in summary and summary["Food"] > 500:
        advice.append("You are spending a lot on food.")

    if "Shopping" in summary and summary["Shopping"] > 1000:
        advice.append("Shopping expenses are high.")

    if len(advice) == 0:
        advice.append("Your spending looks balanced.")

    return advice
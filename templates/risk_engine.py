def calculate_risk(contract_value, money_released, project_progress,
                   unusual_transaction=False,
                   community_delay=False,
                   evidence_missing=False):

    risk_score = 0
    reasons = []

    # 1. Check how much money has been released
    financial_progress = (money_released / contract_value) * 100

    if financial_progress >= 80:
        risk_score += 25
        reasons.append("A large percentage of the contract funds has been released.")

    elif financial_progress >= 60:
        risk_score += 15
        reasons.append("A significant percentage of the contract funds has been released.")

    # 2. Compare financial progress with project progress
    difference = financial_progress - project_progress

    if difference >= 40:
        risk_score += 30
        reasons.append("Spending is significantly ahead of verified project progress.")

    elif difference >= 20:
        risk_score += 15
        reasons.append("Spending is ahead of verified project progress.")

    # 3. Check unusual transactions
    if unusual_transaction:
        risk_score += 20
        reasons.append("An unusual transaction was detected.")

    # 4. Check community reports
    if community_delay:
        risk_score += 10
        reasons.append("Community reports indicate possible project delays.")

    # 5. Check evidence
    if evidence_missing:
        risk_score += 10
        reasons.append("Required project evidence is missing or incomplete.")

    # Make sure score does not go above 100
    if risk_score > 100:
        risk_score = 100

    # Determine risk level
    if risk_score <= 30:
        risk_level = "LOW"

    elif risk_score <= 60:
        risk_level = "MEDIUM"

    elif risk_score <= 80:
        risk_level = "HIGH"

    else:
        risk_level = "CRITICAL"

    # Recommendation
    if risk_level == "LOW":
        recommendation = "Continue monitoring the project."

    elif risk_level == "MEDIUM":
        recommendation = "Review the transactions and project progress."

    elif risk_level == "HIGH":
        recommendation = "Investigate the project before releasing further funds."

    else:
        recommendation = "Hold the next payment and investigate the project."

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons,
        "recommendation": recommendation
    }


# TEST DATA
result = calculate_risk(
    contract_value=20000000,
    money_released=12000000,
    project_progress=30,
    unusual_transaction=True,
    community_delay=True,
    evidence_missing=False
)

print("Risk Score:", result["risk_score"], "/ 100")
print("Risk Level:", result["risk_level"])

print("\nReasons:")
for reason in result["reasons"]:
    print("-", reason)

print("\nRecommendation:")
print(result["recommendation"])
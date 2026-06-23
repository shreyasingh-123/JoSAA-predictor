# JoSAA 2025 Cutoff Data - MNNIT Allahabad,MANIT Bhopal, MNIT Jaipur.
# Format: [Opening Rank, Closing Rank].
# Data from JoSAA 2025, Round 6. Update if 2026 changes.

cutoff_data = {
    "MNNIT_Allahabad": {
        "CSE": {"HS": [2500,6562], "OS": [2730,4594], "Female_HS": [5451,11813], "Female_OS": [5064,10173]},
        "CE": {"HS": [17628,29451], "OS": [8568,31589], "Female_HS": [34243,53343], "Female_OS": [37704,45561]},
        "EE": {"HS": [9668,11483], "OS": [8915,11665], "Female_HS": [19900,24704], "Female_OS": [20650,20844]},
        "ECM": {"HS": [11780,12759], "OS": [7635,12340], "Female_HS": [19937,19937], "Female_OS": [21208,21208]},
        "ECE": {"HS": [6590,9577], "OS": [5326,8532], "Female_HS": [13267,18919], "Female_OS": [10515,14971]},
        "CHE": {"HS": [16240,21558], "OS": [20344,22469], "Female_HS": [30210,32196], "Female_OS": [36209,38172]}
    },
    "MANIT_Bhopal": {
        "CSE": {"HS": [6429,11415], "OS": [5942,9249], "Female_HS": [12477,19840], "Female_OS": [11842,16148]},
        "ECE": {"HS": [11462,18120], "OS": [10618,14205], "Female_HS": [18188,27015], "Female_OS": [19334,24250]},
        "EE": {"HS": [19570,24120], "OS": [16513,20770], "Female_HS": [28241,37576], "Female_OS": [26466,31132]}
    },
    "MNIT_Jaipur": {
        "CSE": {"HS": [2937,6013], "OS": [3027,5601], "Female_HS": [2422,10065], "Female_OS": [5059,8485]},
        "ECE": {"HS": [8273,10539], "OS": [6608,9667], "Female_HS": [10644,17818], "Female_OS": [11903,15895]},
        "EE": {"HS": [11611,14240], "OS": [9803,14665], "Female_HS": [17981,21551], "Female_OS": [22065,23400]},
        "CHE": {"HS": [20902,26449], "OS": [15363,25442], "Female_HS": [26304,32446], "Female_OS": [25687,33976]}
    }
}

def get_user_input():
    print("=== JOSAA 2026 Branch Predictor ===")
    print("Based on JOSAA 2025 Round 6 Cutoffs\n")

    try:
        rank = int(input("Enter your JEE Main Rank: "))
        gender = input("Gender [M/F]: ").upper()
        home_state = input("Enter your state code [UP/MP/RJ]:").upper()
        return rank, gender, home_state
    except ValueError:
        print("Please enter a valid number for rank!")
        return None, None, None

def check_eligibility(rank, college, branch, gender, home_state):
    if college not in cutoff_data or branch not in cutoff_data[college]:
        return "No data"

    branch_data = cutoff_data[college][branch]

    # Determine which cutoff to use
    key = "OS" # default
    if college == "MNNIT_Allahabad" and home_state == "UP":
        key = "HS"
    elif college == "MANIT_Bhopal" and home_state == "MP":
        key = "HS"
    elif college == "MNIT_Jaipur" and home_state == "RJ":
        key = "HS"
    if gender == "F" and f"Female_{key}" in branch_data:
        key = f"Female_{key}"

    if key not in branch_data:
        key = "OS" # fallback

    opening, closing = branch_data[key]

    if rank <= closing:
        if rank <= opening:
            return f"✅ SAFE - Rank {rank} < Opening {opening}"
        else:
            return f"🟡 CHANCE - Rank {rank} between {opening}-{closing}"
    else:
        return f"❌ NO - Rank {rank} > Closing {closing}"

def predict_branches(rank, gender, home_state):
    print(f"\n=== Results for Rank {rank}, {gender}, HS={home_state} ===\n")

    colleges_to_check = [
        ("MANIT_Bhopal", ["CSE", "ECE", "EE"]),
        ("MNIT_Jaipur", ["CSE", "ECE", "EE", "CHE"]),
        ("MNNIT_Allahabad", ["CSE", "CE", "ECE", "ECM", "EE", "CHE"])
    ]

    for college, branches in colleges_to_check:
        print(f"--- {college} ---")
        for branch in branches:
            result = check_eligibility(rank, college, branch, gender, home_state)
            print(f"{branch}: {result}")
        print()

def main():
    rank, gender, home_state = get_user_input()
    if rank is None:
        return

    predict_branches(rank, gender, home_state)

    print("Note: Cutoffs change yearly. Use for reference only.")
    print("Data source: JoSAA 2025 Round 6. OBC/EWS/SC/ST cutoffs not added - upgrade this!")

if __name__ == "__main__":
    main()

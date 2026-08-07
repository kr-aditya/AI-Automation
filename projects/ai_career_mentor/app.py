from chains.career_chain import career_chain

print("=" * 65)
print("🤖 AI Career Mentor")
print("=" * 65)

name = input("Your Name: ")
skills = input("Your Skills (comma separated): ")
experience = input("Your Experience: ")
target_role = input("Target Role: ")

print("\nAnalyzing profile...\n")

result = career_chain.invoke(
    {
        "name": name,
        "skills": skills,
        "experience": experience,
        "target_role": target_role,
    }
)

print("=" * 60)
print("CAREER ANALYSIS")
print("=" * 60)

print(f"\nCurrent Level : {result.current_level}")

print(f"\nJob Match Score : {result.match_score}/100")

print("\nStrengths")
for item in result.strengths:
    print(f"• {item}")

print("\nWeaknesses")
for item in result.weaknesses:
    print(f"• {item}")

print("\nMissing Skills")
for item in result.missing_skills:
    print(f"• {item}")

print("\nLearning Priority")
for item in result.learning_priority:
    print(f"• {item}")

print("\nCareer Summary")
print(result.career_summary)

print("=" * 60)
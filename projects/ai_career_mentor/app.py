from chains.career_chain import career_chain
from chains.roadmap_chain import roadmap_chain
from chains.project_chain import project_chain

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

roadmap_input = {
    "career_analysis": result.model_dump_json(indent=2)
}

roadmap_result = roadmap_chain.invoke(roadmap_input)

project_input = {
    "career_analysis": result.model_dump_json(indent=2),
    "roadmap": roadmap_result.model_dump_json(indent=2)
}

project_result = project_chain.invoke(project_input)

print("=" * 65)
print("CAREER ANALYSIS")
print("=" * 65)

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

print("=" * 65)

print("\n" + "=" * 65)
print("PERSONALIZED CAREER ROADMAP")
print("=" * 65)

print(f"\n🎯 Target Role")
print(roadmap_result.target_role)

print(f"\n⏱️ Recommended Duration")
print(roadmap_result.roadmap_duration)

print(f"\n📚 Learning Phases")
for index, phase in enumerate(roadmap_result.phases, start=1):
    print(f"{index}. {phase}")

print(f"\n🧠 Skills to Learn")
for skill in roadmap_result.skills_to_learn:
    print(f"• {skill}")

print(f"\n🛠️ Projects to Build")
for project in roadmap_result.projects_to_build:
    print(f"• {project}")

print(f"\n💡 Final Advice")
print(roadmap_result.final_advice)

print("\n" + "=" * 65)

print("\n" + "=" * 65)
print("PROJECT RECOMMENDATIONS")
print("=" * 65)

for index, project in enumerate(project_result.projects, start=1):

    print(f"\n🚀 Project {index}: {project.title}")

    print(f"Difficulty: {project.difficulty}")

    print("\nPurpose:")
    print(project.purpose)

    print("\nTech Stack:")
    for tech in project.tech_stack:
        print(f"• {tech}")

    print("\nKey Features:")
    for feature in project.key_features:
        print(f"• {feature}")

    print("\n" + "-" * 65)

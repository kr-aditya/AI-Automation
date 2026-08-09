def display_career_analysis(result):
    print("\n" + "=" * 65)
    print("CAREER ANALYSIS")
    print("=" * 65)

    print(f"\nCurrent Level: {result.current_level}")
    print(f"\nJob Match Score: {result.match_score}/100")

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


def display_roadmap(result):
    print("\n" + "=" * 65)
    print("PERSONALIZED CAREER ROADMAP")
    print("=" * 65)

    print("\n🎯 Target Role")
    print(result.target_role)

    print("\n⏱️ Recommended Duration")
    print(result.roadmap_duration)

    print("\n📚 Learning Phases")
    for index, phase in enumerate(result.phases, start=1):
        print(f"{index}. {phase}")

    print("\n🧠 Skills to Learn")
    for skill in result.skills_to_learn:
        print(f"• {skill}")

    print("\n🛠️ Projects to Build")
    for project in result.projects_to_build:
        print(f"• {project}")

    print("\n💡 Final Advice")
    print(result.final_advice)


def display_projects(result):
    print("\n" + "=" * 65)
    print("PROJECT RECOMMENDATIONS")
    print("=" * 65)

    for index, project in enumerate(result.projects, start=1):
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


def display_interview_preparation(result):
    print("\n" + "=" * 65)
    print("INTERVIEW PREPARATION")
    print("=" * 65)

    print("\n📚 Important Topics")
    for topic in result.important_topics:
        print(f"• {topic}")

    print("\n💻 Technical Questions")
    for index, question in enumerate(
        result.technical_questions,
        start=1
    ):
        print(f"{index}. {question}")

    print("\n🤝 Behavioral Questions")
    for index, question in enumerate(
        result.behavioral_questions,
        start=1
    ):
        print(f"{index}. {question}")

    print("\n🛠️ Practical Questions")
    for index, question in enumerate(
        result.practical_questions,
        start=1
    ):
        print(f"{index}. {question}")

    print("\n🎯 Preparation Strategy")
    for index, strategy in enumerate(
        result.preparation_strategy,
        start=1
    ):
        print(f"{index}. {strategy}")
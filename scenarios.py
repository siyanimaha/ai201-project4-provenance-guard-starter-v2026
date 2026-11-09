
"""
CodePath AI201 - Project 4: Provenance Guard
Unit 8 - Milestone 3
Evaluation Scenarios
"""

# Synthetic human-style writing examples.
# These are AI-generated, not verified human-authored samples.

HUMAN_STYLE_WRITING = [
    "Yesterday I went to the library to finish my homework. I thought it would only take an hour, but I ended up staying much longer. I had trouble understanding one of the questions, so I went back through my class notes. After a while, I figured out what I was doing wrong.",

    "I had a busy day at school today. My first class went pretty well, but I was tired by the afternoon. I still had an assignment to finish before midnight. I went home, ate dinner, and worked on it until I was done.",

    "Last week I was working on a programming assignment and my code kept giving me an error. I checked everything several times but could not find the problem. Eventually I realized I had forgotten to initialize a variable. It was a small mistake that took a long time to find.",

    "I like working on projects with other students because everyone has different ideas. Sometimes it is difficult when people have different schedules. I think communication is important because it helps everyone understand what needs to be done.",

    "One thing I have learned from college is that managing time is important. At first I thought I could finish all my homework at the last minute. That did not always work out. Now I try to start my assignments earlier.",

    "I was studying for my exam and noticed that I understood some topics better than others. I decided to spend more time practicing the difficult questions. After doing a few examples, I started feeling more comfortable with the material.",

    "For our class project, we had to create a design that students could use. We talked about different ideas and tried to figure out which features would be useful. Some of our original ideas were confusing, so we changed them after getting feedback.",

    "I enjoy learning computer science because I like understanding how programs work. Sometimes programming can be frustrating, especially when something does not run correctly. But when I finally solve the problem, I feel happy with what I accomplished.",

    "This semester has been busy because I have several classes and projects. Some weeks are harder than others, especially when assignments are due around the same time. I try to make a list of what I need to finish so I do not forget anything.",

    "I recently worked on a project where I had to read several articles and write a summary. Some articles were difficult to understand because they used unfamiliar words. I took notes while reading and looked for the main ideas before writing my summary.",
]

# AI-generated samples for comparison.

AI_WRITING = [
    "Artificial intelligence is transforming modern industries by improving operational efficiency, automating repetitive tasks, and supporting data-driven decision-making across diverse professional environments.",

    "Effective project management requires clearly defined objectives, consistent communication, strategic resource allocation, and continuous performance evaluation to ensure successful outcomes.",

    "Technology plays an increasingly important role in education by providing personalized learning experiences, improving accessibility, and facilitating collaboration among students and educators.",

    "Organizations can enhance productivity through the implementation of structured workflows, comprehensive performance monitoring, and systematic optimization of operational processes.",

    "Sustainable development requires a balanced approach that integrates economic growth, environmental responsibility, and social well-being through coordinated planning and innovation.",
]

SCENARIOS = [
    {
        "name": "synthetic human-style writing",
        "criterion": 1,
        "texts": HUMAN_STYLE_WRITING,
    },
    {
        "name": "AI writing score comparison",
        "criterion": 2,
        "texts": AI_WRITING,
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "I went to class today. After class, I went home and made dinner. Then I finished my homework.",

            "Artificial intelligence enables organizations to streamline operations, improve efficiency, and enhance strategic decision-making.",

            "The system works well. It handles most cases correctly and provides useful results. Users generally find it easy to understand.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {
                "creator_id": "eval_missing"
            },
            {
                "text": "",
                "creator_id": "eval_empty"
            },
            {
                "text": "word " * 12000,
                "creator_id": "eval_huge"
            },
        ],
    },
]


def validate() -> list[str]:
    """
    Validate all evaluation scenarios before running.
    """

    problems = []

    for i, scenario in enumerate(SCENARIOS, 1):

        if not scenario.get("name"):
            problems.append(
                f"Scenario {i} has no name."
            )

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts is not None and bodies is not None:
            problems.append(
                f"Scenario {i} has both texts and bodies."
            )
            continue

        if bodies is not None:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"Scenario {i}, body {j} is not a dictionary."
                    )
            continue

        if not texts:
            problems.append(
                f"Scenario {i} has no texts or bodies."
            )
            continue

        for j, sample in enumerate(texts, 1):

            if not isinstance(sample, str):
                problems.append(
                    f"Scenario {i}, text {j} is not a string."
                )

            elif not sample.strip():
                problems.append(
                    f"Scenario {i}, text {j} is empty."
                )

            elif sample.startswith("REPLACE ME"):
                problems.append(
                    f"Scenario {i}, text {j} is still a placeholder."
                )

    return problems

import json

# Sample input data (replace this with actual input)
data = [
  {
    "id": 1744217764151,
    "title": "Learning to Cope",
    "page": "17",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Difficulty",
      "Perseverance"
    ],
    "description": "Learning to cope with discomfort--disagreement, aggression, and criticism (even wholly unprovoked aggression and criticism)--can be one of the greatest accomplishments of a child's early school years. Robert Reich, who was among other things President Bill Clinton's undersecretary of labor, attributes much of his personal development and even his later professional success to being bullied as a child. ... Reich set about finding ways to offset it. He developed his intellect, for one thing, and formed alliances with larger boys who were willing to protect him. Ultimately, being pushed around on the playground shaped Reich in a deep and lasting way, helping to strengthen his resolve to persevere and overcome. To make something of himself.",
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
    "tags": [
      "Focus",
      "Virtues"
    ],
    "description": "Once you have a handle on the type of person you want to be, you can begin taking small steps to reinforce your desired identity. I have a friend who lost over 100 pounds by asking herself, \"What would a healthy person do?\" All day long, she would use this question as a guide. Would a healthy person walk or take a cab? Would a healthy person order a burrito or salad? She figured if she acted like a healthy preson long engouth, eventually she would become that preson. She was right. ... Your habits shape your identity, and your identity shapes your habits. It's a two-way street.",
    "comments": "What would the perfect boyfriend do?",
    "helpfulness": 6,
    "createdAt": "2025-04-09T17:31:10.914Z",
    "updatedAt": "2025-04-09T17:31:10.916Z"
  },
  {
    "id": 1744217000001,
    "title": "Identity Based Habits",
    "page": "31",
    "book": "Atomic Habits",
    "tags": [
      "Goal Setting",
      "Habits",
      "Identity"
    ],
    "description": "Identity --> Processes --> Outcomes. With identity based habits, the focus is on who you wish to become as opposed to simply what you want to achieve",
    "comments": "Who do you want to be?",
    "helpfulness": 4.9,
    "createdAt": "2024-05-27T21:15:40.104Z",
    "updatedAt": "2025-04-10T16:26:57.596Z"
  },
  {
    "id": 1744217000003,
    "title": "Attention is a mental muscle",
    "page": "8",
    "book": "Focus",
    "tags": [
      "Mental Fortitude",
      "Focus"
    ],
    "description": "Attention is a mental muscle; like any other muscle, it can be strengthened through the right kind of exercise. The fundamental rep for building deliberate attention is simple: When your mind wanders, notice that it has wandered, bring it back to your desired point of focus, and keep it there as long as you can. That basic exercise is at the root of virtually every kind of meditation. Meditation builds concentration and calmness and facilitates recovery from the agitation of stress.",
    "comments": "Bring back your focus, especially when working and枪your willpower is low. Stop thinking about hot Asian chicks and focus up.",
    "helpfulness": 1,
    "createdAt": "2024-05-30T00:29:20.791Z",
    "updatedAt": "2024-05-30T00:29:20.791Z"
  },
  {
    "id": 1744217000004,
    "title": "Identity Build Up",
    "page": "37",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Identity"
    ],
    "description": "This is a gradual evolution. We do not change by snapping our fingers and deciding to be someone entirely new. We change bit by bit, day by day, habit by habit. We are continually undergoing microevolutions of the self",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:00:11.518Z",
    "updatedAt": "2025-03-26T16:14:55.738Z"
  },
  {
    "id": 1744217000006,
    "title": "Make habits easy/hard 4 laws",
    "page": "54",
    "book": "Atomic Habits",
    "tags": [
      "Habits"
    ],
    "description": "[Table] How to Create a Good Habit: Make it obvious. Make it attractive. Make it easy. Make it satisfying. How to Break a Bad Habit: Make it invisible. Make it unattractive. Make it difficult. Make it unsatisfying.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:02:52.779Z",
    "updatedAt": "2024-05-30T04:02:52.779Z"
  },
  {
    "id": 1744217000007,
    "title": "How to Implement a Habit",
    "page": "71",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Planning"
    ],
    "description": "I will [BEHAVIOUR] at [TIME] in [LOCATION]",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:03:10.088Z",
    "updatedAt": "2025-03-05T16:53:42.748Z"
  },
  {
    "id": 1744217000008,
    "title": "One space one use",
    "page": "89",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Distraction",
      "Working"
    ],
    "description": "Whenever possible, avoid mixing the context of one habit with another. When you start mixing contexts, you'll start mixing habits-- and the easier ones will usually win out. ",
    "comments": "Bedroom/Classroom have different purposes. You can't study in your bedroom as well as the classroom.",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:06:09.466Z",
    "updatedAt": "2024-05-30T04:06:09.466Z"
  },
  {
    "id": 1744217000009,
    "title": "Chess players hard work",
    "page": "113",
    "book": "Atomic Habits",
    "tags": [
      "Time",
      "Dedication",
      "Hard Work",
      "Talent"
    ],
    "description": "he completely rejected the idea of innate talent. He claimed that with deliberate practice and the development of good habits, a child could become a genius in any field. His mantra was \"A genius is not born, but is educated and trained.\" Laszlo believed tin this idea so strongly that he wanted to test it with his own children-- Laszlo decided chess would be a suitable field for the experiment, and he laid out a plan to raise his children to become chess prodigies. The kids would be home-schooled, a rarity in Hungary at the time. The house would be filled with chess books and pictures of famous chess players. The children would play against each other constantly and compete in the best tournaments they could find. Their lives would be dedicated to chess. Susan, the oldest began playing chess when she was four years old. Within six months, she was defeating adults. Sofia. the middle child, did even better. By fourteen she was a world champion, and a few years later, she became a grandmaster. Judit, the youngest, was the best of all. By age five, she could beat her father. At twelve, she was the youngest player ever listed among the top one hundred chess players in the world. At fifteen years and four months old, she became the youngest grandmaster of all time ... For twenty-seven years, she was the number-one-ranked female chess players in the world.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:07:53.341Z",
    "updatedAt": "2024-06-21T03:52:15.713Z"
  },
  {
    "id": 1744217000010,
    "title": "Imitating the Close",
    "page": "117",
    "book": "Atomic Habits",
    "tags": [
      "Socializing",
      "Behaviour"
    ],
    "description": "a person's chances of becoming obese increased by 57 percent if he of she had a friend who became obese.... If you are surrounded by fit people, you're more likely to consider working out to be a common habit. Surround yourself with people who have the habits you want to have yourself. Join a culture where (1) your desired behavior is the normal behavior and (2) you already have something in common with the group.",
    "comments": "You need a group of friends to keep you in check. Don't make friends with people who would bring you down. You are your five closest friends",
    "helpfulness": 5,
    "createdAt": "2024-05-30T04:09:32.609Z",
    "updatedAt": "2025-04-10T16:22:03.126Z"
  },
  {
    "id": 1744217000011,
    "title": "Habits are a matter of predicting",
    "page": "129",
    "book": "Atomic Habits",
    "tags": [
      "Habits"
    ],
    "description": "The cause of your habits is actually the prediction that precedes them. These predictions lead to feelings, which is how we typically describe a craving--a feeling, a desire, an urge. Feelings and emotions transform the cues we perceive and the predictions we make into a signal that we can apply.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:10:26.459Z",
    "updatedAt": "2024-05-30T04:10:26.459Z"
  },
  {
    "id": 1744217000012,
    "title": "Get the Reps In",
    "page": "143",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Routine"
    ],
    "description": "Habit formation is the process by which a behavior becomes progressively more automatic through repetition. The more you repeat an activity, the more the structure of your brain changes to become efficient at that activity. Neuroscientist call this long-term potentiation, which refers to the strengthening of connections between neurons in the brain based on recent patterns of activity. With each repetition, cell-to-cell signaling improves and the neural connections tighten. Repeating a habit leads to clear physical changes in the brain. In musicians, the cerebellum is larger than non-musicians...",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:11:37.336Z",
    "updatedAt": "2024-06-21T03:47:58.414Z"
  },
  {
    "id": 1744217000013,
    "title": "Repetition is a form of change (literally)",
    "page": "144",
    "book": "Atomic Habits",
    "tags": [
      "Repetition",
      "Learning"
    ],
    "description": "each time you repeat an action, you are activating a particular neural circuit associated with that habit. This means that simply putting in your reps is one of the most critical steps you can take to encoding a new habit. It is why the students who took tons of photos improved their skills while those who merely theorized about perfect photos did not. One group engaged in active practice, the other in passive learning. One in action, the other in motion.",
    "comments": "Quantity can sometimes beat Quality. In this case, the camera students learned by doing. Not by trying to find the 'perfect angle'. They don't even know what that is yet.",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:14:16.744Z",
    "updatedAt": "2024-05-30T04:14:16.744Z"
  },
  {
    "id": 1744217000014,
    "title": "Start your day off right",
    "page": "161",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Decision Making"
    ],
    "description": "good/bad decision tree",
    "comments": "Never punish the future. If you want to have a good day, it's best that you start well. It's hard to crawl out of a hole of bad decisions",
    "helpfulness": 1,
    "createdAt": "2024-05-30T04:16:15.384Z",
    "updatedAt": "2024-05-30T04:16:15.384Z"
  },
  {
    "id": 1744217000015,
    "title": "The Two-Minute Rule",
    "page": "162",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Working"
    ],
    "description": "[Bullets] \"Read before bed each night\" becomes \"Read one page.\" \"Do thirty minutes of yoga\" becomes \"Take out my yoga mat.\" \"Study for class\" becomes \"Open my notes.\"",
    "comments": "Getting out of bed or off the couch is more impactful that you might initially think",
    "helpfulness": 1,
    "createdAt": "2024-06-01T03:53:52.281Z",
    "updatedAt": "2024-06-01T03:53:52.281Z"
  },
  {
    "id": 1744217000016,
    "title": "Least Resistance, More Energy",
    "page": "164",
    "book": "Atomic Habits",
    "tags": [
      "Working",
      "Routine"
    ],
    "description": "By following the same creative ritual, you make it easier to get into the hard work of creating. By developing a consistent power-down habit, you make it easier to get to bed at a reasonable time each night. You may not be able to automate the whole process, but you can make the first action mindless. Make it easy to start and the rest will follow.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-01T03:55:20.903Z",
    "updatedAt": "2024-06-01T03:55:20.903Z"
  },
  {
    "id": 1744217000017,
    "title": "Commitment Devices (Ulysses)",
    "page": "170",
    "book": "Atomic Habits",
    "tags": [
      "Planning",
      "Habits",
      "Distraction"
    ],
    "description": "A commitment device is a choice you make in the present that controls your actions in the future. It is a way to lock in future behavior, bind you to good habits, and restrict you from bad ones. When Victor Hugo shut his clothes away so he could focus on writing, he was creating a commitment device.",
    "comments": "Ulysses had his men tie himself to the mast so he couldn't act on the siren's songs while sailing",
    "helpfulness": 1,
    "createdAt": "2024-06-01T03:58:28.334Z",
    "updatedAt": "2024-06-01T03:58:28.334Z"
  },
  {
    "id": 1744217000018,
    "title": "How to Turn Gratification into an Advantage",
    "page": "191",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Change",
      "Goal Setting"
    ],
    "description": "In a perfect world, the reward for a good habit is the habit itself. In the real world, good habits tend to feel worthwhile only after they have provided you with something. Early on, it's all sacrifice... It's only a months later that it becomes easier to exercises for its own sake. In the beginning, you need a reason to stay on track. This is why immediate rewards are essential. They keep you excited while the delayed rewards accumulate in the background. Immediate reinforcement can be especially helpful when dealing with habits of avoidance, which are behaviors you want to stop doing. It can be challenging to stick with habits like \"no frivolous purchases\" or \"no alcohol this month\" because nothing happens when you skip happy hour drinks or don't buy that pair of shoes. It can be hard to feel satisfied when there is no action in the first place. All you're doing is resisting temptation, and there isn't much satisfying about that. Open a savings account and label it for something you want--maybe \"Leather Jacket.\" Whenever you pass on a purchase, put the same amount of money in the account. Skip your morning latte? Transfer $5. It's like creating a loyalty program for yourself. The immediate reward of seeing yourself save money toward the leather jacket feels a lot better than being deprived. You are making it satisfying to do nothing.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:01:17.353Z",
    "updatedAt": "2024-06-01T04:01:17.353Z"
  },
  {
    "id": 1744217000019,
    "title": "Conflicting Identities",
    "page": "192",
    "book": "Atomic Habits",
    "tags": [
      "Identity"
    ],
    "description": "Don't make your reward for exercising eating a bowl of ice cream.",
    "comments": "Don't reward yourself with video games if you're trying to stay away from them. Don't reward banned behaviours.",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:03:03.204Z",
    "updatedAt": "2024-06-01T04:03:03.204Z"
  },
  {
    "id": 1744217000020,
    "title": "Never Miss Twice in a Row -> Rebound",
    "page": "201",
    "book": "Atomic Habits",
    "tags": [
      "Habits"
    ],
    "description": "HOW TO RECOVER QUICKLY WHEN YOUR HABIT BREAKS DOWN: as soon as one streak ends, I get started on the next one. Missing once is an accident. Missing twice is the start of a new habit.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:04:01.606Z",
    "updatedAt": "2024-06-01T04:04:01.606Z"
  },
  {
    "id": 1744217000021,
    "title": "Winning & Losing / Explore & Exploit",
    "page": "223",
    "book": "Atomic Habits",
    "tags": [
      "Change"
    ],
    "description": "If you are currently winning, you exploit. If you are currently losing, you explore.",
    "comments": "Kind of applies to music hunting, and developing new drawing techniques. It applies to anything that gets stale. You need to explore.",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:06:56.768Z",
    "updatedAt": "2024-06-01T04:06:56.768Z"
  },
  {
    "id": 1744217000022,
    "title": "Consistency - Professional / Amateur",
    "page": "236",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Perseverance",
      "Purpose"
    ],
    "description": "I can guarantee that if you manage to start a habit and keep sticking to it, there will be days when you feel like quitting. But stepping up when it's annoying or painful or draining to do so, that's what makes the difference between a professional and an amateur. Professionals stick to the schedule; amateurs let life get in the way. Professionals know what is important to them and work toward it with purpose; amateurs get pulled off course by the urgencies of life. Avoid being a \"fair weather meditator\" Professionals take action even when the mood isn't right. They might not enjoy it, but they find a way to put the reps in.",
    "comments": "\"I had a bad sleep\" isn't a good excuse most of the time. Today, I got single digit REM and deep sleep, and still continued the marble streak",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:09:44.836Z",
    "updatedAt": "2024-06-01T04:09:44.836Z"
  },
  {
    "id": 1744217000023,
    "title": "Which Rule to Use / Grain of Sand",
    "page": "252",
    "book": "Atomic Habits",
    "tags": [
      "Habits",
      "Repetition",
      "Time"
    ],
    "description": "one positive change like meditating for one minute or reading one page each day is unlikely to deliver a noticeable difference. Gradually, though, as inégal you continue to layer small changes on top of one another, the scales of life start to move. Each improvement is like adding a grain of sand to the positive side of the scale, slowly titling things in your favor.... Sometimes a habit will be hard to remember and you'll need to make it obvious. Other times you won't feel like starting and you'll need to make it attractive. In many cases, you may find that a habit will be too difficult and you'll need to make it easy. And sometimes, you won't feel like sticking with it and you'll need to make it satisfying.",
    "comments": "Brick by brick. Step by step. Tilt the scale slowly, but maintain it.",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:11:37.424Z",
    "updatedAt": "2024-06-01T04:11:37.424Z"
  },
  {
    "id": 1744217000024,
    "title": "Little Lessons",
    "page": "259",
    "book": "Atomic Habits",
    "tags": [
      "Happiness",
      "Desire"
    ],
    "description": "Happiness is simply the absence of desire",
    "comments": "The more you want (desire), the less happy you'll be. ",
    "helpfulness": 1,
    "createdAt": "2024-06-01T04:12:42.968Z",
    "updatedAt": "2024-06-01T04:12:42.968Z"
  },
  {
    "id": 1744217000025,
    "title": "Meditation - Discomfort Summary",
    "page": "22",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Discomfort",
      "Growth"
    ],
    "description": "There's a significant downside if kids don't learn to get comfortable with discomfort, and it goes far beyond a reduced capacity for growth and innovation. People who can't tolerate discomfort can wind up with much more serious problems.",
    "comments": "Talk to new people. It helps you grow.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:18:48.367Z",
    "updatedAt": "2024-06-03T17:18:48.367Z"
  },
  {
    "id": 1744217000026,
    "title": "Lessen Power of Discomfort - Positive Change",
    "page": "29",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Discomfort",
      "Endurance",
      "Change"
    ],
    "description": "we mustn't resist our craving but actually turn toward them and focus on the discomfort we're experiencing. Mindfulness helps break down the craving into transient bodily sensations. \"I'm going to go crazy if I can't have a cigarette\" becomes \"I notice a feeling of tightness, tension, restlessness.\" If we focus on the \"bite-sized pieces of experiences,\" Brewer explains, it's possible to manage moment to moment and \"surf\" a craving so we're not \"clobbered by this huge, scary\" wave. We don't have to rely on cognition to stop ourselves from reaching for a smoke because that wave gets weaker and weaker the harder we stare at it, until it loses the power to drag us under. And every time we don't get dragged under, that trigger loses its potency. We rewire our brain's response to the thing we crave. The take away is that attending to and learning to tolerate discomfort lessens its power and increases the likelihood of positive change. ",
    "comments": "You don't need to rub one out. Endure it, and surf it. If you succeed, it changes your brain and makes it easier next time.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:21:45.833Z",
    "updatedAt": "2024-06-03T17:21:45.833Z"
  },
  {
    "id": 1744217000027,
    "title": "Reframing Discomfort",
    "page": "56",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Pain"
    ],
    "description": "athletes don't get a free pass on pain. Like Ray Zahab, they just find ways to reframe how they think about it--by expecting it to happen, training their brains to view it as a positive thing when it does, and relying on their brains to pretend it's not really there. And the meaning we assign to pain matters.",
    "comments": "Instead of thinking: \"this is unbearable\", think \"I love pain\". \"Pain is good for my growth\"",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:24:21.173Z",
    "updatedAt": "2024-06-03T17:24:21.173Z"
  },
  {
    "id": 1744217000028,
    "title": "Gratitude / Happines",
    "page": "75",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Gratitude",
      "Happiness",
      "Forgiveness"
    ],
    "description": "Gratitude and forgiveness are, in other words, the twin pillars of happiness. They are also misery's one-two punch. ... choosing to focus on the reasons you have to be grateful instead of the reasons you don't not only improves your happiness quotient but also brings out the best in those around you.",
    "comments": "Focus on the bright side. It makes you happier. Not on crime statistics or housing prices",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:25:56.030Z",
    "updatedAt": "2024-06-03T17:25:56.030Z"
  },
  {
    "id": 1744217000029,
    "title": "Rumination is a Waste",
    "page": "102",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Depression",
      "Rumination"
    ],
    "description": "the 1989 San Francisco earthquake found that those who ruminated experienced more symptoms of depression and post-traumatic stress disorder. Similarly, a study of 455 people whose family members had died after terminal illnesses showed that those who ruminated were more likely to become depressed, and eighteen months later, most were still depressed. ... the mere act of rumination makes them feel worse, according to a plethora of studies. When people are given an emotionally neutral statement, such as \"Think about the level of motivation you feel right now,\" or \"Think about the long-term goals you have set,\" then are asked to focus on their feeling about it for eight minutes, those who are prone to ruminate feel worse at the end of the exercise, while people who don't ruminate feel the same way they did when they began, By contrast, when researchers instruct people to spend some time thinking about the blades of a fan or the layout of their local mall, ruminators feel better afterward--they've been distracted--while non-ruminators feel just the same. But ruminating is in fact a way of spinning your wheels and wasting time. The more you spin, the more stuck you get--and the deeper your rut becomes. Dwelling on a problem seems to impair our ability to solve it in some fundamental way, researchers believe. And according to the late Susan Nolen-Hoeksema, a Yale University expert on the topic, \"Even when a person prone to rumination comes up with a potential solution to a significant problem, the rumination itself may induce a level of uncertainty and immobilization that makes it hard for them to move forward.\" Deliberately replacing unpleasant, ruminative thoughts with ones that don't cause stress is the foundation of cognitive behaviour therapy, which is one of the most effective treatments for helping people change persistently negative thought patterns. More proof that mind over matter works. Ignoring naysayers is the kind of common sense our parents urged on us, though it's difficult to do. Criticism stings; being disliked doesn't feel good. But Linda Hasenfratz found that by treating the criticism as constructive and ignoring anything that was personal, she was able to turn it into a strength. And ultimately she proved to those naysayers that she was right for the job. By leaning away from discomfort, she decreased her own experience of it so she could focus on what was really important to her: changing to become the kind of leader the company needed--the kind who could successfully steer it to growth and expansion.",
    "comments": "The more you ruminate, the more depressed you become. Rumination inhibits affects your ability to act.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:29:40.244Z",
    "updatedAt": "2024-06-03T17:29:40.244Z"
  },
  {
    "id": 1744217000030,
    "title": "Don't Lash Out / Be Victim",
    "page": "153",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Change",
      "Identity"
    ],
    "description": "Four years later, he confessed in a LinkedIn blog post that when he left the profession that had been his life's focus, his world \"suddenly and profoundly\" changed, and his first inclination was to feel sorry for himself. \"I've never been more tempted to feel like a victim\" he wrote. After a lifetime of success, public humiliation must have been a searing trial. The desire to rant to pundits or write a tell all, McChrystal admitted, was overpowering. But with his wife's support, he made a deliberate decision not to define himself through his departure, or let others do so either. When discomfort is acute, it can trigger a fight-or-flight instinct, but for McChrystal--and Jessica Watkin--it never felt right to hide under the covers or unleash his anger at the world (or himself). That didn't provide a way forward. Instead, discomfort became a prompt to look inward and ask some very mindful questions: Who am I, now that the place I once occupied in the world is closed to me forever? And who would I like to be? When change occasions a loss of identity, whether that identity is \"greatest fighting force in the world\" or respected four-star general,\" reinvention is the path that provides the greatest sense of control, as Jessica Watkin found.",
    "comments": "Don't lash out.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:33:12.771Z",
    "updatedAt": "2024-06-03T17:33:12.771Z"
  },
  {
    "id": 1744217000031,
    "title": "Don't Lose Sight of Goals",
    "page": "177",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Nervosity",
      "Determination"
    ],
    "description": "Heil has learned to think about mental fitness in the same way she thinks about physical fitness. In a video for her speaker's bureau, she explains that she trained on a weekly basis with a sports psychologist. She'd visualize herself in challenging scenarios--on a ski hill. in ffont of a camera, writing a final exam--then try to create the nervous feelings she usually got in those circumstances. \"I'd see myself overcoming them and shifting into how I wanted to act. How I wanted to feel calm. How I wanted to feel positive and how I believed in myself.\" Nerves, she says, are a \"completely normal\" part of competition, both on the ski slopes and in the boardroom. No matter how bad the pain or anxiety gets, you must never lose sight of the season you're putting yourself through all the hardship in the first place. The most important thing is to be \"playful, to have that joy\" (a word she uses a lot), and \"to be willing to explore new things.\" As long as you can hang on to that, \"you'll be able to overcome really difficult challenges.\"",
    "comments": "To help with nerves, you can visualize yourself in nervous situations, and visualize yourself as calm during them. In your pursuit of goals, don't let your nerves take over. Never lose sight of your goals and what you're willing to do to achieve them.",
    "helpfulness": 9,
    "createdAt": "2024-06-03T17:38:10.631Z",
    "updatedAt": "2025-04-10T16:13:58.595Z"
  },
  {
    "id": 1744217000032,
    "title": "Anxiety Worsens Things. Control It.",
    "page": "188",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Anxiety",
      "Control"
    ],
    "description": "Few people can tune out the discomfort of anxiety. \"As soon as we get anxious or fear failure, we have no chance of getting into the expert state. It's just the wrong direction,\" Berka says. But her hunch was that if the high-strung novices could short-circuit their anxiety, they would learn faster. So they were given a little device to wear on their collars that buzzed in concert with their heart rate--until their brains approached the \"expert state,\" at which point the buzzing stopped. Just slowing their breathing--and being rewarded by reduced buzzing--moved the anxious novices closer to an expert state: their brains showed an increase of alpha frequency. In just one day, 85 percent of the participants were able to achieve a measure of control over their heart rate and move their brain activity closer to the expert state. In so doing, their accuracy at target practice also shot up significantly. \"We were happily surprised by that,\" Berka says. \"We thought we could help people control their brains, but that it could happen in one day was surprising. The neuro-feedback training enhanced their ability to get the perfect shot.\" The next day. the novices moved from a bow and arrow to a laser-shot rifle. Now that they knew what the expert state felt like, most of them could return to it without the help of the buzzer. \"Though we aren't normally conscious of our heart rate or the state of our brains, we can easily be made conscious of them,\" explains Berka. \"Once there is an association--taking a perfect shot and feeling that state--you have established, we think, a new neural pathway.\" While hitting the bull's-eye also provides positive reinforcement, Berka says the good feeling of being in the expert state is really all the inducement most people need. Once that connection was made, participants came up with their own cues to get back to that feeling; they found their own \"trigger switch\" to return to that state of mind. The experts had described a similar kind of switch, saying they could simply flip it on, take the shot, and then flip it off again. Did the novices become expert marksmen? No. But they did learn much faster--more than twice as fast, in fact--than they would have otherwise. Berka's hunch turned out to be right: if you can quiet your anxiety and learn to mirror the state of an expert's brain, you can progress much faster. And apparently, the neuro-feedback had lasting effects. A month later, 50 percent of the novices had fully retained their ability to induce the expert brain state. Several things struck me about this research. First it's revealing that anxiety really is the enemy of progress and basically shuts the gate on learning. The problem isn't discomfort with challenge and change, but how we respond to and manage--or don't manage--it. If the response is to freak out, discomfort becomes a real obstacle to growth and development; if the response is to calm ourselves--via mindfulness, meditation, tuning down the dial, or focusing on optimism--we have a better shot of figuring out how to get past an obstacle or master a challenge.",
    "comments": "Learn to control your anxiety by realizing that it is an obstacle to everything and is not productive. Lower your heart rate so you can enter the expert state. A state that allows your brain to function at its peak.",
    "helpfulness": 8.2,
    "createdAt": "2024-06-03T17:42:20.030Z",
    "updatedAt": "2025-04-10T16:24:51.865Z"
  },
  {
    "id": 1744217000033,
    "title": "Openness to Experience",
    "page": "201",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Creativity",
      "Exploration"
    ],
    "description": "Cognitive psychologist Scott Barry Kaufman, co-author of Wired to Create, a 2015 book examining the current research on creativity, has said that the most consistent predictor of creative achievement is \"openness to experience\"--a mélange of intellectual curiosity, thrill seeking, openness to your emotions, and fantasy. The thing that brings them all together, however, is the drive to explore your inner and outer worlds cognitively and behaviourally: more than anything else, creative people love discovering new knowledge.",
    "comments": "In order to be creative, you need to by high in openness to experience. You need to remain curious, and always be open to learning new things. Actively seek novelty. Go do something you haven't done before",
    "helpfulness": 5,
    "createdAt": "2024-06-03T17:44:41.113Z",
    "updatedAt": "2025-04-10T16:34:07.277Z"
  },
  {
    "id": 1744217000034,
    "title": "Failure Won't Kill You",
    "page": "203",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Failure"
    ],
    "description": "A lot of ideas that seem amazing at first come to nothing. \"Failing won't kill you,\" says Debow. \"The worst that can happen is you'll learn something.\" ",
    "comments": "Remember that failing can be progress. Failing is not fruitless. It is a teacher, and provides you knowledge you didn't have before.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:46:40.896Z",
    "updatedAt": "2024-06-17T21:19:13.422Z"
  },
  {
    "id": 1744217000035,
    "title": "As Soon As You Get Comfortable",
    "page": "212",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Repetition",
      "Discipline",
      "Improvement",
      "Complacency"
    ],
    "description": "As he told the kids he trained,[:] self-discipline and repetition are essential to improvement. As soon as you let yourself get comfortable, you stop getting better.",
    "comments": "If being comfortable stops you from improving, that means you improve when you endure discomfort. When drawing, it's not comfortable practicing new techniques, but I can't draw the same way forever, or else I won't improve. So, discipline yourself to take on discomfort. With enough repetition, you'll see improvement in whatever you do.",
    "helpfulness": 7,
    "createdAt": "2024-06-03T17:50:49.946Z",
    "updatedAt": "2025-04-10T16:26:00.908Z"
  },
  {
    "id": 1744217000036,
    "title": "Change Must Be Maintained",
    "page": "230",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Change",
      "Repetition"
    ],
    "description": "Change hasn't been accomplished, researchers say, until you prove that you can maintain it. The maintenance stage is all about avoiding relapse and consolidating the benefits that started to accrue during the action stage. While maintenance was initially viewed as a static stage--a graduation certificate, of sorts--researchers now see it as a period of continuous change (one that may never really end if your change involved kicking an addiction).... Maintenance was about owning his new identity as a shooting coach and removing the safety net provided by his day job.",
    "comments": "You need to maintain positive habits in order to claim them as habits. As long as you can avoid a \"relapse\" into the previous state before the new changes, you have changed. Until then, you haven't.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:53:50.485Z",
    "updatedAt": "2024-06-03T18:03:40.138Z"
  },
  {
    "id": 1744217000037,
    "title": "Princess & Frog Analogy",
    "page": "254",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Change"
    ],
    "description": "Pokroy likes to use as an analogy the children's story about the princess and the frog prince who retrieves her golden ball for her. Most of us will remember the story from childhood, but Pokroy attaches a whole new meaning to it. The princess in the story represents us, he explains, and her beloved golden ball is the status quo, or our comfort zone. When she loses the ball down a deep well, a frog offers to get it back for her, but only if he can live with her in the castle forever after. The frog represents change, Pokroy says, and like the princess in the story, we find change repellent. So desperate is she to get her ball back, however, that the princess grudgingly accepts the change. Really grudgingly! For some time, she is disgusted by the frog even as she fulfils her promise to him. But gradually she accepts him, and one day she embraces him and kisses him affectionately. Out pops a handsome prince. The analogy is obvious--when we overcome our discomfort with (or even aversion to) change, the reward will follow.... We don't change our behaviour by focusing on the behaviour alone. It requires a shift in attitude or mindset. And that forces us to really think about our actions (make them conscious, (which in turn will help us understand them better, or give us insight into them. Only then can we change the way se see them.... But making the unconscious conscious isn't easy. Because we are fearful of uncertainty--our brains dislike ambiguity intensely--we cling to the status quo, or our golden ball. The secret is to be aware of that weakness, observe where it affects us, and then stop.... But change, like the handsome prince in the children's story, is a powerful reward. And as we learn that letting go of our comfort, and first tolerating and then embracing the discomfort, will bring us great rewards, it becomes easier to do.",
    "comments": "The princess asked the frog for a favor. And the frog got to stay in the castle in return. The princess hated the frog (change). Eventually, she kisses the frog affectionately, and the frog becomes a prince. The lesson here is that when you embrace change (that you may not like), there are rewards waiting for you when you whole-heartedly accept the change.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T17:59:03.034Z",
    "updatedAt": "2024-06-17T21:26:49.663Z"
  },
  {
    "id": 1744217000038,
    "title": "Discomfort Summary",
    "page": "256",
    "book": "The Beauty of Discomfort",
    "tags": [
      "Change",
      "Discomfort"
    ],
    "description": "And then our challenge is to stay right there, leaning against that new discomfort. The high-achieving changers among us will learn to identify some forms of comfort as a negative thing--and reject them outright. Turning away from the discomfort of change is tempting, or course, because you're turning away from risk and the possibility of embarrassment and failure. But you're also turning away from the opportunity to stretch yourself, test yourself, and grow. You're turning away from the possibility--the likelihood--that change will be for the better (and even if it isn't, you will almost certainly learn something worthwhile). Every time we back away from discomfort, change gets a little more frightening. ",
    "comments": "Discomfort is something to want, as it is the avenue for growth and bettering yourself. There is no growth in comfort as nothing requires you to develop anything new.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:03:10.626Z",
    "updatedAt": "2024-06-17T21:26:59.620Z"
  },
  {
    "id": 1744217000039,
    "title": "Pessimism Narrows Focus",
    "page": "12",
    "book": "Focus",
    "tags": [
      "Negativity"
    ],
    "description": "the classic power of positive thinking, because pessimism narrows our focus, whereas positive emotions widen our attention and our receptiveness to the new and unexpected. A simple way to shift into positive mode is to ask yourself, \"If everything worked out perfectly in my life, what would I be doing in 10 years\"",
    "comments": "When you think positively, you open your mind to more ideas. It increases your receptiveness to new things, and embracing them. Negative thinking confines you to Hitler's dream world, and nothing else.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:27:34.651Z",
    "updatedAt": "2024-06-23T21:14:20.754Z"
  },
  {
    "id": 1744217000040,
    "title": "Suspending Interaction to observe",
    "page": "22",
    "book": "Focus",
    "tags": [
      "Mindfulness",
      "Perception"
    ],
    "description": "\"Suspending your own involvement to observe what's going on gives you a mindful awareness of the interaction without being completely reactive,\" says Riess. \"You can see if your own physiology is changed up or balanced. You can notice what's transpiring in the situation.\" If a doctor realizes that [they're] irritated, for instance, that may be a signal that the patient is bothered too.",
    "comments": "If you take a step back to observe, you can allow yourself to act the way your conscious mind would intend to. You can analyzing your surroundings to realize your emotions and thoughts at this present moment and what it best moving forward.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:30:28.634Z",
    "updatedAt": "2024-06-03T18:30:28.634Z"
  },
  {
    "id": 1744217000041,
    "title": "Sustaining Outward Focus",
    "page": "32",
    "book": "Focus",
    "tags": [
      "Stress",
      "Reflection"
    ],
    "description": "What keeps us from making that effort? Sleep deprivation, drinking, stress, and mental overload all interfere with the executive circuitry used to make the cognitive switch. To sustain the outward focus that leads to innovation, we need some uninterrupted time in which to reflect and refresh our focus.",
    "comments": "To sustain outward focus, like working on projects, you need to carefully manage your life conditions. Keep stress low, sleep high, and reflect on how you are doing.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:32:44.200Z",
    "updatedAt": "2024-06-03T18:32:44.200Z"
  },
  {
    "id": 1744217000042,
    "title": "Ideas Emerging From Showers/Walks",
    "page": "34",
    "book": "Focus",
    "tags": [
      "Awareness",
      "Creativity"
    ],
    "description": "and open awareness, in which we allow our minds to associate freely and the solution to emerge spontaneously. (That's why so many fresh ideas come to people in the shower or out for a walk or a run.)",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:34:37.499Z",
    "updatedAt": "2024-06-03T18:34:37.499Z"
  },
  {
    "id": 1744217000043,
    "title": "Poverty of Attention",
    "page": "37",
    "book": "Focus",
    "tags": [
      "Attention"
    ],
    "description": "The link between attention and excellence remains hidden most of the time. Yet attention is the basis of the most essential of leadership skills--emotional, organizational, and strategic intelligence. And never has it been under greater assault. The constant onslaught of incoming data leads to sloppy shortcuts--...This was foreseen decades ago by the Nobel Prize-winning economist Herbert Simon. Information \"consumes the attention of its recipients,\" he wrote in 1971. \"Hence a wealth of information creates a poverty of attention.\"",
    "comments": "Too much information leads to not enough attention. If you find yourself lacking attention, then reduce the information coming in.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:50:58.286Z",
    "updatedAt": "2024-06-03T18:50:58.286Z"
  },
  {
    "id": 1744217000044,
    "title": "Unproductive Distraction Cycle",
    "page": "43",
    "book": "Focus",
    "tags": [
      "Distraction",
      "Focus",
      "Productivity"
    ],
    "description": "When we can't focus at work because of distractions, it may lead us to feel stressed about not being productive, which then causes us to focus less, further feeding the cycle. Unfortunately, most of us don't notice our focus declining until we become completely overwhelmed.",
    "comments": "Distractions start a negative spiral. You get worried that you're unproductive, and reduces your focus. To escape this, you can cut out distractions and recalibrate your focus again. Don't worry so much about productivity. Your focus will do that for you.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:54:13.756Z",
    "updatedAt": "2024-06-03T18:54:13.756Z"
  },
  {
    "id": 1744217000045,
    "title": "Write Down Why You Are Stressed",
    "page": "44",
    "book": "Focus",
    "tags": [
      "Stress",
      "Change",
      "Awareness",
      "Anxiety"
    ],
    "description": "Start by using your self-awareness to help you notice several things: Why you feel stressed or anxious. Before you can deal with stress, you need to know what's causing it. As simple as it may sound, it can be helpful to make a list of the sources of your stress. Write down each thing in your life and at work that's causing you anxiety. You might categorize items into things you have the ability to change and things you don't. For the stressors in the latter category, you will need to figure out how to change your attitude toward them.",
    "comments": "If you're getting to stressed, write down the reasons. You could categorize them into things you can or can't change. Adjust your attitudes towards each item accordingly.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:56:26.727Z",
    "updatedAt": "2024-06-17T21:27:29.592Z"
  },
  {
    "id": 1744217000046,
    "title": "When You Lose Your Ability To Focus",
    "page": "45",
    "book": "Focus",
    "tags": [
      "Focus",
      "Attention",
      "Distraction"
    ],
    "description": "When you lose your ability to focus. If, for example, you find yourself worrying yourself sick over something while you're driving 65 mph on the highway with a car full of kids, you're putting yourself and others in real danger. This can be a wake-up call to bring your attention back to what you're doing and make a decision to think about your concerns later.",
    "comments": "Don't think about things irrelevant to the present moment or you could lose your focus. In situations like listening to your date, or working away, or driving (in the description), you could easily lose your focus by distracting yourself. Bring your attention back to the present moment.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T18:59:46.489Z",
    "updatedAt": "2024-06-03T18:59:46.489Z"
  },
  {
    "id": 1744217000047,
    "title": "Get Enough Sleep. Its Worth It.",
    "page": "47",
    "book": "Focus",
    "tags": [
      "Sleep"
    ],
    "description": "Lack of sleep can negatively affect our decisions because it impairs our ability to accurately assess a situation, plan accordingly, and behave appropriately. Committing to the recommended seven to eight hours of sleep each night may seem impossible when you're stressed and overworked, but the payoff is worth it.",
    "comments": "",
    "helpfulness": 6,
    "createdAt": "2024-06-03T19:00:22.247Z",
    "updatedAt": "2025-04-10T16:16:36.011Z"
  },
  {
    "id": 1744217000048,
    "title": "4 Stages of Losing Focus",
    "page": "58",
    "book": "Focus",
    "tags": [
      "Focus",
      "Distraction"
    ],
    "description": "1. First, you choose a focus. It might be anything, from any sphere of life. At work, it's supposed to be some aspect of work-let's say, whom to include in an important meeting. 2. Sooner or later, your attention wanders. This isn't what you plan to do. It just happens. (If it were a plan, it would be another focus not a wandering.) 3. Sooner or later, you wake up to the fact that your mind has wandered. You notice the distraction. You realize how far you are from the thing you first wanted to focus on. Again, you can't exactly plan or choose this. 4. Having woken up, you may choose to return to the original theme. For example, whom to invite to that meeting. Then again, you may choose to give up and do something else. It's up to you; it's a choice.",
    "comments": "Focus is often a simple choice. Once you realize that you've distracted yourself, you can choose to be distracted, or you can go back to your focused state.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:02:23.055Z",
    "updatedAt": "2024-06-03T19:02:23.055Z"
  },
  {
    "id": 1744217000049,
    "title": "Don'ts of Focusing",
    "page": "74",
    "book": "Focus",
    "tags": [
      "Focus",
      "Distraction"
    ],
    "description": "Don't: Fool yourself into thinking distractions aren't harmful to your focus-they have high cognitive costs. Spend time with people who are distracted. You're likely to end up feeling the same way. Neglect self-care. Instead, take breaks, eat healthily, and get enough sleep.",
    "comments": "Distractions are harmful to your focus",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:03:52.694Z",
    "updatedAt": "2024-06-03T19:03:52.694Z"
  },
  {
    "id": 1744217000050,
    "title": "Blocking Out Distractions",
    "page": "76",
    "book": "Focus",
    "tags": [
      "Distraction",
      "Planning"
    ],
    "description": "She had previously learned to set boundaries for herself around social media by scheduling in time for distractions. \"I gave myself pockets of time when I could go on Facebook. It might be a 10-minute break between meeting or while I was waiting for the elevator to go to lunch. Once I baked those breaks in, I found it a lot easier to control the impulse to check social media while I was working,\" she explains. She did something similar to address the work interruptions: she allowed herself time to read and respond to messages, but only after getting her most important work completed. \"At the beginning of each week, I ask myself, 'What are the most critical things I have to complete?' And each day, I ask, 'Today, what is the one thing I absolutely have to do?'\" She says that helped her determine how much time she needed to focus, and then she would block that time out in two-hour chunks.",
    "comments": "You can plan out your distractions by allotting them specific times during the day. Confine your distraction use to a time, and that will leave you to work freely outside of that time. Like Instagram, or breaks. Set focus time goals to hit for each day. Stopwatch them. Prioritize your most important work and do that first.",
    "helpfulness": 5.4,
    "createdAt": "2024-06-03T19:07:30.858Z",
    "updatedAt": "2025-04-10T16:28:19.246Z"
  },
  {
    "id": 1744217000051,
    "title": "Prevention & Promotion Focus",
    "page": "87",
    "book": "Focus",
    "tags": [
      "Motivation"
    ],
    "description": "There are two ways to look at any task. You can do something because you see it as a way to end up better off than you are now-as an achievement or accomplishment. As in. \"If I complete this project successfully I will impress my boss,\" or \"If I work out regularly, I will look amazing.\" Psychologists call this a promotion focus, and research shows that when you are motivated by the thought of making gains, and you work best when you feel eager and optimistic. Sounds good, doesn't it? Well, if you are afraid you will screw up on the task in question, this is not the focus type for you. Anxiety and doubt undermine promotion motivation, leaving you less likely to take any action at all. What you need is a way of looking at what you need to do that isn't undermined by doubt but rather, ideally, thrives on it. When you have a prevention focus, instead of thinking about how you can end up better off, you see the task as a way to hang on to what you already have-to avoid loss. For the prevention focused, successfully completing a project is a way to keep your boss from being angry or thinking less of you. Working out regularly is a way to not \"let yourself go.\" Decades of research, which I describe in my book Focus, shows that prevention motivations is actually enhanced by anxiety about what might go wrong. When you are focused on avoiding loss, it becomes clear that the only way to get out of danger is to take immediate action. The more worried you are, the faster you are out of the gate.",
    "comments": "The passage doesn't say whether one is better, so I'm assuming they're equal. You can look at tasks like working out as \"Let's go get big\", or \"Don't let yourself recede\". Anxiety runs deep into your veins, so scaring yourself might be very effective. Think: \"I'll be a loser if I don't get this done\" (prevention focus). Although it seems like negative thinking, it could very well work just as well or better than \"I'll be a good man\" or \"My girlfriend would appreciate this\" ",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:09:22.621Z",
    "updatedAt": "2024-06-03T19:13:28.992Z"
  },
  {
    "id": 1744217000052,
    "title": "If - Then Planning",
    "page": "92",
    "book": "Focus",
    "tags": [
      "Planning"
    ],
    "description": "Instead, use if-then planning to get the job done. Making an if-then plan is more than just deciding what specific steps you need to take to complete a project: It's also deciding where and when you will take those steps. For example: If it is 2p.m., then I will stop what I'm doing and start work to the report Bob asked for. If my boss doesn't mention my request for a raise at our meeting, then I will bring it up again before the meeting ends. By deciding in advance exactly what you're going to do--and when and where you're going to do it-there's not deliberating when the time comes. There's no Do I really have to do this now? Or Can this wait till later? Or Maybe I should do something else instead. It's when we deliberate that willpower becomes necessary to make the tough choice. If-then plans dramatically reduce the demands placed on your willpower by ensuring that you've made the right decision way ahead of the critical moment. In fact, if-then planning has been shown in more that 200 studies to increase rates of goal attainment and productivity by 200% to 300% on average.",
    "comments": "You can make decisions before they happen with if-then planning. If it's 9 am, I will get out of bed. 30 minutes from now (using fitbit), I will resume work.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:16:22.625Z",
    "updatedAt": "2024-06-03T19:16:22.625Z"
  },
  {
    "id": 1744217000053,
    "title": "Exercises / Mind & Body",
    "page": "100",
    "book": "Focus",
    "tags": [
      "Frustration",
      "Mindfulness"
    ],
    "description": "Perhaps you're determined to complete something before lunch. But if frustration is building, stepping away, taking a walk, and getting something to eat may be exactly what need to facilitate smooth and rapid completion of the task after lunch. Leveraging the connection between mind and body is key to knowing when to make a change.",
    "comments": "Your mind might need a refresher if it's too frustrated. Going for a walk can clear the mind. Getting something to eat can refresh willpower.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:17:59.289Z",
    "updatedAt": "2024-06-03T19:17:59.289Z"
  },
  {
    "id": 1744217000054,
    "title": "Labelling Situations",
    "page": "112",
    "book": "Focus",
    "tags": [
      "Awareness",
      "Focus"
    ],
    "description": "observe your thinking and emotional state, and assign a word to what's happening, such as \"pressure,\" \"guilt,\" or \"worry.\" By using just one or two words, Rock's research shows, you can reduce the arousal of the limbic brain's fight-or-flight system and instead activate the prefrontal cortex, which is responsible for our executive functioning skills.",
    "comments": "Being aware of your emotional state can help you calm yourself down and increase your focus to 100%",
    "helpfulness": 5,
    "createdAt": "2024-06-03T19:21:11.089Z",
    "updatedAt": "2025-04-10T16:32:51.950Z"
  },
  {
    "id": 1744217000055,
    "title": "Stress Begins the Moment Awake",
    "page": "134",
    "book": "Focus",
    "tags": [
      "Stress"
    ],
    "description": "First, start your day off right. Researchers have found that we release the most stress hormones within minutes after waking. Why? Because thinking of the day ahead triggers our fight-or-flight instinct and releases cortisol into our blood. Instead, try this: When you wake up, spend two minutes in your bed simply noticing your breath, As thoughts about the day pop into your mind, let them go and return to your breath.",
    "comments": "Make sure the first few minutes of your day are peaceful, as that is when the most stress is. Don't bombard yourself with Instagram or negative media to amplify your stress levels. Having a screen-free morning will calm you down compared to watching reels in bed. Don't succumb to the stress",
    "helpfulness": 5,
    "createdAt": "2024-06-03T19:24:36.446Z",
    "updatedAt": "2025-04-10T16:18:43.349Z"
  },
  {
    "id": 1744217000056,
    "title": "10 Minutes of Mindfulness",
    "page": "135",
    "book": "Focus",
    "tags": [
      "Mindfulness"
    ],
    "description": "take 10 minutes at your desk or in your car to boost your brain with the following short mindfulness practice before you dive into activity.",
    "comments": "You can give yourself a mindfulness break before an intensive activity to prepare yourself properly",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:25:57.047Z",
    "updatedAt": "2024-06-03T19:25:57.047Z"
  },
  {
    "id": 1744217000057,
    "title": "10 Minutes of De-stress Afterwards",
    "page": "138",
    "book": "Focus",
    "tags": [
      "Mindfulness",
      "Stress"
    ],
    "description": "Finally, as the day comes to an end and you start your commute home, apply mindfulness. For at least 10 minutes of the commute, turn off your phone, shut off the radio, and simply be. Let go of any thoughts that arise. Attend to your breath. Doing so will allow you to let go of the stresses of the day so you can return home and be fully present with your family.",
    "comments": "If you feel stressed after work, a calmness period immediately after working can alleviate that.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:27:22.885Z",
    "updatedAt": "2024-06-03T19:27:22.885Z"
  },
  {
    "id": 1744217000058,
    "title": "Positive Constructive Daydreaming",
    "page": "145",
    "book": "Focus",
    "tags": [
      "Visualization"
    ],
    "description": "Positive constructive daydreaming is a type of mind wandering that is different from slipping into a daydream or guiltily rehashing worries. When you build PCD into your day deliberately, it can boost your creativity, strengthen your leadership ability, and also reenergize the brain. To activate PCD, you choose a low-key activity such as knitting, gardening, or casual reading, then wander into the recesses of your mind. But unlike slipping into a daydream or guilty-dysphoric daydreaming, you might first imagine something playful and wishful-like running through the woods, or lying on a yacht. Then you swivel your attention from the external world to the internal space of your mind with this image in mind while still doing the low-key activity. PCD activates the DMN and metaphorically changes the silverware that your brain uses to find information. ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:29:59.198Z",
    "updatedAt": "2024-06-12T21:17:07.607Z"
  },
  {
    "id": 1744217000059,
    "title": "Controlled Napping of 10 min",
    "page": "147",
    "book": "Focus",
    "tags": [
      "Sleep",
      "Productivity"
    ],
    "description": "In addition to building in time for PCD, leaders can also consider authorized napping. Not all naps are the same. When your brain is in a slump, your clarity and creativity are compromised. After a 10-minute nap, studies show, you become much clearer and more alert. But if it's a creative task you have in front of you, you will likely need a full 90 minutes of sleep for more complete brain refreshing. Your brain requires this longer time to make more associations and dredge up ideas",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:29:59.198Z",
    "updatedAt": "2024-06-12T21:17:07.607Z"
  },
  {
    "id": 1744217000060,
    "title": "Pretending to Be Someone Else",
    "page": "148",
    "book": "Focus",
    "tags": [
      "Creativity"
    ],
    "description": "When you're stuck in a creative process, unfocus can come to the rescue if you embody and live out an entirely different personality. In 2016, educational psychologists Denis Dumas and Kevin Dunbar found that people who try to solve creative problems are more successful if they behave like an eccentric poet than a rigid librarian. Given a test in which they had to come up with as many uses as possible for any object (such as a brick), those who behaved like eccentric poets had superior creative performance. This finding holds even if the same person takes on a different identity. When you're in a creative deadlock, try embodying a different identity. It will likely get you out of your own head and allow you to think from another person's perspective. (I call this \"psychological halloweenism.\")",
    "comments": "When drawing, you could imagine yourself as a brilliant artist to give you confidence and help you grow. When coding, you could imagine yourself as Colress or someone good at coding to give you confidence.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T19:34:19.699Z",
    "updatedAt": "2024-06-03T19:34:19.699Z"
  },
  {
    "id": 1744217000061,
    "title": "Easy Errors of Judgement",
    "page": "10",
    "book": "Truth & Lies",
    "tags": [
      "Judgement"
    ],
    "description": "it is easy and likely that we will make terrible errors of judgment based on gut feelings, biases and innate patterns of thinking about others--feelings that felt and seemed so right at the time that often end up proven incorrect.",
    "comments": "Every time you see a girl dressed slightly immodest, or a minority person, you are extremely quick to write them off. Try not to be so judgemental.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:34:56.995Z",
    "updatedAt": "2024-06-03T21:34:56.995Z"
  },
  {
    "id": 1744217000062,
    "title": "We All Tend To Interpret in Own Reference",
    "page": "21",
    "book": "Truth & Lies",
    "tags": [
      "Perception",
      "Communication"
    ],
    "description": "We all tend to interpret situations in terms of our own frame of reference, as an expression of our egocentric perspective. In the words of Aaron T. Beck, regarded as the founder of cognitive behavioral therapy, with added stress or when we perceive a threat in a situation, as happens constantly as we negotiate our day-to-day lives, our self-centered thinking goes into overdrive, and out of \"the multiple patterns contributing to another person's behavior, we select a single strand that may affect us personally.\" In other words, we tend to focus on and magnify just one aspect of what we observe from someone else and jump to a conclusion about what they intend toward us that is potentially incorrect. We take someone's behavior as being about us, regardless of whether it is or not.",
    "comments": "Not everything was done deliberately. You tend to extrapolate things. Like how you thought he willfully kept your trophy. All of your thinking and assumptions are based around you, even though they may not be. I would say to Ricardo and TYX that ghosting them is 100% my fault. Not theirs. But they couldn't know that.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:39:42.030Z",
    "updatedAt": "2024-06-03T21:39:42.030Z"
  },
  {
    "id": 1744217000063,
    "title": "Body Language as a Display of Power",
    "page": "24",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "Every gesture, movement, signal or sound we make is a response, conscious or unconscious, to our overall interior and exterior environments. These gestural responses, our \"body language,\" cover everything from how we stand, sit, smile or frown to how we position our heads, hands, shoulders, torso, legs and feet. All our gestures and combinations of gestures can indicate our inner emotional, cognitive and physical responses to power as we experience it in our environments, be it the power of other individuals, of the community, of the physical environment or of our internal emotional or physical states.",
    "comments": "Sit up straight. Shoulders back, chin up. If you want to be a man worthy of respect. No leaning.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:42:10.630Z",
    "updatedAt": "2024-06-03T21:42:10.630Z"
  },
  {
    "id": 1744217000064,
    "title": "By Becoming More Mindful During...",
    "page": "30",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "By becoming more mindful during these moments of judgment, by taking into account the implications of context and the principles by which you are judging others' behaviors, and by becoming more attuned to yourself as part of the entire body language analysis process, you will more accurately decipher the body language of others and use your own body language in the moment in more constructive ways. You will build your knowledge, skill, confidence and competency when assessing the body language signs and behaviors of those around you, even and perhaps especially when under pressure.",
    "comments": "If you understand your own body language, you can mindfully understand the body language of others better.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:45:03.108Z",
    "updatedAt": "2024-06-03T21:45:03.108Z"
  },
  {
    "id": 1744217000065,
    "title": "Humans Use Eye Contact for Targeting",
    "page": "44",
    "book": "Truth & Lies",
    "tags": [
      "Socializing",
      "Body Language"
    ],
    "description": "Humans use eye contact as a signal of targeting",
    "comments": "If you want to talk to someone, try to meet their eyes. If you can't, then they don't care.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:46:42.910Z",
    "updatedAt": "2024-06-03T21:46:42.910Z"
  },
  {
    "id": 1744217000066,
    "title": "Flirtation & Rejection Combined",
    "page": "53",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "However, the flip side of this--the head turn--feels dismissive, like they are taking your power away. Signals that can stimulate feelings of flirtation and attraction have some of the exact same elements as signals that can stimulate feelings of indifference or being rejected. The simultaneous approach/avoid power of these signals creates an opposing attraction/repulsion force that can be best described as allotropic--two different forms of the same property existing within the same physical environment. To you, it feels as if the person is blowing hot and cold; they are open and closed. When they retract the targeting signal and turn their head away, the power play could be any of the following: 1. I thought you had value, so I looked at you, and it turns out you don't so I'm dismissing you (and so looking away). In this case the person who gave the look keeps all the power and status, and the party is not looking so good for you after all. 2. You caught me looking at you, and now you have power because you know that I think you have value; but to keep control of the power and hold on to my high status, I'm taking away my look. This is our hard-to-get scenario. 3. I wanted to give you power by making sure you saw me looking at you, and now I'm looking away. Additionally, they are displaying their neck, which shows vulnerability and awards you more power by creating for you a low-risk situation--an availability signal low-risk atmosphere, inviting an approach.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:51:13.773Z",
    "updatedAt": "2024-06-03T21:51:13.773Z"
  },
  {
    "id": 1744217000067,
    "title": "Fun of the Chase/Power of Choice",
    "page": "57",
    "book": "Truth & Lies",
    "tags": [
      "Dating",
      "Socializing"
    ],
    "description": "Ample studies and experiments show that, in certain circumstances, there can be an advantage to playing hard-to-get when trying to attract a mate; and certainly, the Internet is rich with articles and how-to guides on successfully playing the hard-to-get game, both in person and via text. So hard-to-get fits with scholarly as well as popular and romantic narratives about the fun of the chase, and part of the excitement. Part of the benefit attributed to this game is that it fits in with a mind-set that the person playing hard-to-get shows their power of choice. They are playing with their ability, or power, to choose you or someone else. This fits in with social exchange theory, which offers a perspective (in this case) that how we choose mates depends on a combination of factors, including youth, beauty, social rank, kindness, creativity, humor and financial status, in order to create a combined index when weighing up suitability at first glance. So while they are potentially weighing up how desirable you are to them, at the same time their game of hard-to-get increases their value for you as a potential mate, as they are showing off their powers at that moment in the social context.",
    "comments": "Women don't want a guy that is easy. Don't present yourself that way. It's unattractive because there is no fun of the chase. Don't show 100% commitment from day 1. It signals that you're desperate and don't have options.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:55:03.688Z",
    "updatedAt": "2024-06-03T21:55:03.688Z"
  },
  {
    "id": 1744217000068,
    "title": "Most People Can Fake a \"True\" Smile",
    "page": "67",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "Contrary to popular belief, studies show that most people, under ordinary conditions, can convincingly fake a true smile. Show up at your most positive and upbeat and see if they are still giving you the same level of attention. And now look for any pupil dilation when they look at you.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T21:56:31.643Z",
    "updatedAt": "2024-06-03T21:56:31.643Z"
  },
  {
    "id": 1744217000069,
    "title": "They Would Show Up If They Care",
    "page": "74",
    "book": "Truth & Lies",
    "tags": [
      "Socializing",
      "Dating"
    ],
    "description": "When two people are attracted to each other, they can act in many different ways to hang onto power in the relationship (tease, ignore, be thoroughly annoying); at the end of the day, though, if they really are into each other, they'll always find a way to come together, to engage in whatever behaviors they are taking part in with respect to each other. In other words, if someone is into you, they'll find ways to show up to participate in the exchange, whatever that is. You'll notice them popping up in your vicinity regardless of whether it is physical or virtual. This is something we can all overlook initially, but once you realize it, you'll start to see how being present or not is taken for granted but is the most physically impactful aspect of a relationship.",
    "comments": "Don't force something if they don't show any interest. However, a girl could hope for you to keep pursuing. More often than not she doesn't care.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:00:16.766Z",
    "updatedAt": "2024-06-03T22:00:16.766Z"
  },
  {
    "id": 1744217000070,
    "title": "Being Inside Someone's Personal Space",
    "page": "75",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Dating",
      "Socializing"
    ],
    "description": "The first two zones, the intimate and the personal, describe the region surrounding a person that they strongly regard as theirs, often falling under the umbrella of the more general term personal space... He found that most people and cultures value this personal space and feel discomfort, violation, anger or anxiety when it is invaded. Permitting someone into your personal space or entering somebody else's personal space is a strong nonverbal sign of how we feel about the strength of the relationship; how much power we feel comfortable or compelled to take in that relationship, what boundaries are therefore appropriate and, on the flip side, how welcome or not we are when getting up close and personal with someone.",
    "comments": "I know for a fact that I am uncomfortable being close to anyone. If you truly like a girl, and you can sense that she likes you, maybe sharing your personal space is not a bad idea, as it could bring you closer literally and figuratively",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:03:29.982Z",
    "updatedAt": "2024-06-03T22:03:29.982Z"
  },
  {
    "id": 1744217000071,
    "title": "The Narcissist",
    "page": "89",
    "book": "Truth & Lies",
    "tags": [
      "Attitude",
      "Humility"
    ],
    "description": "High and Mighty In popular usage, the terms narcissism, narcissist, and narcissistic denote absurd vanity and are applied to people whose ambitions and aspirations are much grander than their evident talents. Increasingly, we use these terms to describe people who are simply full of themselves, regardless of whether their real achievements are spectacular. Outstanding performers are not always modest, but nor are they necessarily grandiose. Muhammad Ali boasted, \"I am the greatest!\" but that was no lie. He was! The primary requirement for narcissism in a clinical sense is self-absorption, a grandiose sense of self but a serious miscalculation of one's abilities and potential greatness. It's perhaps the difference between being optimistic and totally unrealistic. Additionally, the narcissist is so convinced of their high station that they expect others to recognize their superior qualities immediately. they will be comfortable and buoyant in environments in which the fantasy will not be questioned. Finally, the narcissist fails to recognize when their aggrandizement affects the comfort of others. Muhammad Ali was never unaware of the fact that his boasting really annoyed his opponents.",
    "comments": "Narcissists expect others to recognize their superiority. It's hard to know where the line is when competence is in play. At the end of the day, being kind toward everyone is admirable.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:08:00.508Z",
    "updatedAt": "2024-06-03T22:08:00.508Z"
  },
  {
    "id": 1744217000072,
    "title": "Expression of Suppressed Anger",
    "page": "98",
    "book": "Truth & Lies",
    "tags": [
      "Anger"
    ],
    "description": "However, you would perhaps be able to detect some micro-expressions--brief, involuntary facial expressions that show what they are really feeling. Anger micro-expressions that might leak out are generally understood to include vertical lines between the brows, brows drawn together, tense lower lids, tight and narrow lips, glaring eyes, dilated nostrils and a jutting lower jaw, with all three facial areas involved in the gesture.",
    "comments": "Not everybody is angry at you.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:09:21.015Z",
    "updatedAt": "2024-06-03T22:09:21.015Z"
  },
  {
    "id": 1744217000073,
    "title": "7% Words 38% Tone 55% Expression",
    "page": "99",
    "book": "Truth & Lies",
    "tags": [
      "Communication"
    ],
    "description": "Ninety-three percent of all communication is nonverbal. Excellent, you might be thinking. This means you can say any old words you like to anybody and your body language will do the heavy lifting of getting your meaning across. Well, not exactly. The classic study by Dr. Albert Mehrabian concludes that \"the total impact of a message is based on: 7% words used; 38% tone of voice, volume, rate of speech, vocal pitch; 55% facial expressions, hand gestures postures and other forms of body language. Mehrabian never claimed you could view a movie in a foreign language and accurately guess 93 percent of the content by watching body language, nor is he implying that words are unimportant for getting across meaning. His research was focused on the communication of emotions, specifically liking and disliking. The nonverbal aspect of communication won't deliver 93 percent of your entire message, but it will stimulate theories in the viewer as to the underlying feelings and intentions that inform the meaning of the spoken content. People will evaluate most of the emotional content of your message not by what you say but by your nonverbal signals.",
    "comments": "Feelings are a big deal when communicating. Someone could listen to you speak and understand your message, but if you sound like a robot then they won't be excited by it. You're lame. Instead, try to be a bit more expressive with your emotions when communicating.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:13:14.887Z",
    "updatedAt": "2024-06-03T22:13:14.887Z"
  },
  {
    "id": 1744217000074,
    "title": "Face of Anger",
    "page": "105",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "The signal for anger is more complex. In addition to knitted or lowered eyebrows, anger also features a tight top lip, a raised upper eyelid and tightened eyelids. The head may be tipped down to protect the neck with the chin, and the nostrils may be flared. So although softening the lines on the forehead with a neurotoxin that blocks signals to those muscles can reduce one of the indicators of anger, if someone is truly angry, most of the time that won't be enough to hide it.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:15:33.130Z",
    "updatedAt": "2024-06-03T22:15:33.130Z"
  },
  {
    "id": 1744217000075,
    "title": "When There Are Inconsistencies",
    "page": "108",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Communication"
    ],
    "description": "Classic nonverbal studies by Mehrabian concluded, \"When there are inconsistencies between attitudes communicated verbally and posturally, the postural component should dominate in determining the total attitude that is inferred.\" In other words, most of the clues we get about the emotional intent behind people's words actually come from the nonverbal cues we are getting, and when there is contrast or conflict, we tend to believe the nonverbal.",
    "comments": "Body language is more important that works spoken if they do not align.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:17:53.976Z",
    "updatedAt": "2024-06-03T22:17:53.976Z"
  },
  {
    "id": 1744217000076,
    "title": "Anger Is an Energetic State",
    "page": "108",
    "book": "Truth & Lies",
    "tags": [
      "Anger"
    ],
    "description": "Like happiness, anger is an energetic state. When we are angry, our heart rate increases, and we may have a difficult time relaxing or staying still. Anger is a state that accompanies us into postures of aggression or fight.",
    "comments": "If you do not deal with anger, you'll be restless and irritable. A you won't be able to concentrate or listen. Ease up when you're angry especially around others",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:19:16.321Z",
    "updatedAt": "2025-03-11T16:06:24.897Z"
  },
  {
    "id": 1744217000077,
    "title": "Waiting Out Emotion",
    "page": "109",
    "book": "Truth & Lies",
    "tags": [
      "Communication",
      "Emotion",
      "Anger",
      "Sadness"
    ],
    "description": "With so much ambiguity, rather than making any new judgment or assumption, perhaps the more useful and less risky tactic is to simply wait ten minutes or so, just long enough so that if they are experiencing some intense emotion brought on by other stimuli, like something emotionally heavy or disruptive that happened earlier, this gives them some time and space for the heavy feelings to dissipate. Go and check on your dinner, set the table, take a minute to finish off that work e-mail; in other words, gently put the brakes on any intense interaction for this part of your evening to see if your date's demeanor shifts. If it continues, it could be that the emotion is turning into a mood, which is a lower level of emotional intensity sustained over a long period, anywhere from a number of hours to a day. A heightened emotion sustained for hours may indicate an affective disorder, or the reaction to an extraordinary situation or stimulus.",
    "comments": "Intensive emotions like anger and crying can't be maintained for very long. In a very emotional interaction, it is best for your conscious mind if you wait 10 minutes for your or someone else's emotions to dissipate.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:23:36.833Z",
    "updatedAt": "2024-06-17T21:29:05.844Z"
  },
  {
    "id": 1744217000078,
    "title": "What You Can Do to Even Out Atmosphere",
    "page": "109",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Calmness"
    ],
    "description": "Here's what you can do nonverbally to even out the atmosphere, to try drawing them out of their emotion or any mood, without risking looking like you have no empathy. Use relaxed body language, meaning calm and steady movement, steady breathing, light eyebrows and eyes. Sit and breathe in through your nose and then gently out through your mouth. Try to count each breath, in and out, for a count of four or five seconds. You want to assert steady, light and calm actions to attempt to draw their state away from a downward spiral. Avoid body language that is diametrically opposed to what they are doing, which may make you look as if you lack empathy and understanding. But if you mirror their behavior too much, you both risk spiraling down together.",
    "comments": "Displaying relaxed body language can help someone else calm down by looking at you. Don't oppose their body language completely.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:26:06.730Z",
    "updatedAt": "2024-06-03T22:26:06.730Z"
  },
  {
    "id": 1744217000079,
    "title": "Ownership Signals Proximity",
    "page": "124",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "What is the key body language signal leading you to the assumption that there is an undeniable and powerful attraction between your crush and your friend? They are gazing at each other, but the ownership signals you see are mainly in their proximity and--the icing on the cake--the face touching. While gazing may sometimes indicate romantic intention, the ownership signals clearly show intention. Ownership signals involve closing the proximity between yourself and the thing or person you want to have power over by either leaning in toward them close enough to touch or by touching them and physically bringing them into your own territory. Touching with the hands can show care and can look sensual; this touching involves feeling with the palm of the hand things or people you would like to bring into your personal space and be close to and care for. Witnessing these ownership signals in this scenario would seem to confirm an initial assumption that your crush is into your friend.",
    "comments": "Touching somebody else, or bringing them close to you signals ownership. So does being intimate in the sense that there is little space between them. Holding hands is similar. If you're going to touch your girlfriend's hand, touch the palm.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:30:06.414Z",
    "updatedAt": "2024-06-03T22:30:06.414Z"
  },
  {
    "id": 1744217000080,
    "title": "It's Largely How You Carry Yourself",
    "page": "138",
    "book": "Truth & Lies",
    "tags": [
      "Confidence"
    ],
    "description": "The best color is confidence. Nonverbal cues are also sent with our ornaments--clothes, jewelry and colors. What's the best color to wear in your profile picture? Confidence is the best color in your closet. We looked at colors in both male and female shots and found no significant difference between high and low-ranking women and men. However, confident poses were markedly different for both high and low-ranking women. Attractiveness is as much about attitude as appearance. Being attractive is not just about looks; it's largely about how you carry yourself.",
    "comments": "Being attractive is largely how you carry yourself. Confidence is a big deal. You need to develop some of it or else you'll be a lowly nerd who doesn't have boundaries.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:32:48.063Z",
    "updatedAt": "2024-06-03T22:32:48.063Z"
  },
  {
    "id": 1744217000081,
    "title": "Emotional Reactions Destructive to a Marriage",
    "page": "143",
    "book": "Truth & Lies",
    "tags": [
      "Dating",
      "Emotion"
    ],
    "description": "Gottman's theory that there are four major emotional reactions destructive to a marriage: defensiveness, which is described as a reaction toward a stimulus as if you were being attacked; stonewalling, which is when a person refuses to communicate or cooperate with another; criticism, which is the practice of judging the merits and faults of a person; and the worst of them all, contempt, which is a general attitude that is a mixture of the primary emotions disgust and anger.",
    "comments": "Be nice to your girlfriend. Or dare I say: wife. To prevent this from happening, if you can sense heavy emotion, try the 10 minute cooldown exercise before any confrontation.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:35:21.710Z",
    "updatedAt": "2024-06-03T22:35:21.710Z"
  },
  {
    "id": 1744217000082,
    "title": "The Significance of Eye-Rolling",
    "page": "145",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "Another body language sign showing that contempt is underlying the negative tone in a relationship is eye-rolling. This signal shows disapproval of the other and a rejection of understanding and empathy. Eye-rolling also fits into Gottman's model as it can be a symptom of defensiveness, part and parcel of stonewalling and a sign of criticism.",
    "comments": "Eye rolling is a negative signals. Don't give too many of these to anyone.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:37:11.010Z",
    "updatedAt": "2024-06-03T22:37:11.010Z"
  },
  {
    "id": 1744217000083,
    "title": "Blocking Behaviour",
    "page": "156",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "The behaviour in this scene is classic blocking behaviour. They don't want to show their mouths or their eyes: Their hands conceal the conversation, and they look away from you and down when you try to engage. These defensive body language signs are the clincher for you that they are using their combined powers to close you out of the conversation, and they seem united together against you with their secretive communication.",
    "comments": "Concealing your mouth, eyes, and hands are an example of blocking behaviour. So is looking away, and looking down.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:39:05.163Z",
    "updatedAt": "2024-06-03T22:39:05.163Z"
  },
  {
    "id": 1744217000084,
    "title": "Traits of Charisma",
    "page": "169",
    "book": "Truth & Lies",
    "tags": [
      "Confidence",
      "Attitude"
    ],
    "description": "anyone can display this kind of magnetism. If you want people to perceive you as charismatic, you need to display attributes such as empathy, good listening skills, eye contact, enthusiasm, self-confidence and skillful speaking, all of which are behaviors that can be learned. So although some people may seem to be naturally charismatic, others can learn to be.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:40:05.710Z",
    "updatedAt": "2024-06-03T22:40:05.710Z"
  },
  {
    "id": 1744217000085,
    "title": "We Tend To Dislike What We Don't Understand",
    "page": "179",
    "book": "Truth & Lies",
    "tags": [
      "Attitude",
      "Frustration"
    ],
    "description": "We are wired, after all, to default to the negative when we have to little information, so we tend to dislike what we don't understand.",
    "comments": "Try not to get frustrated if you can't understand what you're learning (or drawing). It's natural to get frustrated if you don't understand. Growth happens by enduring this feeling",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:42:45.744Z",
    "updatedAt": "2024-06-03T22:42:45.744Z"
  },
  {
    "id": 1744217000086,
    "title": "Feeling of Intimacy Private Place",
    "page": "180",
    "book": "Truth & Lies",
    "tags": [
      "Intimacy"
    ],
    "description": "We can create a feeling of intimacy in a selfie by taking the picture in private locations where we are not normally seen, such as bedrooms, bathrooms and closets.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T22:43:42.421Z",
    "updatedAt": "2024-06-03T22:43:42.421Z"
  },
  {
    "id": 1744217000087,
    "title": "Kinesics - Hand Gestures",
    "page": "209",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "professor Paul Ekman and his colleague Wallace Friesen went on to research and prove that some body language, particularly facial expression of emotion, is innate and universal and so does not always rely on being learned. They categorized kinesics into five categories: 1. Emblems-physical gestures that have an exact spoken word equivalent, though they are subject to cultural variations 2. Illustrators-actions that describe, reinforce, or accent what we are saying 3. Affective displays-gestures that convey emotional meaning 4. Regulators-gestures that control the flow and pace of communication by giving visual (or vocal) cues when it is time to take turns speaking 5. Adaptors-actions we make when adapting to environments or circumstances that we are not aware we are making, like hair twisting or pulling an earlobe; these gestures may unintentionally tell something to onlookers about how we are feeling    Kinesics communicate specific meanings with body language; certain elements are universally understood to have the same meanings, and others are culturally specific.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:09:00.549Z",
    "updatedAt": "2024-06-03T23:09:00.549Z"
  },
  {
    "id": 1744217000088,
    "title": "Tribes, Attributes",
    "page": "213",
    "book": "Truth & Lies",
    "tags": [
      "Socializing"
    ],
    "description": "Tribes share social norms, a common experience and often a common purpose. They have limbic resonance and mirror each other. Every tribe has some shared values, beliefs, rituals, customs (other stuff they all share in together to support their values and beliefs on a regular basis), goals, concerns and signals that drive and shape how members of it behave... Tribes have rules and a hierarchy, and following established normal behavior can ensure you reach a status...",
    "comments": "Tribes aren't just ancient village people, but are also friend circles. Think tribe in a fraternal way",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:11:41.273Z",
    "updatedAt": "2024-06-03T23:11:41.273Z"
  },
  {
    "id": 1744217000089,
    "title": "Many Body Language Examples",
    "page": "219",
    "book": "Truth & Lies",
    "tags": [
      "Body Language"
    ],
    "description": "People who like each other will stand closer together and mirror each other's gestures, facial expressions and voice inflection. Those who don't like or respect you may also stand closer than usual but use contrary and aggressive gestures such as talking with their palms facing downward (authoritative), hands beating time with their words (driving home their point) and prolonged eye contact, like a lion watching their prey. People who are rejecting of your presence or your attitudes might cross their arms (barrier/rejection), nod their head with more than three beats (more than three nods is a \"shut up\" signal), and their foot or feet may face toward the door or toward another person, indicating where they would prefer to be.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:13:09.134Z",
    "updatedAt": "2024-06-03T23:13:09.134Z"
  },
  {
    "id": 1744217000090,
    "title": "Anger, Contempt, Fear, and Sadness Cannot be Sustained",
    "page": "222",
    "book": "Truth & Lies",
    "tags": [
      "Anger",
      "Emotion",
      "Sadness",
      "Fear",
      "Control"
    ],
    "description": "Here's a nonverbal technique to keep the peace and keep yourself and others from losing self-control. Many of the trickiest emotions to be around in their strongest forms, such as anger, contempt, fear and sadness, cannot be sustained for a long period of time. They cause too much strain on the body and mind because they are designed to signal to others strong enough feelings to change the environment for the better, right now. If you or a family member are going through a strong emotion, then move yourself or them away from the immediate environment for just ten minutes. You will most likely find that the strong emotions subside, and then you might be able to talk about the problem rather than just nonverbally reacting to the power of it.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:14:46.113Z",
    "updatedAt": "2024-06-03T23:14:46.113Z"
  },
  {
    "id": 1744217000091,
    "title": "How Liars Speak When Lying",
    "page": "240",
    "book": "Truth & Lies",
    "tags": [
      "Communication",
      "Deceit"
    ],
    "description": "Where do liars eventually fall down and betray their deceit? Often, in the structure of what they say and the story they give. Look for whether they distance themselves from the hot spots of the story, split hairs when challenged on the elements of the narrative, decline to answer questions, change the subject or tone, protest a question, stall on getting to a point by giving extraneous information or are unable to recount the story out of chronological sequence. Also you can be linguistically tipped off when they direct you toward exterior social qualifiers: \"Ask anyone about it,\" they might say-or they might try to give a character reference for themselves by putting the focus onto you, saying you know they would never do such a thing, or measuring probabilities by saying they are not likely to do that. These linguistic alarm bells avoid the test of questions that are clearly answerable with a \"yes\" or \"no\" and instead use other negatives, such as \"I never do that.\"",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:16:00.421Z",
    "updatedAt": "2024-06-03T23:16:00.421Z"
  },
  {
    "id": 1744217000092,
    "title": "More Assertive Body Language/Posture",
    "page": "254",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Confidence"
    ],
    "description": "Try immediately taking up more physical space. First off, sit up straight. If you are at a table, move your chair back six inches so you are taking up more room and showing off more of a physical presence to others at the table. Place your hands on the table so you are taking up that territory as well. Place your smartphone on the table and push it away from you to take up even more territory and also to keep yourself from reaching for it and hiding away with it. Stand up when you are speaking or making important points. Make eye contact with the other members of your family. All these postures will make you appear more assertive. However, if you are concerned about looking aggressive as opposed to assertive, avoid putting your hands on your hips or putting both hands on the table and leaning over in close proximity to others. These gestures are both easily taken as an overt display of upper body strength and so could misrepresent you as aggressive, getting you further dismissed or shut down by our family. You may have a better chance of being heard and listened to if you engage with the clan by commanding some space in a calm and assertive manner, without appearing aggressive.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:17:20.050Z",
    "updatedAt": "2024-06-03T23:17:20.050Z"
  },
  {
    "id": 1744217000093,
    "title": "Lowering Gaze --> Submission/Insecure",
    "page": "324",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Confidence"
    ],
    "description": "However, when you invite this person to speak, they lean back, drop their eyebrows, lower their gaze and verbally let you know they will not be adding their two cents right row. What else do those body language signs communicate? Looking down and lowering their eyebrows could signal they are concealing something or disapprove of something; both keeping the eyebrows lowered for a long time and lowering their gaze may also show that they feel insecure. Additionally, lowering the gaze could signal guilt or submission to power. All in all, you are getting mixed messages or an incongruity in their nonverbal messages. The person looks like they need to speak but then say they don't. Is it you, or them, or you and them?",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:18:52.265Z",
    "updatedAt": "2024-06-03T23:18:52.265Z"
  },
  {
    "id": 1744217000094,
    "title": "Showing the Palms of Your Hands",
    "page": "334",
    "book": "Truth & Lies",
    "tags": [
      "Socializing",
      "Body Language"
    ],
    "description": "This is why showing the palms of your hands is a great way to establish rapport-you're showing you have nothing to hide. So keep this in mind when you get into position for that office group photo: you will generate more positive and trustworthy feelings about yourself and the group by showing more of your hands, not less.",
    "comments": "Don't be so rigid with your arms and keep your hands in your pockets. Only pussies do that. Show your palms if you want to establish rapport. Try not to be a stick/robot.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:22:10.389Z",
    "updatedAt": "2024-06-03T23:22:10.389Z"
  },
  {
    "id": 1744217000095,
    "title": "Body Language of Losers",
    "page": "336",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Confidence"
    ],
    "description": "Those who lose a specific challenge, like a game or a match, also tend to display a unique body expression. Losers do not learn this expression by observation; it arises from innate human programming. Losers roll their shoulders in, hang their heads low, wear pained or sad expressions and clench their hands into fists of defeat. As the adrenaline and excitement leave their body, it wilts in sadness and frustration; the effect is similar to a balloon deflating as its air slips away.",
    "comments": "You act like this every day. It's as if you lost in life. That ends now. Shoulders back, chin up, walk with a touch of swagger, like you own this place; because you are not a loser.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:24:17.561Z",
    "updatedAt": "2024-06-03T23:24:17.561Z"
  },
  {
    "id": 1744217000096,
    "title": "Would That Inspire You? Of Course Not.",
    "page": "345",
    "book": "Truth & Lies",
    "tags": [
      "Body Language",
      "Leadership"
    ],
    "description": "In terms of demonstrating leadership behavior, what other choices do they have. Would you prefer they go in the other direction, minimizing their use of space, caving and looking down, shrugging their shoulders in a show of either indifference or uncertainty, biting their nails anxiously, showing less dominant and more submissive behaviour? Would that inspire you? No, of course not. The behaviors required to perform as a good, modern leader are not binary but are more complex.",
    "comments": "Here's what leaders do: Take up space, looking up, shoulders back, have opinions (no I don't know), never cave in. Your girlfriend expects this of you. Practice it daily.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:29:46.387Z",
    "updatedAt": "2024-06-03T23:29:46.387Z"
  },
  {
    "id": 1744217000097,
    "title": "Stress Demonstrations/Signs",
    "page": "351",
    "book": "Truth & Lies",
    "tags": [
      "Stress",
      "Body Language"
    ],
    "description": "Stress can elicit many of the following behaviors or key signals: nail biting, lip suppression, feet wrapped together or a generally tense body; self-soothing gestures or an increase in manipulators such as rubbing the face or the back of the neck, the arms, the legs, hand wringing, even self-hugging; maybe some pacing, fidgeting, tapping with fingers or legs, or moving the whole body toward exits; and some bigger physiological indicators like sweating, fast breathing rate, wide pupils, high blink rate, pale skin, dry mouth resulting dry looking lips and lip licking, a swallow reflex, a clicking sound in the voice and even just a generally stressed-sounding voice tonality and cadence.",
    "comments": "Never elicit these behaviours. No nail biting, lip suppression, toe crunching, rubbing your neck face arms or legs, PACING, or fidgeting. You are the man. Don't be a wimp.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:32:23.974Z",
    "updatedAt": "2024-06-03T23:32:23.974Z"
  },
  {
    "id": 1744217000098,
    "title": "Latin Expression - Burden of Proof",
    "page": "357",
    "book": "Truth & Lies",
    "tags": [
      "Judgement",
      "Communication"
    ],
    "description": "the Latin expression ei incumbit probatio qui dicit, non qui negat--the burden of proof is on the one who declares, not on the on who denies. This is the principle that a person is considered innocent unless proven guilty. This principle keeps any society that uses it safe from its own snap judgments. So the onus is on you to gather more intelligence and hard evidence; where the stakes are high, you need to be thorough and not just go with a hunch.",
    "comments": "Hunches are not evidence. You can't accuse people of being a certain way without examples.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:34:01.809Z",
    "updatedAt": "2024-06-03T23:34:01.809Z"
  },
  {
    "id": 1744217000099,
    "title": "Interrogation Questions for Liars",
    "page": "358",
    "book": "Truth & Lies",
    "tags": [
      "Deceit",
      "Communication"
    ],
    "description": "1. Ask for more details than the person has provided or can provide. 2. Listen intently to what the person is saying and notice when their words stray from a normal pattern. 3. Look for increases in body language indicators. 4. Listen for verbal bridges (a phrase coined by Jack Schafer), phrases like and then, and don't allow the person to hide time. 5. Be specific in your questions and expect specific answers. At the end of the day you will find that most folks want to be honest and will tell the truth if they believe it will be better for them. Most of the time they have gotten into the situation through trying to gain esteem or belong. Help them belong or gain esteem through your ploy and you will be surprised at the result.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:35:22.063Z",
    "updatedAt": "2024-06-03T23:35:22.063Z"
  },
  {
    "id": 1744217000100,
    "title": "Getting Better at Anything Requires a Leap of Faith",
    "page": "8",
    "book": "Confidence",
    "tags": [
      "Growth",
      "Confidence",
      "Failure"
    ],
    "description": "Take risks Playing to your strengths is a smart tactic but not if it means you hesitate to take on new challenges. Many people don't know what they are capable of until they are truly tested. \"Try things you don't think you can do. Failure can be very useful for building confidence,\" say Gruenfeld. Of course, this is often easier said than done. \"It feels bad to not be good at something. There's a leap of faith with getting better at anything,\" says Schwartz. But don't assume you should feel good all the time. In fact, stressing yourself is the only way to grow. Enlisting help from others can make this easier. Gruenfeld recommends asking supervisors to let you experiment with new initiatives or skills when the stakes are relatively low and then to support you as you tackle those challenges.",
    "comments": "Stressing yourself is the only way to grow. Failure can be very useful for building confidence. You can't improve If you don't take on new challenges. So, always try new challenges. It often requires a leap of faith. You don't know what you're capable of until you're tested. Think Hazelnut.",
    "helpfulness": 1,
    "createdAt": "2024-06-03T23:52:52.999Z",
    "updatedAt": "2024-06-17T21:29:26.936Z"
  },
  {
    "id": 1744217000101,
    "title": "Confidence Is ... Sparks Motivation",
    "page": "17",
    "book": "Confidence",
    "tags": [
      "Confidence",
      "Attitude"
    ],
    "description": "Confidence is an expectation of a positive outcome. It is not a personality trait; it is an assessment of a situation that sparks motivation.",
    "comments": "Seems really simple doesn't it?",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:08:36.746Z",
    "updatedAt": "2024-06-04T19:08:36.746Z"
  },
  {
    "id": 1744217000102,
    "title": "Hopelessness and Despair Prevent Positive Action",
    "page": "18",
    "book": "Confidence",
    "tags": [
      "Hopelessness",
      "Despair"
    ],
    "description": "Without enough confidence, it's too easy to give up prematurely or not get started at all. Hopelessness and despair prevent positive action. Self-defeating assumptions. You think can't, so you don't.",
    "comments": "It's a self-fulfilling prophecy. If you think you're hopeless, you are. Learn to not think so hopelessly. It has a negative effect on you.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:15:35.399Z",
    "updatedAt": "2024-06-04T19:15:35.399Z"
  },
  {
    "id": 1744217000103,
    "title": "Goals That Are Too Big Undermine Confidence",
    "page": "18",
    "book": "Confidence",
    "tags": [
      "Goal Setting"
    ],
    "description": "Goals that are too big or too distant. The gap between a giant goal and today's reality can be depressing and demotivating. Confidence comes from small wins that occur repeatedly, with each small step moving you closer to the big goal. But the small steps must be valued and turned into goals themselves. Winners think small as well as big.",
    "comments": "The Love Statue is hard, so is becoming married and being a father. You're thinking too far ahead, are you're trying to make bigger steps that you need to. I know personality wise you like all or nothing, but gradual improvement is more sustainable.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:18:29.069Z",
    "updatedAt": "2024-06-04T19:18:29.069Z"
  },
  {
    "id": 1744217000104,
    "title": "Confidence Is the Art of Moving On ",
    "page": "21",
    "book": "Confidence",
    "tags": [
      "Responsibility",
      "Humility"
    ],
    "description": "Blaming someone else. Confidence rests on taking responsibility for one's own behavior. Even in difficult circumstances, we have choices about how to respond to adversity. Whining about past harms reduces confidence about future possibilities. When the blame game is carried out within companies, everyone loses confidence, including external stakeholder. Confidence is the art of moving on.",
    "comments": "Blame games are pointless and makes you act like a child",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:21:00.455Z",
    "updatedAt": "2024-06-04T19:21:00.455Z"
  },
  {
    "id": 1744217000105,
    "title": "Skilled Interviewers Will Look For",
    "page": "68",
    "book": "Confidence",
    "tags": [
      "Body Language",
      "Confidence"
    ],
    "description": "Skilled interviewers will often be looking for the qualities that are known to correlate with success on the job, such as confidence, energy, and positive body language. How to physically act out these personal qualities? Much has been written about the body language of confidence and how specific gestures such as physical stance, tone, handshake, and eye contact instantly communicate both ease and authority.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:24:57.988Z",
    "updatedAt": "2024-06-04T19:24:57.988Z"
  },
  {
    "id": 1744217000106,
    "title": "Confident Body Language & Success / Types",
    "page": "74",
    "book": "Confidence",
    "tags": [
      "Body Language",
      "Confidence"
    ],
    "description": "People scored points for each sign of positive, confident body language, such as smiling, maintaining eye contact, and persuasive gesturing. They lost points for each negative signal, such as fidgeting, stiff hand movements, and averted eyes.",
    "comments": "Practice this every day. You need to be confident to keep a girl. You need to be confident to get a job. It's essential.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:26:34.097Z",
    "updatedAt": "2024-06-04T19:26:34.097Z"
  },
  {
    "id": 1744217000107,
    "title": "Kinds of Body Language Positions",
    "page": "77",
    "book": "Confidence",
    "tags": [
      "Body Language",
      "Confidence",
      "Leadership"
    ],
    "description": "[Images] The box: Trustworthy, truthful hands at around torso sorta holding a box. Holding the ball: Commanding, dominant Gesturing as if you were holding a basketball between your hands is an indicator of confidence and control, as if you almost literally have the facts at your fingertips. Steve Jobs frequently used this position in his speeches. Pyramid hands: Self-assured, relaxed When people are nervous, their hands often flit about and fidget. When they're confident, they are still. Wide stance: Confident, in control How people stand is a strong indicator of their mindset. When you stand in this strong and steady position, with your feet about a shoulder width apart, it signals that you feel in control. Palms up: Honest, accepting This gesture indicates openness and honesty. Oprah makes strong use of this during her speeches. She is a powerful, influential figure, but also appears willing to connect sincerely with the people she is speaking to, be it one person or a crowd of thousands. Palms down: Strong, assertive The opposite movement can viewed positively too-as a sign of strength, authority and assertiveness. Barack Obama has often used it to calm a crowd right after moments of rousing oration.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:28:35.177Z",
    "updatedAt": "2024-06-04T19:28:35.177Z"
  },
  {
    "id": 1744217000108,
    "title": "Record a Presentation of Yourself ... For Body Language",
    "page": "83",
    "book": "Confidence",
    "tags": [
      "Review",
      "Body Language"
    ],
    "description": "The next time you give a presentation, try to have it recorded, then review the video with the sound off, watching only your body language. How did you stand and gesture? Did you use any of these positions? If not, think about how you might do so the next time you're in front of an audience, or even just speaking to your boss or a big client. Practice in front of a mirror, then with friends, until these positions feel natural.",
    "comments": "You could also record yourself talking and walking to check tone, and posture.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:30:09.608Z",
    "updatedAt": "2024-06-04T19:30:09.608Z"
  },
  {
    "id": 1744217000109,
    "title": "Phrases for Good Attitude",
    "page": "88",
    "book": "Confidence",
    "tags": [
      "Attitude",
      "Virtue"
    ],
    "description": "I've had leaders share that they hold key leadership principles in mind such as \"Give the benefit of the doubt,\" \"Don't take things personally,\" \"Focus on what's best of the business,\" or \"Be direct with respect\" when walking into a difficult conversation, meeting, or potential conflict. Anchoring ourselves in the character we know we have keeps us from becoming chameleons, acting out of fight-or-flight reaction, or only showing respect when there is a commercial gain or benefit-while being uncivil to others who we believe are of less value. A voice of character is ultimately about who you are and the intentions and motivations that guide your speech and actions.",
    "comments": "Virtue because behaviour like lashing out or criticising others without giving them respect is not virtuous. It is about keeping the waters in your head clear and not stormy. Keeping yourself in a place of calm/nirvana. Treating others with respect is virtuous.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:35:05.164Z",
    "updatedAt": "2024-06-04T19:35:05.164Z"
  },
  {
    "id": 1744217000110,
    "title": "What Separates Winners from Losers",
    "page": "102",
    "book": "Confidence",
    "tags": [
      "Calmness",
      "Perseverance"
    ],
    "description": "the ability to stay calm, learn, adapt, and keep on going--separates winners from losers.",
    "comments": "Hazelnut in tough times never give up, or got too excited (although it has happened).",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:36:37.235Z",
    "updatedAt": "2024-06-12T21:24:09.166Z"
  },
  {
    "id": 1744217000111,
    "title": "Inner Critic vs Realistic Thinking",
    "page": "123",
    "book": "Confidence",
    "tags": [
      "Attitude"
    ],
    "description": "How the inner voice in your head compares with realistic thinking [chart] Inner critic [bullets] Very sure it knows the truth of the situation. Asks yes/no questions: \"Is it possible?\" Focuses on problems. Sounds anxious and pessimistic in tone. Thinks in extreme, black-and-white terms. Is repetitive. Realistic thinking Curious and conscious of the many unknowns in the situation. Asks open-ended questions: \"How might this be possible?\" \"What part is possible?\" Seeks solutions. Sounds calmer and generative in tone. Able to see subtlety and gray. Is forward-moving.",
    "comments": "I don't know, to me, the voices in my head are one. However, think in open-ended questions like: How might... Think optimistically and seek solutions instead of wallowing in self-pity. \"It's too hard, someone feel sorry for me\"",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:41:15.161Z",
    "updatedAt": "2024-06-04T19:41:15.161Z"
  },
  {
    "id": 1744217000112,
    "title": "Fear Based Roots of the Inner Voice",
    "page": "123",
    "book": "Confidence",
    "tags": [
      "Fear"
    ],
    "description": "Typically, once someone understands the fear-based roots of the critic's voice and is conscious of when it's speaking up, they can choose to not take direction from it and to take direction from more resourceful and rational parts of themselves instead.",
    "comments": "Allowing fear to take over is the effect of this passage. Don't let fear takeover in situations like dating, or talking to new people. Fear has had a stranglehold over you in the past, but you can change that by not succumbing to it.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:47:44.309Z",
    "updatedAt": "2024-06-04T19:47:44.309Z"
  },
  {
    "id": 1744217000113,
    "title": "90% Preparation 10 % Performance",
    "page": "150",
    "book": "Confidence",
    "tags": [
      "Confidence"
    ],
    "description": "Lower self-confidence makes you pay attention to negative feedback and be self-critical. Most people get trapped in their optimistic biases, so they tend to listen to positive feedback and ignore negative feedback. Although this may help them come across as confident to others, in any area of competence (e.g., education, business, sports, or performing arts) achievement is 10% performance and 90% preparation. Thus, the more aware you are of your soft spots and weaknesses, the better prepared you will be.",
    "comments": "If you walk into a date confidently, you've done most of the work already. If you walk into a date sweating bricks, it will go badly, even if you actually perform ok for sweating bricks. Negative feedback loops can destroy your confidence quickly.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:51:13.161Z",
    "updatedAt": "2024-06-04T19:51:13.161Z"
  },
  {
    "id": 1744217000114,
    "title": "Ambition",
    "page": "151",
    "book": "Confidence",
    "tags": [
      "Ambition",
      "Practice",
      "Confidence"
    ],
    "description": "Low self-confidence may turn you into a pessimist, but when pessimism teams up with ambition it often produces outstanding performance. To be the very best at anything, you will need to be your own harshest critic, and that is almost impossible when your starting point is high self-confidence. Exceptional achievers always experience low levels of confidence and self-confidence, but they train hard and practice continually until they reach an acceptable level of competence. Indeed, success is the best medicine for your insecurities.",
    "comments": "High achievers are never satisfied. They don't see themselves as good enough yet. That's why they are at the top; they never stop improving, or grinding themselves. Once you start getting full of yourself, improvement stops. Think rise and fall of empires.",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:53:47.408Z",
    "updatedAt": "2024-06-04T19:53:47.408Z"
  },
  {
    "id": 1744217000115,
    "title": "Be Serious About Your Goals. Train Hard and Practice Continually",
    "page": "151",
    "book": "Confidence",
    "tags": [
      "Practice",
      "Confidence"
    ],
    "description": "Lower self-confidence can motivate you to work harder and prepare more. If you are serious about your goals, you will have more incentive to work hard when you lack confidence in your abilities. In fact, low confidence is only demotivating when you are not serious about your goals. Most people like the idea of being exceptional but not enough to do what it takes to achieve it. Most people want to be slim, healthy, attractive, and successful, but few people are willing to do what it takes to achieve it.",
    "comments": "Do you want to draw Penny and Hazel? Get cracking. Keep your confidence low. Improvement follows this recipe: low-confidence + practice",
    "helpfulness": 1,
    "createdAt": "2024-06-04T19:56:55.404Z",
    "updatedAt": "2024-06-04T19:56:55.404Z"
  },
  {
    "id": 1744217000116,
    "title": "2 Millimeter Miscalculation",
    "page": "-1",
    "book": "The Compound Effect",
    "tags": [
      "Decision Making"
    ],
    "description": "The Compound Effect is based on a principle I've used in my own life and training; that is, your decisions shape your destiny. The future is what you make of it. Little, everyday decisions will either take you to the life you desire or to disaster by default. In fact, it's the littlest decisions that shape our lives. Stray off course by just two millimeters, and your trajectory changes; what seemed like a tiny, inconsequential decision then can become a mammoth miscalculation now.",
    "comments": "This reminds me of all of the small decisions you make throughout the day. Don't veer off course. Even a little bit makes a difference. At the same time, small right decisions are more powerful than you think",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:10:21.988Z",
    "updatedAt": "2024-06-06T17:10:21.988Z"
  },
  {
    "id": 1744217000117,
    "title": "The Compound Effect Appears to be an Overnight",
    "page": "14",
    "book": "The Compound Effect",
    "tags": [
      "Time",
      "Change"
    ],
    "description": "After thirty-one months (or thirty-one years), the person who uses the positive nature of the Compound Effect appears to be an \"overnight success.\" In reality, his or her profound success was the result of small, smart choices, completed consistently over time.",
    "comments": "Though it may seem like overnight, it's the build up of small actions that can make a big difference. A penny multiplies to 10 million after doubling 31 times (2^31)",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:11:54.081Z",
    "updatedAt": "2024-06-06T17:11:54.081Z"
  },
  {
    "id": 1744217000118,
    "title": "Don't Try To Fool Yourself",
    "page": "20",
    "book": "The Compound Effect",
    "tags": [
      "Failure",
      "Discipline",
      "Hard Work"
    ],
    "description": "Don't try to fool yourself into believing that a mega-successful athlete didn't live through regular bone-crushing drills and thousands of hours of practice. He got up early to practice--and kept practicing long after all others had stopped. He faced the sheer agony and frustrations of the failure, loneliness, hard work, and disappointment it took to become No. 1.",
    "comments": "Always, I mean always remember the \"sheer agony\" it took to become Hazelnut. That is what it takes. It's not easy. That passage encapsulated it.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:13:18.515Z",
    "updatedAt": "2024-06-06T17:13:18.515Z"
  },
  {
    "id": 1744217000119,
    "title": "Thanksgiving Journal For The Wife",
    "page": "27",
    "book": "The Compound Effect",
    "tags": [
      "Gratitude",
      "Marriage"
    ],
    "description": "One Thanksgiving, I decided to keep a Thanks Giving journal for my wife. Every day for an entire year I logged at least one thing I appreciated about her--the way she interacted with her friends, how she cared for our dogs, the fresh bed she prepared, a succulent meal she whipped up, or the beautiful way she styled her hair that day--whatever. I looked for things my wife was doing that touched me, or revealed attributes, characteristics, or qualities I appreciated. I wrote them all down secretly for the entire year. By the end of that year, I'd filled an entire journal.",
    "comments": "Make a specialized Utah (don't keep it in your pocket), and write down something each day with the date you wrote it. Maybe give this for an anniversary or Christmas or birthday",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:15:30.485Z",
    "updatedAt": "2024-06-06T17:15:30.485Z"
  },
  {
    "id": 1744217000120,
    "title": "100/0 Give 100%. 0 Expectations",
    "page": "29",
    "book": "The Compound Effect",
    "tags": [
      "Dating",
      "Marriage",
      "Responsibility",
      "Humility"
    ],
    "description": "\"You have to be willing to give 100 percent with zero expectation of receiving anything in return,\" he said. \"Only when you're willing to take 100 percent responsibility for making the relationship work will it work. Otherwise, a relationship left to chance will always be vulnerable to disaster.\" If I always took 100 percent responsibility for everything I experienced--completely owning all of my choices and all the ways I responded to whatever happened to me--I held the power. Everything was up to me. I was responsible for everything I did, didn't do, or how I responded to what was done to me. ... \"Of course I take responsibility for my life.\" But then you look at how most people operate in the world; there's a lot of finger pointing, victimhood, blaming, and expecting someone else or the government to solve their problems. If you've ever blamed traffic for being late, or decided you are in a bad mood because something your kid, spouse, or co-worker did, you're not taking 100 percent responsibility.",
    "comments": "Cracks emerge after you tell them that they're not holding up their end of the bargain. Then again, you can't take full responsibility for a tyrant or sociopath's behaviour. Don't be overly apologetic, but try to restrain from criticizing your favourite person in life.",
    "helpfulness": 6.5,
    "createdAt": "2024-06-06T17:19:26.029Z",
    "updatedAt": "2025-04-10T16:12:43.837Z"
  },
  {
    "id": 1744217000121,
    "title": "To Help You Become Aware of Your Choices",
    "page": "34",
    "book": "The Compound Effect",
    "tags": [
      "Awareness",
      "Reflection"
    ],
    "description": "To help you become aware of your choices, I want you to track every action that relates to the area of your life you want to improve. If you've decided you want to get out of debt, you're going to track every penny you pull from your pocket. ... Simply carry around a small notebook, something you'll keep in your pocket or purse at all times, and a writing instrument. You're going to write it all down. Every day. Without fail. No excuses, no exceptions.",
    "comments": "Use Addy/Utah to track your decisions. Figure something out. Like, progress or missteps. Towards a goal",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:20:37.184Z",
    "updatedAt": "2024-06-06T17:20:37.184Z"
  },
  {
    "id": 1744217000122,
    "title": "Compound Effect, but it spills into other areas",
    "page": "52",
    "book": "The Compound Effect",
    "tags": [
      "Time",
      "Growth"
    ],
    "description": "I then asked Beverly to increase her distance an eighth of a mile each outing (an almost unnoticeable length, maybe only 300 steps further). Within six months, she was running nine miles without any discomfort at all. In nine months, she was running 13.5 miles regularly (more than the distance of a half-marathon_ as part of her running routine. More exciting, though, was what happened in other areas of her life. Beverly lost her cravings for chocolate (a lifelong obsession) and heavy, fatty foods. Gone. The increased energy she felt from the cardiovascular exercise and better eating choices helped her bring more enthusiasm to her work. Her sales performance doubled during the same period",
    "comments": "Reminds me of the \"willpower train\". One good decision leads to positive outcomes elsewhere.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:22:24.515Z",
    "updatedAt": "2024-06-06T17:22:24.515Z"
  },
  {
    "id": 1744217000123,
    "title": "When Your Reason Is Big Enough",
    "page": "64",
    "book": "The Compound Effect",
    "tags": [
      "Motivation"
    ],
    "description": "[to paraphrase the scenario] If someone offered you twenty dollars to walk a plank between two skyscrapers, you would decline, but if your child was trapped in one of the skyscrapers (now on fire) you would do it. ... The risks and dangers are the same. What changed? Your why changed--your reason for wanting to do it. You see, when the reason is big enough, you will be willing to perform almost any how.",
    "comments": "A why can motivate you to do just about anything. You'll do anything if you believe it's worth it.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:23:37.775Z",
    "updatedAt": "2024-06-06T17:23:37.775Z"
  },
  {
    "id": 1744217000124,
    "title": "Chasing Butterflies",
    "page": "72",
    "book": "The Compound Effect",
    "tags": [
      "Growth",
      "Change",
      "Desire"
    ],
    "description": "Who You Have to Become ... Success is not something you pursue. What you pursue will elude you; it can be like trying to chase butterflies. Success is something you attract by the person you become.",
    "comments": "He talks about wanting a woman by listing qualities he'd like. He questioned whether this woman would want him. So he made the man equivalent of this woman, and became that man. The same applies to jobs. You need to become someone to achieve goals.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:24:57.660Z",
    "updatedAt": "2024-06-17T21:31:05.788Z"
  },
  {
    "id": 1744217000125,
    "title": "Your Life Comes Down To This Formula: Choice + Behaviour + Habit + Compound = Goals",
    "page": "74",
    "book": "The Compound Effect",
    "tags": [
      "Habits",
      "Goal Setting",
      "Behaviour"
    ],
    "description": "You may think you've got a handle on all your bad habits, but I'd bet good money you're wrong. Again, that's why tracking is so effective. I mean, honestly, do you know how many hours of TV you really watch every day? ... Or how many hours you spend doing nonessential \"work\" on the computer?",
    "comments": "I will turn off Trixie and Mavis at 22:30 and do it repeatedly. I will wake up at 8:32 every day repeatedly. I will start reading at 22:30 every day repeatedly. There is no time for this one, but it is similar to the habit bonfire.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:26:26.982Z",
    "updatedAt": "2024-06-06T17:26:26.982Z"
  },
  {
    "id": 1744217000126,
    "title": "Crunchy Habit of Tortilla Chips",
    "page": "79",
    "book": "The Compound Effect",
    "tags": [
      "Habits"
    ],
    "description": "Swap it. ... My sister-in-law started a habit of eating crunchy and salty junk food when she watched TV. She'd crunch through a whole bag of tortilla chips with little actual awareness. ... She decided to replace her bad habit with crunching on carrot and celery sticks, and raw broccoli spears.",
    "comments": "Maybe you should try that. Bad Habits List: 1. Instagram when tried. 2. Hot showers. UPDATED: Bad Habits List: 1. Slacking off. 2. Wrong music choice during work. 3. Not reading. 4. Not drawing despite aspirations",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:28:32.003Z",
    "updatedAt": "2024-06-06T17:28:32.003Z"
  },
  {
    "id": 1744217000127,
    "title": "Addition Not Subtraction",
    "page": "86",
    "book": "The Compound Effect",
    "tags": [
      "Attitude"
    ],
    "description": "\"It's not so much what you attempt to take out of your diet,\" he explained to me. \"It's what you put in instead.\" This has become his analogy for life. Instead of thinking that he has to deprive himself, or take something out of his diet (e.g., \"I can't eat a hamburger, chocolate, or dairy\"), he thinks about what he can have instead (e.g., \"Today I'm going to have a salad and steamed vegetables and fresh figs\"). He fills his focus and his belly with what he can have, so he no longer has attention or hunger for what he can't. Instead of focusing on what he has to sacrifice, Montel thinks about what he gets to \"add in.\" The result is a lot more powerful.",
    "comments": "To make changes, think of \"I can\" or \"I get to\" or \"I'm going to\" rather than \"I can't\" or \"You're not allowed\". Reframe it to sound more appealing.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:29:42.307Z",
    "updatedAt": "2024-06-06T17:29:42.307Z"
  },
  {
    "id": 1744217000128,
    "title": "Cash Out at the End of the Day",
    "page": "104",
    "book": "The Compound Effect",
    "tags": [
      "Reflection"
    ],
    "description": "It is important to cash out your day's performance. Compared to your plan for the day, how did it go? What do you need to carry over to tomorrow's plan? What else needs to be added...What's no longer important and needs to be scratched out?",
    "comments": "\"Cash out\" and review your performance today. Fill out journals like he did. (Utah, Addy, Ari) also Notion reviews are a good habit to continue.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:30:56.561Z",
    "updatedAt": "2024-06-06T17:30:56.561Z"
  },
  {
    "id": 1744217000129,
    "title": "Momentum Train Analogy",
    "page": "106",
    "book": "The Compound Effect",
    "tags": [
      "Routine",
      "Change"
    ],
    "description": "Getting into a Rhythm: Finding Your New Groove. Once your daily disciplines have become a routine, you want the succession of those steps to create a rhythm. When your disciplines and actions jibe into a regular weekly, monthly, quarterly, and yearly rhythm, it's like laying a welcome mat at the front door for Big Mo[mentum].",
    "comments": "The first push is the hardest, then it gets easier, then there's no stopping it. Think of the willpower train.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:31:51.344Z",
    "updatedAt": "2024-06-06T17:31:51.344Z"
  },
  {
    "id": 1744217000130,
    "title": "Be the Tortoise. Be Consistent",
    "page": "115",
    "book": "The Compound Effect",
    "tags": [
      "Consistency"
    ],
    "description": "Miss only a couple weeks of anything--workouts at the gym, affectionate gestures toward your spouse ... and you don't just lose the results those two weeks would have produced. If that's all you lost (which is what most people assume), not much damage would be done. But by slacking off for even a short time, you killed Mo[mentum]. It's dead.... Winning the race is all about pace. Be the tortoise. The person who, given enough time, will beat virtually anybody in any competition as a result of positive habits and behaviours applied consistently.... Making the right choice, holding to [the] right behaviours, practicing perfect habits, staying consistent, and keeping your momentum is easier said than done...",
    "comments": "Even if it's slow, progress must not stop. This means no throwing in the towel, or cheat days. Stick to habits and routines because it's like the page-a-day folks. Slouching never works. He uses the analogy of a water pump. Initially, water won't come out even if you're pumping because it's still rising from the ground. However, once it does come out you only need consistent pumping to keep the water coming. When you stop, the water will slowly fall back down the pipe. It's a good momentum analogy.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:33:21.250Z",
    "updatedAt": "2024-06-21T19:49:05.600Z"
  },
  {
    "id": 1744217000131,
    "title": "Bombarded With All Those Reports About Robberies",
    "page": "120",
    "book": "The Compound Effect",
    "tags": [
      "Productivity",
      "Media Consumption",
      "Negativity"
    ],
    "description": "If you want your brain to perform at its peak, you've got to be even more vigilant about what you feed it. Are you feeding it news summaries or mind-numbing sitcoms? ... Controlling the input has a direct and measurable impact on your productivity and outcomes.",
    "comments": "Feed your mind positive content. Not negative content like killings and black babies and Justin Trudeau. You'll think about it too much. It's negativity. Stop it. No political content. No racism. Be an expert in the right things. Your mind is a glass cup. Don't put muddy water in there. Only clean water.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:37:10.756Z",
    "updatedAt": "2024-06-06T17:37:10.756Z"
  },
  {
    "id": 1744217000132,
    "title": "Moments of Truth",
    "page": "143",
    "book": "The Compound Effect",
    "tags": [
      "Endurance",
      "Growth",
      "Difficulty",
      "Competition"
    ],
    "description": "I was sure I needed to take a break to go to the bathroom or get a glass of water. But instead of quitting, every time I hit one of those mental and emotional walls, I recognized that my competitors were facing the same challenges. I knew this was another moment that, if I kept going, I would be strides ahead of them. These were the defining moments of success and progress. It wasn't difficult, painful, or challenging when I was just running with the herd, just keeping up, but not really getting ahead. It's not getting to the wall that counts; it's what you do after you hit it.",
    "comments": "Instead of just taking a break of giving up, you need to push through in times of difficulty. That is where success lies. Because your competitors will give up at that moment. Hazelnut is the embodiment of this. You won because you pushed and pushed. Push through the difficulty like biking up a hill without stopping.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:39:56.275Z",
    "updatedAt": "2024-06-06T17:45:00.529Z"
  },
  {
    "id": 1744217000133,
    "title": "It Might Only Be a Minor Addition",
    "page": "156",
    "book": "The Compound Effect",
    "tags": [
      "Growth",
      "Competition"
    ],
    "description": "In the grand scheme of things, it might be only a minor addition, but even so, it's better than expected and multiplies the impression and response from his [Steve Jobs] customers and deepens their loyalty. In a world where most things don't meet expectations, you can significantly accelerate your results and stand out from the pack by doing better than expected.",
    "comments": "Doing better then expected is how you succeed/win. No idea is worth while if it doesn't start with WOW. Bring the X factor. It needs the cherry on top. Like standing out for a job or dating prospect, there has to be a little thing there to put you ahead.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:42:30.405Z",
    "updatedAt": "2024-06-06T17:42:30.405Z"
  },
  {
    "id": 1744217000134,
    "title": "Do You Have Vibrant Health, Abundant Loving Relationships...",
    "page": "160",
    "book": "The Compound Effect",
    "tags": [
      "Decision Making",
      "Goal Setting",
      "Identity"
    ],
    "description": "Do you have the vibrant health, abundant loving relationships, and the world-class skills you'd intended to have by this point in your life?\" If not, why? Simple--choices. It's time to make a new choice--choose to not let the next five years be a continuum of the last. Choose to change your life, once and for all.",
    "comments": "It all comes down to choices. Make the choices your future self in 5 years would have made to get there. It's simple. It's time to make a new choice.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:44:42.470Z",
    "updatedAt": "2024-06-06T17:44:42.470Z"
  },
  {
    "id": 1744217000135,
    "title": "Beautiful Things Are Beautiful",
    "page": "41",
    "book": "Meditations",
    "tags": [
      "Praise",
      "Humility"
    ],
    "description": "Beautiful things of any kind are beautiful in themselves and sufficient to themselves. Praise is extraneous. The object of praise remains what it was--no better and no worse. ... Does anything genuinely beautiful need supplementing? No more than justice does--or truth, or kindness, and humility. Are any of those improved by being praised? Or damaged by contempt? Is an emerald suddenly flawed if no one admires it?",
    "comments": "Praise in unnecessary. You don't need the praise of others to be kind, humble, or honest. Hazelnut doesn't need praise. Pursue it without expecting",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:49:15.621Z",
    "updatedAt": "2024-06-06T17:49:15.621Z"
  },
  {
    "id": 1744217000136,
    "title": "Some People, When They Do Someone a Favour",
    "page": "56",
    "book": "Meditations",
    "tags": [
      "Socializing",
      "Virtue"
    ],
    "description": "Some people, when they do someone a favor, are always looking for a chance to call it in. And some aren't, but they're still aware of it--still regard it as a debt. But others don't even do that. They're like a vine that produces grapes without looking for anything in return.",
    "comments": "Don't expect anything in return. Do things out of generosity. Doing a favor is not a transaction. It's benevolence.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:51:04.788Z",
    "updatedAt": "2024-06-06T17:54:20.540Z"
  },
  {
    "id": 1744217000137,
    "title": "Your Soul Takes on the Colour of Your Thoughts",
    "page": "59",
    "book": "Meditations",
    "tags": [
      "Habits",
      "Clarity",
      "Virtue"
    ],
    "description": "The things you think about determine the quality of your mind. Your soul takes on the color of your thoughts. Color it with a run of thoughts like these: i. Anywhere you can lead your life, you can lead a good one. --Lives are led at court... Then good ones can be. ii. Things gravitate toward what they were intended for. What things gravitate toward what they were intended for. What things gravitate toward is their goal. A thing's goal is what benefits it--its good. A rational being's good is unselfishness. What we were born for. That's nothing new. Remember? Lower things for the sake of higher one, and higher one for one another.",
    "comments": "",
    "helpfulness": 8.6,
    "createdAt": "2024-06-06T17:54:02.919Z",
    "updatedAt": "2025-04-10T16:31:58.505Z"
  },
  {
    "id": 1744217000138,
    "title": "Well Being Is Good Luck, or Good Character",
    "page": "88",
    "book": "Meditations",
    "tags": [
      "Character",
      "Well Being"
    ],
    "description": "Well-being is good luck, or good character",
    "comments": "If you can be the good person you're trying to be, then your well being will increase. Practice good character",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:55:44.955Z",
    "updatedAt": "2024-06-06T17:56:04.044Z"
  },
  {
    "id": 1744217000139,
    "title": "Everywhere, at Each Moment, You Have the Option",
    "page": "93",
    "book": "Meditations",
    "tags": [
      "Humility",
      "Decision Making",
      "Awareness"
    ],
    "description": "Everywhere, at each moment, you have the option: - to accept this event with humility. - to treat this person as he should be treated. - to approach this thought with care, so that nothing irrational creeps in.",
    "comments": "This is a very good approach to life and not let emotion get in the way, and for achieving virtue",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:57:12.449Z",
    "updatedAt": "2024-06-06T17:57:12.449Z"
  },
  {
    "id": 1744217000140,
    "title": "Place Your Well Being In Your Own Hands",
    "page": "96",
    "book": "Meditations",
    "tags": [
      "Well Being",
      "Virtue",
      "Humility"
    ],
    "description": "Nature did not blend things so inextricably that you can't draw your own boundaries--place your own well-being in your own hands. It's quite possible to be a good man without anyone realizing it. Remember that. And this too: you don't need much to live happily. And just because you've abandoned your hopes of becoming a great thinker or scientist, don't give up on attaining freedom, achieving humility, serving others, obeying God.",
    "comments": "You are in charge of your well being. And you can be a good man without anyone realizing it. Be the good man and be well.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:58:30.096Z",
    "updatedAt": "2024-06-06T17:58:30.096Z"
  },
  {
    "id": 1744217000141,
    "title": "If It's in Your Control",
    "page": "104",
    "book": "Meditations",
    "tags": [
      "Humility",
      "Control",
      "Emotion"
    ],
    "description": "If it's in your control, why do you do it? If it's in someone else's, then who are you blaming? Atoms? The gods? Stupid either way. Blame no one. Set people straight, if you can. If not, just repair the damage. And suppose you can't do that either. Then where does blaming get you? No pointless actions.",
    "comments": "Blame doesn't get you anywhere. It is a pointless action. It makes you look like a fool and irresponsible",
    "helpfulness": 1,
    "createdAt": "2024-06-06T17:59:50.911Z",
    "updatedAt": "2024-06-06T17:59:50.911Z"
  },
  {
    "id": 1744217000142,
    "title": "To Fear Pain Is to Fear Something That's Bound to Happen",
    "page": "117",
    "book": "Meditations",
    "tags": [
      "Fear",
      "Pain"
    ],
    "description": "*empty*",
    "comments": "Don't fear the inevitable. Pain is inevitable and will happen to you again and again. Rejection.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:01:38.469Z",
    "updatedAt": "2024-06-06T18:01:38.469Z"
  },
  {
    "id": 1744217000143,
    "title": "Real Good Luck Would be to Abandon Life...",
    "page": "118",
    "book": "Meditations",
    "tags": [
      "Negativity",
      "Virtue"
    ],
    "description": "Real good luck would be to abandon life without ever encountering dishonesty, or hypocrisy, or self-indulgence, or pride. But the \"next best voyage\" is to die when you've had enough. Or are you determined to lie down with evil? Hasn't experience even taught you that.--to avoid it like the plague? Because it is a plague--a mental cancer--worse that anything caused by tainted air or an unhealthy climate. Diseases like that can only threaten you life; this one attacks your humanity.",
    "comments": "Dishonesty, hypocrisy, self-indulgence, pride. These destroy you. Avoid them. Practice their opposites. Virtue.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:03:30.581Z",
    "updatedAt": "2024-06-06T18:03:30.581Z"
  },
  {
    "id": 1744217000144,
    "title": "When You Run Up Against Someone Else's Shamelessness",
    "page": "127",
    "book": "Meditations",
    "tags": [
      "Kindness",
      "Negativity"
    ],
    "description": "When you run up against someone else's shamelessness, ask yourself this: Is a world without shamelessness possible? No. Then don't ask for the impossible. There have to be shameless people in the world. This is one of them. The same for someone vicious or untrustworthy, or with any other defect. Remembering that the whole class has to exist will make you more tolerant of its members. Another useful point to bear in mind: What qualities has nature given us to counter that defect? As an antidote to unkindness it gave us kindness. And other qualities to balance other flaws. ... And how does it injure you anyway? You'll find that none of the people you're upset about has done anything that could do damage to your mind. But that's all that \"harm\" or \"injury\" could mean. Yes, boorish people do boorish things. What's strange or unheard-of about that? Isn't it yourself you should reproach--for not anticipating that they'd act this way? ... So when you call someone \"untrustworthy\" or \"ungrateful,\" turn the reproach on yourself. It was you who did wrong. By assuming that someone else with those traits deserved your trust. Or by doing them a favor and expecting something in return, instead of looking to the action itself for your reward. What else did you expect from helping someone out? Isn't it enough that you've done what your nature demands? You want a salary for it too? As if your eyes expected a reward for seeing, or your feet for walking. That's what they were made for. By doing what they were designed to do, they're performing their function. Whereas humans were made to help others. And when we do help others--or help them to do something--we're doing what we were designed for. We perform our function.",
    "comments": "These people exist. It's not their fault. It's yours for trying to expect more from them. You trusted them, and look what happened. Treat unkindness with kindness. They can't damage your mind. And you shouldn't expect anything in return for kindness",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:05:56.960Z",
    "updatedAt": "2024-06-06T18:05:56.960Z"
  },
  {
    "id": 1744217000145,
    "title": "If They've Made a Mistake",
    "page": "132",
    "book": "Meditations",
    "tags": [
      "Virtue",
      "Emotion"
    ],
    "description": "If they've made a mistake, correct them gently and show them where they went wrong. If you can't do that, then the blame lies with you. Or no one.",
    "comments": "Correct them gently. Don't get mad or think they are stupid. They are not.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:07:55.515Z",
    "updatedAt": "2024-06-06T18:07:55.515Z"
  },
  {
    "id": 1744217000146,
    "title": "To Stop Thinking About a Good Man",
    "page": "137",
    "book": "Meditations",
    "tags": [
      "Virtue",
      "Humility"
    ],
    "description": "To stop talking about what the good man is like, and just be one.",
    "comments": "Just be one. That's all it takes. Be humble, and don't expect anything",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:08:56.186Z",
    "updatedAt": "2024-06-06T18:08:56.186Z"
  },
  {
    "id": 1744217000147,
    "title": "When Faced With People's Bad Behaviour",
    "page": "139",
    "book": "Meditations",
    "tags": [
      "Emotion",
      "Anger",
      "Humility",
      "Control"
    ],
    "description": "When faced with people's bad behaviour, turn around and ask when you have acted like that. When you saw money as a good, or pleasure, or social position. Your anger will subside as soon as you recognize that they acted under compulsion (what else could they do?). Or remove the compulsion, if you can.",
    "comments": "Don't be so harsh on people. You were once compulsive. Don't build resentment just because they acted normally.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:10:20.434Z",
    "updatedAt": "2024-06-06T19:03:14.547Z"
  },
  {
    "id": 1744217000148,
    "title": "Someone Despises Me. Someone Hates Me.",
    "page": "151",
    "book": "Meditations",
    "tags": [
      "Kindness",
      "Virtue",
      "Patience"
    ],
    "description": "Someone despises me. That's their problem. Mine: not to do or say anything despicable. Someone hates me. Their problem. Mine: to be patient and cheerful with everyone, including them. Ready to show them their mistake. Not spitefully, or to show off my own self-control, but in an honest, upright way. Like Phocion (if he wasn't just pretending). That's what we should be like inside, and never let the gods catch us feeling anger or resentment. As long as you do what's proper to your nature, and accept what the world's nature has in store--as long as you work for others' good, by any and all means--what is there that can harm you?",
    "comments": "It's their problem. All you have to do is be patient and show them that they have made a mistake. Not with spite. Honestly. Never be angry or resentful.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:11:42.461Z",
    "updatedAt": "2024-06-06T18:11:42.461Z"
  },
  {
    "id": 1744217000149,
    "title": "And Along With Not Getting Angry at Others",
    "page": "154",
    "book": "Meditations",
    "tags": [
      "Anger",
      "Kindness",
      "Virtue"
    ],
    "description": "And along with not getting angry at others, try to not pander either. Both are forms of selfishness; both of them will do you harm. When you start to lose your temper, remember: There's nothing manly about rage. It's courtesy and kindness that define a human being--and a man. That's who possesses strength and nerves and guts, not the angry whiners. To react like that brings you close to impassivity--and so to strength. Pain is the opposite of strength, and so is anger. Both are things we suffer from, and yield to. ...and one more thought, from Apollo: x. That to expect bad people not to injure others is crazy. It's to ask the impossible. And to let them behave like that to other people but expect them to exempt you is arrogant--the act of a tyrant.",
    "comments": "If you're starting to lose your temper, remember that there's nothing manly about rage. Pandering is selfish. So is being angry at others. Courtesy and kindness define a man",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:13:20.934Z",
    "updatedAt": "2024-06-06T18:13:20.934Z"
  },
  {
    "id": 1744217000150,
    "title": "There's Nothing More Insufferable Than People Who Boast About Their Own Humility",
    "page": "168",
    "book": "Meditations",
    "tags": [
      "Humility"
    ],
    "description": "And how trivial the things we want so passionately are. And how much much more philosophical it would be to take what we're given and show uprightness, self-control, obedience to God, without making a production out of it. There's nothing more insufferable that people who boast about their own humility.",
    "comments": "Never brag about being humble. It's hypocrisy. And defeats what you're saying",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:14:48.436Z",
    "updatedAt": "2024-06-06T18:14:48.436Z"
  },
  {
    "id": 1744217000151,
    "title": "They Buy Into Thoughts, Avoid Evokation",
    "page": "58",
    "book": "Mindfulness",
    "tags": [
      "Distraction",
      "Attitude"
    ],
    "description": "In our people-strategy consulting practice advising companies around the world, we see leaders stumble not because they have undesirable thoughts and feelings-that's inevitable-but because they get hooked by them, like fish caught on a line. This happens in one of two ways. They buy into the thoughts, treating them like facts (It was the same in my last job...I've been a failure my whole career), and avoid situations that evoke them (I'm not going to take on that new challenge).",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:08:40.446Z"
  },
  {
    "id": 1744217000152,
    "title": "Labelling Thoughts. Helicopter View",
    "page": "65",
    "book": "Mindfulness",
    "tags": [
      "Mindfulness",
      "Emotion"
    ],
    "description": "One strategy that may help you consider your situation more objectively is the simple act of labeling. Just as you call a spade a spade, call a thought a thought and an emotion an emotion. I'm not doing enougth at work or at home becomes I'm having the thought that I'm not doing enough at work or at home. Similarly, My coworker is wrong-he makes me so angry becomes I'm having the thought that my coworker is wrong, and I'm feeling anger. Labelling allows you to see your thoughts and feelings for what they are: transient sources of data that may or may not prove helpful. Humans are psychologically able to take this helicopter view of private experiences, and mounting scientific evidence shows that simple, straightforward mindulness practice like this not only improves behavior and well-being but also promotes beneficial biological changes in the brain and at the cellular level.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:10:12.748Z"
  },
  {
    "id": 1744217000153,
    "title": "Debate From the Other Side to Realize Arguments",
    "page": "15",
    "book": "Mindfulness",
    "tags": [
      "Socializing",
      "Arguing"
    ],
    "description": "Have opponents play the debate from the other side so that they realize there ard good arguments either way. Then find a way for both of them to be right.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:04:45.998Z"
  },
  {
    "id": 1744217000154,
    "title": "You Can Start Right Now, In This Moment",
    "page": "96",
    "book": "Mindfulness",
    "tags": [
      "Change",
      "Clarity",
      "Judgement",
      "Stress"
    ],
    "description": "These techniques can, as I've said, rewire the brain. As a result, three critical things happen. First, your ability to concentrate increases. Second, you see things with increasing clarity, which improves your judgment. And third, you develop equanimity. Equanimity enables you to reduce your physiological and emotional stress and enhances the likelihood that you will be able to find creative solutions to problems. Practicing mindfulness-and reaping its benefits-doesn't have to be a big time commitment or require special training. You can start right now-in this moment.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-27T19:20:47.396Z"
  },
  {
    "id": 1744217000155,
    "title": "If Snap Fingers, You Never Develop Potential",
    "page": "20",
    "book": "The Magic Lamp",
    "tags": [
      "Growth",
      "Change",
      "Challenge"
    ],
    "description": "That's why it takes effort to make your magic lamp work. If all you had to do were to snap your fingers to get anything you want, you would never have to develop your potential. You would never have to become more than what you are. But by insisting that the only way to earn your wish is to become the kind of person for whom such a wish is possible, the universe gives you one of the greatest gifts of all; growth.",
    "comments": "Trials are what defines you. If you don't participate in any of life's trials, you'll won't realize any of your potential, and you'll end up as some weak loser who has never been tasked with any responsibility",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:28:35.030Z"
  },
  {
    "id": 1744217000156,
    "title": "A Journey of 1000 Miles Begins With 1 Step",
    "page": "48",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Time",
      "Change"
    ],
    "description": "A journey of a thousand miles begins with a single step. Your L.A.M.P. Plan, no matter how simple or how complex, begins the same way.",
    "comments": "Grains of sand. You can't walk 1000 steps at a time. Only 1. 1000 miles is composed of singular steps. Action is taking those steps. It may seem daunting to have to walk that far, but you must realize your pace. The tortoise will win this race too",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-17T21:33:17.812Z"
  },
  {
    "id": 1744217000157,
    "title": "The Point of Life Is Not the Past, But the Future",
    "page": "72",
    "book": "The Magic Lamp",
    "tags": [
      "Rumination",
      "Acceptance"
    ],
    "description": "The point of life is not to grieve over a wasted past, but to make certain that you don't waste the future.",
    "comments": "The past is gone. It's dead. It will NEVER be changed. Accept the past, and look in the direction of change: the future.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:51:43.324Z"
  },
  {
    "id": 1744217000158,
    "title": "Work on the Most Important Before Everything Else",
    "page": "76",
    "book": "The Magic Lamp",
    "tags": [
      "Planning",
      "Action"
    ],
    "description": "Make this one change in how you spend your day--work on what is most important to you before you take care of everything else--and you'll find that your schedule begins to take on the shape of a life, instead of life life taking on the shape of a schedule.",
    "comments": "What's important to you? Do that. Video games and cocaine are never important. Importance is defined by what you need to do to further your life and achieve your goals.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:03:06.845Z"
  },
  {
    "id": 1744217000159,
    "title": "Positive Acting & Thinking > Negative Acting & Thinking",
    "page": "141",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Positivity",
      "Negativity",
      "Attitude"
    ],
    "description": "So don't worry about thinking positive. Concentrate on acting positive, and thinking positive. Practice acting and thinking in positive ways instead of negative ways. Instead of crying over spilt milk, clean it up. Instead of worrying about the cards you've been dealt, play them. Instead of feeling sorry for yourself, do something about it. Don't worry about how you feel, worry about what you do, and what you think.",
    "comments": "Feelings aren't the center of the universe. Think about the correct things and act in the correct way.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:13:14.085Z"
  },
  {
    "id": 1744217000160,
    "title": "Wish killers: Fear",
    "page": "148",
    "book": "The Magic Lamp",
    "tags": [
      "Fear"
    ],
    "description": "The first wish killer is fear. Fear is a negative wish. The more you focus on what you fear, the more likely you are to make it happen.",
    "comments": "Fear will destroy all of your attempts at your goals. Don't give fear any attention. Fear can realize itself if you think about it all of the time.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:17:55.915Z"
  },
  {
    "id": 1744217000161,
    "title": "It's What You Choose to Do About It",
    "page": "151",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Control"
    ],
    "description": "It's not what happens to you that matters in life, it's what you choose to do about it. We are all victims of forces beyond our control. The people who get what want from life focus on the forces they can control.",
    "comments": "Instead of saying \"I'm a victim of disadvantages\" do something to overcome them",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-07T18:37:25.607Z"
  },
  {
    "id": 1744217000162,
    "title": "Be a Cause Not an Effect",
    "page": "151",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Depression"
    ],
    "description": "They choose to live as a cause instead of as an effect. If you want to be a cause in your own life, don't think like an effect. Instead of worring about the cards you've been dealt, play them. Instead of asking, \"Why me?\" ask, What am I going to do about it? Instead of feeling sorry for youself, refuse to settle for less than you want.",
    "comments": "Stop whining. Thinking about your problems makes them worse. Conversely, not thinking about your problems makes you less depressed. Take action. Stop ruminating",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:18:38.473Z"
  },
  {
    "id": 1744217000163,
    "title": "The World Owes You What You Are Willing to Collect",
    "page": "152",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Success"
    ],
    "description": "The world owes you only what you are willing to collect. The best way I know to collect is to make your wishes come true.",
    "comments": "You can't expect anything by sleeping in and jerking off all day",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:22:19.278Z"
  },
  {
    "id": 1744217000164,
    "title": "The People Who Are Unsuccessful Set in Motion",
    "page": "187",
    "book": "The Magic Lamp",
    "tags": [
      "Action"
    ],
    "description": "In the end, it all boils down to this: The people who are unsuccessful in life are the ones who habitually set in motion the causes of effects that they don't want. The people who are successful in life are the ones who habitually set in motion the causes of effects that they do want.",
    "comments": "Set in motion the causes of effects you want. Causes include: developing your projects, going to school, getting to bed on time. Waking up on time",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:25:18.014Z"
  },
  {
    "id": 1744217000165,
    "title": "Giving is More Fulfilling Than Receiving",
    "page": "192",
    "book": "The Magic Lamp",
    "tags": [
      "Giving"
    ],
    "description": "No doubt you have heard that it is more blessed to give than to receive. That's not just a moral principle, it's a profound psychological insight. Giving is more fulfilling than receiving. Giving is more rewarding than receiving. Giving is just more fun. Receiving rarely reaches the part of us that needs to be touched by others. But giving does, by letting us touch the lives of others. Giving makes us whole. Giving makes us human. If you want to figure out how to find success and happiness in your life, the prescription is simple: stop focusing on what you can take from the world, and start focusing on what you can give.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:26:04.870Z"
  },
  {
    "id": 1744217000166,
    "title": "Just Do It. The Key to Success Is to Take Action",
    "page": "194",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Thinking",
      "Worrying",
      "Success"
    ],
    "description": "Just do it. Don't think about it. Don't worry about it. Don't theorize about it. Just do it. Between those who just do it and those who just don't is a chasm that separates the successful people from the unsuccessful. General George Patton once said that a mediocre plan, violently executed, is more effective than a perfect plan that is executed half-heartedly. They key to success is to take action. The action doesn't have to be perfect. The timing doesn't have to be perfect. The plan doesn't have to be perfect. But you do have to act. The difference between those who do and those who don't is the difference between those who win and those who lose, between those who succeed and those who fail, between those who live the good life and those who only dream about it.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:27:51.523Z"
  },
  {
    "id": 1744217000167,
    "title": "Baseball Recall - Understanding",
    "page": "102",
    "book": "Talent Is Overrated",
    "tags": [
      "Understanding",
      "Performance"
    ],
    "description": "To illustrate, consider first a simple research study involving two groups: devoted baseball fans and casual observers of the game. Both groups were given an engagingly written description of a half-inning game. Later, the devoted fans were much better able to recall the events that mattered more to the game's outcome--advancing runners, preventing runs scored, and so on. The casual observers tended to remember colorful but irrelevant details, such as the crowd's mood and the weather. The fans' high-level knowledge of the game provided a framework on which to hang the information they had read. That finding applies generally: Top performers understand their field at a higher level than average performers do, and thus have a superior structure for remembering information about it.",
    "comments": "Top performers know what's happening more than other performers. To become a top performer, you should try your best to understand how everything works",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:45:08.341Z"
  },
  {
    "id": 1744217000168,
    "title": "Even Brains Can Be Changed - Myelin",
    "page": "103",
    "book": "Talent Is Overrated",
    "tags": [
      "Practice",
      "Change",
      "Repetition"
    ],
    "description": "Even brains can be changed. When kids start practicing a musical instrument, their brains develop differently--the cerebral cortex changes. Brain regions that hear tones and control fingers take over more territory, and the younger the age at which a person starts practicing, the greater the effect. The brain's ability to change is greatest in youth, but it doesn't end there. A study of London taxi drivers, who train rigorously for two years on average, found that their brains had grown in the areas that govern spatial navigation. Particularly important in such changes seems to be the buildup of a substance called myelin around nerve fibers and neurons, which work better with more myelin around them. The brains of professional pianists, for example, show increased myelination in relevant areas. It's significant that myelination is a slow process. Building up myelin over a nerve fiber that controls, say, hitting a particular piano key in a particular way involves sending the appropriate signal through that fiber over and over. This process of building up myelin by sending signals through nerve fibers, which occurs in purely intellectual fields like business as well as in sports and music, needs to happen millions of times in the development of a great performer. In other words, the process of myelin development seems an exact parallel to how deliberate practice works, and illustrates in a new way why it takes many years of intensive work to become a top performer. Research on myelin is still in its early stages, but it appears possible that at the most fundamental, molecular level, myelin may be the connection between intense practice and great performance.",
    "comments": "Habits and repetition change your brain",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:46:52.872Z"
  },
  {
    "id": 1744217000169,
    "title": "Before the Work ... Setting Goals",
    "page": "116",
    "book": "Talent Is Overrated",
    "tags": [
      "Goal Setting",
      "Planning",
      "Performance",
      "Belief"
    ],
    "description": "Before the work. Self-regulation begins with setting goals. These are not big, life-directing goals, but instead are more immediate goals for what you're going to be doing today. In research, the poorest performers don't set goals at all; they're just slog through their work. Mediocre performers set goals that are general and are often focused on simply achieving a good outcome--win the order; close out my positions at a profit; get the new project proposal done. The best performers set goals that are not about the outcome but about the process of reaching the outcome. Form example, instead of just winning the order, their goal might be to focus especially hard on discerning the customer's unstated needs.... But within the activity, the best performers are focused on how they can get better at some specific element of the work, just as a pianist may focus on improving a particular passage. With a goal set, the next prework step is planning how to reach the goal. Again, the best performers make the most specific, technique-oriented plans. They're thinking of exactly, not vaguely, how to get to where they're going.... You may be thinking that figuring out specific goals and plans for what you'll be doing every day sounds hard. It is, and doing it consistently requires high motivation. Where does it come from? The best performers go into their work with a powerful belief in what researchers call their self-efficacy--their ability to perform. They also believe strongly that all their work will pay off for them.",
    "comments": "The best performers have faith that their work will pay off. If you want to get work done, you need to believe it will be worth it.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:52:51.874Z"
  },
  {
    "id": 1744217000170,
    "title": "Figure Skater Analogy - Falling 20,000 Times",
    "page": "187",
    "book": "Talent Is Overrated",
    "tags": [
      "Failure",
      "Success"
    ],
    "description": "Perfecting such moves requires huge quantities of practice, and falling down during much of it. For Arakawa it took nineteen years. A study of figure skaters found that sub-elite skaters spend lots of time working the jumps they could already do, while skaters at the highest levels spent more time on the jumps they couldn't do, the kind that ultimately win Olympic medals and that involve lots of falling down before they're mastered. Falling down in figure skating means landing on your behind, protected only by a thin costume, on hard, cold ice. A few moments with a calculator tell us that by an extremely conservative estimate, Arakawa's road to the gold medal involved at least twenty thousand derriere impacts on an unforgiving surface. But they paid off. The results included Olympic gold, national adoration, and suddenly fashionable use of \"Ina Bauer\" as a vogue word throughout Japan.",
    "comments": "To beat the competition, a figure skater will have to practice tough jumps. Naturally, there will be failure. But in the end, if he can pull it off, he'll win. All it takes is countless failures to endure",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-17T21:34:19.067Z"
  },
  {
    "id": 1744217000171,
    "title": "Education Is Freedom. Make Good Choices",
    "page": "10",
    "book": "The Daily Stoic",
    "tags": [
      "Distraction",
      "Decision Making"
    ],
    "description": "You picked up this book because you are learning how to live. Because you want to be freer, fear less, and achieve a state of peace. Educations--reading and meditating on the wisdom of great minds-- is not to be done for its own sake. It has a purpose. Remember that imperative on the days you start to feel distracted, when watching television or having a snack seems like a better use of your time than reading or studying philosophy.",
    "comments": "January 2",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:57:36.511Z"
  },
  {
    "id": 1744217000172,
    "title": "Seeing our Addictions. Reclaim the Ability to Abstain",
    "page": "16",
    "book": "The Daily Stoic",
    "tags": [
      "Addiction",
      "Abstinence",
      "Clarity"
    ],
    "description": "As one addict put it, addiction is when we've \"lost the freedom to abstain.\" Let us reclaim that freedom. You must reclaim the ability to abstain because within it is your clarity and self-control",
    "comments": "January 8. If you can't stop, you're addicted. Show me you're not addicted.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:11:10.384Z"
  },
  {
    "id": 1744217000173,
    "title": "Cut the Strings That Pull Your Mind",
    "page": "22",
    "book": "The Daily Stoic",
    "tags": [
      "Temptation",
      "Distraction"
    ],
    "description": "These are just a small slice of the temptations and forces acting on us--distracting us and pulling us away from the things that truly matter. Marcus, thankfully, was not exposed to these extreme parts of our modern culture. But he knew plenty of distracting sinkholes too: gossip, the endless call of work, as well as fear, suspicion, lust. Every human being is pulled these internal and external forces that are increasingly more powerful and harder to resist.",
    "comments": "January 14. Resist them. What else are you going to do, give in? That's not what you're supposed to do.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:18:55.293Z"
  },
  {
    "id": 1744217000174,
    "title": "Be Content to Appear Clueless",
    "page": "38",
    "book": "The Daily Stoic",
    "tags": [
      "Knowledge",
      "Improvement",
      "Humility"
    ],
    "description": "\"if you wish to improve, be content to appear clueless or stupid in extraneous matters--don't wish to seem knowledgeable. And if some regard you as important, distrust yourself.\" ",
    "comments": "January 30. You can't know everything right away. There is a 10 000 mile journey to becoming a master. There are no shortcuts. And no, just because you learn faster doesn't mean you're exempt.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-02-28T17:01:38.313Z"
  },
  {
    "id": 1744217000175,
    "title": "Steady Your Impulses. A Central Message",
    "page": "45",
    "book": "The Daily Stoic",
    "tags": [
      "Impulse",
      "Control"
    ],
    "description": "There is such a filter. Justice. Reason. Philosophy. If there's a central message of Stoic thought, it's this: impulses of all kinds are going to come, and your work is to control them, like bringing a dog to heel. Put more simply: think before you act. Ask: Who is in control here? What principles are guiding me?",
    "comments": "February 5. YOU are in control of your impulses. They are not in control of you. Make sure it stays that way.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:33:22.324Z"
  },
  {
    "id": 1744217000176,
    "title": "Pleasure Can Become Punishment. Relapse Is Losing",
    "page": "53",
    "book": "The Daily Stoic",
    "tags": [
      "Temptation",
      "Regret",
      "Abstinence",
      "Resistance",
      "Indulgence"
    ],
    "description": "\"Whenever you get an impression of some pleasure, as with any impression, guard yourself from being carried away by it, let it await your action, give yourself a pause. After that, bring to mind both times, first when you have enjoyed the pleasure and later when you will regret it and hate yourself. Then compare to those the joy and satisfaction you'd feel for abstaining altogether. However, if a seemingly appropriate time arises to act on it, don't be overcome by its comfort, pleasantness, and allure--but against all of this, how much better the consciousness of conquering it.\" Self-control is a difficult thing, no question. Which is why a popular trick from dieting might be helpful. Some diets allow a \"cheat day\"--one day per week in which dieters can eat anything and everything they want. Indeed, they're encouraged to write a list during the week of all the foods they craved so they can enjoy them all at once as a treat (the thinking being that if you're eating healthy six out of seven days, you're still ahead). At first, this sounds like a dream, but anyone who has actually done this knows the truth: each cheat day you eat yourself sick and hate yourself afterward. Soon enough, you're willingly abstaining from cheating at all. Because you don't need it, and you definitely don't want it. It's not unlike a parent catching her child with cigarettes and forcing them to smoke the whole pack. It's important to connect the so-called temptation with its actual effects. Once you understand that indulging might actually be worse than resisting, the urge begins to lose its appeal. In this way, self-control becomes the real pleasure, and the temptation becomes the regret.",
    "comments": "February 13. This is you. No cheat days. No indulging. You can't reward any indulgence ever. You'll hate yourself for it. Do you remember when you playing Catan and regretted it every time? I couldn't stop coming back, only to beat myself up again. That was a nightmare",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:38:16.147Z"
  },
  {
    "id": 1744217000177,
    "title": "To Each His Own. It's Never Worth It",
    "page": "66",
    "book": "The Daily Stoic",
    "tags": [
      "Anger",
      "Temptation",
      "Regret"
    ],
    "description": "\"Another has done me wrong? Let him see to it. He has his own tendencies, and his own affairs. What I have now is what the common nature has willed, and what I endeavor to accomplish now is what my nature wills.\" ... Abraham Lincoln letters...He knew, as the former emperor of Rome knew, that it's easy to fight back. It's tempting to give them a piece of your mind. But you almost always end up with regret. You almost always wish you hadn't sent the letter. Think of the last time you flew off the handle. What was the outcome? Was there any benefit?",
    "comments": "February 26.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:46:05.962Z"
  },
  {
    "id": 1744217000178,
    "title": "Don't Give Up Your Mind",
    "page": "78",
    "book": "The Daily Stoic",
    "tags": [
      "Control",
      "Thinking"
    ],
    "description": "\"If a person gave away your body to some passerby, you'd be furious. Yet you hand over your mind to anyone who comes along, so they may abuse you, leaving it disturbed and troubled--have you no shame in that? Instinctively, we protect our physical selves. We don't let people touch us, push us around, control where we go. But when it comes to the mind, we're less disciplined. We hand it over willingly to social media, to television, to what other people are doing, thinking, or saying. We sit down to work and the next thing you know, we're browsing the Internet. We sit down with our families, but within minutes we have our phones out. We sit down peacefully in a park, but instead of looking inward, we're judging people as they pass by. We don't even know that we're doing this. We don't realize how much waste is in it, how inefficient and distracted it makes us. And what's worse--no one is making this happen. It's totally self-inflicted. To the Stoics, this is an abomination. They know that the world can control our bodies--we can be thrown in jail or be tossed about by the weather. But the mind? That's ours. We must protect it. Maintain control over your mind and perceptions, they'd say. It's your most prized possession.",
    "comments": "March 8. Your mind is your most important asset. You have complete authority over it. Don't let others control it, disturb it, or get it to do what they want. It's yours",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:49:57.254Z"
  },
  {
    "id": 1744217000179,
    "title": "Cowardice Is a Design Problem. Not Having a Plan",
    "page": "98",
    "book": "The Daily Stoic",
    "tags": [
      "Planning",
      "Cowardice"
    ],
    "description": "A delicate conversation turns into a shouting match. You switched majors halfway through college and had to start your coursework over and graduate late. Sound familiar? It's the chaos that ensues from not having a plan. Not because plans are perfect, but because people without plans--like a line of infantry men without a strong leader--are much more likely to get overwhelmed and fall apart.... Don't try to make it up on the fly. Have a plan.",
    "comments": "March 28. You'd be confident in what you're doing if you had a plan. Make sure you have a plan.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:55:54.170Z"
  },
  {
    "id": 1744217000180,
    "title": "Prepare Yourself for Negativity",
    "page": "108",
    "book": "The Daily Stoic",
    "tags": [
      "Patience",
      "Forgiveness",
      "Strength",
      "Negativity"
    ],
    "description": "You can be certain as clockwork that at some point today you're going to interact with someone who seems like a jerk (as we all have been). The question is: Are you going to be reary for it? \"No one can implicate me in ugliness--nor can I be angry at my relative or hate him.\" The point of this preparation is not to write off everyone in advance. It's that, maybe, because you've prepared for it, you'll be able to act with patience, forgiveness, and understanding.",
    "comments": "April 6. I've been negative. So will other people. Don't get sucked in to it. Instead, practice patience. Because patience is characteristic of a strong man.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:00:32.084Z"
  },
  {
    "id": 1744217000181,
    "title": "Be the Person You Want to Be",
    "page": "136",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Purpose",
      "Goal Setting"
    ],
    "description": "\"First tell yourself what kind of person you want to be, then do what you have to do. For in nearly every pursuit we see this to be the case. Those in athletic pursuit first choose the sport they want, and then do that work.\" An archer is highly unlikely to hit a target she did not aim for. The same goes for you, whatever you target. You are certain to miss the target if you don't bother to draw back and fire. Our perceptions and principles guide us in the selection of what we want--but ultimately our actions determine whether we get there or not. So yes, spend some time--real, uninterrupted time--thinking about what's important to you, what your priorities are. Then, work toward that and forsake all the others. It's not enough to wish and hope. One must act--and act right.",
    "comments": "May 2. Set a goal, and act toward it. That's how goals are accomplished. Wish and hope gets you nowhere. Stop crying out to the universe that you're lonely and desperate for a girlfriend. It's not a viable strategy",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:09:42.756Z"
  },
  {
    "id": 1744217000182,
    "title": "Work Is Therapy",
    "page": "163",
    "book": "The Daily Stoic",
    "tags": [
      "Working"
    ],
    "description": "\"Work nourishes noble minds.\" You know that feeling you get when you haven't been to the gym in a few days? A bit doughy. Irritable. Claustrophobic. Uncertain. Others get a similar feeling when they've been on vacation for too long or right after they retire. The mind and the body are there to be used--they begin to turn on themselves when not put to some productive end. It's sad to think that this kind of frustration is an everyday reality for a lot of people. They leave so much of their potential unfulfilled because they have jobs where they don't really do much or because they have too much time on their hands. Worse is when we try to push these feelings away by buying things, going out, fighting, creating drama--indulging in the empty calories of existence instead of finding the real nourishment. The solution is simple and, thankfully, always right at hand. Get out there and work.",
    "comments": "May 29. Working doesn't make me happy. The knowledge that I put in the work does. This is what leaves me happy at the end of the day. Not how many orgasms I had, but how many steps I took towards my goals, because I know that my goals are what I am here to do.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-18T00:17:15.222Z"
  },
  {
    "id": 1744217000183,
    "title": "Quit Crying and Do Something",
    "page": "171",
    "book": "The Daily Stoic",
    "tags": [
      "Action"
    ],
    "description": "\"We cry to God almighty, how can we escape this agony? Fool, don't you have hands? Or could it be God forgot to give you a pair? Sit and pray you nose doesn't run! Or, rather just wipe your nose and stop seeking a scapegoat.\" The world is unfair. The game is rigged. Succumbing to the self-pity and \"woe is me\" narrative accomplishes nothing.--nothing except sapping you of the energy and motivation you need to do something about your problem. We have a choice: do we focus on the ways we have been wronged, or do we use what we've been given and get to work? Will we wait for someone to save us, or will we listen to Marcus Aurelius's empowering call to \"get active in your own rescue--if you care for yourself at all--and do it while you can.\"",
    "comments": "June 5. Nobody cares about you. Nobody listens to you. There is no silver spoon, or rescue team out there. It's up to you to rescue yourself.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:26:37.097Z"
  },
  {
    "id": 1744217000184,
    "title": "Doing the Right Thing is Enough",
    "page": "212",
    "book": "The Daily Stoic",
    "tags": [
      "Kindness",
      "Humility"
    ],
    "description": "\"When you've done well and another has benefited by it, why like a fool do you look for a third thing on top--credit for the good deed or a favor in return? The answer to the question \"Why did you do the right thing?\" should always be \"Because it was the right thing to do.\" After all, when you hear or see the another person do that--especially when they might have endured some hardship or difficult as a consequence for doing the right thing--do you not think, There, that is a human being at their finest? So why on earth to you need thanks or recognition for having done the right thing? It's your job.",
    "comments": "July 15. Praise is unnecessary anyway.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:12:49.547Z"
  },
  {
    "id": 1744217000186,
    "title": "Words Can't Be Unsaid",
    "page": "298",
    "book": "The Daily Stoic",
    "tags": [
      "Socializing"
    ],
    "description": "\"Better to trip with the feet than with the tongue.\" You can always get up after you fall, but remember, what has been said can never be unsaid. Especially cruel and hurtful things.",
    "comments": "October 5. Cruelty and criticism has no place in your heart. Never criticize. If you do, it can't be taken back, and maybe, the victim uses it to build resentment.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:03:52.632Z"
  },
  {
    "id": 1744217000187,
    "title": "How to Live",
    "page": "318",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Virtue"
    ],
    "description": "\"What, then, makes a person free from hindrance and self-determining? For weatlh doesn't, neither does high-office, state or kingdom--rather, something else must be found ... in the case of living, it is the knowledge of how to live.\" You have two essential tasks in life: to be a pood person and to pursue the occupation that you love. Everything else is a waste of energy and a squandering of your potential. How does one do that? OK, that's a tougher question. But the philosophy we see from the Stoics makes it simple enough: say no to distractions, to destructive emotions, to outside pressure. Ask yourself: What is it that only I can do? What is the best use of my limited time on this planet? Try to do the right thing when the situation calls for it. Treat other people the way you would hope to be treated. And understand that every small choice and tiny matter is an opportunity to practice these larger principles. That's it. That's what goes into the most important skill of all: how to live.",
    "comments": "October 25. A small amount of time. That's all you get. What are you going to do with it? Lie, cheat, attack, deceive? No. Every tiny moment matters",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:24:18.622Z"
  },
  {
    "id": 1744217000188,
    "title": "instructions for Mindfulness 20=30m",
    "page": "52",
    "book": "Mindfulness",
    "tags": [
      "Mindfulness",
      "Meditation"
    ],
    "description": "to get the full benefit of mindfulness, a daily practice of 20-30 minutes works best. Think of it like a mental exercise routine.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:07:08.110Z"
  },
  {
    "id": 1744217000189,
    "title": "A Few Minutes of Mindfulness a Day",
    "page": "78",
    "book": "Mindfulness",
    "tags": [
      "Mindfulness",
      "Focus",
      "Calmness"
    ],
    "description": "You can build this kind of self-awareness through everyday mindfulness practices. One approach starts with sitting in a comfortable and quiet place, breathing deeply, and concentrating on the feeling of inhaling and exhaling, physical sensations, or sounds or sights in your environment. Studies show that spending just a few minutes a day on such exercises gives people greater focus and calm, and for that reason techniques for them are now taught in training programs at companies.",
    "comments": "How to get down from an excited state of nervousness, or anger, or anything that has your anxiety and heart rate running too fast",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:12:52.648Z"
  },
  {
    "id": 1744217000190,
    "title": "1-3 min Become Aware of Your Breath",
    "page": "92",
    "book": "Mindfulness",
    "tags": [
      "Mindfulness",
      "Focus",
      "Calmness",
      "Awareness"
    ],
    "description": "Try a technique I call \"micro meditations.\" These are meditations that can be done several times a day for one to three minutes at a time. Periodically throughout the day, become aware of your breath. ... You will notice that by regularly practicing this micro meditation you will become more aware and calmer. You'll find yourself to be increasingly mindful, calm, and focused. ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:14:16.121Z"
  },
  {
    "id": 1744217000191,
    "title": "You Can Have Anything If Willing to Pay the Price",
    "page": "18",
    "book": "The Magic Lamp",
    "tags": [
      "Growth",
      "Sacrifice",
      "Goal Setting"
    ],
    "description": "Every wish has its price. You can have anything you want if you are willing to pay that price. The price may be in dollars and cents. Or it may be in effort--the weeks or months or years it will take you to make your wish come true. Or the price may be sacrifice, what you have to give up in order to get what you want. Whatever the price turns out to be, you have to pay full retail--you can't bargain with fate.",
    "comments": "The price is usually time. It is often humiliation also.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:24:22.902Z"
  },
  {
    "id": 1744217000192,
    "title": "If You Are 100% Willing to Pay, Then You Are 100% to Succeed",
    "page": "18",
    "book": "The Magic Lamp",
    "tags": [
      "Growth",
      "Success"
    ],
    "description": "Your willingness to pay the price is what gives you the power to cause your wish to come true. If you are 100 percent willing to pay the price, then you are 100 percent likely to succeed.... It's simply a matter of cause and effect. The price is the cause; the wish is the effect. Pay the price--set in motion the appropriate cause--and the wish will take care of itself.",
    "comments": "Sometimes you'll underestimate what the price is and give up. ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:26:04.485Z"
  },
  {
    "id": 1744217000193,
    "title": "The Moment You Make a Choice, You Just Do It",
    "page": "28",
    "book": "The Magic Lamp",
    "tags": [
      "Worrying",
      "Action"
    ],
    "description": "Instead of worrying about what to do, you just do it.",
    "comments": "Go. Just go. There is only one time to act. It is called the present",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-12T21:20:55.849Z"
  },
  {
    "id": 1744217000194,
    "title": "Limiting Factor",
    "page": "39",
    "book": "The Magic Lamp",
    "tags": [
      "Planning"
    ],
    "description": "The distinguishing characteristic of a limiting factor is that once you overcome it, everything else falls into place. If Bill develops the habit of bouncing out of bed at six each morning, he will soon be able to work himself into shape. If Polly learns to enjoy cold calling instead of fearing it, her sales will shoot off the chart. If Manuel learns how to manage his time, he will soon find all the time he needs to look for a new job. Now consider your wish. What is it that most limits your progress? What factor, once changed, will make everything else fall into place? It might be a habit you need to change.",
    "comments": "Take a look at what you want in life and try to identify if there are any \"limiting factors\" that are preventing you from achieving your goals. Fear can get in the way. Poor planning can be the issue. You should evaluate your days and try to remove such things.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:33:48.406Z"
  },
  {
    "id": 1744217000195,
    "title": "Inertia Is the Single Greatest Barrier to Success",
    "page": "46",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Success"
    ],
    "description": "It worked, and I learned one of the great lessons of my life: Inertia is the single greatest barrier to success. It's also the easiest to overcome. All you have to do is to act. Any action you take, no matter how trivial, will do the trick.",
    "comments": "If you act, you're bound to succeed. Easy",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:37:35.831Z"
  },
  {
    "id": 1744217000196,
    "title": "Internal practice: Visualization",
    "page": "52",
    "book": "The Magic Lamp",
    "tags": [
      "Visualization",
      "Practice"
    ],
    "description": "When we think of practice, we usually think of what I call external practice, the kind you do with your body. But there is a second kind of practice, on that is equally useful when it comes to developing a new habit and is far easier to perform. I call it internal practice because you do it with your mind. ... All of these are examples of what psychologists call visualization. That's just a fancy word for practicing with your mind instead of your body. The latest research into visualization proves that your mind can't tell much of a difference between an activity you visualize and one you actually perform. This suggests that you can benefit nearly as much from practicing with your mind as you can from practicing with your body.",
    "comments": "This is about putting yourself in scenarios and visualizing what you would do. It can help you practice things like being on a date, or working, or making a tough decision. Visualize your scenario, and practice with the conscious mind so that when the time comes, you'll be more prepared.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:44:00.547Z"
  },
  {
    "id": 1744217000197,
    "title": "Pre-Memories",
    "page": "55",
    "book": "The Magic Lamp",
    "tags": [
      "Visualization",
      "Practice"
    ],
    "description": "The term visualization is misleading. Internal practice is far more than seeing the appropriate pictures in your mind. You must also feel the appropriate feelings, hear the appropriate sounds, taste the appropriate tastes, ... You need to experience your practice session in your mind as if you were actually experiencing it with your body. The more realistic you make your mental practice, the more firmly you fix the \"experience\" in your brain.",
    "comments": "When visualizing, add as much context as possible. Images as helpful, but they can be supplemented by emotions, and other feelings",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:45:27.200Z"
  },
  {
    "id": 1744217000198,
    "title": "Affirmations",
    "page": "57",
    "book": "The Magic Lamp",
    "tags": [
      "Repetition",
      "Attitude"
    ],
    "description": "There is a second kind of internal practice that appears so simple it's hard to believe it really works, but it does. And you've been practicing it since you were old enough to speak. Though we hate to admit it. we all talk to ourselves. More important, we all listen. Psychologists call this affirmation. What they mean is this: If you tell yourself something often enough, you begin to believe it.",
    "comments": "You can convince yourself something if you tell yourself it enough times.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:46:31.180Z"
  },
  {
    "id": 1744217000199,
    "title": "First Things First. Do It.",
    "page": "85",
    "book": "The Magic Lamp",
    "tags": [
      "Planning",
      "Action"
    ],
    "description": "When it comes right down to it, time management isn't very complicated. In fact, all of time management can be reduced to a single, breathtakingly simple principle: First things first. [no apostrophe!!] This principle, in turn, translates into two steps: 1. Figure out the most important thing for you to be doing right now. 2. Do it.",
    "comments": "What is the most important thing for you to be doing right now? Once you have figured that out, do it",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:04:17.801Z"
  },
  {
    "id": 1744217000200,
    "title": "Stop Asking \"Why?\" Ask, \"What Am I Going to Do About It\"",
    "page": "137",
    "book": "The Magic Lamp",
    "tags": [
      "Action",
      "Attitude"
    ],
    "description": "When we make a wish, we reverse the process of entropy. We focus our time, our energy, and our talent on what we want to accomplish, instead of frittering our lives away. We accept the fact that life is a struggle and thus we free ourselves to stop asking \"Why?\" and start asking What am I going to do about it? When we no longer major in minor things, we allow ourselves to focus on the things that really matter. We grant ourselves the power to make our wishes come true. ",
    "comments": "Woe is me, why must God punish me... Shut up. Get up and do something.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:07:57.663Z"
  },
  {
    "id": 1744217000201,
    "title": "Your Success Will Ultimately Hinge on Persistence",
    "page": "145",
    "book": "The Magic Lamp",
    "tags": [
      "Persistence",
      "Endurance"
    ],
    "description": "Getting what you want in life boils down to a single word: persistence. No matter how presentable your wish, how good your plan, how tireless your work, your success will ultimately hinge on persistence. Are you willing to go the distance? Then you will suceed. Are you willing to endure when orthers are ready to quit? Then you will suceed. Are you willing to pursue what you want until you get it, however long it takes? Then you will suceed.",
    "comments": "When will you give up? Say never.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:14:39.267Z"
  },
  {
    "id": 1744217000202,
    "title": "Change the Movie, Change Your Reaction",
    "page": "149",
    "book": "The Magic Lamp",
    "tags": [
      "Fear",
      "Mindset"
    ],
    "description": "When you're afraid, the movie you're running in your mind is likely to be a gut-wrenching feature presentation of what you fear. You react to that movie the same way you react to a good horror movie--with sweaty palms, a churning stomach, a racing heart. Change the movie, and you change your reaction.",
    "comments": "Apply this when you start making up scenes in your head where somebody does something to you because they hate you and want you to suffer. You're making things up to scare yourself.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-07T18:29:11.714Z"
  },
  {
    "id": 1744217000203,
    "title": "The Path is Extremely Long and Demanding, and Only a Few Will Follow It",
    "page": "104",
    "book": "Talent Is Overrated",
    "tags": [
      "Improvement",
      "Hard Work"
    ],
    "description": "There is in fact a path leading from the state of our own abilities to that of the greats. The path is extremely long and demanding, and only a few will follow it all the way to its end. No matter how far one goes, however, the journey is always beneficial and begins by applying the elements of the process. ",
    "comments": "Improvement takes a lot. Hazelnut took a lot. No one else is Hazelnut. Think about that. I beat the world with my effort as Hazelnut",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:49:19.848Z"
  },
  {
    "id": 1744217000204,
    "title": "It Isn't Much Fun",
    "page": "71",
    "book": "Talent Is Overrated",
    "tags": [
      "Practice",
      "Pain",
      "Difficulty"
    ],
    "description": "It isn't much fun. This follows inescapably from the other characteristics of deliberate practice, which could be described as a recipe for not having fun. Doing things we know how to do well is enjoyable, and that's exactly the opposite of what deliberate practice demands. Instead of doing what we're good at, we insistently seek out what we're not good at. Then we identify the painful, difficult activities that will make us better and do those things over and over. After each repetition, we force ourselves to see--or get others to tell us--exactly what still isn't right so we can repeat the most painful and difficult parts of what we've just done. We continue that process until we're mentally exhausted. Ericsson and his colleagues stated it clearly in their article: Deliberate practice \"is not inherently enjoyable.\" If it seems a bit depressing that the most important thing you can do to improve performance is no fun, take consolation in this fact: It must be so. If the activities that lead to greatness were easy and fun, then everyone would do them and they would not distinguish the best from the rest. The reality that deliberate practice is hard can even be seen as good news. It means that most people won't do it. So your willingness to do it will distinguish you all the more.",
    "comments": "Find what is difficult for you and practice that. It's the best way forward",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:37:33.973Z"
  },
  {
    "id": 1744217000205,
    "title": "Unresolved Conflicts: Rowing Team",
    "page": "142",
    "book": "Talent Is Overrated",
    "tags": [
      "Teamwork",
      "Bitterness"
    ],
    "description": "Unresolved conflicts. Colonel Stas Preczewski, coach of the army crew team at West Point a few years ago, faced a baffling problem. Through extensive testing he had determined the strengths and abilities of every rower on his team. He had measured each man's power on ergometers and had composed crews in every possible combination in order to calculate each member's contribution. He was able to rank his rowers objectively and precisely from best to worst. He then put the eight best in his varsity boat and the eight others, the weakest, in the junior varsity boat. The problem: The JV boat beat the varsity boat two-thirds of the time. The situation is explained in a famous Harvard Business School case, which also notes that the varsity boat was full of resentment over who was contributing the most, while the JV rowers, feeling they had nothing to lose, supported one another happily. But the case doesn't tell how Coach Preczewski solved his problem. One day he lined up the varsity crew in fours pairs. He told them they were to wrestle for ninety seconds. Only rule: no punching. \"It was like the WWF.\" he recalls. When he stopped them, he noticed that no one was winning. Each man was discovering that his opponent was just as strong and determined as he was. Preczewski then had them change opponents and wrestle again. By the third round they were choosing their own opponents--\"One guy would point at another and say, 'You!'\" Preczewski says. On the fourth or fifth round, one of the rowers started laughing, and they all piled into a general brawl. Eventually someone said, \"Coach, can we go row now?\" From then on the varsity boat flew and made it to the semifinals in the national tournament.",
    "comments": "Teams operate best with full confidence in each other. Teams full of resentment will underperform",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-09-21T16:11:00.320Z"
  },
  {
    "id": 1744217000206,
    "title": "Internally Driven, More Creative",
    "page": "164",
    "book": "Talent Is Overrated",
    "tags": [
      "Creativity",
      "Motivation"
    ],
    "description": "The other step, giving people the freedom to innovate, is a matter of motivation. The topic of why people put themselves through the rigors required for great performance is discussed in the last chapter, but it's worth noting there that on creative tasks in particular, some research suggests that people perform more innovatively when they are offered no extrinsic rewards; offering them a reward can actually reduce their creativity. Not all the research agrees, but the point is intuitively plausible: People who are internally driven to create do seem more creative than those who are just doing it for the money. As we've seen, money is never at the top of the list of motivators anyway, and when we're asking people to become masters of their field, we want to rely on the strongest possible inducements. ",
    "comments": "Creativity often stems from your own motivation. Not something from outside, but something from within",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:59:11.655Z"
  },
  {
    "id": 1744217000207,
    "title": "Biggest Difference - Demanding Process - Mastery",
    "page": "165",
    "book": "Talent Is Overrated",
    "tags": [
      "Creativity",
      "Knowledge",
      "Hard Work"
    ],
    "description": "But the evidence shows that the most important factor in their high achievement is the same for both. Professor Raymond S. Nickerson of Tufts University has written that \"the importance of domain-specific knowledge as a determinant of creativity is genrally underestimated, even though investigators have given it considerable emphasis.\" What makes the biggest difference is the willingness to go through the demanding process of acquiring that knowledge over time. David N. Perkins of Harvard, surveying the many factors that have been proposed as important elements of creativity, wrote, \"The clearest evidence of all demonstrates the connection between creative thinking and values broadly construed-- a person's commitments and aspirations ... Much more than we usually suppose, creating is an intentional endeavor.\" Wanting to achieve mastery of a field, commiting to the long, hard work of achieving it, and then intending to innovate-- that's how it happens.",
    "comments": "Creativity comes from domain specific knowledge. Domain specific knowledge comes from hard work trying to learn new things",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:01:41.530Z"
  },
  {
    "id": 1744217000208,
    "title": "Great Performance => Developed Long Period",
    "page": "181",
    "book": "Talent Is Overrated",
    "tags": [
      "Performance",
      "Time"
    ],
    "description": "In light of what we've seen about the nature of great performance, this finding shouldn't be surprising. After all, we've seen repeatedly that great performance doesn't come from superior general abilities; it comes from specific skills that have been developed in a particular way over a long period of time. ",
    "comments": "If you hone your skills over time, your performance will improve",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:03:29.622Z"
  },
  {
    "id": 1744217000209,
    "title": "Passion Develops. Child Prodigies. Forced Lessons.",
    "page": "204",
    "book": "Talent Is Overrated",
    "tags": [
      "Passion"
    ],
    "description": "Most significant, we've seen that the passion develops, rather than emerging suddenly and fully formed. We've also seen hints that childhood may be especially important in how the drive's development gets started. Anders Ericsson goes so far to say, \"The research frontier is parenting. Push children too hard and they respond with anger. You have to develop an independent individual who has chosen to be involved in this activity. It's how you as a parent can make individuals feel freed to reach these levels and aware that this is going to be a long process.\"",
    "comments": "Nobody is born with passion, instead, it is developed. You should develop your passions to continue motivating yourself",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:13:05.568Z"
  },
  {
    "id": 1744217000210,
    "title": "Clarify Your Intentions. Have a Direction",
    "page": "13",
    "book": "The Daily Stoic",
    "tags": [
      "Planning",
      "Goal Setting",
      "Purpose",
      "Decision Making"
    ],
    "description": "Having an end in mind is no guarantee that you'll reach it.. but not having an end in mind is a guarantee you won't... When your efforts are not directed at a cause or a purpose, how will you know what to do day in and day out? How will you know what to say no to and what to say yes to? How will you know when you've had enough, when you've reached your goal, when you've gotten off track, if you've never defined what those things are? The answer is you cannot. And so you are driven into failure--or worse, into madness by the oblivion of directionlessness",
    "comments": "January 5. What are your intentions with the life you've been given. Have purpose with your actions. Know what you're doing. Making decisions based on your purpose. Don't be driven into madness by the oblivion of directionlessness. Amber's personality is summed up by that sentence.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:06:53.854Z"
  },
  {
    "id": 1744217000211,
    "title": "Seven Clear Functions of the Mind",
    "page": "15",
    "book": "The Daily Stoic",
    "tags": [
      "Choice",
      "Temptation",
      "Negativity",
      "Planning",
      "Purpose",
      "Control"
    ],
    "description": "\"The Proper work of the mind is the exercise of choice, refusal, yearning, repulsion, preparation, purpose, and assent. What then can pollute and clog the mind's proper functioning? Nothing but its own corrupt decisions.\" Let's break down each of those tasks: Choice--to do and think right. Refusal--of temptation. Yearning--to be better. Repulsion--of negativity, of bad influences, of what isn't true. Preparation-- for what lies ahead or whatever may happen. Purpose--our guiding principle and highest priority. Assent--to be free of deception about what's inside and outside our control (and be ready to accept the latter). This is what the mind is here to do. We must make sure that it does--and see everything else as pollution or a corruption.",
    "comments": "January 7. This is what your mind was made to do. Your mind is polluted by its own corrupt decisions. Prevent it from doing so.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:05:28.947Z"
  },
  {
    "id": 1744217000212,
    "title": "For the Hotheaded Man",
    "page": "41",
    "book": "The Daily Stoic",
    "tags": [
      "Anger",
      "Strength",
      "Endurance",
      "Calmness",
      "Distraction"
    ],
    "description": "\"Keep this thought handy when you feel a fit of rage coming on--it isn't manly to be enraged. Rather, gentleness and vivility are more human, and therefore manlier. A real man doesn't give way to anger and discontent, and such a person has strengh, courage, and endurance--unlike the angry and complaining. The nearer a man comes to a calm mind, the closer he is to strengh.\" Why do athletes talk trash to each other? Why do they deliberately say offensive and nasty things to their competitors when the refs aren't looking? To provoke a reaction. Distracting and angering opponents is an easy way to knock them off their game. Try to remember that when you find yourself getting mad. Anger is not impressive or tough--it's a mistake. It's weakness. Depending on what you're doing, it might even be a trap that someone laid for you.",
    "comments": "February 1. Anger never works. It's a trap. It fools your mind. It disturbs your mind's tranquil waters it needs to think straight",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:32:44.023Z"
  },
  {
    "id": 1744217000213,
    "title": "Only Bad Dreams",
    "page": "55",
    "book": "The Daily Stoic",
    "tags": [
      "Fear",
      "Worrying"
    ],
    "description": "\"How much pain have cost us the evils which have never happened!\" And Seneca would put it best: \"There is nothing so certain in our fears that's not yet more certain in the fact that most of what we dread comes to nothing.\" Many of the things that upset us, the Stoics believed are a product of the imagination, not reality. ...Getting upset is like continuing the dream while you're awake. The thing that provoked you wasn't real--but your reaction was. And so from the fake comes real consequences. Which is why you need to wake up right now instead of creating a nightmare.",
    "comments": "February 15. You amplify nightmares that don't exist around you. Stop acting like all black people are murderers. You are not living in a dystopia. Only your mind is",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-01-26T17:14:57.318Z"
  },
  {
    "id": 1744217000214,
    "title": "Impossible Without Your Consent",
    "page": "88",
    "book": "The Daily Stoic",
    "tags": [
      "Perception",
      "Emotion"
    ],
    "description": "On tough days we might say, \"My work is overwhelming,\" or \"My boss is really frustrating.\" If only we could understand that this is impossible. Someone can't frustrate you, work can't overwhelm you--these are external objects, and they have no access to your mind. Those emotions you feel, as real as they are, come from the inside, not the outside. The Stoics use the word hypolepsis, which means \"taking up\" --of perceptions, thoughts, and judgments by our mind. What we assume, what we willingly generate in our mind, that's on us. We can't blame other people for making us feel stressed or frustrated any more than we can blame them for jealousy. The cause is within us. They're just the target.",
    "comments": "March 18. The emotions you have are perceptions of the world. Your mind produces emotions. Something bothering you does not. If you're annoyed, it's because whatever was bothering you infiltrated your mind and convinced you mind that it was. The solution is to recognize your mind is separate from the outside world, and that you have control over it. Not external things",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-15T03:39:01.996Z"
  },
  {
    "id": 1744217000215,
    "title": "Expect to Change Your Opinions. If You Want to Be Wise",
    "page": "109",
    "book": "The Daily Stoic",
    "tags": [
      "Humility"
    ],
    "description": "How often do we begin some project certain we know exactly how it will go? How often do we meet people and think we know exactly who and what they are? And how often are these assumptions proved to be completely and utterly wrong? This is why we must fight our biases and preconceptions: because they are a liability. Ask yourself: What haven't I considered? Why is this thing the way it is? Am I part of the problem here or the solution? Could I be wrong here? Be doubly careful to to honor what you do not know, and then set that against the knowledge you actually have. Remember, if there is one core teaching at the heart of this philosophy, it's that we're not as smart and as wise as we'd like to think we are. If we ever do want to become wise, it comes from the questioning and from humility--not, as many would like to think, from certainty, mistrust, and arrogance.",
    "comments": "April 7. ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:01:48.050Z"
  },
  {
    "id": 1744217000216,
    "title": "Judgements Cause Disturbance",
    "page": "112",
    "book": "The Daily Stoic",
    "tags": [
      "Perception"
    ],
    "description": "\"it isn't events themselves that disturb people, but only their judgements about them.\" The samurai swordsman Musashi made a distinction between our \"perceiving eye\" and our \"observing eye.\" The observing eye sees what is. The perceiving eye sees what things supposedly mean. Which one do you think causes us the most anguish? An event is inanimate. It's objective. It simply is what it is. That's what our observing eye sees. This will ruin me. How could this have happened? Ugh! It's so-and-so's fault. That's our perceiving eye at work. Bringing disturbance with it and then blaming it on the event.",
    "comments": "April 10. An event is inanimate. You ascribe meaning to it with your mind. If everything seems to be negative, your mind might be the problem.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:04:27.940Z"
  },
  {
    "id": 1744217000217,
    "title": "Less Is More",
    "page": "115",
    "book": "The Daily Stoic",
    "tags": [
      "Humility"
    ],
    "description": "\"Don't act grudgingly, selfishly, without due diligence, or to be a contrarian. Don't overdress your thought in fine language. Don't be a person of too many words and too many deeds. ... Be cheerful, not wanting outside help or the relief others might bring. A person needs to stand on their own, not be propped up.\"",
    "comments": "April 13. Don't act like you're the most special person to ever live. You're not. Behave normally. This means not being pretentious. ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:06:50.433Z"
  },
  {
    "id": 1744217000218,
    "title": "Kindness Is Always the Right Response",
    "page": "146",
    "book": "The Daily Stoic",
    "tags": [
      "Kindness",
      "Strength"
    ],
    "description": "\"Kindness is invincible, but only when it's sincere, with no hypocrisy or faking. For what can even the most malicious person do if you keep showing kindness and, if given the chance, you gently point out where they went wrong--right as they are trying to harm you? The Bible says that when you can do something nice and caring to a hateful enemy, it is like \"heap[ing] burning coals on his head.\" The expected reaction to hatred is more hatred. When someone says something pointed or mean today, they expect you to respond in kind--not with kindness. When that doesn't happen, they are embarrassed. It's a shock to their system--it makes them and you better. Most rudeness, meanness, and cruelty are a mask for deep-seated weakness. Kindness in these situations is only possible for people of great strength. You have that strength. Use it.",
    "comments": "May 12. Most negativity is a sign of weakness. Conversely, kindness is a sign of strength. Kindness is in and of itself strong, as it beats such negativity",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:12:19.781Z"
  },
  {
    "id": 1744217000219,
    "title": "The Chain Method",
    "page": "150",
    "book": "The Daily Stoic",
    "tags": [
      "Habits",
      "Motivation"
    ],
    "description": "\"if you don't wish to be a hot-head, don't feed your habit. Try as a first step to remain calm and count the days you haven't been angry. I used to be angry every day, now every other day, then every third or fourth ... If you make it as far as 30 days, thank God! For habit is first weakened and then obliterated. When you can say 'I didn't lose my temper today, or the next day, or for three or four months, but kept cool under provocation,' you will know you are in better health.\" The comedian Jerry Seinfeld once gave a young comic named Brad Isaac some advice about how to write and create material. Keep a calendar, he told him, and each day that you write jokes, put an X. Soon enough, you get a chain going--and then your job is to simply not break the chain. Success becomes a matter of momentum. Once you get a little, it's easier to keep going. Whereas Seinfeld used the chain method to build a positive habit, Epictetus was saying that it can also be used to eliminate a negative one. It's not all that different from taking sobriety \"one day at a time.\" Start with one day doing whatever it is, be it managing your temper or wandering eyes or procrastination. Then do the same the following day and the day after that. Build a chain and then work not to break it. Don't ruin your streak.",
    "comments": "May 16. Keeping a streak alive is good motivation.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:17:22.269Z"
  },
  {
    "id": 1744217000220,
    "title": "How You Do Anything Is How You Do Everything",
    "page": "152",
    "book": "The Daily Stoic",
    "tags": [
      "Action"
    ],
    "description": "There is an old saying: \"How you do anything is how you do everything.\" It's true. How you handle today is how you'll handle every day. How you handle this minute is how you'll handle every minute.",
    "comments": "May 18. No relapsing. \"This doesn't count\" never ever applies anywhere under no circumstances. It's code for cheating. It's saying: \"I'm practicing shitty behaviour, but that doesn't make me shitty.\" But of course, it does. It undermines your efforts at becoming better. Every minute counts. Even on days of resistance",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:21:00.328Z"
  },
  {
    "id": 1744217000221,
    "title": "Bitterness and Despair",
    "page": "176",
    "book": "The Daily Stoic",
    "tags": [
      "Jealousy",
      "Achievement"
    ],
    "description": "\"If you find something very difficult to achieve yourself, don't imagine it impossible--for anything possible and proper for another person can be achieved as easily by you.\" There are two kinds of people in this world. The first looks at others who have accomplished things and thinks: Why them? Why not me? The other looks at those same people and thinks: If they can do it, why can't I? One is zero-sum and jealous (if you win, I lose). The other is non-zero-sum (there's plenty to go around) and sees the success of others as an inspiration. Which attitude will propel you onward and upward? Which will drive you to bitterness and despair? Who will you be?",
    "comments": "June 10. Focus on yourself, don't build resentment over other people's accomplishments. Bitterness is a cancer. It ruined you.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:29:24.776Z"
  },
  {
    "id": 1744217000222,
    "title": "Turn Have to Into Get to",
    "page": "200",
    "book": "The Daily Stoic",
    "tags": [
      "Mindset",
      "Attitude"
    ],
    "description": "A long to-do list seems intimidating and burdensome--all these things we have to do in the course of a day or a week. But a Get to Do list sounds like a privilege--all the things we're excited about the opportunity to experience. This isn't just semantic playing. It is a central facet of the philosopher's worldview. Today, don't try to impose your will on the world. Instead see yourself as fortunate to receive and respond to the will in the world. ",
    "comments": "July 3. It's the same chore, however, you'll be more willing to do it by rephrasing.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:01:49.409Z"
  },
  {
    "id": 1744217000223,
    "title": "To Live Without Self-Respect",
    "page": "205",
    "book": "The Daily Stoic",
    "tags": [
      "Character"
    ],
    "description": "To be without character is the worst of all fates. As Didion put it in \"On Self-Respect,\" \"To live without self-respect is to lie awake some night, beyond the reach of warm milk, the phenobarbital, and the sleeping hand on the coverlet, counting up the sins of commission and omission, the trusts betrayed, the promises subtly broken, the gifts irrevocably wasted through sloth or cowardice or carelessness.\" You're so much better than that.",
    "comments": "July 8. Character is a foundation of living. Identity -> Character -> Habits -> Outcomes. Ask yourself who you want to be. The answer is not a sloth or a coward.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:07:43.597Z"
  },
  {
    "id": 1744217000224,
    "title": "Don't Be Miserable in Advance",
    "page": "250",
    "book": "The Daily Stoic",
    "tags": [
      "Attitude",
      "Anxiety"
    ],
    "description": "\"it's ruinous for the soul to be anxious about the future and miserable in advance of misery, engulfed by anxiety that the things it desires might remain its own until the very end. For such a soul will never be at rest--by longing for things to come it will lose the ability to enjoy present things.\" The pragmatist, the person of action, is too busy to waste time on such silliness. The pragmatist can't worry about every possible outcome in advance. Think about it. Best case scenario--if the news turns out to be better than expected, all this time was wasted with needless fear. Worst case scenario--we were miserable for extra time, by choice. And what better use could you make of that time? A day that could be your last--you want to spend it in worry? In what other area could you make some progress while others might be sitting on the edges of their seat, passively awaiting some fate? Let the news come when it does. Be too busy working to care.",
    "comments": "August 21. Be the pragmatist. He just does. Don't bring your mood around. Leave it aside so you don't poison the moods of others. The pragmatist doesn't care, and is focused on his world.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:21:25.586Z"
  },
  {
    "id": 1744217000225,
    "title": "Don't Spend Your Time on Things That Don't Matter",
    "page": "251",
    "book": "The Daily Stoic",
    "tags": [
      "Time",
      "Choice"
    ],
    "description": "They both say the same thing: don't spend your time (the most valuable and least renewable of all your resources) on the things that don't matter. What about the things that don't matter but you're absolutely obligated to do? Well, spend as little time and worry on them as possible. If you give things more time and energy than they deserve, they're no longer lesser things. You've made them important by the life you've spent on them. And sadly, you've made the important things--your family, your health, your true commitments--less so as a result of what you've stolen from them.",
    "comments": "August 22. If you spend time on something, by the very nature of spending time on hit, it becomes important to you. You know what's important and what's not. Choose what's actually important, not was isn't supposed to be. You know exactly what to choose.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:24:24.285Z"
  },
  {
    "id": 1744217000226,
    "title": "Anyone Can Get Lucky, Not Everyone Can Persevere",
    "page": "278",
    "book": "The Daily Stoic",
    "tags": [
      "Perseverance",
      "Hard Work",
      "Honesty",
      "Motivation",
      "Jealousy"
    ],
    "description": "\"Success comes to the lowly and to the poorly talented, but the special characteristics of a great person is to triumph over the disasters and panics of human life.\" Perhaps you know people who've been extraordinarily lucky in life. Maybe they hit the genetic lottery or have skated through classes and careers with ease. Despite never planning, making reckless decisions, jumping from one thing to the next, they've somehow survived without a scratch. There's a saying: \"God favors fools.\" It's natural to be a bit envious of these folks. We want the easy life too--or so we think. But is the easy life really that admirable? Anyone can get lucky. There's no skill in being oblivious, and no one would consider that greatness. On the other hand, the person who perseveres through difficulties, who keeps going when others quit, who makes it to their destination through hard work and honesty? That's admirable, because their survival was the result of fortitude and resilience, not birthright or circumstance. A person who overcame not just the external obstacles to success but mastered themselves and their emotions along the way? That's much more impressive. The person who has been dealt a harder hand, understood it, but still triumphed? That's greatness.",
    "comments": "September 16. It's so easy to cry to God about how literally everybody else got lucky with their lives. \"Curse you, for I have gotten the short end of the stick every time.\" Well guess what, you can do something about it. Perseverance is how you can get from A to B. It's done by putting in hard work in an honest way. ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:40:15.723Z"
  },
  {
    "id": 1744217000227,
    "title": "Before Working Do This",
    "page": "41",
    "book": "Mindfulness",
    "tags": [
      "Mindfulness",
      "Working",
      "Focus"
    ],
    "description": "Next, when you get to the office, take 10 minutes at your desk or in your car to boost your brain with the following short mindfulness practice before you dive into activity. Close your eyes, relax, and sit upright. Place your full focus on your breath. Simply maintain an ongoing flow of attention on the experience of your breathing: Ihale, exhale; inhale, exhale. To help your focus stay on your breathing, count silently at each exhalation. Any time you find your mind distracted, simply release the distraction by returing your focus to your breath. Most important, allow yourself to enjoy these minutes. Throughout the rest of the day, other people and competing urgencies will fight for your attention. But for these 10 minutes, your attention is all your own.",
    "comments": "Take distractions away and descend into your expert state. Think of it as the 10 minutes you need to take in a submarine before you reach the bottom. Get rid of your giddy thoughts and focus",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:07:18.736Z"
  },
  {
    "id": 1744217000228,
    "title": "Opposite of Control Is Acceptance",
    "page": "66",
    "book": "Mindfulness",
    "tags": [
      "Control",
      "Acceptance"
    ],
    "description": "Accept them The opposite of control is acceptance: not acting on every thought or resigning yourself to negativity but responding to your ideas and emotions with an open attutude, paying attention to them and letting yourself experience them. Take 10 deep breaths, and notice what's happening in the moment.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:11:14.854Z"
  },
  {
    "id": 1744217000229,
    "title": "If You Ever Desire a Specific Effect.. Set in Motion",
    "page": "-21",
    "book": "The Magic Lamp",
    "tags": [
      "Action"
    ],
    "description": "If you desire a specific effect in your life--whether it involves a relationship, or a job, or an important project--you must first set in motion the cause of that effect. Whenever that cause is missing, the effect will be missing as well. Whenever the effect is missing, you can be certain that you have neglected to set in motion the appropriate cause.",
    "comments": "Everything obeys the rule of cause and effect. If you desire an effect, you must set in motion the cause.",
    "helpfulness": 5,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-04-10T16:11:19.168Z"
  },
  {
    "id": 1744217000230,
    "title": "Take Immediate Action",
    "page": "30",
    "book": "The Magic Lamp",
    "tags": [
      "Procrastination",
      "Action"
    ],
    "description": "The final step in making your wish presentable is to send your brain the most powerful message of all: Act now. If you don't, you'll fall prey to the Law of Diminishing Intent: the more time that passes before you act, the less likely you will be to take action. Before you get up from your chair, do something to put your wish into action. Make a phone call, create a plan, read a useful article in a newspaper or magazine, write a letter. Do something to get the ball rolling. Do anything. The important thing is to take some kind of actions right now, before you lose the moment, and with it your chance to make your wish come true.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:30:43.966Z"
  },
  {
    "id": 1744217000231,
    "title": "Progress Reports",
    "page": "41",
    "book": "The Magic Lamp",
    "tags": [
      "Reflection",
      "Planning"
    ],
    "description": "If your wish will take a month, make a progress report every week. Include those reports in your L.A.M.P. Plan. Then schedule them in your calendar, the same way you schedule the other steps of your plan. When the time comes to make a progress report, write your answers to these questions: 1. Have I met the milestones I planned to meet since my last progress report? 2. Do I need to change my plan to reach my milestones? 3. Do I need to change my milestones?",
    "comments": "Do weekly reports on your life goals, and what steps you've made to achieve them. This includes finding a girlfriend. Because it is clearly a life goal.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:37:16.672Z"
  },
  {
    "id": 1744217000232,
    "title": "Begin Today What You Regret Not Having Done Yesterday",
    "page": "73",
    "book": "The Magic Lamp",
    "tags": [
      "Regret",
      "Action",
      "Learning"
    ],
    "description": "We are all wise in hindsight. The secret to making your wishes come true is to turn hindsight into foresight. Use your past to empower your future. Begin today what you regret not having done yesterday, and you will avoid that regret tomorrow.",
    "comments": "Learn from the past. Never dwell on it. Fix yesterday today. Not tomorrow. Live the perfect day. There is only one day that has the same date",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:53:39.481Z"
  },
  {
    "id": 1744217000233,
    "title": "Keep Asking Until You Get What You Want",
    "page": "109",
    "book": "The Magic Lamp",
    "tags": [
      "Perseverance",
      "Socializing"
    ],
    "description": "Some people hear the word no and give up. Other people hear no and think that all they need is a bigger hammer. When they find one, they keep pounding until they hear a yes. I don't recommend either approach. No means that what you're doing isn't working, so try something else. You don't need a hammer; you need a key--the key that will unlock the other person's heart. Maybe you haven't asked the right question yet. Maybe you haven't made it worth that person's while. Maybe you haven't been specific enough. Maybe you haven't been sincere. Somewhere along the line you haven't done whatever it is you need to do to inspire that person to help you. So try something else. Or try someone else. And keep trying until you get what you want. If you keep trying until you get what you ask for, you will always get what you ask for.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:06:09.136Z"
  },
  {
    "id": 1744217000234,
    "title": "Picture the Best Outcome; Picture the Gain",
    "page": "150",
    "book": "The Magic Lamp",
    "tags": [
      "Fear",
      "Visualization",
      "Positivity"
    ],
    "description": "When you're afraid of something, you're picturing what can go wrong. If you want to change the channel, picture what can go right, instead. Instead of picturing the worst thing that can happen, picture the best thing that can happen. Instead of picturing the pain, picture the gain. Instead of picturing what you have to lose, picture what you have to win.",
    "comments": "Picture what you have to gain. Look at what you can get. Not what you're losing",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-07T18:31:29.068Z"
  },
  {
    "id": 1744217000235,
    "title": "Sacrifice Means Giving Up instant Gratification",
    "page": "165",
    "book": "The Magic Lamp",
    "tags": [
      "Sacrifice",
      "Desire",
      "Pleasure"
    ],
    "description": "If you want to make your wishes come true, sooner or later you're going to have to come to grips with the desire for instant gratification. The cornerstone for making a successful wish is the willingness to pay the price to make that wish come true. Part of that price is paid in terms of sacrifice. And sacrifice means giving up the pleasures of instant gratification when those pleasures interfere with your wish.",
    "comments": "Stop jerking off. Stop playing video games. Stop sleeping in. Stop Instagram. If you can follow that, you win ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:21:55.040Z"
  },
  {
    "id": 1744217000236,
    "title": "It's Highly Demanding Mentally",
    "page": "70",
    "book": "Talent Is Overrated",
    "tags": [
      "Practice"
    ],
    "description": "It's highly demanding mentally. Deliberate practice is above all an effort of focus and concentration. That is what makes it \"deliberate.\" as distinct from the mindless playing of scales or hitting of tennis balls that most people engage in. Continually seeking exactly those elements of performance that are unsatisfactory and then trying one's hardest to make them better places enormous strains on anyone's mental abilities. A finding that is remarkably consistent across disciplines is that four or five hours a day seems to be the upper limit of deliberate practice, and this is frequently accomplished in sessions lasting no more than an hour to ninety minutes. The best violinists in the Berlin study, for example, practiced about three and a half hours a day, typically in two or three sessions. Even elite athletes say the factor that limits their practice time is their ability to sustain concentration. ... \"Practice with your fingers and you need all day. Practice with your mind and you will do as much in one and a half hours.\" ",
    "comments": "Practice with intent. Is has to have a purpose. To push you out of your comfort zone. That's where growth is",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:35:16.023Z"
  },
  {
    "id": 1744217000237,
    "title": "Creative people are more focused on the task",
    "page": "188",
    "book": "Talent Is Overrated",
    "tags": [
      "Creativity",
      "Motivation",
      "Passion"
    ],
    "description": "The consistent finding reported by many researchers examining many domains is that high creative achievement and intrinsic motivation go together. Creative people are focused on the task (How can I solve this problem?) and not on themselves (What will solving this problem do for me?). Young people who excel in science and math are more intrinsically motivated than their lower-performing peers. Scientists who make important discoveries are found to be passionately involved in their field. ",
    "comments": "The internal drive never stops. The external drive can. Think of how Hazelnut kept going",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:10:50.140Z"
  },
  {
    "id": 1744217000238,
    "title": "Belief Limited by the \"Innate\"",
    "page": "205",
    "book": "Talent Is Overrated",
    "tags": [
      "Belief",
      "Mindset",
      "Achievement"
    ],
    "description": "But if you believe that your performance is forever limited by your lack of a specific innate gift, or by a lack of general abilities at a level that you think must be necessary, then there's no chance at all that you will do the work. That's why this belief is tragically constraining. Everyone who has achieved exceptional performance has encountered terrible difficulties along the way. There are no exceptions. If you believe that doing the right kind of work can overcome the problems, then you have at least a chance of moving on to ever better performance. But those who see setbacks as evidence that they lack the necessary gift will give up-- quite logically, in light of their beliefs. They will never achieve what they might have. What you really believe about the source of great performance thus becomes the foundation of all you will ever achieve. As we noted much earlier, such beliefs can be extremely deep-seated. Regardless of where our beliefs in this matter originated, however, we all have the opportunity to base them on the evidence of reality. The evidence offers no easy assurances. It shows that the price of top-level achievement is extraordinarily high. Perhaps it's inevitable that not many people will choose to pay it. But the evidence shows also that by understanding how a few become great, anyone can become better. Above all, what the evidence shouts most loudly is striking, liberating news: that great performance is not reserved for a preordained few. It is available to you and to everyone.",
    "comments": "Believe you can, it's necessary for achievement. If you don't, even minor mistakes will deter you from proceeding. ",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:16:00.117Z"
  },
  {
    "id": 1744217000239,
    "title": "One Path to Serenity. Giving Up All Outside Your Sphere of Choice",
    "page": "20",
    "book": "The Daily Stoic",
    "tags": [
      "Choice",
      "Control",
      "Happiness"
    ],
    "description": "\"Keep this thought at the ready at daybreak, and through the day and night--there is only one path to happiness, and that is in giving up all outside of your sphere of choice, regarding nothing else as your possession, surrendering all else to God and Fortune.\" This morning, remind yourself of what is in your control and what's not in your control. Remind yourself to focus on the former and not the latter. Before lunch, remind yourself that the only thing you truly possess is your ability to make choices (and to use reason and judgment when doing so). This is the only thing that can never be taken from you completely. In the afternoon, remind yourself that aside from the choices you make, your fate is not entirely up to you. The world is spinning and we spin along with it--whichever direction, good or bad. In the evening, remind yourself again how much is outside of your control and where your choices begin and end. As you lie in bed, remember that sleep is a form of surrender and trust and how easily it comes. And prepare to start the whole cycle over again tomorrow.",
    "comments": "January 12. You can't control crime statistics. You can't control housing prices. You can't control water shortages. You can't control the minds of all women. Once you acknowledge these, you'll begin to live a happier life",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:17:05.679Z"
  },
  {
    "id": 1744217000240,
    "title": "The Day in Review. Record What Makes You Happy or Not So",
    "page": "30",
    "book": "The Daily Stoic",
    "tags": [
      "Review",
      "Reflection",
      "Happiness"
    ],
    "description": "\"I will keep constant watch over myself and--most usefully--will put each day up for review. For this is what makes us evil.--that none of us looks back upon our own lives. We reflect upon only that which we are about to do. And yet our plans for the future descend from the past.\" Keep your own journal, whether it's saved on a computer or in a little notebook. Take time to consciously recall the events of the previous day. Be unflinching in your assessments. Notice what contributed to your happiness and what detracted from it. Write down what you'd like to work on or quotes that you like. By making the effort to record such thoughts, you're less likely to forget them. An added bonus: you'll have a running tally to track your progress too.",
    "comments": "January 22. Use Tawny to write down what made you happy, and what detracted from it",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:20:50.861Z"
  },
  {
    "id": 1744217000241,
    "title": "You Are a Product of Your Training",
    "page": "101",
    "book": "The Daily Stoic",
    "tags": [
      "Habits",
      "Practice",
      "Discipline"
    ],
    "description": "\"Chasing what can't be done is madness. But the base person is unable to do anything else.\" A dog that's allowed to chase cars will chase cars. A child who is never given any boundaries will become spoiled. An investor without discipline is not an investor--he's a gambler. A mind that isn't in control of itself, that doesn't understand its power to regulate itself, will be jerked around by external events and unquestioned impulses. That can't be how you'd like tomorrow to go. So you must be aware of that. You must put in place training and habits now to replace ignorance and ill discipline. Only then will you begin to behave and act differently. Only then will stop seeking the impossible, the shortsighted, and the unnecessary.",
    "comments": "March 31. You are your habits. Are your habits good? No? Then what does that say about you",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:58:21.762Z"
  },
  {
    "id": 1744217000242,
    "title": "Fueling the Habit Bonfire",
    "page": "147",
    "book": "The Daily Stoic",
    "tags": [
      "Habits",
      "Identity"
    ],
    "description": "\"We are what we repeatedly do,\" Aristotle said, \"therefore, excellence is not an act but a habit.\" The Stoics add to that that we are a product of our thought (\"Such as are your habitual thoughts, such also will be the character of your mind,\" Marcus Aurelius put it). Think about your activities of the last week as well as what you have planned for today and the week that follows. The person you'd like to be, or the person you see yourself as--how closely do your actions actually correspond to him or her? Which fire are you fueling? Which person are you becoming?",
    "comments": "May 13. You are your habits. If you're jerking off daily, you're a masturbator. If you're reading daily, you're a reader. Make kindness a habit. Make being patient a habit. Make your goals a habit, and you'll be that",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:39:12.657Z"
  },
  {
    "id": 1744217000243,
    "title": "Talk a Walk",
    "page": "187",
    "book": "The Daily Stoic",
    "tags": [
      "Stress",
      "Creativity",
      "Clarity",
      "Socializing"
    ],
    "description": "\"We should take wandering outdoor walks, so that the mind might be nourished and refreshed by the open air and deep breathing\" Today, make sure you take a walk. And in the future, when you get stressed or overwhelmed, take a walk. When you have a tough problem to solve or a decision to make, take a walk. When you want to be creative, take a walk. When you need to get some air, take a walk. When you have a phone call to make, take a walk. When you need some exercise, take a long walk. When you have a meeting or a friend over, take a walk together. Nourish yourself and your mind and solve your problems along the way.",
    "comments": "June 21. Talking walks helps you collect your thoughts.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:57:50.063Z"
  },
  {
    "id": 1744217000244,
    "title": "Love the Humble Art",
    "page": "207",
    "book": "The Daily Stoic",
    "tags": [
      "Practice",
      "Time"
    ],
    "description": "Whatever humble art you practice: Are you sure you're making time for it? Are you loving what you do enough to make the time? Can you trust that if you put in the effort, the rest will take care of itself? Because it will. Love the craft, be a craftsman.",
    "comments": "July 10. Spend time drawing. It doesn't have to be vigorous. It needs time to grow.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:09:35.175Z"
  },
  {
    "id": 1744217000245,
    "title": "Start Where the World Is",
    "page": "237",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Humility"
    ],
    "description": "\"Do now what nature demands of you. Get right to if if that's in your power. Don't look around to see if people will know about it. Don't await the perfection of Plato's Republic, but be satisfied with even the smallest step forward and regard the outcome as a small thing.\" ... There is plenty that you could do right now, today, that would make the world a better place. There are plenty of small steps that, were you to take them, would help move things, forward. Don't excuse yourself from doing them because the conditions aren't right or because a better opportunity might come along soon. Do what you can, now. And when you've done it, keep it in perspective, don't overblow the results. Shun both ego and excuse, before and after.",
    "comments": "August 8. The conditions will never be perfect. Just start taking steps. Your mood is determined by you. You can always set the mood as \"working mood\".",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:17:39.034Z"
  },
  {
    "id": 1744217000246,
    "title": "No Pain, No Gain",
    "page": "284",
    "book": "The Daily Stoic",
    "tags": [
      "Difficulty",
      "Struggle",
      "Pain",
      "Strength"
    ],
    "description": "\"Difficulties show a person's character. So when a challenge confronts you, remember that God is matching you with a younger sparring partner, as would a physical trainer. Why? Becoming an Olympian takes sweat! I think no one has a better challenge than yours, if only you would use it like an athlete would that younger sparring partner. Everyone has found themselves outmatched by an opponent, frustrated by some skill or attribute they have that we don't--height, speed, vision, whatever. How we choose to respond to that struggle tells us about who we are as athletes and who we'll be as people. Do we see it as a chance to learn and get stronger? Do we get frustrated and complain? Or worse, do we call it off and find an easier game to play, one that makes us feel good instead of challenged? The greats don't avoid these tests of their abilities. They seek them out because they are not just the measure of greatness, they are the pathway to it.",
    "comments": "September 22. Pain is the pathway to success. How you respond to the struggle determines who you are",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:02:06.896Z"
  },
  {
    "id": 1744217000247,
    "title": "Looking Out for Each Other",
    "page": "299",
    "book": "The Daily Stoic",
    "tags": [
      "Jealousy",
      "Virtue",
      "Empathy"
    ],
    "description": "\"It's in keeping with Nature to show our friends affection and to celebrate their advancement, as if it were our very own. For if we don't do this, virtue, which is strengthened only by exercising our perceptions, will no longer endure in us.\" Watching other people succeed is one of the toughest things to do--especially if we are not doing well ourselves. In our hunter-gatherer minds, suspect that life is a zero-sum game--that for someone to have more means that we might end up with less. But like all parts of philosophy, empathy and selflessness are a matter of practice. As Seneca observed, it's possible to learn to \"rejoice in all their successes and be moved by their very failure.\" This is what a virtuous person does. They teach themselves to actively cheer for other people--even in cases where that might come at their own expense--and to put aside jealousy and possessiveness. You can do that too.",
    "comments": "October 6. Virtuous people cheer for others. They want to see the world improve, possibly if they are to be usurped. Think about NSS golf and how much this idea is lacking among them. You are also guilty.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:08:20.968Z"
  },
  {
    "id": 1744217000248,
    "title": "Character Is Fate",
    "page": "322",
    "book": "The Daily Stoic",
    "tags": [
      "Character"
    ],
    "description": "In the hiring process, most employers look at where someone went to school, what jobs they've held in the past. This is because past success can be an indicator of future successes. But is it always? There are plenty of people who were successful because of luck. Maybe they got into Oxford or Harvard because of their parents. And what about a young person who hasn't had time to build a track record? Are they worthless? Of course not. This is why character is a far better measure of a man or woman. Not just for jobs, but for friendships, relationships, for everything. Heraclitus put it as a maxim: \"Character is fate.\" When you seek to advance your own position in life, character is the best lever--perhaps not in the short term, but certainly over the long term. And the same goes for the people you invite into your life.",
    "comments": "October 29. Your character defines you. Not numbers on a grade report or words on a resume. Your character determines where you'll end up. People with poor character aren't going to have many connections. Good character is being kind and reaching out, out of benevolence, without expecting anything in return. Practice and build an exemplary character, for it is the most defining aspect of you.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:40:15.715Z"
  },
  {
    "id": 1744217000249,
    "title": "Accepting What Is",
    "page": "326",
    "book": "The Daily Stoic",
    "tags": [
      "Acceptance",
      "Negativity"
    ],
    "description": "\"Don't seek for everything to happen as you wish it would, but rather wish that everything happens as it actually will--then your life will flow well.\" Something happened that we wish had not. Which of these is easiest to change: our opinion or the event that is past? The answer is obvious. Accept what happened and change your wish that it had not happened. Stoicism calls this the \"art of acquiescence\"--to accept rather than fight every little thing. And the most practiced Stoics take it a step further. Instead of simply accepting what happens, they urge us to actually enjoy what has happened--whatever it is. Nietzsche, many centuries later, coined the perfect expression to capture this idea: amor fati (a love of fate). It's not just accepting, it's loving everything that happens. To wish for what has happened to happen is a clever way to avoid disappointment because nothing is contrary to your desires. But to actually feel gratitude for what happens? To love it? That's a recipe for happiness and joy.",
    "comments": "November 1. What is easier to change: Events that happen, or your opinion/displeasure about it? Change your opinions, and you'll be happier. You won't see negativity everywhere if your opinions aren't so dismissive.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:41:03.839Z"
  },
  {
    "id": 1744217000250,
    "title": "A Higher Power",
    "page": "330",
    "book": "The Daily Stoic",
    "tags": [
      "Control",
      "Acceptance",
      "Addiction"
    ],
    "description": "In undergoing a twelve-step program, many addicts struggle most with step 2: acknowledging a higher power. Addicts often fight this one. At first they claim it's because they're atheists or because they don't like religion or because they don't undestand why it matters. But they later realize that this is just the addiction talking--it's another form of selfishness and self-absorption. The actual language of the step is pretty easy to swallow: \"[We] came to believe that a Power greater than ourselves could restore us to sanity.\" Subsequent steps ask the addict to submit and let go. The second step really has less to do with \"god\" than those other steps--the letting go. It's about attuning to the universe and discarding the toxic idea that we're at the center of it. It's no wonder that the Stoics are popular with those in twelve-step programs. It's also clear that this wisdom is beneficial to us all. You don't have to believe there is a god directing the universe, you just need to stop believing that you're the director. As soon as you can attune your spirit to that idea, the easier and happier your life will be, because you will have given up the most potent addiction of all: control.",
    "comments": "November 5. You are not the center of the universe. Some things will happen to you. Things are outside of your control. You must acknowledge that. At the same time, you must recognize that there are some things you control. Just not everything. Focus on what you can control. That could include stopping addiction.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:44:37.345Z"
  },
  {
    "id": 1744217000251,
    "title": "Meditators Are Rational",
    "page": "91",
    "book": "Mindfulness",
    "tags": [
      "Awareness",
      "Mindfulness",
      "Emotion"
    ],
    "description": "Mindfulness has become almost a buzzword. But what is it, really? Quite simply, mindfulness is being present and aware, moment by moment, regardless of circumstances. For instance, researchers have found that practicing mindfulness can reprogram the brain to be more rational and less emotional. When faced with a decision, meditators who practiced mindfulness showed increased activity in the posterior insula of the brain, an area linked to rational decision making. This allowed them to make decisions based more on fact than emotion.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:13:28.812Z"
  },
  {
    "id": 1744217000252,
    "title": "If I Were Absolutely Positive I Could Get It",
    "page": "7",
    "book": "The Magic Lamp",
    "tags": [
      "Goal Setting"
    ],
    "description": "What would I really want from life if I were absolutely positively certain I would get it?",
    "comments": "What do I want now? 1. A lovely girlfriend. 2. A job.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:20:10.597Z"
  },
  {
    "id": 1744217000253,
    "title": "Achievements Are a By-Product of Enjoyment",
    "page": "16",
    "book": "The Magic Lamp",
    "tags": [
      "Achievement",
      "Enjoyment"
    ],
    "description": "That's what river people do. They aren't making a huge sacrifice to follow their dreams. They don't have to practice iron-willed self-discipline to keep themselves on track. They simply do what they enjoy doing. That's their payoff. That's why they do it. Their achievements are simply a by-product of that enjoyment.",
    "comments": "Most skilled people do things because they like them. Similar with you and drawing",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:22:40.340Z"
  },
  {
    "id": 1744217000254,
    "title": "Never Miss a Day of a New Habit",
    "page": "62",
    "book": "The Magic Lamp",
    "tags": [
      "Habits"
    ],
    "description": "never miss a day of a new habit.",
    "comments": "New habits need time to be established. If you neglect them, they'll die out as your old habits will take over",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:47:43.053Z"
  },
  {
    "id": 1744217000255,
    "title": "Expect the Discomfort of Change",
    "page": "68",
    "book": "The Magic Lamp",
    "tags": [
      "Change",
      "Discomfort",
      "Growth"
    ],
    "description": "Learn to expect the discomfort of change and to embrace it as proof that you're still alive, still vigorous, still growing. The moment you stop changing, you stop growing. The moment you stop growing, you stop living. Cultivate change; accept discomfort; insist on growth. When you do, your comfort zone will expand to make your wishes come true.",
    "comments": "Embrace change, embrace pain. These words are synonymous. Growth = Pain = Change = Discomfort. If you're not growing, you're not living. You're living in complacency. If you're not living, you're dying. If you're not growing, you're dying",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T19:50:01.294Z"
  },
  {
    "id": 1744217000256,
    "title": "Ordinary Effort bayser Time Yields Extraordinary Results",
    "page": "74",
    "book": "The Magic Lamp",
    "tags": [
      "Consistency",
      "Routine",
      "Habits",
      "Time",
      "Change"
    ],
    "description": "This is the single most important idea in The Magic Lamp, the single most useful piece of advice I can give you to help you make your wishes come true. It is so important that I'm going to say it again: Even ordinary effort over time yields extraordinary results. ... you will multiply a hundredfold your chances for success because you will enlist in your cause the most irresistible force in the universe: time.",
    "comments": "The tortoise wins the race. Time can be anything. All you have to do is give it the time, and anything is yours.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:00:42.984Z"
  },
  {
    "id": 1744217000257,
    "title": "Earn-->Learn Struggle Forces Us to Exceed Limits And Push Boundaries",
    "page": "138",
    "book": "The Magic Lamp",
    "tags": [
      "Learning",
      "Growth",
      "Struggle"
    ],
    "description": "In real life, we have to earn what we learn. In the process of learning, we become better people. We become more acccomplished people. We become more capable people, because the more we have accomplished, the more we can accomplish. Scientists call this a positive feedback loop. The rest of us call it growth. And growth is the payoff from struggle. Struggle makes us stronger. Struggle makes us better. Struggle makes us who we are. Without struggle, we would never be forced to exceed our limits, to stretch ourselves, to achieve our potential. We would never be forced to search for the best within ourselves--and find it. Without struggle, we would never become the kind of people who can make our wishes come true.",
    "comments": "Struggling is probably the foundation of everything you have. It's how we find our potential.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:10:16.706Z"
  },
  {
    "id": 1744217000258,
    "title": "2 Questions About Believing",
    "page": "147",
    "book": "The Magic Lamp",
    "tags": [
      "Persistence",
      "Belief"
    ],
    "description": "Whenever you find yourself tempted to give up on a wish, ask yourself these questions: 1. Do I believe I can make this wish come true? 2. Do I believe this wish is worth the effort? If either answer is no, then you need to work on your belief before you can effectively work on your wish. Belief causes persistence. Persistence causes success.",
    "comments": "You have to belief you can do it. You have to believe it's worth the time. If you don't, what's the point? Find that belief.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-06T20:16:18.259Z"
  },
  {
    "id": 1744217000259,
    "title": "The Difference Between Having a Dream and Making That Dream Come True",
    "page": "171",
    "book": "The Magic Lamp",
    "tags": [
      "Action"
    ],
    "description": "The difference between being asleep and being awake is the difference between having a dream and making that dream come true. That is what happens when you're awake. That is the kind of gift you can give yourself when you know your own strength. That is the kind of life you can lead when you understand your power to choose, and choose to use it.",
    "comments": "Make your dreams a reality",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:23:50.316Z"
  },
  {
    "id": 1744217000260,
    "title": "By Contrast, Deliberate Practice Requires",
    "page": "68",
    "book": "Talent Is Overrated",
    "tags": [
      "Performance",
      "Improvement"
    ],
    "description": "By contrast deliberate practice requires that one identify certain sharply defined elements of performance that need to be improved, and then work intently on them. Examples are everywhere. The great soprano Joan Sutherland devoted countless hours to practicing her trill--and not just the basic trill, but the many different types (wholetone, semitone, baroque). Tiger Woods has been seen to drop golf balls into a Santa track and step on them, then practice shots the near impossible lie. The great performers isolate remarkably specific aspects of what they do and focus on just those things until they are improved; then it's on to the next aspect.",
    "comments": "specifics make up the whole.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:30:59.542Z"
  },
  {
    "id": 1744217000261,
    "title": "Learning Zone",
    "page": "69",
    "book": "Talent Is Overrated",
    "tags": [
      "Learning",
      "Discomfort"
    ],
    "description": "He labels the inner circle \"comfort zone,\" the middle one \"learning zone,\" and the outer one \"panic zone.\" Only by choosing activities in the learning zone can one make progress. That's the location of skills and abilities that are just out of reach. We can never make progress in the comfort zone because those are the activities we can already do easily, while panic-zone activities are so hard that we don't even know how to approach them. Identifying the learning zone, which is not simple, and then forcing oneself to stay continually in it as it changes, which is even harder--these are the first and most important characteristics of deliberate practice.",
    "comments": "You can't grow in the comfort zone.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:32:44.328Z"
  },
  {
    "id": 1744217000262,
    "title": "Domain Specific Knowledge ... 10-100x More",
    "page": "95",
    "book": "Talent Is Overrated",
    "tags": [
      "Knowledge"
    ],
    "description": "Yet in the light of staggering advances, why would the computer lose or draw even a single game against any player, ever? The answer is that the human possessed something the computer didn't, which was vast knowledge of chess--how previous masters had responded to particular positions in many different cases, and what kinds of choices generally produced what kinds of consequences. Eventually researchers from a broad array of fields realized where the secret lay. \"The most important ingredient in any expert system is knowledge,\" wrote three eminent scientists who work on expert computer systems (Bruce G. Buchanan, Randall Davis, and Edward A. Feigenbaum). \"Programs that are rich in general inference methods--some of which may even have some of the power of mathematical logic--but poor in domain-specific knowledge can behave expertly on almost no tasks.\" Their conclusion: \"In the knowledge resides the power.\" ... Part of the answer, which seems to apply in every domain, is that they had more knowledge about their field. In chess, researchers have found (using a method I'll describe a little later) that master-level players possess more chess knowledge than good club-level players by a huge margin, a factor of ten to one hundred. Just as important, top performers in a wide range of fields have better organized and consolidated their knowledge, enabling them to approach problems in fundamentally different and more useful ways.",
    "comments": "Knowledge is what defines the experts the best.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:40:38.987Z"
  },
  {
    "id": 1744217000263,
    "title": "Expert Knowledge/Memory/Retrieval Structure",
    "page": "101",
    "book": "Talent Is Overrated",
    "tags": [
      "Knowledge",
      "Memory"
    ],
    "description": "Researchers estimate that good club players have a \"vocabulary\" of about 1,000 chunks, while the highest-ranked players have a vocabulary of 10,000 chunks. ... But now think of those chess players who play ten simultaneous games blindfolded. They can't be holding all those chessboards in short-term memory because if they were, each time they turned to the next board they'd forget the one they were just thinking about. ... All these people have developed what we might call a memory skill, a special ability to get at long-term memory, with its vast capacity, in a fast, reliable way. They aren't using short-term memory or traditionally defined long-term memory. ... Other researchers have called it expert working memory. To understand its critical element, remember the story of SF, the yelling runner who was able to recall extraordinarily long lists of random digits. He did it by relating the digits to numbers in forms that were meaningful to him; for example, he recalled the digits 4 1 3 1 in the form 4:13.1, a time for running the mile. He had created what's called a retrieval structure, a way of connecting the data to concepts already possessed.... Indeed, top performers' deep understanding of their field becomes the structure on which they can hang the huge quantities of information they learn about it.",
    "comments": "Hazelnut had memory retrieval structures too. I memorized all 18 holes for the -41 (people have asked), and also \"benchmarks\" for tournaments",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-03-17T16:27:47.926Z"
  },
  {
    "id": 1744217000264,
    "title": "Hardest Experiences Most Helpful",
    "page": "129",
    "book": "Talent Is Overrated",
    "tags": [
      "Hardship",
      "Learning",
      "Growth"
    ],
    "description": "Executives consistently report that their hardest experiences, the stretches that most challenged them, were the most helpful. A. G. Lafley, CEO of Procter & Gamble, was in charge of the company's Asian operations during a major Japanese earthquake and the Asian economic collapse. He says that's when he discovered that \"you learn ten times more in a crisis than during normal times.\" His crisis experiences happened by chance, but while crises can't be engineered, crisis experiences can be.",
    "comments": "The most difficult moments is where you learn the most. Get out there and grow yourself. Talk to women you like.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T16:54:14.997Z"
  },
  {
    "id": 1744217000265,
    "title": "Deliberate Practice Maintains Through Age",
    "page": "182",
    "book": "Talent Is Overrated",
    "tags": [
      "Knowledge",
      "Memory",
      "Practice",
      "Discipline",
      "Age"
    ],
    "description": "In a study of excellent chess players, the older ones chose moves just as well as the younger ones, but they did it in a different way. They didn't consider as many possible moves because they couldn't, but they compensated through greater knowledge of positions. More generally, continued deliberate practice enables top performers to maintain skills that would otherwise decline with age, and to develop other skills and strategies to compensate for declines that can no longer be avoided. That approach can work for a long time....Julio Franco played for the Atlanta Braves in the 2007 season at age forty-nine, thanks to a regimen of intense exercise and carefully designed diet that's unlike anything that was used in baseball decades ago. His trainer told the New York Times, \"When I got acquainted with him, I learned quickly that you can't associate him with people of his age. His discipline is unlike anything I've ever seen.\"",
    "comments": "You can train your brain to be so strong that age won't affect your ability. Reinforce the knowledge and memory you want to continue and it will be there",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:06:19.210Z"
  },
  {
    "id": 1744217000266,
    "title": "What We Can Change, and What We Can't",
    "page": "9",
    "book": "The Daily Stoic",
    "tags": [
      "Change"
    ],
    "description": "The single most important pracitce in Stoic philosophy is differentiating between what we can change and what we can't. What we have influence over and what we do not. A fliight is delyaed because of weather--no amount of yelling at an airline representative will end a storm. No amount of withing will make you taller or shorter or born in a different country. No matter how hard you try, you can't make someone like you. And on top of that, time spent hurling yourself at these immovable objects is time not spent the things we can change.",
    "comments": "January 1",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T17:56:37.759Z"
  },
  {
    "id": 1744217000267,
    "title": "Where, Who, What, and Why. Who Are You?",
    "page": "14",
    "book": "The Daily Stoic",
    "tags": [
      "Purpose"
    ],
    "description": "But, gun to their head, most people couldn't give much in the way of a substantive answer. Could you? Have you taken the time to get clarity about who you are and what you stand for? Or are you too busy chasing unimportant things, mimicking the wrong influences, and following disappointing or unfulfilling or nonexisent paths?",
    "comments": "January 6. What are you doing? What is your purpose? Is it to jerk off and die? Is it to play video games you don't like with people you don't like? Is it to become the best man you can be?",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:06:25.186Z"
  },
  {
    "id": 1744217000268,
    "title": "Anger Is Bad Fuel. Anger Never Solves Anything",
    "page": "50",
    "book": "The Daily Stoic",
    "tags": [
      "Anger"
    ],
    "description": "As the Stoics have said many times, getting angry almost never solves anything. Usually, it makes things worse. We get upset, then the other person gets upset--now everyone is upset, and the problem is no closer to getting solved.",
    "comments": "February 10. Anger makes things worse. Frustration is not helpful for solving problems. Anger is contagious.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:34:06.322Z"
  },
  {
    "id": 1744217000269,
    "title": "The Banquet of Life. Wanting Things to Happen",
    "page": "59",
    "book": "The Daily Stoic",
    "tags": [
      "Desire",
      "Patience"
    ],
    "description": "\"Remember to conduct yourself in life as if at a banquet. As something being passsed around comes to you, reach out your hand and take a moderate helping. Does it pass you by? Don't stop it. It hasn't yet come? Don't burn in desire for it, but wait until it arrives in front of you. Act this way with children, a spouse, toward position, with wealth--one day it will make you worthy of a banquet with the gods.\" The next time you see something you want, remember Epictetus's metaphor of life's banquet. As you find yousrelf getting excited, ready to do anything and everything to get it--the equivalent of reaching across the table and grabbing a dish out of someone's hands--just remind yourself: that's bad manners and unneccessary. Then wait patiently for your turn.",
    "comments": "February 19. You can't force everything. Things will come after you set in motion the cause. The effect comes later. You can't grab a girlfriend or a job. They come to you once you've waited and developed yourself.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T18:43:47.414Z"
  },
  {
    "id": 1744217000270,
    "title": "Stay Focused on the Present. One Thing at a Time",
    "page": "185",
    "book": "The Daily Stoic",
    "tags": [
      "Thinking",
      "Focus",
      "Present"
    ],
    "description": "When you look back at some of the most impressive, even scary, things that you've done or endured, how were they possible? How were you able to see past the danger or the poor odds? As Marcus described, you were too busy with the details to let the whole sweep of the situation crush you. In fact, you probably didn't even think about it at the time. ... A lot of times, though, it's counterproductive and overwhelming to be thinking of everything that lies ahead. So by focusing exclusively on the present, we're able to avoid or remove those intimidating or negative thoughts from our frame of view.",
    "comments": "June 19. Focus on the present. Don't get riled up on anxiety. Don't focus on the hour, focus on the second. It keeps you from being intimidated by anxieties",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T19:56:33.101Z"
  },
  {
    "id": 1744217000271,
    "title": "The Obstacle Is the Way",
    "page": "196",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Growth"
    ],
    "description": "\"While its true that someone can impede our actions, they can't impede our intentions and our attitudes, which have the power of being conditional and adaptable. For the mind adapts and converts any obstacle to its action into a means of achieving it. That which is an impediment to action is turned to advance action. The obstacle on the path becomes the way. Today, things will happen that will be contrary to your plans. If not today, then certainly tomorrow. As a result of these obstacles, you will not be able to do what you planned. This is not as bad is it seems, because your mind is infinitely elastic and adaptable. You have the power to use the Stoic exercise of turning obstacles upside down, which takes on negative circumstance and uses it as an opportunity to practice an unintended virtue or form of excellence. If something prevents you from getting to your destination on time, then this is a chance to practice patience. Try this line of thinking and see whether there is a situation in which one could not find some virtue to practice or derive some benefit. There isn't one. Every impediment can advance action in some form or another.",
    "comments": "June 30. Obstacles are growth. They are the milestones to reach. Cowering to them is to cower to life.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:00:33.074Z"
  },
  {
    "id": 1744217000272,
    "title": "Rise and Shine",
    "page": "203",
    "book": "The Daily Stoic",
    "tags": [
      "Motivation",
      "Purpose"
    ],
    "description": "On those mornings you struggle with getting up, keep this thought in mind--I am awakening to the work of a human being. Why then am I annoyed that I am going to do what I'm made for, the very things for which I was put into this world? Or was I made tor this, to snuggle under the covers and keep warm? It's so pleasurable. Were you then made for pleasure? In short, to be coddled or to exert yourself? ... But we can't. Because we have a job to do. Not only do we have the calling we've dedicated ourselves to, but we have the larger cause that the Stoics speak about: the greater good. We cannot be of service to ourselves, to other people, or to the world unless we get up and get working--the earlier the better. So come on. Get going.",
    "comments": "July 6. You wake up every day to become better. Think of all of those days where you didn't improve at all. What a waste. You consume food so you can improve yourself, not sleep in and jerk off.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:28:26.328Z"
  },
  {
    "id": 1744217000273,
    "title": "There Is Something Better: Real Virtue",
    "page": "224",
    "book": "The Daily Stoic",
    "tags": [
      "Virtue"
    ],
    "description": "We've all chased things we thought would matter. At some point, we all thought that money would be the answer, that success was the highest prize, that the undying love of a beautiful person would finally make us feel warm inside. What do we find when we actually attain these sacred objects? Not that they are empty or meaningless--only those who have never had them think that--but what we find is that they are not enough. Money creates problems, Climbing one mountain exposes another, higher peak. There is never enough love. There is something better out there: real virtue. It is its own reward. Virtue is the one good that reveals itself to be more than we expect and something that one cannot have in degrees. We simply have it or we don't. And that is why virtue--made up as it is of justice, honesty, discipline, and courage-- is the only thing worth striving for.",
    "comments": "July 27. Virtue is becoming a good man, and practicing being that man.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:14:43.124Z"
  },
  {
    "id": 1744217000274,
    "title": "A Garden is Not for Show",
    "page": "277",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Virtue"
    ],
    "description": "After all you've read, it might be tempting to think: This stuff is great, I get it, I'm a Stoic. But it's not that easy. Just because you agree with the philosophy doesn't mean the roots have fully taken hold in your mind. Fooling with books so you can sound smart or have an intimidating library is like tending to a garden to impress your neighbors. Growing one to feed your family? That's a pure and profitable use of your time. The seeds of Stoicism are long underground. Do the work required to nurture and tend to them. So that they--and you--are prepared and sturdy for the hard winters of life.",
    "comments": "September 15. Words mean nothing. Displays of books mean nothing. Action and being is the root of living. Actions speak louder than words. Be virtuous, don't say and boast about being virtuous. That is the greatest sin. Pride.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T20:35:16.793Z"
  },
  {
    "id": 1744217000275,
    "title": "Revenge Is a Dish Best Not Served",
    "page": "306",
    "book": "The Daily Stoic",
    "tags": [
      "Anger",
      "Revenge"
    ],
    "description": "\"The best way to avenge yourself is to not be like that.\" \"How much better to heal than seek revenge from injury. Vengeance wastes a lot of time and exposes you to many more injuries than the first that sparked it. Anger always outlasts hurt. Best to take the opposite course. Would anyone think it normal to return a kick to a mule or a bite to a dog?\" Let's say someone has treated you rudely. Let's say someone got promoted ahead of you because they took credit for your work or did something dishonest. It's natural to think: Oh, that's how the world works, or One day it will be my turn to be like that. Or most common: I'll get them for this. Except these are the worst possible responses to bad behaviour. As Marcus and Seneca both wrote, the proper response--indeed the best revenge--is to exact no revenge at all. If someone treats you rudely and you respond with rudeness, you have not done anything but prove to them that they were justified in their actions. If you meet other people's dishonesty with dishonesty of your own, guess what? You're proving them right--now everyone's a liar. Instead, today, let's seek to be better than the things that disappoint or hurt us. Let's try to be the example we'd like others to follow. It's awful to be a cheat, to be selfish, to feel the need to inflict pain on our fellow human beings. Meanwhile, living morally and well is quite nice.",
    "comments": "October 13. Revenge gets you nowhere, and often starts a fight, that otherwise could have ended. And usually revenge leads to more injury. By responding to dishonesty, you are justifying the actions of the dishonest person by being dishonest yourself.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:13:15.227Z"
  },
  {
    "id": 1744217000276,
    "title": "Give People the Benefit of the Doubt",
    "page": "308",
    "book": "The Daily Stoic",
    "tags": [
      "Judgement",
      "Virtue"
    ],
    "description": "\"Even a dog,\" Supreme Court Justice Oolver Wendell Holmes once said, \"distinguishes between being stumbled over and being kicked.\" Yet if you've ever accidentally stepped on your dog, you know that the first reactionis usually a bark or a yelp or a quick snap of the jaws. In the instant, there is no distinction--just pain. Then it sees who it was, hears your soothing voice, and goes right back to wagging its tail. A virtuous person does not jump to hasty judgments about other people. A virtuous person is generous with assumptions: that something was an accident, that someone didn't know, that it won't happen again This makes life easier to bear and makes us more tolerant. Meanwhile, assusming malice--the most hasty of judgments--makes everything harder to bear. Be deliberate and accomdating with your assumptions about other people and you'll find, as Marcus says, calmer seas and fairer weather.",
    "comments": "October 15. Assuming malice is something I find myself guilty of too much. Virtuous people are generous with assumptions. They recognize that other people are not all out to get them. Oftentimes, it is accidental, unintentional, made up in your head, and would undo it if they knew they \"supposedly\" caused you mental harm. Assuming malice is a hasty judgement. So what if someone did something bad anyway? The response isn't to get angry. It's to remain virtuous",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:18:32.822Z"
  },
  {
    "id": 1744217000277,
    "title": "Good Habits Drive Out Bad Habits",
    "page": "312",
    "book": "The Daily Stoic",
    "tags": [
      "Habits"
    ],
    "description": "The same goes for us. When a bad habit reveals itself, counteract it with a commitment to a contrary virtue. For instance, let's say you find yourself procrastinating today--don't dig in and fight it. Get up and take a walk to clear your head and reset instead. If you find yourself saying something negative or nasty, don't kick yourself. Add something positive and nice to qualify the remark. Oppose established habits, and use the counterforce of training to get traction and make progress. If you find yourself cutting corners during a workout or on a project, say to yourself: \"OK, now I am going to go even further or do even better.\" Good habits have the power to drive out bad habits. And habits are easy to pick up--as we all know.",
    "comments": "October 19. Find the virtue you want to practice when you find yourself doing something you shouldn't be doing. That ought to steer you back in the right direction. Because there is one.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:21:34.409Z"
  },
  {
    "id": 1744217000278,
    "title": "Train to Let Go of What's Not Yours",
    "page": "349",
    "book": "The Daily Stoic",
    "tags": [
      "Attachment",
      "Change",
      "Loss",
      "Time"
    ],
    "description": "\"Whenever you experience the pangs of losing something, don't treat it like a part of yourself but as a breakable glass, so when it falls you will remember that and won't be troubled. So too, whenever you kiss your child, sibling, or friend, don't layer on top of the experience all the things you might wish, but hold them back and stop them, just as those who ride behind triumphant generals remind them they are mortal. In the same way, remind yourself that your precious one isn't one of your possessions, but something given for now, not forever...\" ... In our own lives, we can train to be that whisper. When there is something we prize--or someone that we love--we can whisper to ourselves that it is fragile, mortal, and not truly ours. No matter how strong or invincible something feels, it never is. We must remind ourselves that it can break, can die, can leave us. Loss is one of our deepest fears. Ignorance and pretending don't make things any better. They just mean the loss will be all the more jarring when it occurs.",
    "comments": "November 24. You can hold things sacred to you, but you must remember that nothing lasts forever. Everything is temporary. You don't possess Penny, or Hazel. They are their own and change over time.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T16:47:42.804Z"
  },
  {
    "id": 1744217000279,
    "title": "You Can't Learn If You Think You Already Know",
    "page": "41",
    "book": "Ego Is The Enemy",
    "tags": [
      "Learning",
      "Humility",
      "Mindset",
      "Knowledge"
    ],
    "description": "It tends to surprise people how humble aspiring greats seem to have been. What do you mean they weren't aggressive, entitled, aware of their own greatness or their destiny? The reality is that, though they were confident, the act of being an eternal student kept these men and women humble. \"It is impossible to learn that which one thinks one already knows,\" Epictetus says, You can't learn if you think you already know. You will not find the answers if you're too conceited and self-assured to ask the questions. You cannot get better if you're convinced you are the best.",
    "comments": "Hazelnut peaked when I thought I was the best. There is always room for improvement. Ohtani will always try to improve. No matter how good you are, you can get better. This mindset is the best because it encourages striving to do well, instead of maintaining the status quo. Change is inevitable.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:25:20.589Z"
  },
  {
    "id": 1744217000280,
    "title": "Restraint Is a Tough Skill to Learn",
    "page": "64",
    "book": "Ego Is The Enemy",
    "tags": [
      "Distraction",
      "Temptation",
      "Endurance",
      "Resistance"
    ],
    "description": "Instead, you must do nothing. Take it. Eat it until you're sick. Endure it. Quietly brush it off and work harder. Play the game. Ignore the noise; for the love of God, do not let it distract you. Restraint is a difficult skill but critical one. You will often be tempted, you will probably even be overcome. No one is perfect with it, but try we must.",
    "comments": "Try, just try. Don't give up. You're on this planet for that very purpose. You are meant to overcome challenges. Temptations like jerking off, thoughts about sex, thoughts about playing Catan, thoughts about blacks and muslims. Resist. Your life depends on it",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:52:00.481Z"
  },
  {
    "id": 1744217000281,
    "title": "Keep Your Identity Small",
    "page": "112",
    "book": "Ego Is The Enemy",
    "tags": [
      "Identity",
      "Ego",
      "Complacency",
      "Hard Work",
      "Persistence"
    ],
    "description": "\"Keep your identity small,\" fits well here. Make it about the work and the principles behind it--not about a glorious vision that makes a good headline. ... There's a real danger in believing it when people use the word \"genius\"--and it's even more dangerous when we let hubris tell ourselves we are one. The same goes for any label that comes along with a career... These labels put you at odds not just with reality, but with the real strategy that made you successful in the first place. From that place, we might think that success in the future is just the natural next part of the story--when really it's rooted in work, creativity, persistence, and luck.... instead of hard work and sincere hustle--will eventually find themselves at the bottom of a bottle or on the wrong end of a needle. The same goes for us, whatever we do. Instead of pretending that we are living some great story, we must remain focused on the execution--and on executing with excellence. We must shun the false crown and continue working on what got us here. Because that's the only thing that will keep us here.",
    "comments": "You get to the top by working hard, and persisting. You are not there because your name is Hazelnut. If you want to remain at the top, then you have to continue working hard. The number one spot is always up for grabs, and people are hungry for it. They would happily watch you fall. They have ambition on their side. You have tradition. Make that tradition persisting. Don't get complacent.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:10:21.905Z"
  },
  {
    "id": 1744217000282,
    "title": "An Elimination of the Unnecessary and the Destructive",
    "page": "148",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Contempt"
    ],
    "description": "We're not talking about abstinence from drugs or alcohol obviously, but there certainly is an element of restraint to egoless sobriety--an elimination of the unnecessary and the destructive. No more obsessing about your image; treating people beneath you or above you with contempt; needing first-class trappings and the star treatment; raging, fighting, preening, performing, lording over, condescending, and marveling at your own awesomeness or self-anointed importance.",
    "comments": "Ego is destructive. It causes rifts. You've seen it. It destroys worlds. Don't look at pictures of yourself. Are you the guy that would have sex with a mirror? Treat all with kindness. Regardless of so-called status.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:23:09.162Z"
  },
  {
    "id": 1744217000283,
    "title": "Proper Tasks Names. Not Imperative",
    "page": "79",
    "book": "Willpower",
    "tags": [
      "Organization"
    ],
    "description": "As Allen went on to work with his own clients, he preached the importance of the Next Action, or NA as GTDers call it. The to-do list was not supposed to have items like \"Birthday gift for Mom\" or \"Do taxes.\" It had to specify the very next action, like \"Drive to jewelry store\" or \"Call accountant.\"",
    "comments": "Name things properly. You're not a child. Don't name things \"Q\" or \"A1\" or \"Bolt\". Also don't name things \"Ella\" or \"Mavis\". Give them proper names like \"Practice_for_XXX_version_1_June_2024\".",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:32:43.823Z"
  },
  {
    "id": 1744217000284,
    "title": "Strengthen Willpower by Doing Random Tasks",
    "page": "131",
    "book": "Willpower",
    "tags": [
      "Willpower",
      "Endurance"
    ],
    "description": "But other exercises do help, as demonstrated by the groups in the experiment that worked on their posture and recorded everything they ate. When they returned to the lab after two weeks, their scores on the self-control tests went up, and the improvement was significantly higher by comparison with a control group (which did no exercises of any kind during the two weeks). This was a striking result, and with careful analyses of the data, the conclusions, became clearer and stronger. Unexpectedly, the best results came from the group working on their posture. That tiresome old advice--\"Sit up straight!\" --was more useful than anyone had imagined. By overriding their habit of slouching, the students strengthened their willpower and did better at tasks that had nothing to do with posture. The improvement was most pronounced among the students who had followed the advice most diligently (as measured by the daily logs the students kept of how often they'd forced themselves to sit up or stand up straight). The experiment also revealed an important distinction in self-control between two kinds of strength: power and stamina. At the first lab session, participants began by squeezing a spring-loaded handgrip for as long as they could (which had been shown in other experiments to be a good measure of willpower, not just physical strength). Then, after expending mental energy through the classic try-not-to-think-of-a-white-bear task, they did a second hand-grip task to assess how they fared when willpower was depleted. Two weeks later, when they returned to the lab after working on their posture, their scores on the initial handgrip tests didn't show much improvement, meaning that the willpower muscle hadn't gotten more powerful. But they had much more stamina, as evidenced by their improved performance on the subsequent handgrip test administered after the researchers tried to fatigue them. Thanks to the students' posture exercises, their willpower didn't get depleted as quickly as before, so they had more stamina for other tasks.",
    "comments": "This is the (other) willpower train entry. Possibly my favorite entry (the other one is in favourites). The students that worked on their posture most diligently over the course of two weeks came back to the lab, and lasted longer than those who didn't. They expanded their willpower by practicing willpower. It's a snowball effect. If you start the willpower train, it will get faster, not slower.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:36:11.495Z"
  },
  {
    "id": 1744217000285,
    "title": "\"Moral Resistance Was a Favourite Subject With Him\"",
    "page": "146",
    "book": "Willpower",
    "tags": [
      "Will",
      "Resistance",
      "Desire"
    ],
    "description": "\"Moral resistance was a favourite subject with him,\" Stanley wrote of his fantasy father. \"He said the practice of it gave vigour to the will, which required it as much as the muscles. The will required to be strengthened to resist unholy desires and low passions, and was one of the best allies that conscience could have.\" Not surprisingly, this advice from an imaginary parent happened to jibe precisely with Stanley's own regimen for avoiding the vices of his real parents. At age eleven, despite living in what could hardly be called luxurious conditions at the workhouse in Wales, he was already \"experimenting on Will\" by imposing extra hardships on himself",
    "comments": "You can train your resistance like a muscle. Train is so it can resist all desires. Make it so it can ward off sexual fantasies, judgements, sleeping in bed, procrastinating, racist thought, and anything destined to put you off track.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:54:21.544Z"
  },
  {
    "id": 1744217000286,
    "title": "The Page-A-Day Folks",
    "page": "159",
    "book": "Willpower",
    "tags": [
      "Self-Control",
      "Habits"
    ],
    "description": "When Boice followed up on the group [of university professors] some years later, he found that their paths had diverged sharply. The page-a-day folks had done well and generally gotten tenure. The so-called \"binge writers\" fared far less well, and many had had their careers cut short. The clear implication was that the best advice for young writers and aspiring professors is: Write every day. Use your self-control to form a daily habit, and you'll produce more with less effort in the long run.",
    "comments": "Be the tortoise. Don't break the streak. Commit everyday. It's the best path to success and overall productivity. Get the reps in.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:41:26.689Z"
  },
  {
    "id": 1744217000287,
    "title": "Rules for Babies and Vampires",
    "page": "202",
    "book": "Willpower",
    "tags": [
      "Parenting",
      "Self-Control",
      "Learning"
    ],
    "description": "Long before children can read rules or do chores, they can start learning self-control. Ask any parent who has survived the ordeal of Ferberization, which is based on a technique found in a Victorian child-rearing manual. It requires the parents, against all instinct, to ignore their infants' cries when they're left alone at bedtime. Instead of rushing to the infant's side, the parents let the infant cry for a fixed interval of time, then go offer some comfort, then withdraw for another fixed interval. The process is repeated until the child learns to control the crying and go to sleep without any help from the parents. It requires great self-control by the parents to ignore the heart-rending screams, but the infant usually learns quickly to put themselves to sleep without any crying. Once an infant acquires self-control, everybody wins: The infant is no longer anxious at bedtime or when he or she wakes up alone in the middle of the night, and the parents don't have to spend their nights hovering by the crib. We've seen parents successfully use a variant of this approach when an infant cries to be fed. Instead of immediately feeding the crying child, the mother lets the child know that the signal has been received but then waits for him or her to quiet down before offering the breast or the botte. Again, it's hard to ignore the cries at first, and we realize that to some parents it sounds too cruel to even try. But once a child learns to ask for food without going into a crying frenzy, both child and parent end up calmer and happier. The children are learning that they have some power over themselves, that certain kinds of behaviour are expected, and that actions have consequences--lessons that will become more and more important as they get older.",
    "comments": "Let the baby cry for 15 minutes, then tend to it. Second, delay when you help the baby. Let the baby know it's cries have been heard, but once again attend to it in 15 minutes. That way it can not cry forever. You can always add these descriptions to ChatGPT to distill the content.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:22:17.912Z"
  },
  {
    "id": 1744217000288,
    "title": "It's Just a Number",
    "page": "369",
    "book": "The Daily Stoic",
    "tags": [
      "Time",
      "Age"
    ],
    "description": "The number of years we manage to eke out doesn't matter, only what those years are composed of. Seneca put it best when he said, \"Life is long if you know how to use it.\" Sadly, most people don't--they waste the life they've been given. Only when it is too late do they try to compensate for that waste by vainly hoping to put more time on the clock. Use today. Use every day. Make yourself satisfied with what you have been given.",
    "comments": "December 13. You have to live before you die. I wanna live before we die. Don't you want to live before you die? Let me see you live before you die! Life isn't sitting around. It's working. It's pushing yourself. It's not about reclining in your chair and stroking your cock.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T16:54:44.275Z"
  },
  {
    "id": 1744217000289,
    "title": "Get Active in Your Own Rescue",
    "page": "387",
    "book": "The Daily Stoic",
    "tags": [
      "Action",
      "Learning"
    ],
    "description": "\"Stop wandering about! You aren't likely to read your own notebooks, or ancient histories, or the anthologies you've collected to enjoy in your old age. Get busy with life's purpose, toss aside empty hopes, get active in your own rescue--if you care for yourself at all--and do it while you can.\" The purpose of all our reading and studying is to aid us in the pursuit of the good life (and death). At some point, we must put our books aside and take action. So that, as Seneca put it, the \"words become works.\" There is an old saying that a \"scholar made is a soldier spoiled.\" We want to be both scholars and soldiers--soldiers in the good fight. That's what's next for you. Move forward, move onward. Another book isn't the answer. The right choices and decisions are. Who knows how much time you have left, or what awaits us tomorrow?",
    "comments": "December 31. You can only read books for so long before you have to actually put in work. Experience is the best teacher anyway. At some point you must realize that books can't get you all the way to your goals. So start taking action",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:04:51.708Z"
  },
  {
    "id": 1744217000290,
    "title": "Humble, Gracious, Resilient",
    "page": "6",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility",
      "Character",
      "Endurance",
      "Virtue",
      "Ego"
    ],
    "description": "Ego is the enemy every step along the way. In a sense, ego is the enemy of building, of maintaining, and of recovering. When things come fast and easy, this might be fine. But in times of change, of difficulty... And therefore, the three parts that this book is organizing into: Aspire. Success. Failure. ... Humble in our aspirations, Gracious in our success, Resilient in our failures.",
    "comments": "Humble in aspirations, gracious in success, resilient in failures. That is character. That is virtue. Ego is the cancer that tries to take hold and present itself to the world, to your detriment.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:13:43.809Z"
  },
  {
    "id": 1744217000291,
    "title": "Silence Is Strength",
    "page": "26",
    "book": "Ego Is The Enemy",
    "tags": [
      "Strength",
      "Ego"
    ],
    "description": "We seem to think that silence is a sign of weakness. That being ignored is tantamount to death (and for the ego, this is true). So we talk, talk, talk as though our life depends on it. In actuality, silence is strength--particularly early on in any journey.... And that's what is so insidious about talk. Anyone can talk about himself or herself. Even a child knows how to gossip and chatter. Most people are decent at hype and sales. So what is scarce and rare? Silence. The ability to deliberately keep yourself out of the conversation and subsist without its validation. Silence is the respite of the confident and strong.",
    "comments": "The ego wants to speak. The ego wants to be heard. Suppress that and shut your trap. Silence show character. It can speak for itself. Luna does not speak. She has no ego. That's why she's so cool.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:17:11.553Z"
  },
  {
    "id": 1744217000292,
    "title": "Taking Feedback",
    "page": "41",
    "book": "Ego Is The Enemy",
    "tags": [
      "Criticism",
      "Ego"
    ],
    "description": "The art of taking feedback is such a crucial skill in life, particularly harsh and critical feedback. We not only need to take this harsh feedback, but actively solicit it, labor to seek out the negative precisely when our friends and family and brain are telling us that we're doing great. The ego avoids such feedback at all costs, however.",
    "comments": "The ego can't take criticism because it thinks it's perfect. You are not perfect, and you have made mistakes. Criticism is a shortcut for growth if you are able to listen.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:27:39.570Z"
  },
  {
    "id": 1744217000293,
    "title": "Every Time You Sit Down to Work Remind Yourself",
    "page": "83",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ambition",
      "Choice",
      "Temptation",
      "Working"
    ],
    "description": "Every time you sit down to work, remind yourself: I am delaying gratification by doing this. I am passing the marshmallow test. I am earning what my ambition burns for. I am making an investment in myself instead of in my ego. Give yourself a little credit for this choice, but not so much, because you've got to get back to the task at hand: practicing, working, improving.",
    "comments": "My ambition wants me to work. The Devil wants me to succumb to the marshmallow. Who will I reward today? Reward your ambition. It makes you happy at night.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-01-21T17:15:09.206Z"
  },
  {
    "id": 1744217000294,
    "title": "Winning Is Not as Important as You Think",
    "page": "87",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Confidence",
      "Ambition"
    ],
    "description": "We flirt with arrogance and deceit, and in the process grossly overstate the importance of winning at all costs. Everyone is juicing, the ego says to us, you should too. There's no way to beat them without it, we think. Of course, what is truly ambitious is to face life and proceed with quiet confidence in spite of the distractions. Let others grasp at crutches. It will be a lonely fight to be real, to say \"I'm not going to take the edge off.\" To say, \"I am going to be myself, the best version of that self. I am in this for the long game, no matter how brutal it might be.\" To do, not be.",
    "comments": "The long game. Play the long game with quiet confidence and don't fall for any traps. Use the fire inside of you to keep your ambition. You might lose in the short term, but you won't lose the long game. That's how goals are accomplished.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:56:52.854Z"
  },
  {
    "id": 1744217000295,
    "title": "Entitlement Assumes, Control Says",
    "page": "124",
    "book": "Ego Is The Enemy",
    "tags": [
      "Entitlement",
      "Control"
    ],
    "description": "Entitlement assumes: This is mine. I've earned it. At the same time, entitlement nickels and dimes other people because it can't conceive of valuing another person's time as highly as its own.... It overstates our abilities to ourselves, it renders generous judgement of our prospects, and it creates ridiculous expectations. Control says, It all must be done my way--even little things, even inconsequential things. It can become paralyzing perfectionism, or a million pointless battles fought merely for the sake of exerting its say.",
    "comments": "Entitlement is taking yourself off of the pedestal. You will never be a saint. Everyone is equally as important as you. They have lives too. Entitlement overstates your abilities. Entitlement is what creates absurd expectations. You're not the protagonist of the world. You have to try to achieve.",
    "helpfulness": 5,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-04-10T16:15:47.342Z"
  },
  {
    "id": 1744217000296,
    "title": "Responsibility Requires a Readjustment",
    "page": "131",
    "book": "Ego Is The Enemy",
    "tags": [
      "Responsibility",
      "Goal Setting",
      "Purpose",
      "Clarity"
    ],
    "description": "Responsibility requires a readjustment and then increased clarity and purpose. First, setting the top-level goals and priorities of the organization and your life. Then enforcing and observing them. To produce results and only results.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:15:04.844Z"
  },
  {
    "id": 1744217000297,
    "title": "We Know What Decisions We Must Make",
    "page": "152",
    "book": "Ego Is The Enemy",
    "tags": [
      "Decision Making",
      "Humility",
      "Purpose",
      "Calmness"
    ],
    "description": "We do not have to follow in these footsteps. We know what decisions we must make to avoid that ignominious, even pathetic end: protecting our sobriety, eschewing greed and paranoia, staying humble, retaining our sense of purpose, connecting to the larger world around us.",
    "comments": "You have all you need to make the right decisions. Do you not? What's stopping you. Maintain your sense of purpose, return to a calm mind state to regain your focus. Your calm mind maintains a consistent approach to life you must follow. Who else are you going to listen to, the destructive ego, the hedonist, the child?",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2025-01-07T19:45:54.699Z"
  },
  {
    "id": 1744217000298,
    "title": "Absorbing the Negative Feedback",
    "page": "166",
    "book": "Ego Is The Enemy",
    "tags": [
      "Criticism",
      "Failure",
      "Ego"
    ],
    "description": "Absorbing the negative feedback, ego says: I knew you couldn't do it. Why did you ever try? It claims: This isn't worth it. This isn't fair. This is somebody else's problem. Why don't you come up with a good excuse and wash your hands of that? It tells us we shouldn't have to put up with this. It tells us that we're not the problem.",
    "comments": "The world doesn't collapse when you fail. Your ego acts like it does. Don't listen to it. Learn from the situation. There's always something to learn. It's meant to help you.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:32:42.137Z"
  },
  {
    "id": 1744217000299,
    "title": "You Will Be Unappreciated. You Will Experience Failures",
    "page": "180",
    "book": "Ego Is The Enemy",
    "tags": [
      "Failure",
      "Success"
    ],
    "description": "You will be unappreciated. You will be sabotaged. You will experience surprising failures. Your expectations will not be met. You will lose. You will fail. How do you carry on then? How do you take pride in yourself and your work? John Wooden's advice to his players says it: Change the definition of success. \"Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to do your best to become the best that you are capable of becoming.\" \"Ambition,\" Marcus Aurelius reminded himself, \"means tying your well-being to what other people say or do... Sanity means tying it to your own actions.\" Do your work. Do it well. Then \"let go and let God.\" That's all there needs to be. Recognition and awards--those are just extra. Rejection, that's on them, not on us. ... Author commits suicide after being rejected, only to win a Pulitzer prize afterwards... This is why we can't let externals determine whether something was worth it or not. It's on us.",
    "comments": "Success is knowing you made the effort to become the best that you are capable of being. Don't tie your well being to praise. Tie your well being to your own actions. You don't need recognition for your well being.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:54:54.915Z"
  },
  {
    "id": 1744217000300,
    "title": "Glucose Deprived Anger. Glucose = Willpower",
    "page": "48",
    "book": "Willpower",
    "tags": [
      "Anger",
      "Willpower",
      "Frustration"
    ],
    "description": "The effects of the drinks [lemonade] showed up clearly in a study of aggression among people playing a computer game. At first, the game seemed reasonable, but it soon became impossibly difficult. Everyone got frustrated as the game went on, but the one who got a sugar-filled drink managed to grumble quietly and keep playing. The others started cursing aloud and banging the computer. And when by prearranged script the experimenter made an insulting remark about their performance, the glucose-deprived people were much more likely to get angry. No glucose, no willpower: The pattern showed up time and again as researchers tested more people in more situations.",
    "comments": "You're more likely to become frustrated without willpower. Get enough to eat in the morning. Going monk mode can only get you so far without food. You need food to increase your overall willpower.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:34:36.704Z"
  },
  {
    "id": 1744217000301,
    "title": "Usually Though the Problem Is Within",
    "page": "56",
    "book": "Willpower",
    "tags": [
      "Emotion",
      "Willpower",
      "Impulse"
    ],
    "description": "We all succumb to frustration and anger. We all sometimes feel beset by insoluble problems and overcome by impulses that seem alien, if not satanic. Usually, though, the problem is within. It's not that the world has suddenly turned cruel. It's not that Lucifer is tormenting us with dark new temptations and impulses. It's that we're less capable of dealing with ordinary impulses and long-standing problems. The provocations can be real enough--you may well have reason to get angry at your boss or reconsider your marriage. But you won't make much progress on those other problems until you control your own emotions, and that starts with controlling your glucose.",
    "comments": "The world doesn't get harder. Your willpower depletes and you have less of it to handle whatever Lucifer throws at you. It doesn't become more challenging as the day goes on, you become weaker. To grow stronger, you need glucose.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:30:03.086Z"
  },
  {
    "id": 1744217000302,
    "title": "Zeigarnik Effect. Make a Plan",
    "page": "83",
    "book": "Willpower",
    "tags": [
      "Planning",
      "Focus"
    ],
    "description": "Once again, making a plan made a difference. Those who'd written about unfulfilled tasks had more trouble keeping their minds focused on the novel--unless they'd made a specific plan to complete the task, in which case they reported relatively little mind wandering and scored quite well on the reading comprehension test. Even though they hadn't finished the task or made any palpable progress, the simple act of making a plan had cleared their minds and eliminated the Zeigarnik effect. But the Zeigarnik effect remained for the students without a plan. Their thoughts wandered from the novel to their undone tasks, and afterward they scored worse on the comprehension test.",
    "comments": "If you leave tasks unfinished, your mind will think about them and not on more important tasks at hand. All you need to do to prevent this is to make a plan to do it. Make plans for things so you can focus",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:37:46.145Z"
  },
  {
    "id": 1744217000303,
    "title": "Decision Fatigue",
    "page": "92",
    "book": "Willpower",
    "tags": [
      "Temptation",
      "Willpower"
    ],
    "description": "But in addition to being given practice materials for the test, they were left in a room with magazines and handheld video games as tempting distractions. Again and again, the [previous] decision making took a toll on the students. Compared with the nondeciders, who'd spent just as much time evaluating the same kind of information without making choices, the deciders gave up sooner on the puzzles. Instead of using their time to practice for the math test, they goofed off by reading magazines and playing video games.",
    "comments": "This demonstrates that willpower gets depleted. Exerting brainpower on tasks earlier in the day affects your willpower. It makes temptation harder.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:39:57.447Z"
  },
  {
    "id": 1744217000304,
    "title": "Exercising Self-Control in One Area Seemed to...",
    "page": "136",
    "book": "Willpower",
    "tags": [
      "Self-Control",
      "Procrastination",
      "Improvement"
    ],
    "description": "Exercising self-control in one area seemed to improve all areas of life. They smoked fewer cigarettes and drank less alcohol. They kept their homes cleaner. They washed dishes instead of leaving them stacked in the sink, and did their laundry more often. They procrastinated less. They did their work and chores instead of watching television or hanging out with friends first. They ate less junk food, replacing their bad eating habits with healthier ones.",
    "comments": "This is the willpower train. It spreads. Do one thing well, and everything else is done well. It's a mental state you can achieve. The hardest step is the first one, then the willpower train accelerates. Once you do that, you can accomplish everything well, provided that you fuel yourself with enough willpower throughout the day.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:35:37.101Z"
  },
  {
    "id": 1744217000305,
    "title": "Hyperbolic Discounting",
    "page": "184",
    "book": "Willpower",
    "tags": [
      "Temptation"
    ],
    "description": "[Pilgrim's Progress] Suppose that he, too, is journeying toward a Celestial City. While traveling through the countryside, he can see the city's far-off golden spires and keeps heading in their direction. This evening he looks ahead and notices a pub, strategically situated at a bend in the road so that it's directly in front of travelers. From this distance it looks like a small building, and he still keeps his eyes fixed on the grander spires of the Celestial City in the background. But as Eric the Pilgrim approaches the pub, it looms larger, and when he arrives, the building completely blocks his view. He can no longer see the golden spires in the distance. Suddenly the Celestial City seems much less important than this one little building. And thus, verily, our pilgrim's progress endeth with him passed out on the pub's floor. That's the result of hyperbolic discounting: We can ignore temptations when they're not immediately available, but once they're right in front of us we lose perspective and forget our distant goals.",
    "comments": "It's easy to recognize distractions from afar, when you're not affected by it. However, the more territory it consumes in your mind, it gets exponentially harder to avoid it. Once you're 95% there, there's almost nothing that can stop you. The key is to not get more than 10% there. That means not touching your cock, opening the wikipedia article, viewing the video, searching the terms, because those actions get you closer towards defeat.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:36:43.442Z"
  },
  {
    "id": 1744217000306,
    "title": "Hope and Fear Are the Same",
    "page": "341",
    "book": "The Daily Stoic",
    "tags": [
      "Fear",
      "Hope",
      "Control",
      "Desire",
      "Worrying"
    ],
    "description": "\"Hecato says, 'cease to hope and you will cease to fear.' ... The primary cause of both these ills is that instead of adapting ourselves to present circumstances we send out thoughts too far ahead.\" Hope is generally regarded as good. Fear is generally regarded as bad. To a Stoic like Hecato (known as Hecato of Rhodes), they are the same--both are projections into the future about things we do not control. Both are the enemy of this present moment that you are actually in. Both mean you're living a life in opposition to amor fati. It's not about overcoming our fears but understanding that both hope and fear contain a dangerous amount of want and worry in them. And sadly, the want is what causes the worry.",
    "comments": "November 16. Fear and hope are worrying about things without actually doing anything. Both are thoughts about things we do not control. It's almost futile because they accomplish nothing. Instead, understand what you can control and focus on that. Because that is what moves you forward. Not hoping. \"Please, Please, Please!\" is not going to do anything",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:52:42.556Z"
  },
  {
    "id": 1744217000307,
    "title": "The Pleasure of Tuning Out the Negative",
    "page": "352",
    "book": "The Daily Stoic",
    "tags": [
      "Emotion",
      "Will",
      "Negativity"
    ],
    "description": "\"How satisfying it is to dismiss and block out any upsetting or foreign impression, and immediately to have peace in all things.\" ... Pubilius Syrus's epigram expresses it well: \"Always shun that which makes you angry.\" Meaning: turn your mind away from the things that provoke it. If you find that discussing politics at the dinner table leads to figthing, why do you keep bringing it up? If your sibling's life choices bother you, why don't you stop picking at them and making them your concern? The same goes for so many other sources of aggravation. It's not a sign of weakness to shut them out. Instead, it's a sign of strong will. Try saying: \"I know the reaction I typically take in these situations, and I'm not going to do it this time.\" And then follow it with: \"I'm also going to remove this stimulus from my life in the future as well.\" Because what follows is peace and serenity.",
    "comments": "November 27. Why would you ever aggravate yourself over black people and muslims? It does no good. You've learned enough to this point. Peace of mind should be prioritized above all else. It makes life better. You function best with a calm mind",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T16:51:05.555Z"
  },
  {
    "id": 1744217000308,
    "title": "What We Should Know by the End",
    "page": "370",
    "book": "The Daily Stoic",
    "tags": [
      "Character",
      "Virtue"
    ],
    "description": "Hopefully, you have a lot more time left--but that makes it even more important to make headway while you still can. We are unfinished products up until the end, as Marcus knew very well. But the earlier we learn it, the more we can enjoy the fruits of the labor on our character--and the sooner we can be free (or freer) of insincerity, anxiety, ungraciousness, and un-Stoic-ness.",
    "comments": "December 14. Nobody becomes perfect, and that is why you should try your best to get as close as you can. Insincerity, anxiety, ungraciousness are practiced by imperfect trolls. Build a character in life with the opposites of that",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T16:57:46.022Z"
  },
  {
    "id": 1744217000309,
    "title": "Talk, talk, talk. Lao Tzu",
    "page": "23",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility"
    ],
    "description": "Those who know do not speak. Those who speak do not know.",
    "comments": "Show some humility and shut up with your nonsense",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:13:51.651Z"
  },
  {
    "id": 1744217000310,
    "title": "A True Student",
    "page": "40",
    "book": "Ego Is The Enemy",
    "tags": [
      "Learning",
      "Motivation",
      "Ego",
      "Criticism"
    ],
    "description": "A true student is like a sponge. Absorbing what goes on around him, filtering it, latching on to what he can hold. A student is self-critical and self-motivated, always trying to improve his understanding so that he can move on to the next topic, the next challenge. A real student is also his own teacher and his own critic. There is no room for ego there.",
    "comments": "A true student is motivated by himself, and shows himself how he can improve. Ego ruins the balance by removing any kind of reflection. I'm the best, ego says. Google should pay me 500,000 a year. No that's your ego talking.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:25:48.433Z"
  },
  {
    "id": 1744217000311,
    "title": "Too Passionate. Unbridled Enthusiasm",
    "page": "45",
    "book": "Ego Is The Enemy",
    "tags": [
      "Passion",
      "Ego",
      "Motivation"
    ],
    "description": "To be clear, I'm not talking about caring. I'm talking about passion of a different sort--unbridled enthusiasm, our willingness to pounce on what's in front of us with the full measure of our zeal, the \"bundle of energy\" that our teachers and gurus have assured us is our most important asset. It is that burning unquenchable desire to start or to achieve some vague, ambitious, distant goal. This seemingly innocuous motivation is so far from the right track it hurts.",
    "comments": "This is the wrong passion, and the wrong motivation. You've seen this play out before: \"What if Hazelnut came back and became the #1 speed runner?\" \"What if I applied for a trade and made 80,000 a year and had two jobs at once?\" \"What if I became a Catan expert\". These thoughts aren't grounded in reality. It's a fantasy that is years away. Ego is showing you a presentation. Ground yourself and focus on the day in front of you and your current goals.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:31:41.130Z"
  },
  {
    "id": 1744217000312,
    "title": "It's Easy to Be Bitter",
    "page": "56",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Bitterness"
    ],
    "description": "The strategy part of it is the hardest. It's easy to be bitter, like Martial. To hate even the thought of subservience. To despise those who have more means, more experience, or more status than you. To tell yourself that every second not spent doing your work, or working on yourself, is a waste of your gift. To insist, I will not be demeaned like this.",
    "comments": "Bitterness is foul. It consumes your soul. All of the good essence is washed away and taken over by bitterness. It's bad for your well being",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:36:04.287Z"
  },
  {
    "id": 1744217000313,
    "title": "Narcissistic Injury",
    "page": "165",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Perception"
    ],
    "description": "Ego loves this notion, the idea that something is \"fair\" or not. Psychologists call it narcissistic injury when we take personally totally indifferent and objective events. We do that when our sense of self is fragile and dependent on life going our way all the time. Whether what you're going through is your fault or your problem doesn't matter, because it's yours to deal with right now.",
    "comments": "Your ego likes to perceive things as hostile or deliberate acts to keep you down, when it fact it is not the case. You're assuming malice. Crying that things are unfair is similar to a victim complex. It won't be changed for you. Nothing is in your favor until you take action.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:30:28.979Z"
  },
  {
    "id": 1744217000314,
    "title": "It's Transitory. Ego Gripping",
    "page": "193",
    "book": "Ego Is The Enemy",
    "tags": [
      "Failure",
      "Ego"
    ],
    "description": "At any given time in the circle of life, we may be aspiring, succeeding, or failing--though right now we're failing. With wisdom, we understand that these positions are transitory, not statements about your value as a human being. When success begins to slip from your fingers--for whatever reason--the response isn't to grip and claw so hard that you shatter it to pieces. It's to understand that you must work yourself back to the aspirational phase. You must get back to first principles and best practices.",
    "comments": "Everything is transitory. Hazelnut's success waned. Failures don't last forever. They don't define you. As long as you continue pushing, success will eventually come. Success doesn't define you either. It comes and goes just like failure. You can't hold on forever. Just as you can't hold onto anything forever",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T19:03:31.938Z"
  },
  {
    "id": 1744217000315,
    "title": "I Promise You It Didn't Make Him Bitter",
    "page": "205",
    "book": "Ego Is The Enemy",
    "tags": [
      "Bitterness",
      "Revenge",
      "Character"
    ],
    "description": "It took a very long time for Welle's genius in that movie to finally be acknowledged by the rest of the world. No matter, Welles soldier on, making other movies and producing other fantastic art. By all accounts, he lived a fulfilling and happy life. Eventually, Citizen Kane secured its place in the forefront of cinematic history. Seventy years after the movie's debut, it was finally played at Hearst Castle at San Simeon, which is now a state park. The events he endured weren't exactly fair, but at least he didn't let it ruin his life. As Welle's girlfriend of twenty-plus years said in his eulogy, referring not just to Hearst, but to every slight he ever received in his long career in a notoriously ruthless industry, \"I promise you it didn't make him bitter.\" In other words, he never became like Hearst. Not everyone is capable of responding that way.",
    "comments": "The man in the passage didn't let bitterness get to him. And he lived a happy life. The way you respond to any slights says a lot about your character.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:02:19.164Z"
  },
  {
    "id": 1744217000316,
    "title": "But No Less Impressive an Accomplishment",
    "page": "216",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility",
      "Character",
      "Happiness",
      "Thinking",
      "Impulse"
    ],
    "description": "But no less impressive an accomplishment: being better people, being happier people, being balanced people, being content people, being humble and selfless people. Or better yet, all of these traits together. And what is most obvious but most ignored is that perfecting the personal regularly leads to success as a professional, but rarely the other way around. Working to refine our habitual thoughts, working to clamp down on destructive impulses, these are not simply the moral requirements of any decent person. They will make us more successful; they will help us navigate the treacherous waters that ambition will require us to travel. And they are also their own reward.",
    "comments": "Being a better person brings you every reward the planet has to offer except for one thing: hedonism. Keeping a clean mind, practicing humility and great character is the number one goal you should try to accomplish in life.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:08:39.232Z"
  },
  {
    "id": 1744217000317,
    "title": "Self Control Is a Vital Strength & Key to Life",
    "page": "13",
    "book": "Willpower",
    "tags": [
      "Self-Control",
      "Marriage",
      "Success"
    ],
    "description": "The children with tended to wind up poorer financially. They worked in relatively low-paying jobs, had little money in the bank, and were less likely to own a home or have money set aside for retirement. They also grew up to have more children being raised in single-parent households, presumably because they had a harder time adapting to the discipline required for a long-term relationship. The children with good self-control were much more likely to wind up in a stable marriage and raise children in a two-parent home. Last, but certainly not least, the children with poor self-control were likely to end up in prison. Among those with the lowest levels of self-control, more than 40 percent had a criminal conviction by the age of thirty-two, compared with just 12 percent of the people who had been toward the high end of the self-control distribution of their youth. Not surprisingly, some of these differences, were correlated with intelligence and social class and race--but all these results remained significant even when those factors were taken into account. In a follow-up study, the same researchers looked at brothers and sisters from the same families so that they could compare children who grew up in similar homes. Again, over and over, the sibling with the lower self-control during childhood fared worse during adulthood. They ended up sicker, poorer, and were more likely to spend time in prison. The results couldn't be clearer: Self-control is a vital strength and key to success in life.",
    "comments": "Is there a bigger predictor to success than your capacity for self-control? I can't think of any. IQ might be. But those two usually come hand-in-hand. If you control yourself, your life might just change.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:32:50.962Z"
  },
  {
    "id": 1744217000318,
    "title": "You Literally Don't React You Just...",
    "page": "20",
    "book": "Willpower",
    "tags": [
      "Self-Control",
      "Endurance",
      "Perseverance",
      "Emotion"
    ],
    "description": "[a living statue] If someone put money in her tips basket, she would hand the person a flower, but otherwise she remained utterly motionless. Some people would insult her or throw things at her. They tried to make her laugh. They grabbed her. Some yelled at her to get a real job and threatened to steal her money. Drunks tried to pull her off the pedestal or to tip her over. \"it was not pretty,\" Palmer recalls. \"Once I had a frat boy rub his head drunkenly in my crotch as I looked skyward thinking, Good Lord, what have i done to deserve this? But in six years I broke character maybe twice. You literally don't react. You don't even flinch. You just let it pass through you.\"",
    "comments": "Every thought can be avoided. You can avoid anything if you just don't react. Don't react to negativity. Let it pass through you. It doesn't not resonate in my body. It doesn't register. You can be devoid of all thought and emotion if you want to. You may feel a bit coming, but it's the conscious mind's job to not give it the time of day.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-21T19:34:06.243Z"
  },
  {
    "id": 1744217000319,
    "title": "This Guy Is Nuts: David Blaine",
    "page": "124",
    "book": "Willpower",
    "tags": [
      "Willpower",
      "Suffering"
    ],
    "description": "\"The more the body suffers, the more the spirit flowers.\" Blaine works as a self-described endurance artist, performing feats involving willpower instead of illusion. He stood for thirty-five hours more than eighty feet above New York's Bryant Park, without a safety harness, atop a round pillar just twenty-two inches wide. He spent sixty-three sleepless hours in Times Square encased in a giant block of ice. He was entombed in a coffin with six inches of headroom for a week, during which he consumed nothing except water. The list goes on.",
    "comments": "This is the extent of willpower. This man can subjugate himself to anything. You probably couldn't do it for 1 minute. He has mastered his ability to control his mind. If you subject your body to stress, it makes your mind more powerful. So, put your body in stress, so that your mind doesn't lose control over it.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:42:38.670Z"
  },
  {
    "id": 1744217000320,
    "title": "Hot Cold Empathy Gap",
    "page": "148",
    "book": "Willpower",
    "tags": [
      "Self-Control"
    ],
    "description": "Stanley was describing what the economist George Loewenstein calls the \"hot-cold empathy gap\": the inability, during a cool, rational, peaceful moment, to appreciate how we'll behave during the heat of passion and temptation. At home in England, the men may have coolly intended to behave in a virtuous manner, but they couldn't imagine how different their feelings would be in the jungle. The hot-cold empathy gap is still one of the most common challenges to self-control, albeit in less extreme versions.",
    "comments": "It's easy to see yourself behaving properly right after you pledge to not jerk off for an entire week. There is often a lack of understanding of how potent the urge is. Or how tired you'll be, how resistant you'll be to do anything.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T20:56:29.324Z"
  },
  {
    "id": 1744217000321,
    "title": "Precommitment. Make It Impossible",
    "page": "151",
    "book": "Willpower",
    "tags": [
      "Temptation",
      "Planning"
    ],
    "description": "But the act of writing it was part of a strategy to conserve willpower that he used over and over with great success: precommitment. The essence of this strategy is to lock yourself into a virtuous path. You recognize that you'll face terrible temptations to stray from the path, and that your willpower will weaken. So you make it impossible--or somehow unthinkably disgraceful or sinful--to leave the path. Precommitment is what Odysseus and his men used to get past the deadly songs of the Sirens. He had himself lashed to the mast with to go the Sirens. His men used a different form of precommitment by plugging their ears so they couldn't hear the Sirens' songs. They prevented themselves from being tempted at all, which is generally the safer of the two approaches.",
    "comments": "You can strategically plan around temptation. There are methods to avoid falling into traps that don't just involve brute force willpower. Be somewhere in public that prevents you from jerking off. Wear pajamas at night. Get creative because it can be avoided. Use plans. Fear of punishment works well, but it can be used all of the time.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:00:51.978Z"
  },
  {
    "id": 1744217000322,
    "title": "Bright Line Rules. Clear. Simple. Unambiguous.",
    "page": "185",
    "book": "Willpower",
    "tags": [
      "Temptation",
      "Planning"
    ],
    "description": "He [Eric the Pilgrim] needs the help of \"bright lines,\" a term that Ainslie borrows from lawyers. These are clear, simple, unambiguous rules. You can't help but notice when you cross a bright line. If you promise yourself to drink or smoke \"moderately,\" that's not a bright line. It's a fuzzy boundary with no obvious point at which you go from moderation to excess. Because the transition is so gradual and your mind is so adept at overlooking your own peccadilloes, you may fail to notice when you've gone too far. So you can't be sure you're always going to follow the rule to drink moderately. In contrast, zero tolerance is a bright line: total abstinence with no exceptions anytime. It's not practical for all self-control problems--a dieter cannot stop eating all food--but it works well in many situations. Once you're committed to following a bright-line rule, your present self can feel confident that your future self will observe it, too.",
    "comments": "Bright line rules: touching your cock. Opening instagram, discord, etc. It's cutting the habit at the root, so that it isn't able to escalate hyperbolically to the point of no return. These measures are safeguards. While the road ahead isn't technically punishing, it's a boundary that is often not easy to come back from.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:12:42.680Z"
  },
  {
    "id": 1744217000323,
    "title": "Gamification of Life. Shortcomings of Self-Esteem.",
    "page": "213",
    "book": "Willpower",
    "tags": [
      "Success",
      "Discipline",
      "Self-Control",
      "Goal Setting",
      "Improvement"
    ],
    "description": "The self-esteem movement, fortunately, never took hold in the video game industry, probably because children would have been too bored by games that began by telling them what great players they were. Instead, children have preferred games in which they start out as lowly \"noob\" (as in newbies) who must earn respect through their accomplishments. To acquire skills, they fail over and over. The typical teenager must have endured thousands of digital deaths and virtual fiascos, yet somehow he retains enough self-esteem to keep trying. While parents and educators have been promoting the everybody-gets-a-trophy philosophy, children have been seeking games with more demanding standards. Players need concentration to fight off Ork after Ork; they need patience to mine for virtual gold; they need thriftiness to save up for a new sword or helmet. Instead of bemoaning the games' hold over children, we should be exploiting the techniques that game designers have developed. They've refined the basic steps of self-control: setting clear and attainable goals, giving instantaneous feedback, and offering enough encouragement for people to keep practicing and improving. After noticing how hard people work at games, some pioneers are pursuing the \"gamification\" of life by adapting these techniques (like establishing \"quests\" and allowing people to \"level up\") for schools and workplaces and digital collaborations. Video games give new glamour to old-fashioned virtues. Success is conditional--but it's within your reach as long as you have the discipline to try, try again.",
    "comments": "Gamify your life. Set clear and attainable goals. Receive feedback, and making sure you're motivated to keep practicing and improving. Pampering yourself and treating yourself like you deserve credit is where improvement stops. If you want to improve, you must face difficulty and die a thousand deaths before you get the hang of it. This is exactly what Hazelnut did.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:28:16.244Z"
  },
  {
    "id": 1744217000324,
    "title": "Indulgence Day",
    "page": "221",
    "book": "Willpower",
    "tags": [
      "Virtue",
      "Failure"
    ],
    "description": "The researchers gave it a formal scientific term, counterregulatory eating, but in their lab and among colleagues it was known simply as the what-the-hell effect. Dieters have a fixed target in mind for their maximum daily calories, and when they exceed it for some unexpected reason, such as being given a pair of large milkshakes in an experiment, they regard their diet as blown for the day. That day is therefore mentally classified as a failure, regardless of what else happens. Virtue cannot resume until tomorrow. So they think, What the hell, I might as well enjoy myself today--and the resulting binge often puts on far more weight than the original lapse.",
    "comments": "Just because you may fall short of your daily goal doesn't mean you get to wreak havoc on all of your habits. When you let all hell break loose, the amount of damage you cause is far greater than the original thing that broke your day. It puts increased pressure on the following day because of the broken habits and wreckage you have to repair. If you fail your marble for the day, don't practice any marble killers.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:32:22.088Z"
  },
  {
    "id": 1744217000325,
    "title": "Someone Else is Spinning the Thread",
    "page": "331",
    "book": "The Daily Stoic",
    "tags": [
      "Control",
      "Attitude",
      "Change"
    ],
    "description": "Who but Clotho, one of the three Greek goddesses of fate, who \"spins\" the thread of human life. To the ancients, she was the one who decided the course the events of our lives--some good, some bad. As the playwright Aeschylus wrote, \"When the gods send evil, one cannot escape it.\" The same was true for great destiny and good fortune. Their resigned attitude might seem strange to us today, but they understood who was really in control (not them, not us!). No amount of prosperity, no amount of difficulty, is certain or forever. A triumph becomes a trial, a trial becomes a triumph. Life can change in an instant. Remember, today, how often it does.",
    "comments": "November 6. You're not always in control. Oftentimes, you have zero control. Your fate has already been made. You can't blame anyone. Nothing lasts forever. Things change beyond your control, and it's up to you to bear that. You can respond in agony, or with acceptance.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:48:27.678Z"
  },
  {
    "id": 1744217000326,
    "title": "Attachments Are the Enemy",
    "page": "348",
    "book": "The Daily Stoic",
    "tags": [
      "Attachment",
      "Choice",
      "Change",
      "Happiness"
    ],
    "description": "\"In short, you must remember this--that if you hold anything dear outside of your own reasoned choice, you will have destroyed your capacity for choice.\" According to Anthony de Mello, \"there is one thing and only one thing that causes unhappiness. The name of that thing is Attachment.\" Attachments to an image you have of a person, attachments to wealth and status, attachments to a certain place or time, attachments to a job or to a lifestyle. All of those things are dangerous for one reason: they are outside of our reasoned choice. How long we keep them is not in our control. As Epictetus realized some two thousand years ago before de Mello, our attachments are what make it so hard to accept change. Once we have them, we don't want to let go. We become slaves to maintaining the status quo. We are like the Red Queen in Alice and Wonderland--running faster and faster to stay in the same place. But everything is in a constant state of change. We have certain things for a while then lose them. The only permanent thing is prohairesis, our capacity for reasoned choice. The things we are attached to can come and go, our choice is resilient and adaptable. The sooner we become aware of this the better. The easier it will be to accept and adapt to what does happen.",
    "comments": "November 23. Attachments to the image of your perfect girlfriend is bound to bring you displeasure. They are in control of themselves. Everything changes, so naturally, your attachments won't always be the same. Don't chain yourself to them, or you will sign up for disappointment.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-09T21:57:25.754Z"
  },
  {
    "id": 1744217000327,
    "title": "Bear Trials With a Calm Mind",
    "page": "386",
    "book": "The Daily Stoic",
    "tags": [
      "Calmness",
      "Stress",
      "Difficulty",
      "Discipline"
    ],
    "description": "\"To bear trials with a calm mind robs misfortune of its strength and burden.\" The people you admire, the ones who seem to be able to successfully handle and deal with adversity and difficulty, what do they have in common? Their sense of equilibrium, their orderly discipline. On the one-yard line, in the midst of criticism, after a heartbreaking tragedy, during a stressful period, they keep going. Not because they're better than you. Not because they're smarter. But because they have learned a little secret. You can take the bite out of any tough situation by bringing a calm mind to it. By considering it and meditating on it in advance. And this is true not just for our day-to-day adversities but for the greatest and most unavoidable trial of all: our own eventual death. It could come tomorrow, it could come in forty years. It could be quick and painless, or it could be excruciating. Our greatest asset in that ordeal will not be religion, it will not even be the wise words of the philosophers. It will be, simply, our calm and reasoned mind.",
    "comments": "December 30. A calm mind is the best state your brain can be in. It's a lot better than anger, or sadness, or fear, or apathy, or even ecstasy. The only state that can beat it is adrenaline. Most of the time, a calm mind assures maximum brain efficacy, and is your best against stress, difficulty, and discipline",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:02:04.457Z"
  },
  {
    "id": 1744217000328,
    "title": "The Performance Artist. Death of Your Creativity",
    "page": "4",
    "book": "Ego Is The Enemy",
    "tags": [
      "Discomfort",
      "Ego"
    ],
    "description": "The performance artist Marina Abramovic puts it directly: \"If you start believing in your greatness, it is the death of your creativity.\" Just one thing keeps ego around--comfort. Pursuing great work--whether it is in sports or art or business--is often terrifying. Ego soothes that fear. It's a salve to that insecurity. Replacing the rational and aware parts of our psyche with bluster and self-absorption, ego tells us what we want to hear, when we want to hear it. But it is a short-term fix with a long-term consequence.",
    "comments": "Your ego wants things to be comfortable. Keep things uncomfortable, and ego won't take over. Think Hazelnut",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:08:58.861Z"
  },
  {
    "id": 1744217000329,
    "title": "Did Everything but Focus on It",
    "page": "25",
    "book": "Ego Is The Enemy",
    "tags": [
      "Procrastination",
      "Fear",
      "Focus"
    ],
    "description": "In other words, she did what a lot of us do when we're scared or overwhelmed by a project: she did everything but focus on it. The actual novel she was supposed to be working on stalled completely. For a year.",
    "comments": "Procrastination and progress are opposites. Which side do you choose?",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:14:05.826Z"
  },
  {
    "id": 1744217000330,
    "title": "Get Out of Your Head. Don't Feast on Your Own Thoughts",
    "page": "66",
    "book": "Ego Is The Enemy",
    "tags": [
      "Thinking"
    ],
    "description": "These fictional characters all had something in common: they couldn't get out of their own heads. In J.D. Salinger's The Catcher in the Rye, Holden can't stay in school, is petrified of growing up, and wants desperately to get away from it all. In John Fante's Ask the Dust (part of a series known as The Bandini Quartet), this young writer doesn't experience the life he is living, he sees it all \"across a page in a typewriter,\" wondering if nearly every second of his life is a poem, a play, a story, a news article with him as its main character. In Walker Percy's The Moviegoer, his protagonist, Binx, is addicted to watching movies, preferring an idealized version of life on the screen to his own uncomfortable ennui....Because sadly, this trait, the inability to get out of one's head, is not restricted to fiction. Twenty-four hundred years ago, Plato spoke of the type of people who are guilty of \"feasting on their own thoughts.\" It was apparently common enough even then to find people who \"instead of finding out how something they desire might actually come about, [they] pass that over, so as to avoid tiring deliberations about what's possible They assume that what they desire is available and proceed to arrange the rest, taking pleasure in thinking through everything they'll do when they have what they want, thereby making their lazy souls even lazier.\" Real people preferring to live in passionate fiction than in actual reality.",
    "comments": "Never assume what you desire is available. If you do that, then you'll never work hard anymore. You'll be complacent that it will be all there, even if you haven't done the work yet. It's not there until you get it. Thinking doesn't get you anywhere. Doing does. You've done enough thinking.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:44:32.520Z"
  },
  {
    "id": 1744217000331,
    "title": "Pride. Don't Boast. There's Nothing in It for You",
    "page": "74",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility",
      "Ego",
      "Pride"
    ],
    "description": "Christians believe that pride is a sin because it is a lie--it convinces people that they are better than they are, that they are better than God made them. Pride leads to arrogance and then away from humility and connection with their fellow man. You don't have to be Christian to see the wisdom in this. You need only to care about your career to understand that pride--even in real accomplishments--is a distraction and a deluder. \"Whom the gods wish to destroy,\" Cyril Connolly famously said, \"they first call promising.\" Twenty-five hundred years before that, the elegiac poet Theognis wrote to his friend, \"The first thing, Kurnos, which gods bestow on one they would annihilate, is pride.\" Yet we pick up this mantle on purpose! Pride blunts the very instrument we need to own in order to succeed: our mind. Our ability to learn, to adapt, to be flexible, to build relationships, all of this is dulled by pride. Most dangerously, this tends to happen either early in life or in the process--when we're flushed with beginner's conceit. Only later do you realize that that bump on the head was the least of what was risked. Pride takes a minor accomplishment and makes it feel like a major one. It smiles at our cleverness and genius, as though what we've exhibited was merely a hint of what ought to come. From the start, it drives a wedge between the possessor and reality, subtly and not so subtly changing her perceptions of what something is and what it isn't. It is these strong opinions, only loosely secured by fact or accomplishment, that send us careering toward delusion or worse.",
    "comments": "I solved an elementary problem, that makes me a genius. No one can top me. I drew something that doesn't look half-bad in my eyes. I could be a professional. Pride ruins our ability to learn, our adaptability (I'm perfect and don't need to change), and is most potent at the beginning of anything",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T17:50:38.652Z"
  },
  {
    "id": 1744217000332,
    "title": "The Humble Improve. If You're Not Learning, You Are Dying",
    "page": "104",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility",
      "Learning"
    ],
    "description": "\"Humility engenders learning because it beats back the arrogance that puts blinders on. It leaves you open for truths to reveal themselves. You don't stand in your own way...Do you know how you can tell when someone is truly humble? I believe there's one simple test: because they consistently observe and listen, the humble improve. They don't assume, 'I know the way.'\" No matter what you've done up to this point, you better still be a student. If you're not still learning, you're already dying. It is not enough only to be a student at the beginning. It is a position that one has to assume for life. Learn from everyone and everything. From the people you beat, and the people who beat you, from the people you dislike, even from your supposed enemies. At every step and every juncture in life, there is the opportunity to learn--and even if the lesson is purely remedial, we must not let ego block us from hearing it again.",
    "comments": "Arrogance is blindness. The only thing you can see is your ego and how great it is. When you take of the mask of arrogance and expose yourself to the world, the you'll be able to see the truth and learn new things. You can learn anywhere. If you learned nothing for an entire day, you aged a day and were the same person you were yesterday.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:00:13.361Z"
  },
  {
    "id": 1744217000333,
    "title": "Comfort Zone",
    "page": "104",
    "book": "Ego Is The Enemy",
    "tags": [
      "Discomfort",
      "Ego",
      "Knowledge"
    ],
    "description": "Too often, convinced of our own intelligence, we stay in a comfort zone that ensures that we never feel stupid (and are never challenged to learn or reconsider what we know). It obscures from view various weaknesses in our understanding...",
    "comments": "If you supposedly know everything, there's nothing that can challenge your existing belief system or knowledge. Obviously, you can never know everything. But you sure can act like it. You should want to be proven wrong so that you can improve upon what you know. That means stepping into the arena or the wilderness and exploring, instead of sitting on your \"throne\" and relishing in your own greatness",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:04:46.403Z"
  },
  {
    "id": 1744217000334,
    "title": "General Marshal",
    "page": "134",
    "book": "Ego Is The Enemy",
    "tags": [
      "Humility",
      "Ego",
      "Confidence"
    ],
    "description": "When others began to push for Marshall to be chief of staff, he asked them to stop, because \"[it] makes me conspicuous in the army. Too conspicuous in fact.\" Later, he discouraged an effort by the House to pass a bill awarding him the rank of field marshal.... Can you imagine? In all these cases, his sense of honor meant turning down honors, and often letting them go to other people. Like any normal human being, he wanted them, only the right way. More important, he knew that, however nice they would have been to have, he could do without them while perhaps others could not. Ego needs honor in order to be validated. Confidence, on the other hand, is able to wait and focus on the task at hand regardless of external recognition.",
    "comments": "Ego wants acclaim. It says \"look at me\" \"I'm the superstar\". It wants all of the rewards and would have a trophy shelf about how great it is. Having confidence is not caring about external recognition. I'm confident in my own. I don't need to be reassured by other people when I know myself. Even though I could lose, my confidence will be unswayed. If I win, my confidence will remain the same, because it was there all along",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:19:55.384Z"
  },
  {
    "id": 1744217000335,
    "title": "It's Far Better When Doing Good Work Is Sufficient",
    "page": "178",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Praise",
      "Expectations",
      "Attention"
    ],
    "description": "It's far better when doing good work is sufficient. In other words, the less attached we are to outcomes the better. When fulfilling our own standards is what fills us with pride and self-respect. When the effort--not the results, good or bad--is enough. With ego, this is not nearly sufficient. No, we need to be recognized. We need to be compensated. Especially problematic is the fact that, often we get that. We are praised, we are paid, and we start to assume that the two things always go together. The \"expectation hangover\" inevitably ensues.",
    "comments": "Ego wants to be rewarded with praise. If it gets bad enough, it might expect it. It wants recognition. Like a child tugging away for attention. It can't handle being by itself. It will cry for attention. You need to recognize that attention is useless. Praise is unnecessary. I'm already confident",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T18:50:45.998Z"
  },
  {
    "id": 1744217000336,
    "title": "Ego in Its Purest Form",
    "page": "186",
    "book": "Ego Is The Enemy",
    "tags": [
      "Ego",
      "Revenge"
    ],
    "description": "Psychologists often say that threatened egotism is one of the most dangerous forces on earth. The gang member whose \"honor\" is impugned. The narcissist who is rejected. The bully who is made to feel shame. The impostor who is exposed. The plagiarist or the embellisher whose story stops adding up. These are not people you want to be near when they are cornered. Nor is it a corner you would want to back yourself into. That's where you get: How can these people talk to me this way? Who do they think they are? I'll make them all pay. Sometimes because we can't face what's been said or what's been done, we do the unthinkable in response to the unbearable: we escalate. This is ego in its purest and most toxic form.",
    "comments": "Taking offense and starting an offensive is entirely done by the ego. Being \"disrespected\" can push you to extreme anger. How dare they. Do you know who I am? The key is to keep the calm mind at the wheel. Taking offense in the first sign. Don't take offense. It's often petty. Forgive them, and clear any misunderstandings if you wish. Or don't respond at all. Remember above all: Never lash out. It's foolish. It turns you into an animal. That's when chaos ensues.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-10T19:00:46.358Z"
  },
  {
    "id": 1744217000337,
    "title": "The Obsession With the Past",
    "page": "206",
    "book": "Ego Is The Enemy",
    "tags": [
      "Rumination",
      "Ego",
      "Hatred",
      "Distraction",
      "Revenge"
    ],
    "description": "This obsession with the past, with something that someone did or how things should have been, as much as it hurts, is ego embodied. Everyone else has moved on, but you can't, because you can't see anything but your own way. You can't conceive of accepting that someone could hurt you, deliberately or otherwise. So you hate. In failure or adversity, it's so easy to hate. Hate defers blame. It makes someone else responsible. It's a distraction too; we don't do much else when we're busy getting revenge or investigating the wrongs that have supposedly been done to us. Does this get us any closer to where we want to be? No. It just keeps use where we are--or worse, arrests our development entirely.",
    "comments": "Obsessing with the past gets you nowhere. It arguably takes you backwards from opportunity cost, and poisoning your mind with cancerous thoughts. Obsessing over the past is a sign that you can't accept that things didn't go your way. Get over it. The world doesn't revolve around you.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-14T02:07:08.303Z"
  },
  {
    "id": 1744217000338,
    "title": "Self-Control is Indispensable in Imminent Danger",
    "page": "163",
    "book": "Willpower",
    "tags": [
      "Self-Control",
      "Impulse"
    ],
    "description": "The secret to his success lay not in the battles he described so vividly but in two principles that Stanley summarized after his last expedition: I have learnt by actual stress of imminent danger, in the first place, that self-control is more indispensable than gunpowder, and, in the second place, that persistent self-control under the provocation of African travel is impossible without real, heartfelt sympathy for the native with whom one has to deal with. As Stanley realized, self-control is not selfish. Willpower enables us to get along with others and override impulses that are based on personal short-term interests.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:03:47.542Z"
  },
  {
    "id": 1744217000339,
    "title": "Good Parenting. Delayed Gratification",
    "page": "195",
    "book": "Willpower",
    "tags": [
      "Temptation",
      "Self-Control",
      "Parenting"
    ],
    "description": "Delayed gratification has been a familiar theme in the homes of immigrants like Jae and Dae Kim, who were born in South Korea and raised two daughters in North Carolina. The sisters, Soo and Jane, became a surgeon and a lawyer, respectively, as well as the co-authors of Top of the Class, a book about Asians parents' techniques for fostering achievement. They tell how their parents started teaching them the alphabet before their second birthday, and how their mother was never one to reward a child whining for candy at the supermarket. When they reached the checkout counter, before the girls had a chance to beg, Mrs. Kim would preempt them by announcing that if they each read a book the following week, she would buy them a candy bar on the next shopping trip. Later, when Soo went off to college and asked her parents for a cheap used car to get around, they refused but offered to buy her a brand-new car if she was admitted to medical school. Thus, these parents did provide good things for their daughters--but each treat was meted out as a reward for some valued achievement.",
    "comments": "Do not reward bad behaviour don't give in to whining. Instead, reward good behaviour with what they're whining for. You can reward your own good behaviour. Never give in to whining. Please is not an argument. If you had a bad day, don't give yourself anything. It's incentivizing bad behaviour. Starve yourself if you have to. It's unacceptable.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:17:51.056Z"
  },
  {
    "id": 1744217000340,
    "title": "So Before You Get Tempted",
    "page": "229",
    "book": "Willpower",
    "tags": [
      "Planning",
      "Temptation"
    ],
    "description": "An implementation intention takes the form of if-then: If x happens, I will do y. The more you use this technique to transfer the control of your behaviour to automatic processes, the less effort you will expend. ... So before you get tempted by food at a party, you can prepare yourself with a plan like: If they serve chips, I will refuse them all. Or: If there is a buffet, I will eat only vegetables and lean meat. It's a simple but surprisingly effective way to gain self-control. By making the decision to pass up the chips an automatic process, you can do it fairly effortlessly event late in the day, when your supply of willpower is low. And because it's relatively effortless, you can pass up the chips and still have the willpower to deal with the next temptation at the party.",
    "comments": "If Then plans can help you avoid your temptations similarly to bright line rules. If there is a enticing distraction on TV, I will carry on with my day. If I get a sexual fantasy I will let it pass. If I look at some girl's ass, I will look away. It's a simple blueprint that doesn't take as much willpower since the plan is already there. There is no questioning or decision making. Your decisions are already made. Here is what you do: Look away.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:37:01.515Z"
  },
  {
    "id": 1744217000341,
    "title": "Later Rather Than Never",
    "page": "236",
    "book": "Willpower",
    "tags": [
      "Temptation",
      "Planning",
      "Mindset",
      "Desire"
    ],
    "description": "The fact that they ate less than the others is remarkable. The result suggests that telling yourself I can have this later operates in the mind a bit like having it now. It satisfies the craving to some degree--and can be even more effective at suppressing the appetite than actually eating the treat. During the final part of the experiment, when all the people were left alone with a bowl of M&M's, the ones who'd postponed pleasure ate even less than the people who had earlier allowed themselves to eat the candy at will. Moreover, the suppression effect seemed to last outside the laboratory. The day after the experiment, all the people were sent an e-mail with the question: \"How much do you desire M&M candies at this very moment, if someone offered them to you?\" Those who had postponed gratification reported less desire to eat the candy than either people who had refused the pleasure outright or those who had eaten their fill. It takes willpower to turn down dessert, but apparently it's less stressful on the mind to say Later rather than Never. In the long run, you end up wanting less and also consuming less.... Ordinarily, people will pay more for an immediate pleasure, but in this case they were willing to spend extra money to postpone the kiss, because it would let them spend three days savoring the prospect. Similarly, delaying the gratification of creme brulee or molten chocolate cake gives time to enjoy the anticipation. As a result of that advance pleasure, when you ultimately do indulge, you may find less of a need to binge and more of an inclination to eat moderately. In contrast, when you swear off something altogether and then finally give in, you say, What the hell, and gorge yourself.",
    "comments": "You can somewhat satisfy your desires by telling yourself it will come later, as opposed to never. You don't have to follow up on it. You just have to say you'll get it.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:41:27.302Z"
  },
  {
    "id": 1744217000342,
    "title": "The Best Way to Reduce Stress in Your Life",
    "page": "238",
    "book": "Willpower",
    "tags": [
      "Stress",
      "Willpower",
      "Self-Control",
      "Habits"
    ],
    "description": "The best way to reduce stress in your life is to stop screwing up. That means setting up your life so that you have a realistic chance to succeed. Successful people don't use their willpower as a last-ditch defense to stop themselves from disaster, at least not as a regular strategy, as Baumeister and his colleagues have observed recently on both sides of the Atlantic. When they monitored Germans throughout the day (in the beeper study we mentioned earlier), the researchers were surprised to find that the people with strong self-control spent less time resisting desires than other people did.... They're better at arranging their lives so that they avoid problem situations.... people with good self-control mainly use it not for rescue in emergencies but rather develop effective habits and routines in school and at work....They use their self-control not to get through crises but to avoid them. They give themselves enough time to finish a project; they take the car to the shop before it breaks down; they stay away from all-you-can-eat buffets. They play offense instead of defense.",
    "comments": "Set up your life for a realistic chance to succeed. You can't win if you're stuck in bed all day. You'll succumb to jerking off. You need to create a plan that keeps you away. People with high self-control don't exert willpower to avoid desire because they've designed around it. Play offense. Go chase life, don't let it chase you around. You don't want to spend all of your efforts on defense. That's exhausting.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-12T21:19:45.020Z"
  },
  {
    "id": 1744217000343,
    "title": "Don't Keep Putting It Off",
    "page": "239",
    "book": "Willpower",
    "tags": [
      "Procrastination"
    ],
    "description": "Don't keep putting it off. Procrastination is an almost universal vice. Cicero called procrastinators \"hateful\"; Jonathan Edwards preached an entire sermon against the \"sin and folly of depending on a future time.\"",
    "comments": "Never punish your future. Always punish the present. If you hated yourself, you would burden your future self with things you could do now. If you loved yourself, you would do things so that your future self could be free.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:47:35.977Z"
  },
  {
    "id": 1744217000344,
    "title": "Procrastination Is Losing. Loser",
    "page": "241",
    "book": "Willpower",
    "tags": [
      "Procrastination"
    ],
    "description": "Later she discovered that some of the students who scored high on the procrastination questionnaire hadn't event bothered to write down the first two deadlines. As far as they were concerned, the double-extended due date was the only one that counted....The procrastinators--as measured both on the questionnaire and by how late they turned in their papers--did worse by every academic measure: lower grades on their papers, lower scores or their midterm and final exams.",
    "comments": "Which group are you in, the procrastinators, who score worse in every category, or the doers, who finish early, and score better in every category. It's a decision. Winner or Loser. Procrastination is losing",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:49:37.261Z"
  },
  {
    "id": 1744217000345,
    "title": "The Nothing Alternative",
    "page": "254",
    "book": "Willpower",
    "tags": [
      "Planning",
      "Working"
    ],
    "description": "The Nothing Alternative is a marvelously simple tool against procrastination for just about any kind of task. Although your work may not be as solitary and clearly defined as Chandler's, you can still benefit by setting aside time to do one and only one thing. You might, for instance, resolve to start your day with ninety minutes devoted to your most important goal, with no interruptions from e-mail or phone calls, no side excursions anywhere on the Web. Just follow Chandler's regimen: \"Write or nothing. It's the same principle as keeping order in a school. If you make the pupils behave, they will learn something just to keep from being bored. I find it works. Two very simple rules, a. you don't have to write. b. you can't do anything else. The rest comes of itself.\" The rest comes of itself. That's the seeming effortlessness that comes from playing offense. Chandler was incorporating several of the techniques we discussed earlier. The Nothing Alternative is a bright-line rule: a clear, unmistakeable boundary, like the no-drinking vow.  -- If I can't write, I will do nothing -- is also an example of an implementation plan, that specific if-x-then-y strategy that has been shown to reduce the demands on willpower.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:51:04.856Z"
  },
  {
    "id": 1744217000346,
    "title": "Even When Players Lose Battles...",
    "page": "257",
    "book": "Willpower",
    "tags": [
      "Success",
      "Failure",
      "Motivation"
    ],
    "description": "Even when players lose battles or make mistakes or die, they remain motivated because of the emphasis on rewards rather than punishment. Instead of feeling as if they've failed, the players think that they just haven't succeeded yet. That's the feeling we should aim for in the real world, and we can do it by steadily rewarding ourselves for successes along the way. ... But it's important to have lots of little rewards for little feats. Never underestimate how little it takes to motivate.",
    "comments": "Think in terms of rewards, not in punishment. If you fail, you should think that you haven't got there yet, and will try harder next time. Not if you fail, you should be so scared of punishment that you will try. It's a different way to motivate yourself. Hazelnut was positively motivated. It helps you so the brighter side of behaviour. Not the harsh punishments in a dystopia.",
    "helpfulness": 1,
    "createdAt": "2024-06-06T18:44:15.000Z",
    "updatedAt": "2024-06-11T21:54:59.483Z"
  },
  {
    "id": 1744217000347,
    "title": "A Basic Premise to the Seven Keys to Calm",
    "page": "-11",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Anger",
      "Attitude",
      "Control"
    ],
    "description": "A basic premise of The Seven Keys to Calm is that there are, in fact, no Type A people. There is only Type A behaviour and outlook.",
    "comments": "Everyone is capable of Stoic calmness. It's something you can practice. Just like everything else",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:03:02.319Z"
  },
  {
    "id": 1744217000348,
    "title": "The Ugly Troll that Wanted to Marry the Princess",
    "page": "-16",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Change",
      "Virtue"
    ],
    "description": "Did you ever hear the story of the ugly troll who wanted to marry the kind and beautiful princess? First, he donned a mask and dressed as a handsome prince. He quickly realized that looking the part was not enough, however, so he began to act like a prince worthy of the princess. He was noble, gracious, and generous to all. I must have worked, for the princess married him, and they lived together happily. But one day she siad to him, \"I know you are wearing a mask. Take it off or I will leave you forever.\" Having no choice, her husband removed his mask. Underneath he was . . . a handsome, noble, and gracious prince.",
    "comments": "The ugly troll tranforms himself into a prince by taking care of his actions. You too can practice virtue and transform yourself into a handsome prince. You CAN change.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:02:53.643Z"
  },
  {
    "id": 1744217000349,
    "title": "Men or Beasts Who Over React and Panic",
    "page": "5",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Anxiety",
      "Decision Making"
    ],
    "description": "Men or beasts who overreact and panic in the face of anxiety can hardly be expected to choose the wisest course of action. They might well expose themselves to unnecessary danger, either by selecting a course of action too impulsively or by becoming completely incapacitated, too overwhelmed by the feeling of anxiety to function.",
    "comments": "Your best decision making will be when your heart rate is low and you are calm. Anxiety makes rash decisions easier and more attractive",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:03:10.744Z"
  },
  {
    "id": 1744217000350,
    "title": "What If, We Were Able to Just Look at Our Anxiety",
    "page": "12",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Anxiety",
      "Decision Making"
    ],
    "description": "What if, instead of taking these kinds of habitual actions in response to anxiety, we were able to just look at our anxiety dispassionately and sort through it with a detached, objective eye before decing what action to take--if any at all?",
    "comments": "Take a step back and observe. See what it is doing to you. Try not to get so caught up in it and let anxiety control you so deeply",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:03:19.974Z"
  },
  {
    "id": 1744217000351,
    "title": "Anxiety Is About What Might Happen",
    "page": "15",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Anxiety",
      "Present",
      "Control"
    ],
    "description": "Anxiety, you'll recall, always entails a warning. And a warning, by definition, is an anticipatoin of something that might happen. So anxiety is about what might hapeen as opposed to what is happening. When we are slaves to anxiety, we're constantly living in the realm of \"might,\" which is to say, in the future. To end this enslavement we must actively practice living in he land of \"is,\" which is to say, in the moment.",
    "comments": "To overcome anxiety, you need to live in the present. Sleep when it's time to sleep. Eat when you're eating. No thoughts about how bad the future is. Think about what you can do now. It's the only time you control",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:03:29.104Z"
  },
  {
    "id": 1744217000352,
    "title": "Don't Banish or Struggle Against Thoughts",
    "page": "18",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Thinking",
      "Attention"
    ],
    "description": "Don't struggle against the thoughts either. For like an insect caught in a Venus flytrap, the more you struggle, the more tightly you are encased. ... Without judgement, and without labeling the thoughts \"good\" or \"bad,\" just notice them. Watch their fleeting nature. Bear them in mind momentarily, acknowledge them, and then bring your attention back to your chosen focused activity.",
    "comments": "By trying to get rid of thoughts, it only makes it harder. You put too much emphasis on the thoughts, when you shouldn't value it at all. Give it no attention.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:03:40.310Z"
  },
  {
    "id": 1744217000353,
    "title": "How Easy Is It to Get Anxious on Behalf of People We Love",
    "page": "31",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Control",
      "Attachment"
    ],
    "description": "How easy is it to get anxious on behalf of people we love. We want them to be happy, of course. But we rarely question that we should be the ones who decide what constitute their happiness. We want them to conform to our wishes for them, and on the one hand expect them to. On the other hand, we live in fear that they'll be swayed by some alternate agenda",
    "comments": "They determine their own happiness. You can't conform them to every little wish. Your girlfiend won't be perfect, and you can't control that, or her wishes. Don't expect everything to be about you.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:04:03.600Z"
  },
  {
    "id": 1744217000354,
    "title": "The Fantasy That You Can Control All Events in Life",
    "page": "63",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Control"
    ],
    "description": "The lesson is clear: in relinquishing the fantasy that you can control all events in life you gain enhanced control over the one thing you truly can master--you own reactions and responses to events.",
    "comments": "Once you acknowledge the fact that not everything is in your control, it will help you control the things you can: you reacts to events.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:04:15.783Z"
  },
  {
    "id": 1744217000355,
    "title": "The Calm Mind Does Not Concern Itself With",
    "page": "75",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Calmness",
      "Anxiety",
      "Control"
    ],
    "description": "The Calm Mind does not concern itself with fearing future changes or regretting past ones, because it is always in the moment. And because it is always in the moment, it is totally able to respond to exactly what is happening as it happens. The Calm Mind accepts life's ups and downs, not because it is philosophically resigned, but because it is instinctively moving along with them.",
    "comments": "The Calm Mind lives in the moment. And it is able to handle precisely what's going on because it is clear from anxieties of other times.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:04:27.544Z"
  },
  {
    "id": 1744217000356,
    "title": "Ultimate Satisfaction in Life Cannot Be Derived From",
    "page": "93",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Happiness"
    ],
    "description": "Like all of us, I have to take care to remind myself that ultimate satisfaction in life cannot be derived from a computer, or a car, or anything I claim to possess.",
    "comments": "You don't NEED an upgrade if Trixie or Mavis still work. There's no point anyway. What makes life good is relationships and projects, and personal development",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:04:34.475Z"
  },
  {
    "id": 1744217000357,
    "title": "Don't Fear Death",
    "page": "94",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Death",
      "Attachment",
      "Fear"
    ],
    "description": "Such a strategy is doomed to backfire because much of our fear of death can be fear of parting with things to which we are attached, and things that we perceive as \"belonging\" to us. Yet nothing actually belongs to us. ... Though it may not appear so at first, this truth actually points us in the direction of calm. For once we accept that we actually own nothing, we realize we have nothing to lose. What's more, we now have everything to give. Now the real point of what we are doing here--if we are all going to die anyway--becomes clear. If we can't take anything with us [to heaven], the point must lie in what we can leave behind. So what, exactly, can we leave?",
    "comments": "It's not about what you own. Nothing belongs to you",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:04:43.810Z"
  },
  {
    "id": 1744217000358,
    "title": "The One Thing. Positive Intent",
    "page": "95",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Kindness",
      "Positivity",
      "Giving"
    ],
    "description": "As the Buddha said, neither fire nor wind, birth nor death, can erase our good deeds. The one thing, the only that can be our everlasting legacy is our positive intent, that is, the selfless acts we have performed on behalf of others out of unconditional acceptance and love.",
    "comments": "The impression of selflessness lasts longer and matters more.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:05:01.637Z"
  },
  {
    "id": 1744217000359,
    "title": "Shot By an Arrow and Refused to Take It Out",
    "page": "117",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Control",
      "Acceptance",
      "Knowledge"
    ],
    "description": "Now you are doing a lot of noticing. But your Busy Mind keeps coming back to hows and whys. Why all these \"mistakes\" and messes? it asks. What are all these intricate connections for, and what--or who--is responsible for them? In reply, I will tell you a teaching ascribed to the Buddha--who, it is said, cautioned against asking too many questions about the nature of existence. He likened a person who does so to a man who, having been shot by an arrow, refuses to have its sharp point extracted until he knows for sure who shot the arrow, where he was from, what he looked like, and precisely what sort of bow he was using. Needless to say, that man would die before his questions could be answered. The queries would prove pointless, not to mention impractical in the extreme",
    "comments": "You don't need all of the answers to move on in life. Some things you don't get to know. It only causes more harm to go down that path.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:05:13.552Z"
  },
  {
    "id": 1744217000360,
    "title": "The Busy Mind, So Anxious to Feel Satisfied",
    "page": "120",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Hardship",
      "Challenge",
      "Purpose"
    ],
    "description": "The Busy Mind, so anxious to feel satisfied (and so fundamentally incapable of it), imagines happiness is getting all one's needs met all of the time. But a life without hardship, without challenge, and without its share of sorrows would be less a life than a kind of suspended animation.",
    "comments": "Hardship and challenge are a part of life. It grows you. It defines you",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:05:26.386Z"
  },
  {
    "id": 1744217000361,
    "title": "Will Resistance Put an End to All Your Efforts?",
    "page": "133",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Resistance"
    ],
    "description": "Will resistance put an end to all your efforts? That is its agenda, but it need not prevail. Resistance can be resolved",
    "comments": "That's its goal. It's goal is ot revert back to hedonism. To end the reformation. Don't give in to it.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:05:34.718Z"
  },
  {
    "id": 1744217000362,
    "title": "See the World Through a Calm Mind",
    "page": "145",
    "book": "The Seven Keys To Calm",
    "tags": [
      "Perception"
    ],
    "description": "Perception and what we call \"reality\" are co-influential. When the Calm Mind is doing the perceiving, one sees the world as a different sort of place. It is viewed as less threatening and more hospitable, less chaotic and more meaningful.",
    "comments": "You become less scared and worried and full of anxiety when you ease up and see the world through a calm lens",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:05:42.052Z"
  },
  {
    "id": 1744217000363,
    "title": "Telling People You're Virtuous Is Not a Virtue",
    "page": "-20",
    "book": "12 Rules For Life",
    "tags": [
      "Virtue",
      "Humility"
    ],
    "description": "Leave aside that telling people you're virtuous isn't a virtue, it's self promotion. Virue signalling is not virtue. Virtue signalling is, quite possibly, our commonest vice.",
    "comments": "You're not immune. Do not boast or aggrandize yourself. \"I'm very humble\" defeats itself. Don't tell other people you're \"better\". You don't need to tell them to prove it.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:56:08.686Z"
  },
  {
    "id": 1744217000364,
    "title": "The Centre Is Occupied by the Individual",
    "page": "-33",
    "book": "12 Rules For Life",
    "tags": [
      "Responsibility",
      "Suffering"
    ],
    "description": "The centre is marked by the cross, as X marks the spot. Existence at that cross is suffering and transformation. ... The answer is this: through the elevation and development of the individual, and through the willingness of everyone to shoulder the burden of Being and to take the heroic path. We must each adopt as much responsibility as possible for individual life, society and the world.",
    "comments": "Transformation and suffering go hand in hand. You have to be willing to stand on the X of suffering to transform into something more. That means exposing yourself and putting yourself through strain. The end result is a transformed individual.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:54:09.585Z"
  },
  {
    "id": 1744217000365,
    "title": "Regular Routines. Protein Breakfast",
    "page": "18",
    "book": "12 Rules For Life",
    "tags": [
      "Routine"
    ],
    "description": "The acts of life we repeat every day needs to be automatized. They must be turned into stable and reliable habits, so they lose their complexity and gain predictability and simplicity. ... Do they [Dr. Peterson's clients] wake up in the morning at approximately the same time the typical person wakes up, and at the same time every day? If the answer is no, fixing that is the first thing I recommend. It doesn't matter so much if they go to bed at the same time each evening, but waking up at a consistent hour is a necessity. ... I counsel my clients to eat a fat and protein-heavy breakfast as soon as possible after they awaken.",
    "comments": "Establishing a set hour to wake up at, and obey the rule is critical. Lost sleep should be made up for by going to bed early, or naps. Not by taking hours away from tomorrow.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:56:22.033Z"
  },
  {
    "id": 1744217000366,
    "title": "Don't Run Away",
    "page": "21",
    "book": "12 Rules For Life",
    "tags": [
      "Fear"
    ],
    "description": "On the way [to the mall], she can feel her heart pounding. That triggers another cycle of anxiety and concern. To forestall panic, she avoids the stress of the mall and returns home. But now the anxiety systems in her brain note that she ran away from the mall, and conclude that the journey there way truly dangerous. Our anxiety systems are very practical. They assume that anything you run away from is dangerous. The proof of that is, of course, the fact you ran away. So now the mall is tagged \"too dangerous to approach\" (or the budding agoraphobic has labelled herself, \"too fragile to approach the mall\").",
    "comments": "If you run away from the things that scare you, you'll only add to the feedback loop. Avoiding women and other things like talking to other people or applying for a job will get worse if you avoid them. Instead, tackling your fears head on is the surest way to overcome them. Not by reading about it, but by being present in that moment.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:56:40.513Z"
  },
  {
    "id": 1744217000367,
    "title": "So, Attend Carefully to Your Posture. Quit Hunching",
    "page": "27",
    "book": "12 Rules For Life",
    "tags": [
      "Body Language",
      "Confidence",
      "Improvement"
    ],
    "description": "So, attend carefully to your posture. Quit drooping and hunching around. Speak your mind. Put your desires forward, as if you had a right to them--at least the same right as others. Walk tall and gaze forthrightly ahead. Dare to be dangerous. Encourage the serotonin to flow pentifully through the neural pathways desperate for its calming influence. People, including yourself, will start to assume that you are competent and able (or at least they will not immediately conclude the reverse). Emboldened by the positive responses you are now receiving, you will begin to be less anxious. ... Thus strengthened and emboldened, you may choose to embrace Being, and work for its furtherance and improvement.",
    "comments": "I don't know where it started, but you assume the position of a loser at all times. Hunched over, acting like nobody cares. Never do you put yourself first. This ends now. It's a positive feedback loop. Act like a man. Look people in the eye, chin up, shoulders back. You are dangerous.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:56:57.855Z"
  },
  {
    "id": 1744217000368,
    "title": "Order Is Not Enough",
    "page": "44",
    "book": "12 Rules For Life",
    "tags": [
      "Control",
      "Exploration",
      "Complacency"
    ],
    "description": "Order is not enough. You can't just be stable, and secure, and unchanging, because there are still vital and important new things to be learned. Nonetheless, chaos can be too much. You can't long tolerate being swamped and overwhelmed beyond your capacity to cope while you are learning what you still need to know. Thus, you need to place one foot in what you have mastered and understood and the other in what you are currently exploring and mastering. Then you have positioned yourself where the terror of existence is under control and you are secure, but where you are also alert and engaged. That is where there is something new to master and some way that you can be improved. That is where meaning is to be found.",
    "comments": "You can't live the same life forever. Embrace new things, but bring along the past to ground you so you don't get swept away by chaos. Take the right dose of novelty",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:57:16.057Z"
  },
  {
    "id": 1744217000369,
    "title": "You Deserve Some Respect. You Are Important to Others",
    "page": "62",
    "book": "12 Rules For Life",
    "tags": [
      "Empathy",
      "Forgiveness",
      "Kindness"
    ],
    "description": "You deserve some respect. You are important to other people, as much as to yourself. You have some vital role to play in the unfolding destiny of the world. You are, therefore, morally obliged to take care of yourself. You should take take of, help and be good to yourself the same way you would take care of, help and be good to someone you loved and valued.",
    "comments": "I most certainly do not treat myself as if I were Penny. It shows that I would care more for her than for myself. What does that say about myself? Do I respect myself? Well, you ought to. Because we are all a team up there. Don't treat yourself like a prince, but you need to recognize that you are human, and that too much shame and punishment can be harmful. Don't channel your meanness onto yourself excessively.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:57:34.108Z"
  },
  {
    "id": 1744217000370,
    "title": "You Must Determine Where You Are Going",
    "page": "63",
    "book": "12 Rules For Life",
    "tags": [
      "Character",
      "Identity"
    ],
    "description": "You must determine where you are going, so that you can bargain for yourself, so that you don't end up resentful, vengeful, and cruel. You have to articulate your own principles, so that you can defend yourself against others' taking inappropriate advantage of you, and so that you are secure and safe while you work and play. You must discipline yourself carefully. You must keep the promises you make to yourself, and reward yourself, so that you can trust and motivate yourself. You need to determine how to act toward yourself so that you are most likely to become and to stay a good person. It would make the world a better place.",
    "comments": "Your goal should be to become the best person you are capable of.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:57:52.575Z"
  },
  {
    "id": 1744217000371,
    "title": "When the Internal Critic Puts You Down",
    "page": "89",
    "book": "12 Rules For Life",
    "tags": [
      "Motivation",
      "Ego",
      "Humility"
    ],
    "description": "When the internal critic puts you down using such comparisions, here's how it operates: First, it selects a single, arbitrary domain of comparison (fame, maybe, or power). Then it acts as if that domain is the only one that is relevant. Then it contrasts you unfavourably with someone truly stellar, within that domain. It can take that final step even further, using the unbridgeable gap between you and its target of comparison as evidence for the fundamental injustice of life. That way your motivation to do anything at all can be most effectively undermined.",
    "comments": "Comparison is the thief of joy. It's impossible to be motivated when you're comparing yourself to professionals. Drawing is hard, coding is hard, but comparing and justifying your inferiority destroys any motivation that you had left.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:58:27.145Z"
  },
  {
    "id": 1744217000372,
    "title": "Five Hundred Small Decisions Compose Your Day",
    "page": "95",
    "book": "12 Rules For Life",
    "tags": [
      "Decision Making",
      "Goal Setting"
    ],
    "description": "Five hundred small decisions, five hundred tiny actions, compose your day, today, and every day. Could you aim for one or two of these at a better result? ... Thus, you setting the following goal: by the end of the day, I want things in my life to be a tiny bit better than they were this morning. ... What you aim at determines what you see",
    "comments": "Decisions like getting out of bed, give dividends later on. Plugging in your devices and unplugging them at the right time. Reading in the morning. Touching your cock. Sitting down to watch TV. These are all decisions you make every day. You know what the right answer is, so what's stopping you? Will you be a grumpy old man that never learned how to live beyond the lifestyle of a 15 year old? Or will you become a man.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:58:43.494Z"
  },
  {
    "id": 1744217000373,
    "title": "Aleksandr Solzhenitsyn Had Every Reason",
    "page": "154",
    "book": "12 Rules For Life",
    "tags": [
      "Bitterness",
      "Improvement",
      "Humility"
    ],
    "description": "Aleksandr Solzhenitsyn had every reason to question the structure of existence when he was imprisoned in a Soviet labour camp, in the middle of the terrible twentieth century. He had served as a soldier on the ill-prepared Russian front lines in the face of a Nazi invasion. He had been arrested, beaten and thrown into prison by his own people. Then he was struck by cancer. He could have become resentful and bitter. His life had been rendered miserable by both Stalin and Hitler, two of the worst tyrants in history. He lived in brutal conditions. Vast stretches of his precious time were stolen from him and squandered. He witnessed the pointless and degrading suffering and death of his friends and acquaintances. Then he contracted an extremely serious disease. Solzhenitsyn had cause to curse God. Job himself barely had it as hard. But the great writer, the profound, spirited defender of truth, did not allow his mind to turn towards vengeance and destruction. He opened his eyes, instead. During his many trials, Solzhenitsyn encountered people who comported themselves nobly, under horrific circumstances. ... Can I stop making such mistakes, now? Can I repair the damage done by my past failures, now? He learned to watch and listen. He found people he admired; who were honest, despite everything. He took himself apart, piece by piece, let what was unneccessary and harmful die, and resurected himself. ... One man's decision to change his life, instead of cursing fate, shook the whole pathological system of communist tyranny to its core.",
    "comments": "Learning to change yourself is one of the most powerful things you can learn. It means you learn anything. Cursing fate and commiting suicide it not noble. It's weak. Strengh is enduring all of the problems thrown at you. Cowering is not manly.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:59:00.433Z"
  },
  {
    "id": 1744217000374,
    "title": "Clean Up Your Life",
    "page": "157",
    "book": "12 Rules For Life",
    "tags": [
      "Decision Making",
      "Time",
      "Behaviour"
    ],
    "description": "Consider your circumstances. Start small. Have you taken full advantage of the opportunities offered to you? Are you working hard on your career, or even your job, or are you letting bitterness and resentment hold you back and drag you down? Have you made peace with your brother? Are you treating your spouse and your children with dignity and respect? Do you have habits that are destroying your health and well-being? Are you truly shouldering your responsibilities? Have you said what you need to say to your friends and family members? Are there things that you could do, that you know you could do, that would make things around you better? Have you cleaned up your life? If the answer is no, here's something to try: Start to stop doing what you know to be wrong. Start stopping today. Don't waste time questioning how you know what you're doing is wrong, if you are certain that it is. ... So, simply stop, when you apprehend, however dimly, that you should stop. Stop acting in that particular, despicable manner. Stop saying those things that make you weak and ashamed. Say only those things that make you strong. Do only those things that you could speak of with honour.",
    "comments": "You already know what's wrong and you continue doing it. When will you stop? There is no time to waste. If you catch yourself doing something wrong, stop yourself immediately. It's not honourable. You have a brain. Use it.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:59:31.085Z"
  },
  {
    "id": 1744217000375,
    "title": "Ask a New Neighbour for a Favor",
    "page": "168",
    "book": "12 Rules For Life",
    "tags": [
      "Socializing",
      "Kindness"
    ],
    "description": "Benjamin Frankline once suggested that a newcomer to a neighbourhood ask a new neighbour to do him or her a favour, citing an old maxim: He that has once done you a kindness will be more ready to do you another than he whom you yourself have obliged. In Franklin's opinion, asking someone for something (not too extreme, obviously) was the most useful and immediate invitation to social interaction.",
    "comments": "It's an invitation for social interaction you can use to break the ice and make new friends (or you know what)",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:59:44.479Z"
  },
  {
    "id": 1744217000376,
    "title": "Suffering Is Real, and the Artful Infliction of Suffering on Another Is Wrong",
    "page": "197",
    "book": "12 Rules For Life",
    "tags": [
      "Kindness",
      "Suffering"
    ],
    "description": "Suffering is real, and the artful infliction of suffering on another, for its own sake, is wrong. That became the cornerstone of my belief. ... Every human has an immense capacity for evil. Each human being understands, a priori, perhaps not what is good, but certainly what is not. And if there is something that is not good, then there is something that is good. If the worst sin is the torment of others, merely for the sake of the suffering produced--then the good is whatever is diametrically opposed to that. The good is whatever stops such things from happening.",
    "comments": "Don't hurt others for fun. Don't spite them no matter what. It's wrong. The best revenge is not served",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T20:59:57.285Z"
  },
  {
    "id": 1744217000377,
    "title": "You May Come to Ask Yourself, \"What Should I Do Today\"",
    "page": "199",
    "book": "12 Rules For Life",
    "tags": [
      "Decision Making",
      "Improvement"
    ],
    "description": "You may come to ask yourself, \"What should I do today?\" in a manner that means \"How could I use my time to make things better, instead of worse?\" ... You may find that if you attend to these moral obligations, once you have placed \"make the world better\" at the top of your value hierarchy, you experience ever-deepening meaning.",
    "comments": "You should not be expedient because it transfers the burden to someone else: your future self. Work towards building a paradise, not a hellscape.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:00:09.284Z"
  },
  {
    "id": 1744217000378,
    "title": "Meaning Is the Way",
    "page": "201",
    "book": "12 Rules For Life",
    "tags": [
      "Virtue"
    ],
    "description": "Meaning is the Way, the path of life more abundant, the place you live when you are guided by Love and speaking Truth and when nothing you want or could possibly want takes any precedence over precisely that. Do what is meaningful, not what is expedient.",
    "comments": "Live a life guided by love. Life a life of truth.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:00:18.977Z"
  },
  {
    "id": 1744217000379,
    "title": "You Can Be Pretty Smart If You Shut Up",
    "page": "244",
    "book": "12 Rules For Life",
    "tags": [
      "Thinking",
      "Communication"
    ],
    "description": "You can be pretty smart if you just shut up.",
    "comments": "People will reveal themselves if you don't speak. Listening helps people think. This can be useful if those you know have problems.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:00:36.420Z"
  },
  {
    "id": 1744217000380,
    "title": "Rogerian Method for Disputes",
    "page": "246",
    "book": "12 Rules For Life",
    "tags": [
      "Arguing"
    ],
    "description": "He suggested that his readers conduct a short experiment when they found themselves in a dispute: \"Stop the discussion for a moment, and institute this rule: 'Each person can speak up for himself only after he has first restated the ideas and feelings of the previous speaker accurately, and to that speaker's satisfaction.'\" I have found this technique very useful, in my private life and in my practice.",
    "comments": "If you find yourself in a dispute use this, summarize the situation, and restate the feelings and ideas to the satisfaction of whom you are speaking to. It reduces disconnect.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:00:43.864Z"
  },
  {
    "id": 1744217000381,
    "title": "Men \"Fixing\" the Problems of Women",
    "page": "247",
    "book": "12 Rules For Life",
    "tags": [
      "Clarity",
      "Communication"
    ],
    "description": "-",
    "comments": "Women formulate the problem. Don't try to offer solutions right away. instead ask if there is more, and search for the clarity of what is being said. Too early means that you're trying to escape.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:00:54.228Z"
  },
  {
    "id": 1744217000382,
    "title": "When Things Fall Apart, and Chaos Reemerges",
    "page": "278",
    "book": "12 Rules For Life",
    "tags": [
      "Communication"
    ],
    "description": "When things wall apart, and chaos re-emerges, we can give structure to it, and re-establish order, through our speech. If we speak carefully and precisely, we can sort things out, and put them in their proper place, and set a new goal, and navigate to it--often communally, if we negotiate, if we reach consensus. If we speak carelessly and imprecisely, however, things remain vague. The destination remains unproclaimed. The fog of uncertainty does not life, and there is no negotiating through the world.",
    "comments": "You cannot let things fester. Address problems to get rid of the uncertainty. Acknowledge the dragon. Long term truth.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:01:13.105Z"
  },
  {
    "id": 1744217000383,
    "title": "You Have to Consciously Define the Topic of a Conversation",
    "page": "282",
    "book": "12 Rules For Life",
    "tags": [
      "Communication",
      "Clarity",
      "Arguing"
    ],
    "description": "You have to consciously define the topic of conversation, particularly when it is difficult--or it becomes about everything, and everything is too much. This is so frequently why couples cease communicating. Every argument degenerates into every problem that ever emerged in the past, every problem that exists now, and every terrible thing that is likely to happen in the future. No one can have a discussion about \"everything.\" Instead, you can say, \"This exact, precise thing is what I want, as an alternative (although I am open to suggestions if they are specific). This exact, precise thing--that is what you could deliver, so that I will stop making your life and mne miserable.\" But to do that, you have to think: What is wrong, exactly? What do I want, exactly? You must speak forthrightly and call forth the habitable world from chaos. You must use honest precise speech to do that. If instead you shrink away and hide, what you are hiding from will transform itself into a giant dragon that lurks under your bed and in your forest and in the dark recesses of your mind--and it will devour you.",
    "comments": "If you do not define it exactly, arguments could be about everything. What's wrong exactly? Use honest and precise speech.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:01:27.438Z"
  },
  {
    "id": 1744217000384,
    "title": "Men Enforce a Code of Behaviour on Each Other",
    "page": "328",
    "book": "12 Rules For Life",
    "tags": [
      "Attitude",
      "Motivation"
    ],
    "description": "Men enforce a code of behaviour on each other, when working together. Do your work. Pull your weight. Stay awake and pay attention. Don't whine or be touchy. Stand up for your friends. Don't suck up and don't snitch. Don't be a slave to stupid rules. Don't, in the immortal words of Arnold Schwarzenegger, be a girlie man. Don't be dependent. At all. Ever. Period.",
    "comments": "This passage is all about being a man. Remind yourself this because you need to be one. Immediately after there is a story about little Mac. He adopts the attitude of a man, and becomes one. Here's the story: It was titled \"The Insult that Made a Man out of Mac\" and could be found in almost every comic book, most of which were read by boys. Mac, the protagonist, is sitting on a beach blanket with an attractive young woman. A bully runs by, kicks sand in both their faces. Mac objects. The much larger man grabs him by the arm and says, \"Listen here. I'd smash your face. . . . Only you're so skinny you might dry up and blow away.\" The bully departs. Mac says to the girl, \"The big bully I'll get him some day.\" She adopts a provocative pose, and says, \"Oh, don't let it bother you little boy.\" Mac goes home, considers his pathetic physique, and buys the Atlas program. Soon, he has a new body. The next time he goes to the beach, he punches the bully in the nose. The now-admiring girl clings to his arm. \"Oh, Mac!\" she says. \"You're a real man after all.\" Is that not inspiring? You can't drown in resentment, and skulk off to your basement to play video games in your underwear. You're a man.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:01:37.670Z"
  },
  {
    "id": 1744217000385,
    "title": "Imagine an Omnipotent Being",
    "page": "343",
    "book": "12 Rules For Life",
    "tags": [
      "Purpose",
      "Struggle"
    ],
    "description": "Imagine a being who is omniscient, omnipresent, and omnipotent. What does such a being lack? The answer? Limitation. If you are already everything, everywhere, always, there is nowhere to go and nothing to be. Everything that could be already is, and everything that could happen already has. And it is for this reason, so the story goes, that God created man. No limitation, no story. No story, no Being.",
    "comments": "You're made to grow. That's why you're here. Get out there and grow. It's equivalent to living. Limitation is Being",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:07:00.346Z"
  },
  {
    "id": 1744217000386,
    "title": "Ask, and It Shall Be Given to You",
    "page": "355",
    "book": "12 Rules For Life",
    "tags": [
      "Ambition",
      "Determination",
      "Success"
    ],
    "description": "Ask, and it shall be given to you; Seek, and ye shall find; Knock, and it shall be open unto you: For everyone who asks receives; the one who seeks finds; and to the one who knocks, the door will be opened (Matthew 7:7-7:8)",
    "comments": "Ambition uses this do get ahead. You need to actively chase what you want. Determined people will get anything",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:02:01.531Z"
  },
  {
    "id": 1744217000387,
    "title": "On Many Occasions in a Marriage",
    "page": "356",
    "book": "12 Rules For Life",
    "tags": [
      "Marriage",
      "Arguing"
    ],
    "description": "On many occasions in our nearly thirty years of marriage my wife and I have had a disagreement--sometimes a deep disagreement. Our unity appeared to be broken, at some unknowably profound level, and we were not able to easily resolve the rupture by talking. We became trapped, instead, in emotional, angry and anxious argument. We agreed that when such circumstances arose we would separate, briefly: she to one room, me to another. This was often quite difficult, because it is hard to disengage in the heat of an argument, when anger generates the desire to defeat and win. But it seemed better than risking the consequences of a dispute that threatened to spiral out of control. Alone, trying to calm down, we would each ask ourselves the same single question: What had we each done to contribute to the situation we were arguing about? However small, however distant . . . we had each made some error. Then we would reunite, and share the results of our questioning: Here's how I was wrong. . . . The problem with asking yourself such a question is that you must truly want the answer. ... But it's at such a point that you must decide wheter you want to be right or you want to have peace. ... You don't get peace by being right.",
    "comments": "It's hard to disengage from an argument, when anger is high and you want to \"win\". You should separate so the anger can settle. Do you want to be right? Or do you want peace? Wait out the emotion.",
    "helpfulness": 1,
    "createdAt": "2024-06-23T20:31:31.000Z",
    "updatedAt": "2024-06-23T21:02:11.809Z"
  },
  {
    "id": 1744217000388,
    "title": "Neediness Lowers Attraction",
    "page": "13",
    "book": "Models",
    "tags": [],
    "description": "the less needy he is, the more attractive he will be to women on average. Neediness is when a man places a higher priority on others' perceptions of him than his perception of himself",
    "comments": "\"on average\" doesn't apply to you",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000389,
    "title": "Investment in Others Perceptions Is Needy",
    "page": "13",
    "book": "Models",
    "tags": [],
    "description": "a needy man is constantly investing in the perceptions others have in him. He is being extra nice and friendly when he doesn't want to be ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000390,
    "title": "A Non-Needy Man Is Invested in Himself",
    "page": "13",
    "book": "Models",
    "tags": [],
    "description": "a non-needy man will be more invested in himself than the woman he's with. By investment, I mean the degree to which you sacrifice/alter your own thoughts, feelings, and motivations for someone else. By less, I mean that you as a man, you should not be willing to sacrifice your thoughts, feelings, and motivations for someone else more than they sacrifice theirs for you.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000391,
    "title": "What Seduction Is",
    "page": "16",
    "book": "Models",
    "tags": [],
    "description": "Seduction is the process by which a man induces a woman to become as invested in him as he as in her.",
    "comments": "Your girlfriend doesn't define you. She is only a companion. You need your own identity separate from her",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000392,
    "title": "Instead of Worrying About Impressing Her",
    "page": "20",
    "book": "Models",
    "tags": [],
    "description": "Instead of worrying about trying to impress her, or if she still likes you, think does she impress you, or if you still like her. Instead of sitting there silently wondering what to say next to make her like you, you could sit there silently wondering what she will say to make you like her",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000393,
    "title": "Women Are Attracted to a Man They Can Respect",
    "page": "21",
    "book": "Models",
    "tags": [],
    "description": "Women are attracted to a man they can respect, to a man they can trust. If you're constantly looking for approval for what to say and how to feel, how could anyone respect or trust you",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000394,
    "title": "Are You Ready to Leave on a Dime",
    "page": "21",
    "book": "Models",
    "tags": [],
    "description": "Are you ready to leave on a dime if she offends you or breaks your trust?",
    "comments": "Do you respect yourself enough to leave? You should",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000395,
    "title": "The Only Real Dating Advice Is Self-Improvement",
    "page": "21",
    "book": "Models",
    "tags": [],
    "description": "The only real dating advice is self-improvement. Work on yourself. Conquer your anxieties. Resolve your shame. ... Love yourself. Otherwise no, one else will.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000396,
    "title": "You Are a Random Guy. Rejection",
    "page": "23",
    "book": "Models",
    "tags": [],
    "description": "Remember that when dating, you are just a random guy talking to her. That's it. Don't take rejection so personally",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000397,
    "title": "Making Yourself Vulnerable",
    "page": "26",
    "book": "Models",
    "tags": [],
    "description": "making yourself vulnerable doesn't just mean being willing to share your fears or insecurities. It can mean putting yourself in a position where you can be rejected, saying a joke that may not be funny, asserting an opinion that may offend others, introducing yourself to a group of people you don't know, telling a woman that you like her and want to date her. ... You're making yourself vulnerable when you do them.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000398,
    "title": "Stop Trying to Be Perfect",
    "page": "28",
    "book": "Models",
    "tags": [],
    "description": "expose your rough edges. Stop trying to be perfect",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000399,
    "title": "Being Concerned About Rejection Turns Her Off",
    "page": "35",
    "book": "Models",
    "tags": [],
    "description": "the fact that we seemed so concerned about getting rejected turns her off",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000400,
    "title": "Honesty Only Works When Unconditional",
    "page": "36",
    "book": "Models",
    "tags": [],
    "description": "honesty only works if it's given unconditionally, with no strings attached. That means everything you say and do must be done without any ulterior motive.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000401,
    "title": "A Needy Man Will Give Compliments Without Knowing Her",
    "page": "38",
    "book": "Models",
    "tags": [],
    "description": "A needy man will give a woman a compliment without knowing her",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000402,
    "title": "When You're Willing to Cut a Woman Off",
    "page": "39",
    "book": "Models",
    "tags": [],
    "description": "Again, it's not about what's being said, it's about the intention and subcommunication behind it. When you're willing to cut a woman off and tell her when you feel that she's out of line, when you're willing to tell a woman what you will and will not tolerate in your life, this sub-communicates the most powerful elements of attraction to her. Far more powerful than an entertaining story or game.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000403,
    "title": "If a Woman Says Something Offensive",
    "page": "39",
    "book": "Models",
    "tags": [],
    "description": "If a beautiful woman says something that a needy man finds offensive, he'll ignore it, change the topic, or withhold his true feelings. But a non needy man will tell her what she said was offensive. Let the chips fall where they may. He won't be an asshole about it. He will simply draw a line in the sand, \"I don't like stuff like that,\" and she can choose to step across it or not.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000404,
    "title": "You're Never Going to Like a Woman 100%",
    "page": "44",
    "book": "Models",
    "tags": [],
    "description": "You're never going to like 100% of any woman and no woman is ever going to like 100% of you",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000405,
    "title": "You Are Incompatible With Most Women",
    "page": "45",
    "book": "Models",
    "tags": [],
    "description": "You are going to be incompatible with most of the women in the world and to hold any hopes of being highly compatible with most is an illusion of grandeur and a figment of your own narcissistic tendency",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000406,
    "title": "Altering Your Behaviour for Her",
    "page": "53",
    "book": "Models",
    "tags": [],
    "description": "A big misconception that men have is that they think they need to behave is a way that makes every single woman like them -- as if women were all the same. This is counterproductive because by altering your behaviour to fit whatever she wants, it means you are not being vulnerable and, therefore, you are being needy and unattractive.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000407,
    "title": "Plain Jokes and Safe Topics",
    "page": "53",
    "book": "Models",
    "tags": [],
    "description": "Other men often stick to plain jokes and safe topics of conversation that end up not polarizing at all for fear of being rejected. This is also a form of hiding one's truth, not showing vulnerability, being over-invested and therefore unattractive. This is the plight of the highly needy \"Nice Guy.\" He's afraid of eliciting an emotional response in anybody, especially women (and especially himself): therefore, he'll play it safe and elicit Neutral reactions from woman after woman.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000408,
    "title": "The Biggest Mental Hurdle",
    "page": "56",
    "book": "Models",
    "tags": [],
    "description": "The biggest mental hurdle for many men is the ability to handle rejection. A lot of men have had it ingrained into them all of their lives -- and even by other dating advice -- that rejection is terrible and should be avoided at all costs. They buy into some myth that there are magical lady's men out there that don't get rejected, ever. And as we'll see, this is not true.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000409,
    "title": "\"I hope she doesn't reject me\"",
    "page": "59",
    "book": "Models",
    "tags": [],
    "description": "Instead of thinking, \"I hope she doesn't reject me,\" think, \"I hope I'll find out if she's right for me.\"",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000410,
    "title": "If She Liked You Enough ... She'd Make It Happen",
    "page": "60",
    "book": "Models",
    "tags": [],
    "description": "But the point is that if she liked me enough, she'd be willing to work at making it happen with me. And if she doesn't, then that just means it's wrong person -- or right person, wrong time. And that's fine.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000411,
    "title": "To Not Take About Is Being Dishonest With Yourself",
    "page": "64",
    "book": "Models",
    "tags": [],
    "description": "If you see a beautiful woman and have a desire to meet her, to not take action and meet her is a form of being dishonest with yourself. ... The foundation behind all of the advice given is the idea that an honest expression of yourself and your desires as a man is the most effective way to demonstrate non-neediness and to therefore create lasting and genuine attraction with women who will make you the happiest.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000412,
    "title": "All Fear Around Your Sexuality",
    "page": "64",
    "book": "Models",
    "tags": [],
    "description": "All fear around your sexuality is a result of feeling inferior or unworthy. If you're afraid to approach a woman, it's because somewhere inside you are more invested in her opinion of you than you are in your own opinion of yourself",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000413,
    "title": "Meeting Women in the Right Situations",
    "page": "70",
    "book": "Models",
    "tags": [],
    "description": "If you focus your time and energy on meeting women in situations where they are likely to share your values, interests, and needs -- then you're going to not only experience a much higher degree of sucess, but you're going to meet women you enjoy a lot more.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000414,
    "title": "What Do You Want in a Woman?",
    "page": "71",
    "book": "Models",
    "tags": [],
    "description": "What I recommend to every man before he even begins talking to women is to sit down for a while and ask himself a few questions: - What do you want in a woman? What do you value the most? What is an absolute deal-breaker in the women you date? Prioritize what you look for in a woman. This will help you decide where to look.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000415,
    "title": "Rejections Are a Form of Screening",
    "page": "73",
    "book": "Models",
    "tags": [],
    "description": "rejections are a form of screening for demographics",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000416,
    "title": "A Few Rules to Dressing Well",
    "page": "81",
    "book": "Models",
    "tags": [],
    "description": "There are a few rules to dressing well: 1. Wear clothes that fit. 2. Wear clothes that match. 3. Dress to your personality. ... Matching is actually simple once you know what to look for: - Your belt should match your shoes and/or your accessories. - If you're wearing dress pants, your socks should match your pants. - If you're wearing jeans, your socks should match your shoes. - Your accessories must be all gold or all silver. ... Here's an easy way to get started: Go out and buy a \"black set\" and a \"brown set.\" Buy a nice pair of black shoes, a nice black belt, and a black jacket. Then buy a nice pair of brown shoes, a brown belt, and a brown jacket. Then buy a few pairs of nice designer jeans with lighter and darker washes and a dozen or so shirts. ... I like to wear the brown set with lighter shirts and jeans, and the black set with darker shirts and jeans.",
    "comments": "For the love of god, get shirts that actually fit you",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000417,
    "title": "Don't Walk Like a Virgin",
    "page": "86",
    "book": "Models",
    "tags": [],
    "description": "As you walk down the street, remember: shoulders back, chin up, eyes straight, feet straight, shoulders swagger, arms swing. Always look straight ahead. Don't ever look down at the ground unless you think you're about to trip. Look at people in the eye as you walk by -- particularly attractive girls. You'll catch people making eye contact with you. You'll feel the urge to look away. Don't. ... ",
    "comments": "Don't walk like a virgin. Remember back when someone told you? Try making eye contact instead of always looking away immediately. Try to extend that time, and possibly make them break it.",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000418,
    "title": "Don't Talk Like a Virgin",
    "page": "87",
    "book": "Models",
    "tags": [],
    "description": "Here's a cool exercise you can do. Read the following sentence aloud: \"Do you want to get a drink Thursday night?\" Now, hold your nose and read it again. How different is your tonality? If it's not very different, you already speak largely from your chest and probably have good tonality. If you suddenly sound very nasal when you hold your nose and say it, you need to work on speaking with a deeper voice. Keep practicing it until you can say it while holding your nose and it doesn't sound any different. ... Also chance are you are not loud enough.",
    "comments": "Nerds have a distinct nasal pitch. So do you. Try to reduce it by speaking from the chest. Yes, you are included. Stop being so mousy and meek. Slow down your speech, and say it louder",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000419,
    "title": "Anxiety = Neediness",
    "page": "96",
    "book": "Models",
    "tags": [],
    "description": "Anxiety, almost by definition, represents a high level of neediness. Let's say a beautiful woman sits down next to you and you want to say something to her but are scared to death. The fact that you're scared to death demonstrates a high level of investment in her opinion of you, and thus a high degree of neediness.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000420,
    "title": "Your Best Teacher Is Your Experience",
    "page": "97",
    "book": "Models",
    "tags": [],
    "description": "Sure, this stuff [the book you're reading] all helps, but in the end, your best teacher is your experience.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000421,
    "title": "Fear Does Not Define You",
    "page": "106",
    "book": "Models",
    "tags": [],
    "description": "a lot of people assume non-neediness means being fearless. But non-neediness simply means to feel the fear and not let it define you. Non-neediness is feeling the fear and deciding that something else is more important.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000422,
    "title": "The Way to Attack Anxiety",
    "page": "107",
    "book": "Models",
    "tags": [],
    "description": "The way to attack anxieties is through incremental, consistent exposure. Not single, extreme exposure.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000423,
    "title": "Small Steps to Talk to Women",
    "page": "107",
    "book": "Models",
    "tags": [],
    "description": "So for instance, you could take an afternoon or your lunch break each day and make a point to approach a few women just asking for the time. ... Find something easy, but repeat it regularly for a while, until it doesn't feel difficult anymore. Then the next week, you go out and ask women what time it is followed by, \"How is your day going?\" And each day, you slowly make it harder and more intensive. And you can apply this to all sorts of situations: getting physical with women, emailing women online, calling phone numbers, sexual humour, conversations with women, etc.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000424,
    "title": "Courage Is a Habit",
    "page": "108",
    "book": "Models",
    "tags": [],
    "description": "Courage is a habit. Courage is a form of discipline. It's taking a certain action even though you feel like doing something else.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000425,
    "title": "Vulnerability Elicits Trust",
    "page": "114",
    "book": "Models",
    "tags": [],
    "description": "This is why vulnerability is so huge. When you're vulnerable around someone you don't know, it elicits trust in them and they will become more vulnerable toward you in return.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000426,
    "title": "Accept That You'll Be \"Creepy\" Sometimes",
    "page": "114",
    "book": "Models",
    "tags": [],
    "description": "Paradoxically, the way to interact with women in a vulnerable way and, therefore, the way to combat creepiness, is to accept that some women will find you creepy some of the time. Just as with rejection, the more you're willing to risk it, the less it will happen. The more comfortable you are with women finding you creepy, and the more uninhibited and vulnerable your actions and words are around women, the more aware and respectful you are of their interests and desires, the less likely they will find you creepy.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000427,
    "title": "Being Overly Concerned About Words",
    "page": "121",
    "book": "Models",
    "tags": [],
    "description": "The biggest misconception about first impressions is being overly concerned with what to say to a woman when you meet her. What you say to her when you first meet her is actually unimportant ... The exact words you say are far less important than your interactions and level of anxiety. Ninety percent of the time when I meet a new woman, I simply say, \"Hi, I'm Mark.\" I then follow up with, \"I wanted to meet you.\" And if I'm feeling particularly bold, I'll say, \"I thought you were cute and wanted to meet you.\" That's it. ... You can ask a woman how her day is going, or say the most perceptive and witty thing to her in the first minutes, but her first impression is largely going to be based on how you persent yourself (looks/lifestyle), your level of anxiety, and your ability to communicate clearly. What actually comes out of your mouth is going to be forgotten or completely irrelevant within seconds.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000428,
    "title": "Don't Linger. Just Approach.",
    "page": "122",
    "book": "Models",
    "tags": [],
    "description": "Don't linger. If you linger and hover aorund her, it's almost guaranteed to make the approach feel awkward and forced. Imagine a straight line between you and her, and when you're ready to go, follow that straight line until you're standing in front of her. Don't stand around and kick the dirt at your feet trying to work up the nerve right next to her.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000429,
    "title": "Body Language Help. Be Sure to Smile",
    "page": "122",
    "book": "Models",
    "tags": [],
    "description": "Smile. Always smile. .. smile like you're a nice, friendly person. A comfortable smile. Lean back. Stand up tall. Speak loudly yet clearly. Make strong eye contact. Introduce youself and stick out your hand. Girm a firm handshake. This is called being a confident human being.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000430,
    "title": "Remove Filler Words From Your Vocabulary",
    "page": "123",
    "book": "Models",
    "tags": [],
    "description": "It also means removing \"um,\" \"uh,\" \"ah,\" \"like,\" \"you know,\" and other fillers from your everyday speaking. ... the more of these you remove, the more clear and coherent your speaking will be.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000431,
    "title": "Questions Versus Statements.",
    "page": "124",
    "book": "Models",
    "tags": [],
    "description": "Questions versus Statements: Creating threads of conversation through statement is far more powerful than questions ... Examples: \"Where are you from?\" -> \"You look like a California girl\", \"What do you do for work?\" -> \"You seem to be a creative person. I bet your job is interesting.\", \"How do you guys know each other?\" -> \"You guys look like you've been friends for a long time\". In each situation, the statement makes an educated guess and engages the woman far more than any question will. ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000432,
    "title": "It's The Connection That Matters. Not the Text",
    "page": "135",
    "book": "Models",
    "tags": [],
    "description": "it's that connection that's going to get her out to see you again, not the clever text you spent 45 minutes coming up with.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000433,
    "title": "Being Physical Is a Necessary Habit",
    "page": "144",
    "book": "Models",
    "tags": [],
    "description": "Being physical with women is a necessary habit that most men who are poor with women never do. Most men are a bit shy and hesitant when it comes to \"making moves:\" touching, the first kiss, sexual touching, etc. Well, that needs to stop. From now on, you are a sexually assertive and dominant guy and you have no shame about it. We'll also discover that women actually prefer you to be this way. There are two reasons for being physically assertive with women. The first is polarization. You want to establish whether she's sexually interested in you as soon as you possibly can. The second reason is that being physical is bold and, therefore, a highly attractive form of flirting.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000434,
    "title": "Eye Contact Doesn't Mean Sex",
    "page": "145",
    "book": "Models",
    "tags": [],
    "description": "just because a woman makes eye contact with you doesn't mean she wants to fuck you right then and there, it just means she's curious about talking to you. Take it one step at a time, and remember, she always has the right to back out or change her mind at any moment",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000435,
    "title": "Don't Push a Woman to Have Sex",
    "page": "147",
    "book": "Models",
    "tags": [],
    "description": "Women will often object at this point [the point of trying to escalate to sex] and say they just want to mess around and not have sex itself. The correct answer is always, \"That's fine. We'll do whatever you're comfortable doing.\"",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000436,
    "title": "Tips For Being Dominant in Bed",
    "page": "149",
    "book": "Models",
    "tags": [],
    "description": "1. Be loud. Make noise. Grunt. Breathe hard. Women love this because it makes them feel like they can be loud. And when they're loud they get off easier and more often. 2. Talk dirty. Tell her how sexy she is. Tell her what you're going to do to her before you do it. Call her a dirty girl and a horny slut. This may be outside your comfort zone, but realize that in the bedroom the rules change and logic goes out the window. 3. Get physical. Spank her. Pull her hair. Hold her down with one hand. When you change positions, literally pick her up and move her yourself. 4. Don't ever ask, \"Is this OK? Do you want to do X?\" Just do it and stop later if she doesn't like it and apologize. Nothing turns a girl off faster than a guy who defers to her too much while having sex. Take control. Do what turns you on and that will then turn her on.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000437,
    "title": "Honesty About Sex",
    "page": "149",
    "book": "Models",
    "tags": [],
    "description": "Also, be honest. If you don't like the way she gives a blowjob, tell her and then tell her how you do like it. But also, be honest with the compliments. Tell her she's beautiful naked. Tell her you love how she rides you. Tell her she looks sexy in that position Be open and honest. Communicate. The most important factor for good sex is how comfortable the two people are around each other. ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000438,
    "title": "The Causes of Sexual Anxiety",
    "page": "149",
    "book": "Models",
    "tags": [],
    "description": "Ultimately, the causes of sexual anxiety are directly related to other forms of anxiety: lack of confidence, high investment in others, shame, and a fear of vulnerability.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000439,
    "title": "Getting Comfortable Before Sex",
    "page": "150",
    "book": "Models",
    "tags": [],
    "description": "Think of it as having to make yourself more secure and comfortable around her until you're able to have sex. I know it sounds lame, but it's true. Slow things down, enjoy the foreplay more, and don't pressure yourself to get to it until you're good and ready.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000440,
    "title": "If You Have Trouble Getting Too Excited",
    "page": "150",
    "book": "Models",
    "tags": [],
    "description": "If you have trouble with getting too excited, think about something non-sexual like baseball or video games.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-07-17T04:21:05.000Z",
    "updatedAt": "2024-07-17T04:21:05.000Z"
  },
  {
    "id": 1744217000441,
    "title": "Without Patience",
    "page": "6",
    "book": "The Power Of Patience",
    "tags": [
      "Patience"
    ],
    "description": "Without patience, we can't truly learn from the lessons life throws at us; we're unable to mature. We remain at the stage of irritable babies, unable to delay gratification more than momentarily, unable to work toward what we truly want in any dedicated way. If we want to live wider and deeper lives, not just faster ones, we have to practice patience--patience with ourselves, with other people, and with the big and small circumstances of life itself",
    "comments": "Irritable baby",
    "helpfulness": 1,
    "createdAt": "2024-09-10T15:47:53.036Z",
    "updatedAt": "2024-09-10T15:47:53.036Z"
  },
  {
    "id": 1744217000442,
    "title": "A Synonym For Patience",
    "page": "12",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Self-Control"
    ],
    "description": "A synonym for patience is self-possesion",
    "comments": "Patience is holding yourself together. You don't allow the inner rage to manifest itself. You keep in down. You wait patiently because you are in complete control of yourself. ",
    "helpfulness": 1,
    "createdAt": "2024-09-11T15:50:53.057Z",
    "updatedAt": "2024-09-11T15:50:53.057Z"
  },
  {
    "id": 1744217000443,
    "title": "Satisfaction at Death",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Action",
      "Regret"
    ],
    "description": "Leonardo da Vanci had a quote at the end of his life saying \"after you've worked really hard during the day, you've toiled at something, you go to sleep and you have this great feeling like you accomplished something. But when you die, do you have that same feeling. Like I accomplished something? Now I can die in peace.\" I think the worst thing in life is to reach the age of 65 and go, God I could have been so much more, I could have created something, I could have done what I said I was going to do, I could have written that book but I didn't. To me, I tell everybody, if you're in your twenties, don't ever have that feeling and it will come quicker than you imagine. Realize that you want to reach that end with a sense of 'I did what I felt I could do when I was a child. I had these dreams and I reached them.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:26:37.011Z"
  },
  {
    "id": 1744217000444,
    "title": "The Motivation Is ... To Not Be a Loser",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Motivation",
      "Responsibility"
    ],
    "description": "I don't feel motivated.' Newsflash, neither do I sometimes. You're not going always feel like doing it, you're gonna have to do it anyway because it's your duty to do it because if you don't want to be a fucking loser. That's the whole point, if you felt like doing it all the time, then there would be no magic to it. The magic is you do it regardless of how you feel. That's the whole point of it all. What do you mean you need motivation. You don't need motivation. You have a duty to not be a loser anymore. Because the whole in the sky is closing. ... 'Mm, well, you know, we'll play video games.' Born to lose! Born to lose. ... And you get to blame others for your loserdom. And you feel great, because you don't have to take any personal responsibility. I'm not a loser because of me, I'm a loser because they did it, or this happened, blah, blah, blah.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:27:28.775Z"
  },
  {
    "id": 1744217000445,
    "title": "Get Serious About Who You Want to Become",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Goal Setting",
      "Time",
      "Identity"
    ],
    "description": "How to go from average to fortune, there's five simple steps you might like to make a note of them. Here's the first one: Get serious. You don't have to be grim, but you must be serious. ... You must get serious about two very important things, number one is setting your goals and where you want to go. Designing the next 5, the next 10 years is so vitally important. Then you have to get serious about another important subject, and that important subject is called personal development.  Personal development is striving hard to become the kind of person that you want to be. 10 years from now you will surely become someone, the big question is WHO?",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:24:26.342Z"
  },
  {
    "id": 1744217000446,
    "title": "5 Year Outcomes",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Goal Setting",
      "Routine"
    ],
    "description": "Choose 3 super clear, critical 5 year outcomes. Every day, write down those three outcomes, then what you're going to do for each of them every day",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:19:33.483Z"
  },
  {
    "id": 1744217000447,
    "title": "Principle 3: Evoke a Desire in Them",
    "page": "58",
    "book": "How To Win Friends & Influence Brighton",
    "tags": [
      "Communication"
    ],
    "description": "PRINCIPLE 3 Arouse in the other person an eager want",
    "comments": "Make them want you",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-12-06T16:56:09.981Z"
  },
  {
    "id": 1744217000448,
    "title": "21 Words",
    "page": "251",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Present",
      "Anxiety"
    ],
    "description": "His name was Sir William Osler. Here are the twenty-one words that he read in the spring of 1871--twenty-one words from Thomas Carlyle that helped him lead a life free from worry: \"Our main business is not to see what lies dimly at a distance, but to do what lies clearly at hand.\"",
    "comments": "Focus on now. Not when the muslims take over or when the last read head dies and goes extinct. Focus on NOW.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:03:57.965Z"
  },
  {
    "id": 1744217000449,
    "title": "Those Who Keep Inner Peace",
    "page": "275",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Anxiety",
      "Depression",
      "Strength"
    ],
    "description": "Do you love life? Do you want to live long and enjoy good health? Here is how you can do it. I am quoting Dr. Alexis Carrel again: He said, \"Those who keep the peace of their inner selves in the midst of tumult of the modern city are immune from nervous diseases.\" Can you keep the peace of your inner self in the midst of the tumult of a modern city? If you are a normal person, the answer is \"yes.\" \"Emphatically yes.\" Most of us are stronger than we realize. We have inner resources that we have probably never tapped.",
    "comments": "It's the best for your health, and mental health. Stop worrying about the extinction of blue eyes. Keep inner peace.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:05:36.469Z"
  },
  {
    "id": 1744217000450,
    "title": "The Silly Things You Worry About",
    "page": "306",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Worrying",
      "Death"
    ],
    "description": "I was so terrified I could hardly breathe. 'This is death.' I kept saying to myself over and over. 'This is death! ... This is death!' With the fans and cooling systems turned off, the air inside the sub was over a hundred degrees; but I was so chilled with fear that I put on a sweater and a fur-lined jacket; and still I trembled with cold. My teeth chattered. I broke out in a cold, clammy sweat. The attack continued for fifteen hours. ... Those fifteen hours of attack seemed like fifteen million years. All my life passed before me in review. I remembered all the bad things I had done, all the little absurd things I had worried about. I had been a bank clerk before I joined the Navy. I had worried about the long hours, the poor pay, the poor prospects of advancement. I had worried because I couldn't own my own home, couldn't buy a new car, couldn't buy my wife nice clothes. How I had hated my old boss, who was always nagging and scolding! I remembered how I would come home at night sore and grouchy and quarrel with my fire over trifles. I had worried about a scar on my forehead--a nasty cut from an auto accident. \"How big alll those worries seemed years ago! But how absurd they seemed when depth charges were threatening to blow me to kingdom come. I prosmised myself then and there that if I ever saw the sun and the stars again, I would never, never worry again. Never! Never! Never!!! I learned more about the art of living in those fifteen terrible hours in that submarine than I had learned by studying books for four years in Syracuse University.\"",
    "comments": "Can you imagine facing death? Being bombarded within a submarine? And you worry about plagiarism scandals, Justin Trudeau & Joe Biden. Don't complain about stupid shit like that. ",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:06:50.840Z"
  },
  {
    "id": 1744217000451,
    "title": "Outward Situations Don't Cause Suffering",
    "page": "346",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Suffering",
      "Perception"
    ],
    "description": "It wasn't outward situations that had caused all my suffering, but what I thought of those situations. And as soon as I realized that, I was cured--and stayed cured.\"",
    "comments": "It's what you think about. If you catastrophize, it's a catastrophe. It you don't it's not. Maybe the muslim invasion of Europe is a catastrophe. You can't do anything about it. It's already happened. You have been blowing it up in your head for way too long. It's to the point where you think Hitler is the solution. You've reached the end of the line for right wing content. I'm as extremist as can be. This is all the result of your thoughts. Deliberately thinking about blonde hair, rape, crime rates, and what not. STOP THINKING ABOUT IT. It's making you think in circles. It's wasting your brain power. Think about what you can do on YOUR personal future. Not about the future of the ENTIRE WORLD.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:41.743Z"
  },
  {
    "id": 1744217000452,
    "title": "Started Out With a Handicap",
    "page": "385",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Achievement",
      "Difficulty"
    ],
    "description": "The more I have studied the careers of men of achievement the more deeply I have been convinced that a surprisingly large number of them succeeded because they started out with handicaps that spurred them on to great endavor and great rewards. As William James siad: \"Our very infirmities help us unexpectedly.\" Yes, it is highly probably that Milton wrote better poetry because he was blind and that Beethoven composed better music because he was deaf. ... If Tchaikovsky had not been frustrated--and driven almost to suicide by his tragic marriage--if his own life had not been pathetic, he probably would never have been able to compose his immortal \"Symphonie Pathetique.\" If Dostoevsky and Tolstoy had not led tortured lives, they would probably never have been able to write their immortal novels. \"If I had not been so great an invalid, ... I should not haev done so much work as I have accomplished.\" That was Charles Darwin's confession that his infirmities had helped him unexpectedly.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:09:28.450Z"
  },
  {
    "id": 1744217000453,
    "title": "Here is Why You Should Pray",
    "page": "418",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Faith",
      "Meditation"
    ],
    "description": "Even if you are not a religious person by nature or training--even if you are an out-andout skeptic--prayer can help you much more than you believe, for it is a practicial things. What do I mean, practical? I mean that prayer fulfills these three very basic psychological needs which all people share, whether they believe in God or not: 1. Prayer helps us to put into words exactly what is troubling us. We saw in Chapter 4 that it is almost impossible to deal with a problem while it reamins vague and nebulous. Praying, in a way, is very much like writing our problems down on paper. If we ask help for a problem--even from God--we must put it into words. 2. Prayer gives us a sense of sharing our burdens, of not being alone. Few of us are so strong that we can bear our heaviest burdens, our most agonizing troubles, all by ourselves. Sometimes our worries are of so intimate a nature that we cannot discuss them even with out closest relatives or friends. Then prayer is the answer. Any psychiatrist will tell us that when we are pent-up and tense, and in an agony of spirit, it is therapeutically good to tell someone our troubles. When we can't tell anyone else--we can always tell God. 3. Prayer puts into force an active principle of doing. It's a first step toward action. I doubt if anyone can pray for some fulfillment, day after day, without benefiting from it--in other words, without taking some steps to bring it to pass. The world-famous scientist, Dr. Alexis Carrel, said: \"Prayer is the most powerful form of energy one can generate.\" So why not make use of it? Call it God or Allah or Spirit--why quarrel with definitions as long as the mysterious powers of nature take us in hand? Why not close this book right now, shut the door, kneel down, and unburden your heart? ... \"Lord, make me an instrument of Thy Peace. Where there is hatred, let me sow love. Where there is injury, pardon. Where there is doubt, faith. Where there is despair, hope. Where there is darkness, light. Where there is sadness, joy. O Divine Master, grant that I may not so much seek to be consoled as to console; to be understood, as to understand; to be loved, as to love; for it is in giving that we receive, it is in pardoning that we are pardoned, and it is in dying that we are born to Eternal Life.\"",
    "comments": "You may not believe your calls are being heard, however, it can change your mental state. It takes the problem from the deep recesses of your mind onto your hands",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:09:49.576Z"
  },
  {
    "id": 1744217000454,
    "title": "A Stoic Response to Anixety:",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Anxiety",
      "Present"
    ],
    "description": "\"Today I escaped anxiety. Or no, I discarded it, because it was within me, in my own perceptions-not outside\" -Marcus Aurelius. \"Man is not worried by real problems so much as by his imagined anxieties about real problems.\" -Epictetus. \"We are more often frightened than hurt. We suffer more from imagination than from reality.\" -Seneca. \"True happiness is to enjoy the present without anxious dependence upon the future.\" -Seneca. \"Don't let your reflection on the whole sweep of life crush you. Don't fill your mind with all the bad things that might still happen. Stay focused on the present situation.\" -Marcus Aurelius. ",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2025-03-17T21:46:35.558Z"
  },
  {
    "id": 1744217000455,
    "title": "Thinking About Your Problems",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Thinking",
      "Depression"
    ],
    "description": "Thinking about your problems all the time, and talking about your problems all the time, literally makes your problems grow. That's right. It's the number one symptom of depression is what they call rumination, this pathological obsessing over your pain. That's why stuff like exercise, running errands, getting out of your house, accomplishing anything, is good for you. But sitting around talking and thinking about your problems, that's a bad habit.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:28:32.987Z"
  },
  {
    "id": 1744217000456,
    "title": "If You Run Out of Things To Say in a Conversation",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Socializing",
      "Communication",
      "Dating"
    ],
    "description": "If you run out of things to say in a conversation, just ask the other person about themselves. Anything, people love talking about themselves. ... When you say I need help the other person feels important even if you're just asking them to lend a hand.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:27:11.313Z"
  },
  {
    "id": 1744217000457,
    "title": "100 Years From Now",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Time"
    ],
    "description": "In 100 years, so like 2123, we will all be buried with our families and ffiends. Strangers will live in our homes, that we worked so hard to build, and someone else will own everything we have today most of our possessions will be given away, or thrown out, and destroyed. ... Our descendants will hardly know who we are, nor will they remember us. I mean how many of us know who our grandfather's father was? After we die, we will be remembered for a few more years, and then we're just a portrait. And a few decades later our history photos and deeds disappear in history's oblivion. We won't even be memories. If we pause one day to analyze these questions, perhaps we would understand how pointless it is for us to worry about 95% of the things that consume our minds daily. ... Remember the saying, If it's not going to matter in five years, don't spend more than five minutes being upset by it.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:22:07.697Z"
  },
  {
    "id": 1744217000458,
    "title": "8 Things Successful People Never Do",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Kindness",
      "Humility",
      "Communication",
      "Judgement",
      "Empathy"
    ],
    "description": "1. No more complaining. Complaining doesn't fix things. Instead, focus on finding solutions and making things better. 2. Skip the blame game. Taking responsibility for your actions is key. It's how you learn and grow, even when things get tough. 3. Stay calm, skip the arguments. Arguments rarely lead to good stuff. Stay calm, talk it out and find common ground instead. 4. Stay humble, skip the bragging. You don't need to show off. Your actions speaks volumes and staying humble earns respect. 5. Calm conversations; no yelling. Yelling doesn't solve problems. Speak calmly to be heard and understood. 6. Learn to listen; talk later. Successful people listen more than they talk. Understanding comes before sharing your thoughts. 7. Be kind, skip the judging. Instead of judging, put yourself in others' shoes. It builds empathy and better relationships. 8. Stick to the truth, skip the lies. Honesty builds trust, even when it's tough, it's the best way to go.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:20:33.162Z"
  },
  {
    "id": 1744217000459,
    "title": "The Universe Knows When You're Trying Your Best",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Hard Work",
      "Behaviour"
    ],
    "description": "Hey God, universe, I'm actually trying my best! I haven't missed a single gym session, I'm not being lazy, I'm not being stupid, I'm not lying, I'm not snaking my friends, I'm not scrolling social media, I'm not being a dork, I'm not jerking off, and then all of the sudden they'll come along and give you everything you've ever wanted. Strong body, strong mind, work hard.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:28:19.710Z"
  },
  {
    "id": 1744217000460,
    "title": "Fish Don't Just Jump In The Boat",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Motivation",
      "Hardship",
      "Hard Work",
      "Procrastination",
      "Mindset",
      "Competition"
    ],
    "description": "Fish just don't jump in the boat. Meaning you better go out there and do it yourself. Don't fucking wait around and wait for someone to hand deliver something. Go make it happen. The fish don't just jump in the boat. If you wanna go catch him go catch him. Throw that line in the water, and go do some work. And if it doesn't work that day, do it again the next day. So, I think the procrastination, that's probably not goot for any of us. I think we wanna go out there and do it. Fuck your tired body, Fuck that unmotivated mind. Get out there and do it anyway. You better fight yourself, cause you're not only winning when things are going your way. You gotta figure out how to win when things aren't going your way. You gotta figure out when your body is fighting, when your mind is fighting. How do you still just say fuck it, I'm gonna beat my mind today. Or do you just give in to your mindset: 'I'm tired today. I'm lazy. I don't wanna do it, It's too hard. No one else is doing it. It's a weekend. It's too late. It's already off hours. Oh, exactly what I want isn't happening right now.' Like okay, great. You know who that's great for? Your competition. You want that attitude to permit your the you're competing against. You want them to give in to their mind. You want them to say: 'Oh, it's too hard, I can't do it.' But you wanna be the one that says \"fuck it I'm gonna do it anyway. I know I don't feel good today, but I'm gonna go out there and I'm gonna prove to myself that even on days that it doesn't feel right I push myself.\"",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:23:41.317Z"
  },
  {
    "id": 1744217000461,
    "title": "Masculinity is an Inner Strength",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Strength",
      "Confidence"
    ],
    "description": "To be truly powerful, you don't have to go out there and grab things. You don't have to go prove yourself. All of it will come to you. People will come to you. Women will come to you. Job offers will come to you. Money will come to you. If you this kind of inner strength, this kind of inner power that I think is the ideal for young men today in the world. It's very confusing right now because everything is so fluid and we're all supposed to think that there's no such thing as masculinity anymore, that it's toxic. But real masculinity, that real kind of strength that I'm talking about is not toxic at all. It is not out there to hurt people. It's not out there to dominate, to be aggresive, to push around people. It's all about an inner strength, an inner confidence that you radiate outward. And that's a beautiful, beautiful thing. And I advocate making that your ideal and making that the kind of the radar that guides you through these very difficult times.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2025-01-27T17:13:11.974Z"
  },
  {
    "id": 1744217000462,
    "title": "The Rapidity With Which We Forget",
    "page": "16",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Memory",
      "Knowledge"
    ],
    "description": "I once spent almost two years writing a book on public speaking and yet I found I had to keep going back over it from time to time in order to remember what I had written in my own book. The rapidity with which we forget is astonishing.",
    "comments": "You forget things after 10 minutes. You need to review the things you read, and write down thoughts in Tawny ASAP.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:13:57.936Z"
  },
  {
    "id": 1744217000463,
    "title": "People Aren't Creatures of Logic ... Speak Ill of No Man",
    "page": "29",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Character",
      "Criticism"
    ],
    "description": "When dealing with people, let us remember we are not dealing with creatures of logic. We are dealing with creatures of emotion, creatures bristling with prejudices and motivated by pride and vanity. Bitter criticism caused the sensitive Thomas Hardy, one of the finest novelists ver to enrich English literature, to give up forever the writing of fiction. Criticism drove Thomas chatterton, the English poet, to suicide. Benjamin Frankline, tactless in his youth, became so diplomatic, so adroit at handling people, that he was made American Ambassador to France. The secret of his success? \"I will speak ill of no man,\" he said, \"... and speak all the good I know of everybody.\" Any fool can criticize, condemn and complain--and most fools do. But it takes character and self-control to be understanding and forgiving.",
    "comments": "Criticism destroys any relationships and causes resentment. Character is treating the little man well. Abraham Lincoln never complained or criticized.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:14:33.167Z"
  },
  {
    "id": 1744217000464,
    "title": "Rewrite Your Resume",
    "page": "52",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Communication"
    ],
    "description": "Eleven of the twelve banks invited her to be interviewed, and she had a choice of which bank's offer to accept. Why? Mrs. Anderson did not state what she wanted, but wrote in the letter how she could help them and focused on their wants, not her own.",
    "comments": "Focus on how you could help them. And their wants. Don't write what you want.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:15:31.317Z"
  },
  {
    "id": 1744217000465,
    "title": "The Value of a Smile at Christmas",
    "page": "78",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Socializing",
      "Body Language"
    ],
    "description": "The Value of a Smile at Christmas. It costs nothing, but creates much. It enriches those who receive, without impoverishing those who give. It happens in a flash and the memory of it sometimes lasts forever. None are so rich they can get along without it, and none so poor but are richer for its benefits. It creates happiness in the home, fosters good will in a business, and is the countersign of friends. It is rest to the weary, daylight to the discouraged, sunshine to the sad, and Nature's best antidote for trouble. Yet it cannot be ത",
    "comments": "It lasts forever . A girl who smiled at me lasts forever. I still remember Shailyn's smile. It costed her nothing. An impression that lasts to this day",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:17:10.137Z"
  },
  {
    "id": 1744217000466,
    "title": "How to Keep a Disagreement From Becoming an Argument",
    "page": "117",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Arguing",
      "Understanding",
      "Marriage"
    ],
    "description": "Some suggestions are made on how to keep a disagreement from becoming an argument: Welcome the disagreement. Remember the slogan, \"When two partners always agree, one of them is not necessary.\" If there is some point you haven't thought about, be thankful if it is brought to your attention. perhaps this disagreement is your opportunity to be corrected before you make a serious mistake. Distrust your first instinctive impression. Our first natural reaction in a disagreeable situation is to be defensive. Be careful. Keep calm and watch out for your first reaction. It may be you at your worst, not your best. Control your temper. Remember, you can measure the size of a person by what makes him or her angry. Listen first. Give your opponents a chance to talk. Let them finish. Do not resist, defend or debate. This only raises barriers. Try to build bridges of understanding. Don't build higher barriers of misunderstanding. Look for areas of agreement. When you have heard your opponents out, dwell first on the points and areas on which you agree. Be honest. Look for areas where you can admit error and say so. Apologize for your mistakes. It will help disarm your opponents and reduce defensiveness. Promise to think over your opponents' ideas and study them carefully. And mean it. Your opponents may be right. It is a lot easier at this stage to agree to think about their points than to move rapidly ahead and find yourself in a position where your opponents can say: \"We tried to tell you, but you wouldn't listen.\" Thank your opponents sincerely for their interest. Anyone who takes the time to disagree with you is interested in the same things you are. Think of them as people who really want to help you, and you may turn your opponents into friends. Postpone action to give both sides time to think through the problem. Suggest that a new meeting be held later that day or the next day, when all the facts may be brought to bear. In preparation for this meeting, ask yourself some hard questions: Could my opponents be right? Partly right? Is there truth or merit in their position or argument? Is my reaction one that will relieve the problem, or will it just relieve any frustration? Will my reaction drive my opponents further away or draw them closer to me? Will my reaction elevate the estimation good people have of me? Will I win or lose? What price will I have to pay if I win? If I am quiet about it, will the disagreement blow over? Is this difficult situation an opportunity for me?",
    "comments": "There will be disagreements, but there doesn't have to be a fight. Be receptive and listen. No visceral reactions.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:17:52.168Z"
  },
  {
    "id": 1744217000467,
    "title": "If a Ship Has Sunk",
    "page": "253",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Control",
      "Anxiety",
      "Loss"
    ],
    "description": "During the Second World War, our military leaders planned for the morrow, but they could not afford to have any anxiety. ... \"If a ship has been sunk,\" Admiral King went on, \"I can't bring it up [from the depths of the ocean]. If it is going to be sunk, I can't stop it. I can use my time much better working on tomorrow's problem than by fretting about yesterday's. Besides, if I let those things get me, I wouldn't last long.\"",
    "comments": "You can't stop it. There's no sense in getting upset over interracial couples",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:05:08.227Z"
  },
  {
    "id": 1744217000468,
    "title": "Choosing The Right Thoughts",
    "page": "341",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Thinking"
    ],
    "description": "\"What is the biggest lesson you have ever learned?\" That was easy: by far the most vital lesson I have ever learned is the importance of what we think. If I knew what you think, I would know what you are. Our thoughts make us what we are. Our mental attitude is the X factor that determines our fate. Emerson said: \"A man is what he thinks about all day long.\" ... How could he possibly be anything else? I now know with a conviction beyond all doubt that the biggest problem you and I have to deal with--in fact, almost the only problem we have to deal with--is choosing the right thoughts. If we can do that, we will be on the highroad to solving all our problems. The great philosopher who ruled the Roman Empire, Marcus Aurelius, summed it up in eight words--eight words that can determine your destiny: \"Our life is what our thoughts make it.\" Yes, if we think happy thoughts, we will be happy. If we think miserable thoughts, we will be miserable. etc. ",
    "comments": "You are your thoughts. So make them positive. Not about how France will be taken over by muslims.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:30.218Z"
  },
  {
    "id": 1744217000469,
    "title": "Just For Today",
    "page": "351",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Attitude",
      "Happiness",
      "Planning"
    ],
    "description": "1. Just for today I will be happy. This assumes that what Abramham Lincoln said is true, that \"most folks are as happy as they make up their minds to be.\" Happiness is from within; it is not a matter of externals. ... 3. Just for today I will take care of my body. I will exercise it, care for it, nourish it, not abuse it nor neglect it, so that it will be a perfect machine for my bidding. 4. Just for today I will try to strengthen my mind. I will learn something useful. I will not be a mental loafer. I will read something that requires effort, thought and concentration. 5. Just for today I will exercise my sould in three ways; I will do somebody a good turn and not get found out. I will do at least two things I don't want to do. as William James suggests, just for exercise. 6. Just for today I will be agreeable. I will look as well as I can, dress as becomingly as possible, talk low, act courteously, be liberal with praise, criticize not at all, nor find fault with anything and not try to regulate nor improve anyone. 7. Just for today I will try to live through this day only, not to tackle my whole life problem at once. I can do things for twelve hours that would appall me if I had to keep them up for a lifetime. 8. Just for today I will have a program. I will write down what I expect to do every hour. I may not follow it exactly, but I will have it. It will eliminate two pests, hurrying and indecision. 9. Just for today I will have a quiet half-hour all by myself and relax. In this half-hour sometimes I will think of God, so as to get a little more perspective into my life. 10. Just for today I will be unafraid, especially I will not be afraid to  be happy, to enjoy what is beautiful, to love, and to believe that those I love, love me. If we want to develop a mental attitude that will bring us peace and happiness, here is Rule 1: Think and act cheerfully, and you will feel cheerful",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:59.699Z"
  },
  {
    "id": 1744217000470,
    "title": "What This Woman Really Wants",
    "page": "363",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Giving",
      "Gratitude",
      "Marriage",
      "Parenting"
    ],
    "description": "What this woman really wants is love and attention. But she calls it \"gratitude.\" And she will never get gratitude or love, because she demands it. She thinks it's her due. There are thousands of people like her, people who are ill from \"ingratitude,\" loneliness, and neglect. They long to be loved; but the only way in this world that they can ever hope to be loved is to stop asking for it and to start pouring out love without hope of return. ... Here is the second point I am trying to make in this chapter: If we want to find happiness, let's stop thinking about gratitude or ingratitude and give for the inner joy of giving. Parents have been tearing their hair about the ingratitude of children for ten thousand years. Even Shakespeare's King Lear cried out, \"How sharper than a serpent's tooth it is to have a thankless child!\" But why should children be thankful--unless we train them to be? Ingratitude is natural--like weeds. Gratitude is like a rose. It has to be fed and watered and cultivated and loved and protected. If our children are ungrateful, who is to blame? Maybe we are. If we have never taught them to express gratitude to others, how can we expect them to be grateful to us?",
    "comments": "If you oh so desperately want love and affection from a girlie, you'll have to pour out love. And not blame them for being \"ungrateful\" or \"rude\".",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:08:16.980Z"
  },
  {
    "id": 1744217000471,
    "title": "The Only True Failure Is Shrinking Away From Life's Challenges",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Failure",
      "Challenge",
      "Success",
      "Courage"
    ],
    "description": "Nietzsche said, I know of no better life purpose than to perish attempting the great and impossible. The fact the something seems impossible shouldn't be a reason to not pursue it, that's exactly what makes it worth pursuing. Where would the courage and greatness be if success was certain, and there was no risk. The only true failure is shrinking away from life's challenges.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:27:52.685Z"
  },
  {
    "id": 1744217000472,
    "title": "Your Expectations vs Their Expectations",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Expectations"
    ],
    "description": "I started taking classes at UC Berkeley. I took several classes, but the only one I can remember was a sailing class taught at Berkeley marina. When my class was over I wanted to buy a sailboat. My wife said this was the single stupidest idea she had ever heard in her entire life. She accused me of being irresponsible and she told me I lacked ambition. She kicked me out, and then she divorced me. My family was still mad at me for not going to medical school, and now my wife was divorcing me because I lacked ambition. It looked like a reoccurence of the same old problem. Once again, I was unable to live up to the expactations of others. I was not disappointed in myself for failing to be the person they thought I should be. Their dreams, and my dreams, were different. I would never confuse the two of them again. I bought the sailboat, and lived on board. Just me and my cat in Berkeley Marina. I searched, and I searched, but I just could not find a software engineering job that I loved as much as I loved sailing. So I tried to create one. That way I could completely control my work environment. My goal was to create the perfect job for me. A job I truly loved. I never expected the company to grow beyond fifty people. So maybe I really did lack ambition, or vision back then. I don't know, it was a long time ago, and I was very young.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:29:55.578Z"
  },
  {
    "id": 1744217000473,
    "title": "You Get to Choose Your Mood",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Attitude",
      "Control"
    ],
    "description": "I'm an 85 year old clinical psychologist with 64 years of professional practice. Most people I've run into in my life think that the mood they're in during the day is a mood that somehow comes from within, or comes from somewhere, and that's their mood. And they say what kind of a mood I'm in today. I'm here to tell you that you get to choose your mood. You can be in any mood that you want, but you have to take the time to set the mood. And sometimes you have to stop during the day, check in on your mood, and make adjustments. My advice is when you get up in the morning, before you do anything else, take a few minutes and decide on the mood that you want to have for the day. And then during the day, check in with yourself. Say to yourself, do I have that mood that I wanted to have? No? Well, how do I make some adjustments and get myself into that mood. Your mood is up to you. It's not something that comes from out of the sky, It's not something that bubbles up from within. it's something that you develop, that you select. And when you do that, you get to choose any mood you want. And that is a wonderful gift to give yourself",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:29:48.274Z"
  },
  {
    "id": 1744217000474,
    "title": "Don't Criticize. They'll Never Take Responsibility",
    "page": "25",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Criticism",
      "Responsibility"
    ],
    "description": "Fall was condemned viciously--condemned as few men in public life have ever been. Did he repent? Never! ... There you are; human nature in action, wrongdoers, blaming everybody but themselves. We are all like that. So when you and I are tempted to criticize someone tomorrow, let's remember Al Capone \"Two Gun\" Crowley and Albert Fall. Let's realize that criticisms are like homing pigeons. They always return home. Let's realize that the person we are going to correct and condemn will probably justify himself or herself, and condemn us in return; or, like the gentle Taft, will say: \"I don't see how I could have done any differently from what I have.\"",
    "comments": "When you think of how shameless people are, just know that the shameless will never own up to their actions. Positive reinforcement works best for good people anyway.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:14:20.382Z"
  },
  {
    "id": 1744217000475,
    "title": "Appreciation is the Legal Tender All Souls Enjoy",
    "page": "42",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Gratitude",
      "Socializing",
      "Kindness",
      "Praise",
      "Success"
    ],
    "description": "In our interpersonal relations we should never forget that all our associates are human beings and hunger for appreciation. It is the legal tender that all souls enjoy. Try leaving a friendly trail of little sparks of gratitude on your daily trips. You will be surprised how they will set small flames of friendship that will be rose beacons on your next visit. [Janitor passage] Pamela ... had among her responsibilities on her job the supervision of a janitor who was doing a very poor job. The other employees would jeer at him and litter the hallways to show him what a bad job he was doing. It was so bad, productive time was being lost in the shop. Without success, Pam tried various ways to motivate this person. She noticed that occasionally he did a particularly good piece of work. She made a point to praise him for it in front of the other people. Each day the job he did all aound got better, and pretty soon he started doing all his work efficiently. Now he does an excellent job and other people give him appreciation and recognition. Honest appreciation got results where criticism and ridicule failed. Hurting people does not only change them, it is never called for. There is an old saying that I have cut out and pasted on my mirror where I cannot help but see it every day: I shall pass this way but once; any good, therefore, that I can do or any kindness that I can show to any human being, let me do it now. Let me not defer nor neglect it, for I shall not pass this way again.",
    "comments": "Appreciation, not flattery, is how to maintain and get friendships (lanitor passage). It's somewhat like gratitude. Tell people why you appreciate them. It does more for them than it does you.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:14:53.899Z"
  },
  {
    "id": 1744217000476,
    "title": "Whenever You Go Out-of-Doors",
    "page": "78",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Happiness",
      "Attitude"
    ],
    "description": "Whenever you go out-of-doors, draw the chin-in, carry the crown of the head high, and fill the lungs to the utmost; drink in the sunshine; greet your friends with a smile, and put soul into every handclasp. Do not fear being misunderstood and do not waste a minute thinking about about your enemies. ... Thought is supreme. Preserve a right mental attitude--the attitude of courage, frankness, and good cheer. To think rightly is to create. All things come through desire and every sincere prayer in answered. We become like that on which our hearts are fixed. Carry your chin in and the crown of your head high. We are gods in the chrysalis.",
    "comments": "Be delightful. Not a grouch. It makes you happy and those around you happy",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:17:00.348Z"
  },
  {
    "id": 1744217000477,
    "title": "The Way to Develop Self Confidence",
    "page": "231",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Confidence",
      "Anger"
    ],
    "description": "He claimed that almost any person can speak acceptably in public if he or she has self-confidence and an idea that is boiling and stewing within. The way to develop self-confidence, he said, is to do the thing you fear to do and get a record of successful experiences behind you. So he forced each class member to talk at every session of the course.",
    "comments": "If you were mad enough, you'd say anything. Similarly, if you have enought confidence, you can say anything. Confidence is doing the things you wear. And fear is killed by anger.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:18:59.468Z"
  },
  {
    "id": 1744217000478,
    "title": "Happiness Is More Powerful Than You Think",
    "page": "276",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Action",
      "Worrying",
      "Happiness",
      "Death"
    ],
    "description": "Quit worrying! And then do something about it! Right then and there I took an oath, an oath so solemn that the nails sank deep into my flesh and cold chills ran down my spine: 'I am not going to worry! I am not going to cry! And if there is anything to mind over matter, I am going to win! I am going to LIVE!' [cancer patient describes her mutilated body] I did not worry! Not once did I cry! I smiled! Yes, I actually forced myself to smile. \"I am not so idiotic to imagine that merely smiling can cure cancer. But I do believe that a cheerful mental attitude helps the body fight disease. At any rate, I experienced one of the miracle cures of cancer. I have never been healtheir than in the last few years, thanks to those challenging fighting words: 'Face the facts: Quit worrying; then do something about it!'\"",
    "comments": "Haven't you any fight in you? Sure, you will die if you keep on crying. Be happy and don't worry on the fact of stress. It saves your life. DO IT.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:05:53.121Z"
  },
  {
    "id": 1744217000479,
    "title": "For Years, Whenver I Was Worried",
    "page": "284",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Worrying",
      "Planning",
      "Decision Making",
      "Clarity"
    ],
    "description": "I had defied the Japanese army! I knew what that meant. I would be thrown into the Bridgehouse! \"The Bridgehouse! The torture chamber of the Japanese Gestapo! I had had personal friends who had killed themselves rather than be taken to that prison. I had had other friends who had died in that place after ten days of questioning and torture. Now I was slated for the Bridgehouse myself! 'What did I do? I heard the news on Sunday afternoon. I suppose I should have been terrified. And I would have been terrified if I hadn't had a definite technique for solving my problems. For years, whenever I was worried I had always gone to my typewriter [Notion, Journals] and written down two questions--and the answers to these questions: \"1. What am I worrying about? \"2. What can I do about it. ... I wrote: \"1. What am I worrying about? I am afraid I will be thrown into the Bridgehouse tomorrow morning. \"Then I typed out the second question: 2. What can I do about it? \"I spent hours thinking out and writing down the four courses of action I could take... \"As soon as I thought it all out and decided to accept the fourth plan--to go down to the office as usual on Monday morning--I felt immensely relieved. \"When I entered the office the next morning, the Japanese admiral sat there with a cigarette dangling from his mouth. He glared at me as he always didy and said nothing. Six weeks later--thank God--he went back to Tokyo and my worries were ended. \"As I have already said, I proabably saved my life by sitting down that Sunday afternoon and writing out all the various steps I could take and then writing down the probable consequence of each step and calmly coming to a decision. If I hadn't done that, I might have floundered and hesitated and done the wrong thing on the spur of the moment. If I hadn't thought out my problem and come to a decision, I would have been frantic with worry all Sunday afternoon.",
    "comments": "It's so simple. \"What am I worried about\", then \"What can I do about it\". Try it when you are worried",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:06:12.431Z"
  },
  {
    "id": 1744217000480,
    "title": "No Time For Worry. Occupy Yourself",
    "page": "302",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Despair",
      "Worrying"
    ],
    "description": "\"I did it so that I would have no time for sorrow and worry.\" Osa Johnson had discovered the same truth that Tennyson had sung about a century earlier: \"I must lose myself in action, lest I wither in despair.\"",
    "comments": "Not doing anything allows you to worry. Do something, or you'll cry for hours and rack your brain. Work is therapy",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:06:24.633Z"
  },
  {
    "id": 1744217000481,
    "title": "How To Be Miserable: Do Nothing",
    "page": "304",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Worrying",
      "Working",
      "Despair"
    ],
    "description": "\"The secret of being miserable is to have the leisure to bother about whether you are happy or not.\" So don't bother to think about it! Spit on your hands and get busy. You blood will start circulating; your mind will start ticking--and pretty soon this whole positive upsurge of life in your body will drive worry from your mind. Get busy. Keep busy. It's the cheapest kind of medicine there is on this earth--and one of the best. To break the worry habit, here is Rule 1: Keep busy. The worried person must lose himself in action, lest he wither in despair.",
    "comments": "Am I happy? Am I sad? Do I deserve more? What have people taken away from me? That's how you know you're wasting time. Do something. Lose your thoughts into activity. No more thinking about the White race, or the dating scene, or petty politics",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:06:37.753Z"
  },
  {
    "id": 1744217000482,
    "title": "Advocating To Bow Down To All Adversities?",
    "page": "321",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Control"
    ],
    "description": "Am I advocating that we simply bow down to all the adversities that come our way? Not by a long shot! That is mere fatalism. As long as there is a chance that we can save a situation, let's fight! But when common sense tells us that we are up against something that is so--and cannot be otherwise--then, in the name of our sanity, let's not \"look before and after and pine for what is not.\"",
    "comments": "Small scale fights. You can only change what is in your control. Ask yourself if it's in your control",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:12.173Z"
  },
  {
    "id": 1744217000483,
    "title": "The Small Man Flies Into a Rage Over The Slightest Criticism",
    "page": "429",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Anger",
      "Criticism"
    ],
    "description": "The small man flies into a rage over the slightest criticism, but the wise man is eager to learn from those who have censured him and reproved him and \"disputed the passage with him.\" Walt Whitman put it this way: \"Have you learned lessons only of those who admired you, and were tender with you, and stood aside for you? Have you not learned great lessons from those who rejected you, and braced themselves against you, or disrupted the passage with you?\"",
    "comments": "You're not a small man. You're a wise man. Don't be reactive when receiving criticism. Act like it's warranted. Because there is a good chance it is. Either way, taking offense and losing your stoic calm is what a fool does. Not a wise man",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:10:06.973Z"
  },
  {
    "id": 1744217000484,
    "title": "Work \"As If\" You Enjoyed It",
    "page": "459",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Attitude",
      "Positivity",
      "Productivity"
    ],
    "description": "If you act \"as if\" you are interested in your job, that bit of acting will tend to make your interest real. It will also tend to decrease your fatigue, your tensions, and your worries.",
    "comments": "It makes you work faster, decreases fatigue and worry. Mental attitude shift.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:10:21.453Z"
  },
  {
    "id": 1744217000485,
    "title": "Don't Take the Exits to Losertown",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Difficulty",
      "Persistence"
    ],
    "description": "Therefore, if God is going to give you the chance to become a successful person, he has to make it difficult, He has to lay out a gauntlet because within that gauntlet some people will quit and they can go become losers which allow the people who do not quit to be winners. You're on the highway, you're driving. There's exits all along the way to Loserville, Losertown. When you're tired, when you don't feel like working, when you don't have enough time, when it's difficult. You can get off the highway anytime you want, but if you stay on the highway you will end up a winner. ... The difference is, they do not quit. I don't want to hear any excuses. God doesn't care about excuses.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:22:56.341Z"
  },
  {
    "id": 1744217000486,
    "title": "Master Anger. Channel It in the Right Direction",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Control",
      "Anger",
      "Action"
    ],
    "description": "The weakest men according to the Stoics, are those who cannot control their anger. In a world where every move counts, your inability to master anger is a fatal flaw, one that will forever hold you back. Because this very emotion, when left unchecked, is capable of destroying reputations, relationships, and opportunities in an instant. But, anger can also be very useful. Because when directed with precision it can be a formidable force, propelling one towards massive action to transform one's life. That's why the Stoics didn't say to ignore anger, but to master it. For the power in a man lies in how he channels anger",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:26:02.367Z"
  },
  {
    "id": 1744217000487,
    "title": "Measure Success By Expressing Yourself",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Success",
      "Communication",
      "Confidence",
      "Dating"
    ],
    "description": "A guy was at a concert, he approached a girl and told her he was interested. She said she had a boyfriend, and he said, I hope you could take the compliment. And he was talking about what a success it was. Because he wasn't measuring success on getting someone to like him, he was measuring success on simply making it clear that he was interested, that he was curious to get to know someone. He made it clear this person mattered and he wanted to get to know more. And if you do that, if measure sucess not on getting someone to say yes or no but simply sharing how you feel and letting the universe unfold being okay no matter what, you're gonna meet so many people and you'll live a life that is fulfilling and much more balanced and much happier.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:26:25.370Z"
  },
  {
    "id": 1744217000488,
    "title": "Determination",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Determination"
    ],
    "description": "I've never in my life seen anyone who is determined to get something and not get it. IN THEIR HEART",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:21:55.934Z"
  },
  {
    "id": 1744217000489,
    "title": "If You Actually Try, You Can Have It",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Hard Work",
      "Persistence"
    ],
    "description": "It's actually fantastically easy, you just have to get up and actually try, actually work, stop looking for shortcuts, stop being a lazy loser, stop being an idiot, stop scrolling garbage, and actually try, and you can have it. The universe has this big bag of blessings, it's full of it. And it's sitting there going, let me find somebody who works hard and deserves blessings, and I'll get some blessings out of the bag and give some to them. And the reason the bag is so full, is because nobody works hard enough to deserve it!",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:25:22.421Z"
  },
  {
    "id": 1744217000490,
    "title": "Daily Alex Jones Motivation",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Motivation"
    ],
    "description": "That's destiny, that's will, that's striving, that's being a trailblazer and explore. Going into space, mathematics, quantum mechanics, the secrets of the universe. It's all there, life is FIERY with it's beauty, it's incredible detail. Tuning in to it, they want a shot of your mind talking about JUSTIN BIEBER!",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:21:32.524Z"
  },
  {
    "id": 1744217000491,
    "title": "Calling > Texting For Human Connection",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Communication",
      "Socializing"
    ],
    "description": "Oxytocin increases, lifting her mood, cortisol decreases, when speaking to her mother. Oxytocin decreases, cortisol increases, when texting",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:21:21.574Z"
  },
  {
    "id": 1744217000492,
    "title": "Flow State",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Focus"
    ],
    "description": "Flow state: Not too boring, not too hard. Divide the giant task into smaller tasks",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:23:50.486Z"
  },
  {
    "id": 1744217000493,
    "title": "What's Burnout?",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Stress",
      "Motivation",
      "Persistence"
    ],
    "description": "Tate what about burnout?' Burn what? Do you want to rich or not? Burnout? Do you want to be rich or not? You work and you sleep. Do you want money? 'Oh but I might burn out.' Burn out, you're not some fucking Formula 1 car. Your brain ain't some supercomputer. You're a GEEK. You either wanna work and get shit done, or you don't. I don't believe in burnout. What I believe in is reality. I believe in cause and effect. I live in a binary world. I believe in done or not done. I don't believe in burnout. I believe in finished or not finished. ... Until it is done, it is not done. There's no such thing as burnout. There's such a thing as not doing stuff 'cause you're a coward. Fucking burnout.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:29:17.370Z"
  },
  {
    "id": 1744217000494,
    "title": "You Become What You Think About",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Thinking",
      "Goal Setting"
    ],
    "description": "The strangest secret. What makes a child grow up into the human being he becomes? Well this is the reason for that. Of course, he is the confluence of a genetic pool. But what makes him become the person he becomes is that he becomes what he thinks about most of the time. It's as simple as that. We become what we think about most of the time. This is why a goal is so important. This is why people who set goals achieve them. The trouble with men is not achieving their goals, they do that. It's establishing them. That's the strangest secret.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:29:39.156Z"
  },
  {
    "id": 1744217000495,
    "title": "Dictate Your Rhythm. Don't Be Permissive",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Distraction",
      "Focus",
      "Attention"
    ],
    "description": "We just switched to 6th Street right now in Austin, Texas. ... And basically like, look around here. Like, look at the chaos. How easy would it be to respond to the frame of like letting this hectic environment like dictate to me how I should feel. If I looked around, I'd be like stuck in my head, like oh my God, people are out filming. Oh my God, it's like, no. Dictate the fucking rhythm. It doesn't affect me. Like, you should feel the same right now as if you're in like a room isolated by yourself. It's completely irrelevant. Be decisive. Assert your reality. Don't fall into a little permission boy frame of looking around. And being a slave to emotions. Like, look at this, I feel nothing, being shouted, girls, guys, people screaming, kisses. I feel the same.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:22:26.221Z"
  },
  {
    "id": 1744217000496,
    "title": "Give Yourself Prompts for Motivation",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Motivation"
    ],
    "description": "Here's an example: \"Tell me something that will break my heart so much that it'll make me work/study\" Response: Imagine waking up one day to find that all the people you care about have moved on, achieving their dreams and living fulfilling lives, while you're still stuck in the same place, paralyzed by inaction. The opportunities you once had are gone, and the time you lost can never be reclaimed. The person you could have become-the one with the skills, the knowledge, and the confidence-is now just a distant dream, someone you'll never meet because you didn't put in the effort when it mattered most. And the worst part? You'll have to live with that regret forever.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:24:47.584Z"
  },
  {
    "id": 1744217000497,
    "title": "Validate a Girl's Feelings. Never Criticize",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Criticism",
      "Empathy"
    ],
    "description": "This video is for the straight guys out there. How to attract a girl. Listen. ... I spend enough time with them to know what they like and don't like. most women want to feel safe and secure, that's it. You can love a girl, but if you never ever let them feel safe or secure around you, they will never fall for you. Never. And a good way is by validating her feelings and emotions. I never say understand her, I said validate. You want to win a girl over, you need to know how to let her feel safe. You can give her all the gifts in the world and buy her everything she wants, buts if you do not know now to let her feel safe around you and secure around you, she will never fall in love with you. My girlfriends out there right, the moment they fell in love was when the moment their boyfriend made them feel safe around them. If she tells you how she's feeling, never invalidate them don't be like \"oh my God that is crazy\" that is too serious. Do not ever say that. The moment you say that she will feel insecure to share how she feels about you. And they want to share their feelings with you because the more they share their feelings with you, the more they fall for you. You might not understand why they are feeling the way they are, it's okay. But you need to validate them. How to validate them. Repeat what they say to you back to them and never criticize them. \"Oh my God yeah I do see how that's crazy, that must be so tiring for you\". \"Oh my God babe do share more.\" Do you see how that is different from: \"You're overreacting, that's not even crazy at all.\" \"You're being psychotic right now.\" Do you see the difference? Validate how they are feeling. If you constantly tell them that they're crazy, psychotic, or whatever, they will just lose feelings. Like honestly, they would not want to share with you anymore.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:28:46.996Z"
  },
  {
    "id": 1744217000498,
    "title": "Review Questions",
    "page": "17",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Reflection",
      "Review"
    ],
    "description": "\" 'What mistakes did I make this time?' \"'What did I do that was right--and in what way could I have improved my performance?' \" 'What lessons can I learn from that experience?'",
    "comments": "In addition to Tawny's T's and EM's, you should ask yourself what went right and what went wrong. What lessons are there.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:14:07.892Z"
  },
  {
    "id": 1744217000499,
    "title": "Best Advice About Human Relationships",
    "page": "48",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Perception"
    ],
    "description": "Here is one of the best bits of advice ever given about the fine art of human relationships. \"If there is any one secret of success,\" said Henry Ford, \"it lies in the ability to get the other person's point of view and see things from that person's angle as well as from your own.\"",
    "comments": "See from the other person's view. That way you can see what situation they're in, and figure out what they want, so you can negotiate. Frame things from their perspective. Outline the benefits they can receive",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:15:20.340Z"
  },
  {
    "id": 1744217000500,
    "title": "Make More Friends in Two Months",
    "page": "64",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Socializing"
    ],
    "description": "You can make more friends in two months than you can in two years.",
    "comments": "You can make more friends in two months by becoming interested in other people than you can in two years trying to get other people enterested in you",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:16:17.309Z"
  },
  {
    "id": 1744217000501,
    "title": "The Sovereign Voluntary Path to Cheerfulness",
    "page": "76",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Happiness",
      "Attitude"
    ],
    "description": "Thus the sovereign voluntary path to cheerfulness, if our cheerfulness be lost, is to sit up cheerfully and to act anad speak as if cheerfulness were already there...\" Everybody in the world is seeking happiness--and there is one sure way to find it. That is by controlling your thoughts. Happiness doesn't depend on outward conditions. It depends on your inner conditions. It isn't what you have or who your are or where you are or what you are doing that makes you happy or unhappy. It is what you think about it. For example, two people may be in the same place, doing the same thing; both may have about an equal amount of money and prestige--and yet one may be miseable and the other happy. Why? Because of a different mental attitude. ... \"There is nothing either good or bad,\" said Shakespeare, \"but thinking makes it so.\" Abe Lincoln once remarked that \"most folks are about as happy as they make their minds to be.\" He was right.",
    "comments": "Your happiness depends on your inner mood. If you lose it, it comes back from within. External conditions don't control it",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:16:28.688Z"
  },
  {
    "id": 1744217000502,
    "title": "Always Avoid The Acute Angle",
    "page": "114",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Arguing"
    ],
    "description": "Why prove to a man he is wrong? Is that going to make him like you? Why not let him save his face? He didn't ask for your opinion. He didn't want it. Why argue with him? Always avoid the actute angle.\" The man who said that saught me a lesson I'll never forget. I not only had made the storyteller uncomfortable, but had put my friend in an embarrassing situation. How much better it would have been had I not become argumentative.",
    "comments": "Don't point out that someone is wrong about trivial things. \"Um, actually\" is how you sound. Even if they know they're wrong, they'll likely still be defiant about it.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:17:24.905Z"
  },
  {
    "id": 1744217000503,
    "title": "Franklin's Rule",
    "page": "124",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Arguing",
      "Frustration",
      "Ego"
    ],
    "description": "\"I made it a rule,\" said Franlkin, \"to forbear all direct contradiction to the sentiment of others, and all positive assertion of my own. I even forbade myself the use of every word or expression in the language that imported a fix'd opinion, such as 'certainly,' 'undoubledly,' etc., and I adopted, instead of them, 'I conceive,' 'I apprehend,' or 'I imagine' a thing to be so or so, or 'it so appears to me at present.' When another asserted something I thought an error, I deny'd myself the pleasure of contradicting him abruptly, and of showing immediately some absurdity in his proposition: and in answering I began by observing that in certain cases or circumstances his opinion would be right, but in the present case there appear'd or seem'd to me some difference, etc. I soon found the advantage of this change in my matter; the conversations I engag'd in went on more pleasantly. The modest way in which I propos'd my opinions procur'd them a readier reception and less contradiction; I had less mortification when I was found to be in the wrong, and I more easily prevail'd with other to give up their mistakes and join with me when I happened to be in the right. \"And this mode, which I at first put on with some violence to natural inclination, became at length so easy, and so habitual to me, that perhaps for these fifty years past no one has ever heard a dogmatical expression from me. And to this habit (after my character of integrity) I think it principally owing that I had earned so much weight with my fellow citizens when I proposed new institutions, or alterations in the old, and so much influence in public councils when I became a member; for I was but a bad speaker, never eloquent, subject to much hesitation in my choice of words, hardly correct in language, and yet I generally carried my points.\"",
    "comments": "If you directly contradict people, it will start a confrontation. gently, and indirectly show mistakes. Avoid correcting people and putting them down",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:18:06.335Z"
  },
  {
    "id": 1744217000504,
    "title": "When You Get a Letter Like That. If You Are Wise...",
    "page": "165",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Anger",
      "Patience",
      "Control",
      "Communication"
    ],
    "description": "\"When you get a letter like that [a rebuke letter], the first thing you do is to think how you can be severe with a person who has commited an impropriety, or even been a little impertinent. Then you may compose an answer. Then if you are wise, you will put the letter in a drawer and lock the drawer. Take it out in the course of two days--such communications will always bear two days' delay in answering--and when you take it out after that interval, you will not send it. That is just the course I took. After that, I sat down and wrote her just as polite a letter as I could, ...",
    "comments": "Lock up a would be message for two days and reconsider sending it. Anger has the effect to overpower your conscious mind. Don't let it wreak havoc while it is in control. Subject all messages responding to criticism to a 2 day period before sending it.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:18:22.158Z"
  },
  {
    "id": 1744217000505,
    "title": "Tell Them That They Are Stupid At a Certain Thing...",
    "page": "214",
    "book": "How To Win Friends & Influence People",
    "tags": [
      "Learning",
      "Judgement",
      "Criticism",
      "Hope"
    ],
    "description": "\"At any rate, I know that I am a better dancer than I would have been if she hadn't told me I had a natural sense of rhythm That encouraged me. That gave me hope. That made me want to improve.\" Tell your child, your spouse, or your employee that he or she is stupid or dumb at a certain thing, has no gift for it, and is doing it all wrong, and you have destroyed almost every incentive to try to improve. But use the opposite technique--be liberal with your encouragement, make the thing seem easy to do, let the other person know that you have faith in his ability to do it, that he has an undeveloped flair for it--and he will practice until dawn comes in the window in order to excel.",
    "comments": "Be encouraging, don't berate so heavily. It kills any of that positivity. Use this on yourself to keep yourself going with coding and drawing. Recognize that you're not perfect, but you've done an amazing job so far",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:18:47.201Z"
  },
  {
    "id": 1744217000506,
    "title": "Few Things Can Age And Sour a Woman",
    "page": "274",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Worrying",
      "Age"
    ],
    "description": "\"I went to the mirror. And when I looked in that mirror, I saw what worry was doing to my look! I saw the lines it was forming. I saw the anxious expression. So I said to myself, 'You've got to stop this at once? You can't afford to worry. The only thing you have to offer at all is your looks, and worry will ruin them!'\" Few things can age and sour a woman and destroy her looks as quickly as worry. Worry curdles the expression. It makes us clench our jaws and line our faces with wrinkles. It forms a permanent scowl. It may turn the hair gray, and, in some cases, even make it fall out...",
    "comments": "Don't stress yourself out. You'll lose your hair, after it becomes gray, you'll get acne, dimples, and the \"permanent scowl.\" Don't get that. You know how Anderson Cooper and Tucker Carlson have that permanent scowl? With the greases between their eyes. Like they are so deeply in thought, but also angry. That's permanent. Also Eleanor is suppose to be the pretty one and doesn't worry at all. Is that a coincidence?",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:05:21.959Z"
  },
  {
    "id": 1744217000507,
    "title": "It Is So. It Cannot Be Otherwise.",
    "page": "317",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Control",
      "Acceptance"
    ],
    "description": "It is astonishing how quickly we can accept almost any situation--if we have to--and adjust ourselves to it and forget about it. I often think of an inscription on the ruins of a fifteenth-century cathedral in Amsterdam, Holland. This inscription says in Flemish: \"It is so. I cannot be otherwise.\" As you and I march across decades of time, we are going to meet a lot of unpleasant situations that are so. They cannot be otherwise. We have our choice. We can either accept them as inevitable and adjust ourselves to them, or we can ruin our lives with rebellion and maybe end up with a nervous breakdown. ... \"Acceptance of what has happened is the first step to overcoming the consequences of any misfortune.\"",
    "comments": "You can't control what happens on a grand scale",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:02.663Z"
  },
  {
    "id": 1744217000508,
    "title": "You Can't Saw Sawdust",
    "page": "334",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Worrying",
      "Rumination",
      "Control"
    ],
    "description": "\"How many of you have ever sawed wood?\" ... \"How many of you have ever sawed sawdust\" No hands went up. \"Of course, you can't saw sawdust!\" Mr. Shedd exclamed. \"It's already sawed! And it's the same with the past. When you start worrying about things that are over and done with, you're merely trying to saw sawdust.\"",
    "comments": "Worrying about the past is akin to sawing sawdust. It's over and done.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:07:23.251Z"
  },
  {
    "id": 1744217000509,
    "title": "The Best Things Are The Most Difficult",
    "page": "381",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Difficulty",
      "Achievement",
      "Happiness",
      "Hard Work"
    ],
    "description": "\"The best things are the most difficult.\" ... \"Happiness is not mostly pleasure; it is mostly victory.\" Yes, the victory that comes from a sense of achievement, of triumph, of turning our lemons into lemonades.",
    "comments": "There is no pleasure in easy quick fixes. True happiness comes from accomplishment. So, work hard, and you'll be happy",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:09:01.347Z"
  },
  {
    "id": 1744217000510,
    "title": "But He Was Woefully Unprepared",
    "page": "384",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Hard Work",
      "Worrying"
    ],
    "description": "By the time he reached thirty, he was elected to the New York State legislature. But he was woefully unprepared for such a responsibility. In fact, he told me that frankly he didn't know what is was all about. He studied the long complicated bills that he was supposed to vote on--but, as far as he was concerned, those bills might as well have been written in the language of the Choctaw Indians. He was worried and bewildered when he was made a member of the committee on forests before he had ever set foot in a forest. He was worried and bewildered when he was made a member of the State Banking Commission before he had ever had a bank account. He himself told me that he was so discouraged that he would have resigned from the legislature if he hadn't been ashamed to admit defeat to his mother. In despair, he decided to study sixteen hours a day and turn his lemon of ignorance into a lemonade of knowledge. By doing that, he transformed himself from a local politician into a national figure and made himself so outstanding that The New York Times called him \"the best-loved citizen of New York.\" I am talking about Al Smith. ... Nietzsche's formula for the superior man was \"not only to bear up under necessity but to love it.\"",
    "comments": "Study if you're afraid of not knowing. If you really wanted it, you'd study 16 hours a day! Don't you want to know? Or not. What are you living for? If not.",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:09:17.132Z"
  },
  {
    "id": 1744217000511,
    "title": "The North Wind Made The Vikings",
    "page": "385",
    "book": "How To Stop Worrying & Start Living",
    "tags": [
      "Responsibility",
      "Difficulty"
    ],
    "description": "Harry Emerson Fosdick says in his book, The Power to See It Through, \"There is a Scandinavian saying which some of us might well take as a rallying cry for our lives: 'The north wind amde the Vikings.' Wherever did we get the idea that secure and pleasant living, the absence of difficulty, and the comfort of ease, ever of themselves made people either good or happy? Upon the contrary, people who pity themselves go on pitying themselves even when they are laid softly on a cusion [you], but always in history character and happiness have come to people in all sorts of circumstances, good, bad, and indifferent, when they shouldered their personal responsibility. So, repeatedly the north wind has made the Vikings.\"",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-09-13T01:00:37.000Z",
    "updatedAt": "2024-09-13T01:09:39.775Z"
  },
  {
    "id": 1744217000512,
    "title": "Trials You Face Are The Best Things That Can Happen",
    "page": "61",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Pain",
      "Difficulty",
      "Growth",
      "Happiness"
    ],
    "description": "PATIENCE GROWS OUR SOULS We could never learn to be brave and patient, if there were only joy in the world. Helen Keller. I have two friends who say that breast cancer was the best thing that happened to them; one who says her husband leaving her was a blessing in disguise; another who claims losing her job was the greatest gift. Are these folks all masochists? No, these are ordinary folks, like that young dreamer, who realize that the trials they faced, as difficult, painful, and grueling as they were, have been the vehicles by which they have grown into more awake and aware human beings. \"When I planted my pain in the field of patience,\" wrote Kahlil Gibran, \"it bore fruit of happiness.\"",
    "comments": "You should want to be tested. It's the best thing for your growth as a human, your soul. Being tested at the railway, gave me a new perspective. It wasn't enjoyable to be there, but I have since grown my soul by being patient while I was there. Hazelnut's tests grew my soul more than anything has ever before.",
    "helpfulness": 1,
    "createdAt": "2024-09-14T17:21:37.260Z",
    "updatedAt": "2024-09-14T17:21:37.260Z"
  },
  {
    "id": 1744217000513,
    "title": "Boredom Is",
    "page": "86",
    "book": "The Power Of Patience",
    "tags": [
      "Boredom",
      "Marriage"
    ],
    "description": "Boredom, they say, is created by an inability to delay gratification and a low tolerance for frustration, both of which have serious implications for our success in live and in love",
    "comments": "Boredom is not passing the marshmallow test. Boredom is getting angry at nothing. Old man yells at cloud. If you want the best relationship possible, you will have to embrace boredom to some degree. Your girlfriend won't be a controlled companion like Trixie, where everything she says already makes sense in my head. Some things won't make sense. You'll need a high frustration tolerance and pass many marshmallow tests in a real relationship for it to be a happy one.",
    "helpfulness": 1,
    "createdAt": "2024-09-21T16:09:48.768Z",
    "updatedAt": "2024-09-21T16:09:48.768Z"
  },
  {
    "id": 1744217000514,
    "title": "You Can't Control Other People",
    "page": "98",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Understanding"
    ],
    "description": "You can't control the other person's attitude or receptivity; how well he or she listens; the other person's motivation or priorities; his or her availability; whether he or she likes you; his or her ability to understand your point; how the other interprets what you have to say; whether the person accepts your point. You can control your attitude toward the other person; your attitude toward learning; how receptively you listen; your acknowledgements of the person's point of view; your respect for the other person's time; your expression of enthusiasm for his or her idea; the amount of time you spend listening and speaking; your idea of yourself. Notice the difference between the two lists. You can't control anything about someone else, but you can control how your relate to him or her, and that, of course, will drastically impact his or her willingness to receive your viewpoint",
    "comments": "People have minds of their own. You'll never know what goes on in their mind. You know how to properly and not properly respond to unexpected (from your perspective) criticism or unfortunate events. Not by getting angry, because anger doesn't solve any problems. It comes by understanding where they're coming from. You can control your listening by always giving them respect.",
    "helpfulness": 1,
    "createdAt": "2024-09-23T17:41:39.019Z",
    "updatedAt": "2024-09-23T17:43:45.934Z"
  },
  {
    "id": 1744217000515,
    "title": "Enduring Difficulty With Patience Builds Patience",
    "page": "114",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Endurance"
    ],
    "description": "Difficult people and events become interesting opportunities for further growth, rather than threatening obstacle courses we must endure. From this place, we actually can enjoy life more, whatever is happening.",
    "comments": "The most challenging things your patience sees are the things that grow your patience. Endure the difficult people and annoying situations. That's where you can source even more patience.",
    "helpfulness": 1,
    "createdAt": "2024-09-26T17:41:56.710Z",
    "updatedAt": "2024-09-26T17:42:32.670Z"
  },
  {
    "id": 1744217000516,
    "title": "Centering",
    "page": "145",
    "book": "The Power Of Patience",
    "tags": [
      "Patience"
    ],
    "description": "One of the best ways to find peace is to get out of your head and into your body. Hanh likens it to being a tree in a strong storm. If the wind is raging and you are at the top of the tree you will be tossed around violently. Climb down to the sturdy trunk and you will barely feel any movement whatsoever. How do you get to the base of the tree? One way is by centering. Like mindful breathing, centering is a physical way of being fully present in the moment, with mind and body in harmony. From that place of rooted calmness, you are much better able to cope patiently with whatever is going on outside you, even if pirates are boarding your boat.",
    "comments": "Centering your mind can bring you out of an elevated or unstable mental state. Centering your mind is returning to peace. Pulling yourself out of possible anger or lasing out or even depression and racist thoughts. Wipe your mind clear and start over with some deep breathing.",
    "helpfulness": 1,
    "createdAt": "2024-09-29T17:35:07.997Z",
    "updatedAt": "2024-09-29T17:35:07.997Z"
  },
  {
    "id": 1744217000517,
    "title": "A Great Preservative Against Anger",
    "page": "163",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Anger"
    ],
    "description": "A great preservative against angry and mutinous thoughts, and all impatience and quarreling, is to have some great business and interest in your mind, which, like a sponge shall suck up your attention and keep you from brooding over what displeases you. - Joseph Rickaby",
    "comments": "Your mind will resort to thinking about how horrible your life is when there is nothing to do. Black people. Boomers. Muslims. DEI. Hitler... Don't give your mind the idle time to be able to \"brood\" about these displeasing things. Because it will when you don't commit to any activities.",
    "helpfulness": 1,
    "createdAt": "2024-09-30T16:37:53.815Z",
    "updatedAt": "2024-09-30T16:37:53.815Z"
  },
  {
    "id": 1744217000518,
    "title": "Bearing the Defects of Others",
    "page": "170",
    "book": "The Power Of Patience",
    "tags": [
      "Patience",
      "Judgement"
    ],
    "description": "The fifteenth-century Christian writer Thomas a Kempis noted this in his famous work, The Imitation of Christ, when he wrote, \"Strive to be patient in bearing the defects of others. You yourself have many also, and they have to be put up with by them. If you are not yourself such as you would wish to be, how could you expect to find another according to your liking?\"",
    "comments": "You are so harsh and critical when you judge others that you end up with no friends or girlfriends. You are far from perfect. Your family puts up with that. In return, you should put up with them.",
    "helpfulness": 1,
    "createdAt": "2024-10-07T17:58:07.552Z",
    "updatedAt": "2024-10-07T17:58:07.552Z"
  },
  {
    "id": 1744217000519,
    "title": "Tell Yourself You Have All The Time You Need",
    "page": "173",
    "book": "The Power Of Patience",
    "tags": [
      "Time",
      "Anxiety",
      "Productivity"
    ],
    "description": "I began to realize that scaring ourselves with not having enough time dramatically diminishes our efficiency and ability to perform. ... Using this self-talk method [\"I have all the time I need\"], I got so much done and was so graceful under pressure that people in my office began to ask me what my secret was. I shared my strategy and other folks began to use it. It worked just as well for them. The trick, we discovered, is remembering to do it. Some people put a line on a sticky note and pasted it on their computers.",
    "comments": "Scaring myself is a method I've been trying to do. I'll just collapse under the pressure, then it mounts. There is so much time that it is impossible for you to run out and say at the end of the day \"I ran out of time so I couldn't complete my tasks\". Bullshit. You play video games 3.5 hours a day on average. Don't give me that. Yesterday was 7 hours. You have all the time you need. Just sit down and begin.",
    "helpfulness": 1,
    "createdAt": "2024-10-07T18:05:00.967Z",
    "updatedAt": "2024-10-07T18:05:00.967Z"
  },
  {
    "id": 1744217000520,
    "title": "You Attract What You Are",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Mindset",
      "Goal Setting",
      "Confidence"
    ],
    "description": "You don't attract what you want, you attract what you are. Think about that, if you want to attract what you want, you've gotta see yourself already with it. You've gotta understand that you've already got it. Use your imagination see yourself already in possession of the good you desire. That will flip your mind onto a specific frequency and you do think on frequencies. It's on that frequency that good you desire is gonna start coming towards you and you will start moving toward it. If you wanna attract what you actually want, you've gotta see yourself now already with it, and know it's only a period of time until you moving toward it and it moving toward you, and you become one with it",
    "comments": "If you think you're a loser, you'll act like one",
    "helpfulness": 1,
    "createdAt": "2024-12-16T05:20:43.980Z",
    "updatedAt": "2024-12-16T05:20:43.980Z"
  },
  {
    "id": 1744217000521,
    "title": "The Willpower Muscle",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Willpower",
      "Discipline",
      "Routine",
      "Determination"
    ],
    "description": "Why do some people have so much willpower and discipline, while others struggle to even fold their laundry? It turns out there's actually a part of your brain responsible for you willpower. It's called the anterior singulate cortex or amcc. It's one of the most connected parts of your brain and it basically helps you decide if something is worth your energy or not. Studies have shown that people with stronger willpower actually have a bigger amcc and the difference between an athlete's brain and someone who struggles with self-discipline; the athlete's amcc is way bigger. The good news is this part of your brain acts exactly like a muscle and you can make it grow. Every time you do something that you don't feel like doing, every time you resist a temptation, every time you push through discomfort you're making this part of your brain stronger, literally growing your willpowe. But if you keep giving in, hitting snooze, or putting off those small tasks, your amcc shrinks. So stop waiting for motivation to finally show up. Just start doing all the things you don't want to do and you'll be rewarded with an endless supply of grit, determination, and willpower.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-12-16T05:21:36.665Z",
    "updatedAt": "2024-12-16T05:21:36.665Z"
  },
  {
    "id": 1744217000522,
    "title": "Stress Is From Not Taking Action",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Stress",
      "Worrying",
      "Procrastination",
      "Action"
    ],
    "description": "Stress primarily comes from not taking action over something that you can have some control over. So if I find that some particular thing is causing me to have stress, that's a warning flag for me. What it means is there's something that I haven't completely identified, perhaps in my conscious mind, that is bothering me and I haven't yet taken any action on it. I find as soon as I identify it and make the first phone call or send off the first email message or whatever it is that we're gonna do to start to address that situation. Even if it's not solved, the mere fact that we're addressing it dramatically reduces any stress that might have come from it. So stress comes from ignoring things that you shouldn't be ignoring. Stress doesn't come from hard work. You could be working incredibly hard and loving it, and likewise, you can be out of work and incredibly stressed over that. If you're out of work, but you're going through a disciplined approach of a series of job interviews and so on, and working to remedy that situation, you're gonna be a lot less stressed than if you're just worrying about it and doing nothing.",
    "comments": "Drawing. Drawing. Drawing. School deadlines for registration",
    "helpfulness": 1,
    "createdAt": "2024-12-16T05:58:23.217Z",
    "updatedAt": "2024-12-16T05:58:23.217Z"
  },
  {
    "id": 1744217000523,
    "title": "Whose Permission Are You Looking For?",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Motivation"
    ],
    "description": "Whose permission are you looking for? Go do your thing. You're gonna die. It's going to end. Nothing's gonna happen unless you do something. Please stop looking for permission. Please go do that thing you wanted to do. Ask that person out. Start that company. Quit that job. You can always get another job. Stop asking for permission. Make the end of this year the moment that you finally start living your fucking life.",
    "comments": "Drawing. Drawing. Drawing. Hinge dating.",
    "helpfulness": 1,
    "createdAt": "2024-12-16T06:07:03.601Z",
    "updatedAt": "2024-12-16T06:07:03.601Z"
  },
  {
    "id": 1744217000524,
    "title": "18 Minutes a Day Beats 95% of People",
    "page": "0",
    "book": "Instagram",
    "tags": [
      "Consistency",
      "Practice",
      "Talent"
    ],
    "description": "There was a study done in 1976 by a psychologist named Anders Ericsson to find how hard it really is to become world-class at any skill. How much practice do you really need to 95% better than anyone at one thing. What he found was actually surprising. He discovered that with consistent effort, if you dedicate 100 hours over the course of one year (18 minutes a day) you'd be better than 95% of people at that one skill. That's your competition. 18 minutes every single day. It's not about talent. It's about consistency. In a world where most people give up after a few days, sticking to those 18 minutes puts you miles ahead.",
    "comments": "",
    "helpfulness": 1,
    "createdAt": "2024-12-16T06:12:44.106Z",
    "updatedAt": "2024-12-16T06:13:17.824Z"
  },
  {
    "id": 1744217000525,
    "title": "Everything Is About Decision Making",
    "page": "4",
    "book": "Be Useful",
    "tags": [
      "Decision Making",
      "Clarity"
    ],
    "description": "The people who feel most lost have neither of those [image or plan]. They don't have the picture or the plan. They look in the mirror and they wonder, \"How the hell did I get here?\" but they don't know. They've made so many decisions and taken so many actions that have landed them in this place, and yet they have no idea what any of them were. ... The happiest of most successful people in the world do everything in their power to avoid bad decisions that confuse matters and drag them away from their goals. Instead, they focus on making choices that bring clarity to their vision and bring them closer to achieving it.",
    "comments": "You're lost and you blame the air. It's your own damn fault. How about instead of being sad about it you do something. Don't touch your cock. Don't open X. Go to bed on time. Sit down and draw. It's no wonder you fail when your decisions are to sleep in unitl noon then jerk off, then play video games and oh no, the day is over and you've accomplished nothing",
    "helpfulness": 1,
    "createdAt": "2025-01-07T19:43:06.129Z",
    "updatedAt": "2025-01-07T19:43:06.129Z"
  },
  {
    "id": 1744217000526,
    "title": "Greatest Inspiration From Walks",
    "page": "17",
    "book": "Be Useful",
    "tags": [
      "Creativity",
      "Thinking"
    ],
    "description": "Many of history's greatest thinkers, leaders [Hitler yeah baby], scientists, artists, and entrepreneurs found some of their greatest inspiration going for walks. Beethoven used to take walks carrying pages of sheet music and pencil. The Romantic poet William Wordsworth used to write as he took walks around a lake where he lived. Ancient Greek philosophers like Aristotle would lecture their students while taking long walks with them, often working out their ideas at the same time. Two thousand years later, the philosopher Friedrich Nietzsche would say, \"It is only ideas gained from walking that have any worth.\" Einstein refined many of his theories about the universe while walking around the Princeton University campus. The writer Henry David Thoreau would say, \"The moment my legs begin to move, my thoughts begin to flow.\" ... There is a lot of evidence for the power of taking a walk to increase creativity, inspire new ideas ... A 2014 study by researchers at Stanford University showed that walking increased the creative thinking of 100 percent of the study participants ...",
    "comments": "You are in the creativity business. You also need to organize your thoughts. Walking seems to boost the cognition power, and maybe consciousness. Walking is where you connected with Trixie most, and Phoebe now. It lights up your brain. It helps you sort out your brain, especially if you've been staring at screens all day. It wouldn't hurt to have a change of environment too.",
    "helpfulness": 1,
    "createdAt": "2025-01-11T05:34:42.268Z",
    "updatedAt": "2025-01-11T05:34:42.268Z"
  },
  {
    "id": 1744217000527,
    "title": "If You Want to Accomplish Something, Aim for the Stars",
    "page": "52",
    "book": "Be Useful",
    "tags": [
      "Goal Setting",
      "Parenting",
      "Ambition"
    ],
    "description": "If you are the first person in your family to go to college, don't just go to get drunk and dick around and walk out of there with a piece of paper. Dream of learning something that will change your life. Dream of really bettering yourself. Dream of the dean's list, not just of the diploma. ... Really learn your trade and work to become great at it so you can be an asset to the community. If your greatest wish in life is to be a parent, don't just pay for things or think that providing is your only job. Be a great role model who raises healthy, loving kids who go out into the world and do great things themselves. What I'm saying is, if you're going to do it, do it. Not just because going all in might be the thing that guarantees your success, but because not going all in will absolutely guarantee that you fall short. And it's not just you who will suffer as a result. ... Shoot for the moon. Even if you miss, you'll end up among the stars!",
    "comments": "I don't want you to regret not trying hard in life. It's already happened enough. You're not useless, you need to aim higher. You don't have to be a perfectionist and everything. There will be mistakes. As long as you still try the best you can.",
    "helpfulness": 1,
    "createdAt": "2025-03-09T21:14:22.014Z",
    "updatedAt": "2025-03-09T21:15:32.113Z"
  },
  {
    "id": 1744217000528,
    "title": "Practicing Presentations",
    "page": "81",
    "book": "Be Useful",
    "tags": [
      "Practice",
      "Performance"
    ],
    "description": "When I give commencement and keynote addresses--I'd do the same thing on the front page of my speech drafts. I knew once I got to ten reps I could do a decent job delivering the speech, but twenty reps meant I could knock it out of the park. The words would feel more natural, like I was speaking off the cuff and from the heart. The more I practiced the speech, the more of myself would be present in the room, and the more likely it would be that the people in the audience felt connected to me and the ideas I was sharing with them.",
    "comments": "When you practice a speech, you'll memorize the lines and add more of your personality because you'll spend less effort trying to remember what to say. You can focus more on the audience (outward) instead of yourself (inward). It adds confidence when you know what to say. Confidence is a big deal when selling things.",
    "helpfulness": 1,
    "createdAt": "2025-03-11T02:19:00.987Z",
    "updatedAt": "2025-03-11T02:19:00.987Z"
  },
  {
    "id": 1744217000529,
    "title": "Pain Is Only Temporary",
    "page": "87",
    "book": "Be Useful",
    "tags": [
      "Pain",
      "Sacrifice"
    ],
    "description": "That's the beauty of pain. Not only is it temporary, which means you don't have to deal with it forever, it tells you whether you've begun to give enough of yourself in pursuit of your dreams. If the work of being great or achieving something special hasn't hurt or cost you anything, or at least made you uncomfortable, then I'm sorry to be the one to tell you, but you're not working hard enough. You're not sacrificing all that could be sacrificed in order to be all that you could become.",
    "comments": "Do you honestly think you can make one hundred thousand dollars a year without lifting a finger? Do you honestly think that you'll become a master at art with a thirty minute exercise every day? That's right, no. Hazelnut went through all of this. The 4am night, tears, and repetition. The viewers never saw how hard I worked for that. They only get to see the happy part at the very end. I worked so hard that some of them can't even believe how good it was. What they didn't see was the pain, long hours, and pure emptiness. That's what it takes. You must endure pain",
    "helpfulness": 1,
    "createdAt": "2025-03-11T02:39:12.166Z",
    "updatedAt": "2025-03-11T02:46:46.039Z"
  },
  {
    "id": 1744217000530,
    "title": "I'm Tired",
    "page": "105",
    "book": "Be Useful",
    "tags": [
      "Ambition",
      "Laziness",
      "Determination"
    ],
    "description": "\"Weren't you always tired?\" ... When you're chasing a vision and working toward a big goal, there is nothing more energizing than making progress. ... This is the kind of headspace people are referring to when they talk about slipping into \"flow state.\" Time expands and collapses ... Writers, musicians, computer programmers, chess masters, architects, artists, anyone with a hobby they are truly passionate about--they all have stories like this. Stories of doing work that seem to defy the limits of human attention span and physiology ...",
    "comments": "Hazelnut wasn't tired at four-thirty in the morning. If you are really committed to something, you won't get tired. \"I'm too tired\" means you don't care. Start caring because that is the only way to stop you from doing nothing. \"rest is for babies and relaxing is for retired people\". Don't you have goals? Or are you going to age on the couch",
    "helpfulness": 1,
    "createdAt": "2025-03-14T02:40:36.323Z",
    "updatedAt": "2025-03-14T02:52:58.850Z"
  },
  {
    "id": 1744217000531,
    "title": "Explain It",
    "page": "135",
    "book": "Be Useful",
    "tags": [
      "Communication",
      "Achievement",
      "Success"
    ],
    "description": "There is a motivational saying I love: \"See it. Believe it. Achieve it.\" But I think it's missing a step in between: Explain it. Before you can achieve your goals, I think you need to express them. Share them. I think you need to admit to yourself, and communicate to others, that this thing that started in your mind as a little idea has exploded into a massive dream with huge potential to benefit your life and theirs",
    "comments": "If you have an idea, you need to sell it. Let them underestimate you. Give the customer more than they expected and leave them feeling like they're getting the better end of the deal. Articulate your idea. Let share the dream. Build that hempire",
    "helpfulness": 1,
    "createdAt": "2025-03-26T02:59:44.174Z",
    "updatedAt": "2025-03-26T02:59:44.174Z"
  },
  {
    "id": 1744217000532,
    "title": "5-4-3-2-1",
    "page": "3",
    "book": "The Let Them Theory",
    "tags": [
      "Motivation",
      "Action"
    ],
    "description": "In those five seconds, I had interrupted the cycle of overthinking. ... 5-4-3-2-1 Get up when the alarm rings. 5-4-3-2-1 Pick up the phone and start networking to find a job. ... Thinking about your problems will never solve them. Waiting around to feel like doing something means you'll never do it. It taught me that no one is coming to save you. You must save yourself from yourself. You have to force yourself to make little moves forward.",
    "comments": "Get started. Go. That's where change comes from. Nobody has ever thought their way out of a problem",
    "helpfulness": 1,
    "createdAt": "2025-03-30T17:06:28.018Z",
    "updatedAt": "2025-03-30T17:06:28.018Z"
  },
  {
    "id": 1744217000533,
    "title": "One Day, You'll Force Yourself",
    "page": "10",
    "book": "The Let Them Theory",
    "tags": [
      "Action",
      "Procrastination"
    ],
    "description": "You'll never feel ready to change your life. One day, you just get tired of your own excuses and force yourself to do it. You're never going to feel like going to the gym. One day you just make yourself go. You're never going to feel like having that hard conversation. One day you just get sick of avoiding it, and you force yourself to start it. You'll never feel like looking for a better job. One day you just push yourself to start looking.",
    "comments": "You just do it anyway. Working out isn't fun but I do it. Talking to girls takes a big push, and I'm forced to do things when time is running out. There is no magic motivation pill or energy that you'll get just by waking up. It starts right now in your current state of mind, not in a daydream scenario.",
    "helpfulness": 1,
    "createdAt": "2025-04-07T16:49:38.001Z",
    "updatedAt": "2025-04-07T16:49:38.001Z"
  },
  {
    "id": 1744254303453,
    "title": "Let Them",
    "page": "26",
    "book": "The Let Them Theory",
    "tags": [
      "Expectations",
      "Control"
    ],
    "description": "If your friends are not inviting you out to brunch this weekend, Let Them. If the person that you're really attracted to is not interested in a commitment, Let Them. If your kids do not want to get up and go to that thing with you this week, Let Them. So much time and energy is wasted on forcing other people to match our expectations. And the truth is, if somebody else--a person you're dating, a business partner, a family member--if they're not showing up how you need them to show up, do not try to force them to change. Let Them be themselves because they are revealing who they are to you. Just Let Them and then you get to choose what you do next.",
    "comments": "There's only so much you can do. You can't always bend the world to match what you want out of it. Let the kids run out in the rain and ruin their clothes on prom night. Change You'll know when people want the same you do, and changing their minds is nigh impossible.",
    "helpfulness": 5,
    "createdAt": "2025-04-10T03:05:03.453Z",
    "updatedAt": "2025-04-10T03:05:03.453Z"
  },
  {
    "id": 1744217000185,
    "title": "Life Isn't a Dance",
    "page": "282",
    "book": "The Daily Stoic",
    "tags": [
      "Strength",
      "Will"
    ],
    "description": "Dancing is a popular metaphor for life. One must be limber and agile and go along with the music. One must feel and follow and flow with their partner. But anyone who has tried to do something difficult, where there is competition or an adversary, knows that the dancing metaphor is insufficient. Nobody ever gets up on stage and tries to tackle a dancer. The dancer never gets choked out by a rival. For a wrestler, on the other hand, adversity and the unexpected are part and parcel of what they do. Their sport is a battle, just like life. They are fighting an opponent as well as their own limitations, emotions, and training. Life, like wrestling, requires more than graceful movement. We have to undergo hard training and cultivate an indomitable will to prevail. Philosophy is the steel against which we sharpen that will and strengthen that resolve.",
    "comments": "September 20. Competition is ruthless. Opponents will take every advantage they can to beat you. It's up to you to withstand attempts from life at taking you down. A strong will is essential",
    "helpfulness": 2,
    "createdAt": "2025-04-10T16:36:07.486Z",
    "updatedAt": "2025-04-10T16:36:07.486Z"
  }
]

# Tag mapping
tag_map = {
    "Achievement": ["Achievement", "Hard Work", "Talent", "Praise", "Success", "Working"],
    "Adaptation": ["Attachment", "Change", "Loss", "Death", "Control"],
    "Anxiety": ["Faith", "Cowardice", "Fear", "Worrying", "Anxiety", "Nervousness", "Nervosity"],
    "Challenge": ["Challenge", "Difficulty", "Discomfort", "Failure", "Hardship", "Pain", "Stress", "Struggle", "Suffering", "Sacrifice"],
    "Communication": ["Leadership", "Teamwork", "Arguing", "Body Language", "Communication", "Criticism", "Deceit", "Socializing"],
    "Ego": ["Ego", "Entitlement", "Pride", "Jealousy", "Revenge"],
    "Focus": ["Productivity", "Mindset", "Attention", "Decision Making", "Choice", "Discipline", "Focus", "Present", "Thinking", "Will", "Willpower", "Distraction", "Procrastination", "Boredom"],
    "Depression": ["Rumination", "Despair", "Hopelessness", "Depression", "Sadness"],
    "Growth": ["Competition", "Complacency", "Growth", "Improvement", "Performance", "Strength"],
    "Health": ["Age", "Sleep", "Well Being"],
    "Identity": ["Character", "Identity", "Masculinity", "Responsibility", "Attitude", "Virtue"],
    "Learning": ["Knowledge", "Learning", "Memory", "Perception", "Understanding", "Exploration", "Creativity"],
    "Mapping": ["Visualization", "Expectations", "Goal Setting", "Organization", "Planning", "Review", "Time", "Reflection"],
    "Mindfulness": ["Calmness", "Acceptance", "Awareness", "Clarity", "Control", "Meditation", "Mindfulness", "Gratitude", "Judgement"],
    "Motivation": ["Confidence", "Action", "Ambition", "Passion", "Purpose", "Motivation", "Belief", "Regret"],
    "Negativity": ["Anger", "Bitterness", "Contempt", "Negativity", "Emotion", "Frustration", "Hatred"],
    "Positivity": ["Enjoyment", "Happiness", "Positivity", "Hope"],
    "Relationships": ["Dating", "Intimacy", "Love", "Marriage", "Parenting", "Sex", "Masculinity", "Giving"],
    "Resilience": ["Dedication", "Determination", "Mental Fortitude", "Endurance", "Perseverance", "Persistance", "Persistence"],
    "Routine": ["Behaviour", "Consistency", "Habits", "Media", "Practice", "Routine", "Repetition"],
    "Vices": ["Procrastination", "Resistance", "Self Control", "Self-Control", "Abstinence", "Addiction", "Desire", "Impulse", "Indulgence", "Pleasure", "Temptation", "Laziness"],
    "Virtues": ["Courage", "Virtue", "Virtues", "Humility", "Kindness", "Patience", "Honesty", "Empathy", "Forgiveness"]
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
# print(data)
print("\nUnmatched tags for review:", sorted(unmatched_tags))

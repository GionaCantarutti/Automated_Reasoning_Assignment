from TestBatch import TestBatch

BASIC_BATCHES = [
    TestBatch(
        "Trivial",
        n=5,
        tilecount=15,
        reps=20
    ),
    TestBatch(
        "Easy",
        n=10,
        tilecount=60,
        reps=10
    ),
    TestBatch(
        "Medium",
        n=11,
        tilecount=100,
        reps=4
    ),
    TestBatch(
        "Hard",
        n=12,
        tilecount=90,
        reps=2
    ),
    TestBatch(
        "Extreme",
        n=15,
        tilecount=120,
        reps=1
    )
]

HARD_BATCHES = [
    TestBatch(
        "Trivial",
        n=10,
        tilecount=60,
        reps=20
    ),
    TestBatch(
        "Easy",
        n=18,
        tilecount=180,
        reps=10
    ),
    TestBatch(
        "Medium",
        n=25,
        tilecount=340,
        reps=5
    ),
    TestBatch(
        "Hard",
        n=30,
        tilecount=470,
        reps=3
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=560,
        reps=2
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=850,
        reps=1
    )
]

EXTREME_BATCHES = [
    TestBatch(
        "Restricted tiles",
        n=33,
        tilecount=548,
        reps=2
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=600,
        reps=3
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=850,
        reps=2
    ),
    TestBatch(
        "Uber",
        n=42,
        tilecount=970,
        reps=2
    )
]

EXTREME_QUICK = [
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=600,
        reps=2
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=850,
        reps=2
    ),
    TestBatch(
        "Uber",
        n=42,
        tilecount=970,
        reps=2
    )
]

EXTREME_DETAILED = [
    TestBatch(
        "Restricted tiles very hard",
        n=33,
        tilecount=548,
        reps=3
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=600,
        reps=3
    ),
    TestBatch(
        "Restricted tiles extreme",
        n=40,
        tilecount=810,
        reps=3
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=880,
        reps=3
    ),
    TestBatch(
        "Uber",
        n=42,
        tilecount=970,
        reps=3
    )
]

EXAUSTIVE = [
    TestBatch(
        "Toy",
        n=6,
        tilecount=41,
        reps=10
    ),
    TestBatch(
        "Trivial",
        n=10,
        tilecount=56,
        reps=10
    ),
    TestBatch(
        "Easy",
        n=18,
        tilecount=179,
        reps=10
    ),
    TestBatch(
        "Medium",
        n=25,
        tilecount=343,
        reps=6
    ),
    TestBatch(
        "Hard",
        n=30,
        tilecount=495,
        reps=4
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=598,
        reps=3
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=880,
        reps=2
    )
]

TRIVIAL_BATCHES = [
    TestBatch(
        "Very Trivial",
        n=5,
        tilecount=15,
        reps=5
    ),
    TestBatch(
        "Trivial",
        n=7,
        tilecount=27,
        reps=5
    ),
    TestBatch(
        "Easy",
        n=10,
        tilecount=56,
        reps=3
    ),
]

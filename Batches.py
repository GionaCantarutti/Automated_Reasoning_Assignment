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
        n=50,
        tilecount=1375,
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
        n=50,
        tilecount=1375,
        reps=2
    )
]
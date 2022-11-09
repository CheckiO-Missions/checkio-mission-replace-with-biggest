"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[17, 18, 5, 4, 6, 1]],
            "answer": [18, 6, 6, 6, 1, -1],
        },
        {
            "input": [[1, 2, 3, 4, 5, 6]],
            "answer": [6, 6, 6, 6, 6, -1],
        },
        {
            "input": [[1, 1, 1]],
            "answer": [1, 1, -1],
        },
    ],
    "Extra": [
        {
            "input": [[6, 5, 4, 3, 2, 1, 0, -1]],
            "answer": [5, 4, 3, 2, 1, 0, -1, -1],
        },
        {
            "input": [[-1, -1, -1]],
            "answer": [-1, -1, -1],
        },
        {
            "input": [[1, 0, 1, 0, 1, 0]],
            "answer": [1, 1, 1, 1, 0, -1],
        },
        {
            "input": [[0, 0, 0]],
            "answer": [0, 0, -1],
        },
        {
            "input": [[]],
            "answer": [],
        },
        {
            "input": [[1]],
            "answer": [-1],
        },
    ]
}

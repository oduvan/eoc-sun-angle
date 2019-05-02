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
            "input": '07:00',
            "answer": 15
        },
        {
            "input": '12:15',
            "answer": 93.75
        }
    ],
    "Extra": [
        {
            "input": '12:30',
            "answer": 97.5
        },
        {
            "input": '05:55',
            "answer": "I don't see the sun!"
        },
	{
            "input": "18:01",
            "answer": "I don't see the sun!"
        },
	{
            "input": "18:00",
            "answer": 180
        },
	{
            "input": "06:00",
            "answer": 0
        }
    ]
}

medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

place_score = {
    1: 3,
    2: 2,
    3: 1,
}


def createMedalTable(results):
    medalTable = {}

    for result in results:
        for country in result["podium"]:
            tmp = country.split(".")

            tmp_place = tmp[0]
            tmp_country = tmp[1]

            if tmp_country in medalTable:
                medalTable[tmp_country] += place_score[int(tmp_place)]
            else:
                medalTable[tmp_country] = place_score[int(tmp_place)]

    sort_orders = sorted(medalTable.items(), key=lambda x: x[1], reverse=True)

        
    print(sort_orders)

    return medalTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

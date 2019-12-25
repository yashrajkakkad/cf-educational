import requests
import pickle


def get_ids():
    response = requests.get('https://codeforces.com/api/contest.list')
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    ids = []
    for contest in response:
        if(contest["name"].startswith("Educational")):
            ids.append(contest["id"])
    with open("ids.pickle", "wb") as f:
        pickle.dump(ids, f)
    return ids


def load_ids():
    with open("ids.pickle", "rb") as f:
        ids = pickle.load(f)
    return ids


def get_problems(tags):
    ids = get_ids()
    response = requests.get(
        'https://codeforces.com/api/problemset.problems', params={"tags": tags})
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    problems_response = response["problems"]
    problems = []
    for problem in problems_response:
        if problem["contestId"] in ids:
            url = 'https://www.codeforces.com/problemset/problem/' + \
                str(problem["contestId"]) + '/' + problem["index"]
            problems.append((problem["rating"], problem["name"], url))
    return sorted(problems)


if __name__ == "__main__":
    problems = get_problems("dp")
    for problem in problems:
        print(problem[0], problem[1], problem[2], sep="\t")

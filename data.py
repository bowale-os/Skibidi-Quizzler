import html
import requests
parameters = {
    "amount":19,
    "type":"boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
new_questions = response.json()
# print(new_questions)


question_data = []

for item in new_questions['results']:
    # item["question"] = html.unescape(item["question"])
    question_data.append(item)

# print(question_data)
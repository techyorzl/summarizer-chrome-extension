import requests

backend_url = "http://localhost:8000/generate_summary"

data = {
    "text": (
        "The history of artificial intelligence (AI) dates back to antiquity, with myths, stories, and rumors of artificial "
        "beings endowed with intelligence or consciousness by master craftsmen. The modern field of AI research was founded as "
        "an academic discipline in 1956, and in the years since has experienced several waves of optimism, followed by disappointment "
        "and the loss of funding (known as AI winters), followed by new approaches, success, and renewed funding. AI research has explored "
        "various approaches, including simulating the human brain, formal logic, statistical methods, and cybernetics. Today, AI applications "
        "range from natural language processing, computer vision, and expert systems to robotics and autonomous systems."
    )
}

try:
    response = requests.post(backend_url, json=data)

    print("Response Status Code:", response.status_code)
    print("Full Response JSON:", response.json())  # Print the full response

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

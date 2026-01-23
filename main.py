import json
import time
from pathlib import Path
import google.genai as genai

client = genai.Client(api_key="ENTER_API_KEY")

MAX_RETRIES = 1
RETRY_DELAY = 5

BASE_DIR = Path(__file__).parent
PROMPT_DIR = BASE_DIR / "prompts"
LOG_DIR = BASE_DIR / "logs"
OUTPUT_DIR = BASE_DIR / "outputs"
output_file = OUTPUT_DIR / "latest_result.json"

PROMPT_FILE = PROMPT_DIR / "evaluator.txt"

INPUT_JSON_FOLDER = BASE_DIR / "input_json_folder"

def log(file_path, data):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False)+ ("\n"))

def load_prompt(path, topic, blog):
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()
        return template.replace("{{topic}}", topic).replace("{{blog}}", blog)

def run_evaluator(topic, blog):
    prompt = load_prompt(PROMPT_FILE, topic, blog)

    log(LOG_DIR / "requests.jsonl", {
        "prompt": "evaluator",
        "topic": topic,
        "blog": blog
    })

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            raw = response.text.strip()

            log(LOG_DIR / "responses.jsonl", {
                "topic": topic,
                "raw_response": raw
            })

            data = json.loads(raw)

            return data

        except Exception as e:
            log(LOG_DIR / "errors.jsonl", {
                "topic": topic,
                "attempt": attempt,
                "error": str(e)
            })

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

    return {
        "topic": topic,
        "readability_score": 0,
        "content_structure_score": 0,
        "engagement_score": 0
    }

results = []

for file in INPUT_JSON_FOLDER.glob("*.json"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

        topic = data["topic"]
        blog = data["blog"]

        print(f"Evaluating: {topic}")

        result = run_evaluator(topic, blog)
        results.append(result)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
    
print(f"\nSaved results to: {output_file}")
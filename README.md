# **LLM Control Lab**

*This is a industry grade framework for controlling and deploying Large Language Models, such as OpenAI, Claude, and Gemini using optimised/structured prompts and JSON pipelines.*

## Why build this project

LLM'S are very powerful and intuitive with their responses, but when it comes to production, they can run into errors.
This often leads to hallucination, varying formats, and broken systems and pipelines.

This project shows how to optimise LLM's into great **software components** using:

* System & user/developer prompts
* responses in JSON (outputs)
* Parsing
* Logging and identifying errors

## What this project does

This system allows you to run multiple **LLM modules**:

| Module       | Purpose                                       |
| ------------ | --------------------------------------------- |
| Summarizer   | To reduce the detailed text into structured bullet points |
| Fact-Checker | This helps check and verify if the output sticks to the facts or evidence |
| Rewriter     | Helps reconstruct the output with better clarity and user-friendliness |

In projects or tasks, each module above:

* A **system prompt** is used to define the purpose or intent.
* **JSON format** is used to retrieve a structured output.
* **Parsing and validation** is performed by **Python**.
* Finally, it's **logged** for better **traceability**.

## Project Architecture

```
mermaid
flowchart TD
    A[User Input]
    B[Prompt Module / System Instructions]
    C[OpenAI / Claude API<br/>(Importing packages & triggering API calls to Gemini)]
    D[Structured JSON Response]
    E[Parser & Validator]
    F[Logs and Output Files]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

```

## Project Structure

```
mermaid
graph TD
    A[llm-control-lab/] --> B[main.py]
    A --> C[config.py]

    A --> D[prompts/]
    D --> D1[summarizer.txt]
    D --> D2[fact_checker.txt]
    D --> D3[rewriter.txt]

    A --> E[logs/]
    E --> E1[requests.jsonl]
    E --> E2[responses.jsonl]
    E --> E3[errors.jsonl]

    A --> F[outputs/]
    F --> F1[latest_result.json]

```

## Why Follow this Structure/Technique

The techniques and workflows are used in various areas including AI Copilots and content automation pipelies for SEO optimisation.

## Integration with Prompt Engineering Portfolio

This system uses prompts that are already conceptualised and utilised in the portfolio link below:

> **Prompt Engineering Portfolio**
> *https://github.com/blackstag2k*


## Applications of this Project

This project is for:

* Developers building LLM-powered applications
* Companies seeking AI automated pipelines
* Anyone who wants to experiment with prompting
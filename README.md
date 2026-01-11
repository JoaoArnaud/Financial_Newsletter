# Financial Newsletter (Study Project)

This repository is a study project built to explore how an automated financial newsletter can be generated and delivered by email. It is not a professional product. The goal is to learn and experiment with prompt design, data sourcing, and email delivery while working with currently available financial information.

Many companies are exploring similar ideas today, such as automated market briefings, personalized updates, and AI-assisted research summaries. This project is a simple, educational version of that broader trend.

## What it does

- Uses an agent to search for recent financial information
- Builds a structured newsletter from the prompt in `src/prompt.py`
- Extracts a subject line from the generated content
- Sends the email through Gmail SMTP

## Project structure

- `src/main.py`: Orchestrates the agent run and email delivery
- `src/agent.py`: Agent configuration (model + tools)
- `src/prompt.py`: Newsletter template and rules
- `src/email_tool.py`: Gmail SMTP send utility

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`
- Additional packages referenced by the code: `agno`, `python-dotenv`

Depending on your configuration, you may also need API keys for the model and search tool in your environment (e.g., `OPENAI_API_KEY`, `TAVILY_API_KEY`).

## Environment variables

Create a `.env` file at the project root with:

```env
EMAIL_ADDRESS=your.email@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENTS=recipient1@example.com,recipient2@example.com
```

Use a Gmail App Password, not your normal password.

## How to run

```bash
python src/main.py
```

The agent will generate the newsletter content and the email tool will send it to the recipients.

## Notes

- This is a learning project, not production software.
- The newsletter content is only as reliable as the sources returned by the search tool.
- Always review outputs before sending if you plan to use it beyond testing.

## Disclaimer

No investment advice is provided. The project is for educational purposes only.

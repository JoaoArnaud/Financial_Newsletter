import re

from agent import my_agent
from email_tool import send_email_tool
from prompt import prompt


def _clean_subject(value: str) -> str:
    cleaned = value.strip()
    cleaned = cleaned.lstrip("-•*# ")
    cleaned = re.sub(r"^\*+|\*+$", "", cleaned).strip()
    return cleaned or "Resumo Diario do Mercado"


def _extract_subject(body: str) -> str:
    lines = [line.strip() for line in body.splitlines()]
    for idx, line in enumerate(lines):
        if re.search(r"assunto\s+do\s+email", line, re.IGNORECASE):
            if ":" in line:
                _, subject = line.split(":", 1)
                if subject.strip():
                    return _clean_subject(subject)
            for next_line in lines[idx + 1 :]:
                if next_line:
                    return _clean_subject(next_line)
    for line in lines:
        if line:
            return _clean_subject(line)
    return "Resumo Diario do Mercado"


def _get_content(result) -> str:
    if hasattr(result, "content"):
        return result.content
    if hasattr(result, "output"):
        return result.output
    return str(result)


if __name__ == "__main__":
    response = my_agent.run(prompt)
    content = _get_content(response)
    subject = _extract_subject(content)
    send_email_tool(subject, content)

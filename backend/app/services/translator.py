from groq import Groq

from app.core.config import settings


class TranslatorService:
    def __init__(self) -> None:
        self.client = Groq(api_key=settings.groq_api_key)

    def translate(self, text: str, target_language: str, tone: str) -> str:
        system_prompt = (
            f"Tu es un traducteur expert. Traduis en {target_language} avec un ton {tone}. "
            "Reponds uniquement par la traduction."
        )

        result = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
        )
        return result.choices[0].message.content or ""


translator_service = TranslatorService()

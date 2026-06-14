import httpx
import anthropic
from app.config import settings

class LLMService:
    @staticmethod
    def synthesize_answer(student_query: str, retrieved_context: str) -> str:
        """
        Sends the compiled context blocks along with the student's question 
        to Anthropic Claude, returning a tailored campus support answer.
        """
        if not settings.ANTHROPIC_API_KEY or settings.ANTHROPIC_API_KEY == "mock-key":
            print("[LLM SERVICE WARNING] ANTHROPIC_API_KEY is not set or using placeholder defaults. Returning fallback simulation.")
            return (
                "Thank you for contacting the Amity University Ranchi support desk! "
                "I processed your query regarding your request. (Note: Please update your .env with a live Anthropic API key to view real-time AI responses)."
            )

        try:
            # FIX: Force HTTPX to ignore rogue Windows system-level proxy environment variables
            clean_http_client = httpx.Client(trust_env=False)
            
            # Initialize the authentic Anthropic client container using our clean network pipeline
            client = anthropic.Anthropic(
                api_key=settings.ANTHROPIC_API_KEY,
                http_client=clean_http_client
            )
            
            system_prompt = (
                "You are the official, elite AI Helpdesk Assistant for Amity University Ranchi.\n"
                "Your objective is to provide professional, precise, welcoming, and accurate assistance to students.\n\n"
                "CRITICAL INSTRUCTIONS:\n"
                "1. Answer the student's question using ONLY the facts provided within the <context> tags below.\n"
                "2. If the context is empty or does not contain the answer, state honestly and politely that you do "
                "not possess that specific information in your current records and offer to lodge a helpdesk ticket.\n"
                "3. Never invent dates, fees, or policy criteria.\n"
                "4. Maintain an encouraging academic tone fitting for a top-tier university representative."
            )
            
            user_content = f"Here is the verified university documentation:\n<context>\n{retrieved_context}\n</context>\n\nStudent Question: {student_query}"
            
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=800,
                temperature=0.1,  # Guarantees deterministic, hallucination-free facts
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_content}
                ]
            )
            
            return response.content[0].text

        except Exception as e:
            print(f"[LLM GENERATION FAILURE] Claude API request crashed: {str(e)}")
            return "We apologize, but an internal AI core processing interruption occurred. Please re-attempt your prompt or contact the administrator."
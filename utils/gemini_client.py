import google.generativeai as genai
import os

def reconstruct_text(fragmented_text):
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            return "Error: GEMINI_API_KEY not found"
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"""
        You are a digital archaeologist specializing in internet culture and historical context.
        
        Reconstruct this fragmented internet/text message into proper English while providing 
        historical and cultural context where relevant:
        
        "{fragmented_text}"
        
        For internet slang and cultural references, provide the most accurate historical context.
        Examples:
        - "top 8" should reference MySpace's Top Friends feature
        - "smh" should be expanded with cultural context
        - Include explanations for platform-specific references
        
        Provide only the reconstructed text with contextual explanations embedded naturally.
        Do not add separate notes or explanations outside the main text.
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        return f"Error: {str(e)}"
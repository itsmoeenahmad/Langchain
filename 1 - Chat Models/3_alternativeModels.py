# In previous files, we use OPEN_AI LLM, Which API KEYS are not available freely so it will
# be costly, That's Why here: We use Google - Gemini (Free to use)

# Google - Gemini

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() # Loading GOOGLE_API_KEY

# Gemini LLM Model Is
gemini_LLM = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Calling the Gemini LLM
responseIs = gemini_LLM.invoke('Write down a short quote for me')

print('GEMINI LLM, Response Is: ',responseIs.content)

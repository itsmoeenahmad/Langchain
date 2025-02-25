# Importing Package
from langchain.prompts import PromptTemplate

# Defining the Template with placeholder
template = PromptTemplate(
 input_variables=['topic'],
 template='write down a joke on {topic}',
)

# Generate the Final Prompt
promptIs = template.format(topic='Developer')
print(promptIs)



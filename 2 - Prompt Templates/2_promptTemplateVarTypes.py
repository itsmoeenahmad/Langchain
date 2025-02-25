# importing Package
from langchain.prompts import PromptTemplate

# Defining the prompt template for Single Variable
promptTemplateForSingleVar = PromptTemplate(
    input_variables=['topic'],
    template='Write down the quote on {topic}'
)

# Generating the prompt
singlePromptIs = promptTemplateForSingleVar.format(topic='development')

# Showing the Final prompt
print('Prompt Template For Single Variable Is: ',singlePromptIs)


# Defining the prompt template for Multiple Variable
promptTemplateForMultiVar = PromptTemplate(
    input_variables=['topic','length'],
    template='Write down the quote for the {topic} with {length} words'
)

#Generating the prompt
multiPromptIs = promptTemplateForMultiVar.format(topic='development',length=10)

#showing the Final Prompt
print('Prompt Template For Multi Variable Is: ',multiPromptIs)
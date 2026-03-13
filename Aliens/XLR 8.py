from scarper import fetch_website_contents
from openai import OpenAI
import wikipedia


def wiki(user_input):
    wikip=wikipedia.summary(user_input)
    system_prompt=f"""
    Analyize the wikipideia informationa {wikip} and understand the user input tone. Show only that level information in systamatic way.
    
    Note: Information should be short and celar
    """
    return  AI(user_input,wikip)
def web_content(company_name, site):
    web_page_name = company_name
    web_content = fetch_website_contents(site)
    user_prompt= f"""
    Here is the details of information {web_page_name} web page:
    \n {web_content}
    """
    System_prompt= """
    You ara an Webpage content analyzieser. Provide the only relative information about the given site.
    Here is the example of output:
    
    site name: "ABC compnay"
    Site information: "This is site is related to the constructions. And shows the all new project's which are coming up in next few year."
    
    Note: Keep the information short and straight forword.
    """

    return AI(user_prompt,System_prompt)

def AI(user_prompt, system_prompt):
    url = "http://localhost:11434/v1"

    ollama = OpenAI(base_url=url, api_key="Ollama")

    message = [{'role': 'user', 'content': user_prompt},
               {'role': 'system', 'content': system_prompt}]

    rep = ollama.chat.completions.create(model='llama2', messages=message)
    return rep.choices[0].message.content


if __name__ == '__main__':
    #res=web_content("geeks for Geeks","https://search.brave.com/search?q=geeks+for+geeks")
    user=input("You:")
    print("GPT:"+wiki(user))

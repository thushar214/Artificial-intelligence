import litellm

mesg=[{"role":"user","content":"Write a 10,000-word detailed research article on black hole thermodynamics with mathematical equations, references, citations, and section breakdowns."}]
#mesg=[{"role":"user","content":"Hi"}]

def ollamaAI():
    ollama=litellm.completion(
        base_url='http://localhost:11434',
        model='ollama/llama2'
        ,messages=mesg)

    print('ollama 2 model :'+ollama['choices'][0]['message']['content'])

def deepseekAI():
    ollama2=litellm.completion(
        base_url='http://localhost:11434',
        model='ollama/deepseek-r1:8b',
        messages=mesg
    )

    print('Deepseek model : '+ollama2['choices'][0]['message']['content'])

def geminiAI():
    model=litellm.completion(
        base_url='http://localhost:11434',
        model='ollama/deepseek-r1:8b',
        messages=mesg,
        fallbacks=[
            {'model':'gemini/gemini-2.5-flash','api_key':'AIzaSyDk9Vh5NZcncfhqG0RpmGeMl_celfMVUvw'},
            {'model':'ollama/llama2'}
        ]
    )

    print('Model :' + model['model'])
    print(model['choices'][0]['message']['content'])
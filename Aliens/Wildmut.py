import gradio as gr
import litellm


def AI(Drp,sys):
    inp=[{"role": "user", "content":sys}]
    if Drp=='Deepseek':
        model_name='ollama/deepseek-r1:8d'
    else:
        model_name='ollama/llama2'
    olla=litellm.completion(
        base_url='http://localhost:11434',
        model=model_name,
        fallbacks=['ollama/deepseek-r1:8b'],
        messages=inp
    )
    return olla['choices'][0]['message']['content'] #ola['choices'][0]['message']['content']

def prit(s):
    print(s.upper())
    return s


#Components:
input_text=gr.Textbox(label="Enter your text here",lines=7)
output_text=gr.Markdown(label="")
Drp=gr.Dropdown(choices=['Deepseek','Ollama'], value='Ollama',label='AI Model')

demo = gr.Interface(fn=AI,inputs=[Drp,input_text],outputs=output_text,flagging_mode='never')

demo.launch(debug=True)

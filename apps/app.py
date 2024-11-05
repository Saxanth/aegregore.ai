import ollama
from services.models import NomicModel, CodestralModel, FluxModel

def main():
    model_list = { item['name'] for item in ollama.list()['models'][:-1] }
    prompt = "a simple python script to print a range of integers in the console."    
    print ("Ollama Models:\n" + '\n'.join(model_list))

    result = CodestralModel.generate_code(
        user_message=prompt,
        api_params={
            "model": 'codestral:latest',
            "temperature": 0.9,
            "max_tokens": 100_000,                
            "top_p": 0.9185, 
            "presence_penalty": 0.6, 
            "frequency_penalty": 1.2
        }
    )[0]
    print (f"\nCode Result:\n{result}")

    prompt = "Hello World!"
    result = NomicModel.generate_embedding("hello world")
    print (f'\nEmbeddingResult:\n{result}')

    prompt = """ a cute kitten holding a sign which reads "I'm a cute kitten" """
    result = FluxModel.generate_image(prompt)

if __name__ == "__main__": main()
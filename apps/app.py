import ollama
from services.models import NomicModel, CodestralModel, FluxModel

def main():
    # we have problems loading both the 'ollama' models and the 'flux' fp model.
    # so if you want to test 'image_gen' then set this value to true
    enable_image_gen = False

    if not enable_image_gen:
        model_list = { item['name'] for item in ollama.list()['models'][:-1] }
        print ("Ollama Models:\n" + '\n'.join(model_list))

        prompt = "a simple python script to print a range of integers in the console."
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

    # generate image using flux, and custom long version clip model. 
    # Need to possibly change over to flan-t5-xxl-gguf for the clip model | or possibly Qwen2.5??
    # Need to possibly change over the fp-8 for the diffusion model.
    else:
        prompt = """ a cute kitten holding a sign which reads "I'm a cute kitten" """
        FluxModel.generate_image(prompt) # loads the full model into gpu... probably best to test vram size, and quantize if necessary....

if __name__ == "__main__": main()
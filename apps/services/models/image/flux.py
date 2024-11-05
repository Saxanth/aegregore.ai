from typing import Literal
import torch, os, uuid, tqdm
from huggingface_hub import login
from diffusers import FluxPipeline
from transformers import CLIPModel, CLIPProcessor, CLIPConfig

import warnings
warnings.simplefilter("ignore") # Stop spam of future warnings I'm seeing

login('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')
MODEL_NAME = 'Flux.1-dev'

class FluxModel():
    def __init__(self, model: Literal['Flux.1-dev'] = 'Flux.1-dev') -> None:
        MODEL_NAME = model
        pass

    @staticmethod
    def generate_image(prompt: str):
        image_folder = os.path.abspath('./apps/services/models/.cache/images')
        if not os.path.exists(image_folder) : os.makedirs(image_folder)

        model_id = "zer0int/LongCLIP-GmP-ViT-L-14"
        config = CLIPConfig.from_pretrained(model_id)
        maxtokens = 248

        config.text_config.max_position_embeddings = maxtokens

        clip_model = CLIPModel.from_pretrained(model_id, torch_dtype=torch.bfloat16, config=config, device_map="balanced")
        clip_processor = CLIPProcessor.from_pretrained(model_id, padding="max_length", max_length=maxtokens, return_tensors="pt", truncation=True)

        pipe = FluxPipeline.from_pretrained(f"black-forest-labs/{MODEL_NAME}", torch_dtype=torch.bfloat16, device_map="balanced")
        pipe.set_progress_bar_config(disable=True)

        # Set the custom tokenizer and text encoder from your CLIP model
        pipe.tokenizer = clip_processor.tokenizer   # Replace with the custom CLIP tokenizer
        pipe.text_encoder = clip_model.text_model   # Replace with the custom CLIP text encoder
        pipe.tokenizer_max_length = maxtokens       # Long-CLIP token max
        pipe.text_encoder.dtype = torch.bfloat16    # Ensure the text encoder uses bfloat16

        pipe.vae.enable_slicing()
        pipe.vae.enable_tiling()

        seed:int = torch.randint(low=1337, high=61337, size=[1])[0].item()
        rand_generator = torch.Generator("cuda").manual_seed( seed )    

        image = pipe( 
            prompt=prompt,
            height=384,
            width=680,
            guidance_scale=3.5,
            num_inference_steps=16,
            max_sequence_length=maxtokens,
            generator=rand_generator,
        ).images[0]

        image.save(f"{image_folder}\\{ str(uuid.uuid4()) }.png")
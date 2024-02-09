# %pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# %pip install peft
# %pip install diffusers
# %pip install huggingface_hub
# %pip install ipywidgets
# %pip install accelerate
# %pip install transformers
# %pip install pillow

import os, torch
from diffusers import DiffusionPipeline, LCMScheduler
from PIL import Image
from huggingface_hub import notebook_login
notebook_login()

pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
).to("cuda")

# set scheduler
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

# load LoRAs
pipe. load_lora_weights("latent-consistency/lcm-lora-sdxl", adapter_name="1cm")
pipe. load_lora_weights("TheLastBen/Papercut_SDXL", weight_name="papercut.safetensors", adapter_name="papercut")

# Combine LoRAs
pipe.set_adapters(["1cm", "papercut"], adapter_weights=[1.0, 0.8])

prompt = "papercut, a cute fox"
generator = torch.manual_seed(0)

image = pipe(prompt, num_inference_steps=4, guidance_scale=1, generator=generator).images[0]
# image

if not isinstance(image, Image.Image):
    image = Image.fromarray(image.numpy())

# Ensure the 'images' directory exists
os.makedirs('images', exist_ok=True)

# Save the image to a file
image_path = os.path.join('images', 'generated_image.png')
image.save(image_path)

print(f"Image saved to {image_path}")
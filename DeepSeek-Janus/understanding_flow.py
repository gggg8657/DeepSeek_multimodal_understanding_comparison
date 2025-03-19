
import torch
from janus.janusflow.models import MultiModalityCausalLM, VLChatProcessor
from janus.utils.io import load_pil_images

# specify the path to the model
model_path = "deepseek-ai/JanusFlow-1.3B"
vl_chat_processor: VLChatProcessor = VLChatProcessor.from_pretrained(model_path)
tokenizer = vl_chat_processor.tokenizer

vl_gpt = MultiModalityCausalLM.from_pretrained(
    model_path, trust_remote_code=True
)
vl_gpt = vl_gpt.to(torch.bfloat16).cuda().eval()
# question = "Identify key objects and people in the image, including their count, positions, actions, and appearances."
question = "화면에서 무슨일이 일어나고 있는지 서술해줘"
PATH = "/home/cine/Documents/DJ/CCTV_3.8.20/DeepSeek-Janus/516303_633410_1319.jpg"
# PATH = "/home/cine/Documents/DJ/CCTV_3.8.20/DeepSeek-Janus/news.jpg"
# PATH = "/home/cine/Documents/DJ/CCTV_3.8.20/DeepSeek-Janus/street_fight.jpeg"
# PATH = "/home/cine/Documents/DJ/CCTV_3.8.20/DeepSeek-Janus/street_fight2.jpg.png"

conversation = [
    {
        "role": "<|User|>",
        "content": f"<image_placeholder>\n{question}",
        "images": [f"{PATH}"],
    },
    {"role": "<|Assistant|>", "content": ""},
]

# load images and prepare for inputs
pil_images = load_pil_images(conversation)
prepare_inputs = vl_chat_processor(
    conversations=conversation, images=pil_images, force_batchify=True
).to(vl_gpt.device)

# # run image encoder to get the image embeddings
inputs_embeds = vl_gpt.prepare_inputs_embeds(**prepare_inputs)

# # run the model to get the response
outputs = vl_gpt.language_model.generate(
    inputs_embeds=inputs_embeds,
    attention_mask=prepare_inputs.attention_mask,
    pad_token_id=tokenizer.eos_token_id,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    max_new_tokens=512,
    do_sample=False,
    use_cache=True,
)

answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
print(f"{prepare_inputs['sft_format'][0]}", answer)

import random
import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state


class Script(scripts.Script):  
    def title(self):
        return "Random Image Size"
      
    def ui(self, is_txt2img):
        gr.HTML("<p>Width</p>")
        with gr.Row():
            rw_min = gr.Slider(minimum=64.0, maximum=2048.0, step=64, label='Min Width Size', value=512.0, elem_id=self.elem_id("rw_min"))
            rw_max = gr.Slider(minimum=64.0, maximum=2048.0, step=64, label='Max Width Size', value=512.0, elem_id=self.elem_id("rw_max"))
        
        gr.HTML("<p>Height</p>")
        with gr.Row():   
            rh_min = gr.Slider(minimum=64.0, maximum=2048.0, step=64, label='Min Height Size', value=512.0, elem_id=self.elem_id("rh_min"))
            rh_max = gr.Slider(minimum=64.0, maximum=2048.0, step=64, label='Max Height Size', value=512.0, elem_id=self.elem_id("rh_max"))

        return [rw_max, rw_min, rh_min, rh_max]

    def run(self, p, rw_max, rw_min, rh_min, rh_max):
        p.width = random.randint(rw_min, rw_max)
        p.height = random.randint(rh_min, rh_max)
        
        proc = process_images(p)
        
        return proc

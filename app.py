import gradio as gr

from backend import medical_ai

# UI
with gr.Blocks() as demo:

    # Title
    gr.Markdown(

        """
# AI Medical Assistant

Ask about:
- Diseases
- Medicines
- Symptoms

Supports:
- Hindi
- English
"""
    )

    # Input
    user_input = gr.Textbox(

        label="Enter Disease or Medicine",

        lines=4,

        placeholder="Example: Mujhe fever hai"
    )

    # Output
    output = gr.Textbox(

        label="Medical Response",

        lines=20
    )

    # Button
    submit_btn = gr.Button(

        "Analyze"
    )

    # Event
    submit_btn.click(

        fn=medical_ai,

        inputs=user_input,

        outputs=output
    )

    # Footer
    gr.Markdown(

        """
---
© 2026 Shadab Rathore

Educational purposes only.
"""
    )

# Launch
demo.launch()
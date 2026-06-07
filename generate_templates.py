import os

base_dir = r'd:\work\POSTER\poster\templates\poster\templates'
os.makedirs(base_dir, exist_ok=True)

# CSS/SVG snippet for the grainy texture overlay
noise_overlay = """
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- SVG Noise Texture Overlay -->
    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.4; z-index: 10; pointer-events: none;" xmlns="http://www.w3.org/2000/svg">
        <filter id="noiseFilter">
            <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>
        </filter>
        <rect width="100%" height="100%" filter="url(#noiseFilter)"/>
    </svg>
"""

# HTML block for the Program Name anchored at the bottom
bottom_program_block = """
        <!-- Bottom: Program Name & Authority -->
        <div style="position: absolute; bottom: 3rem; left: 0; width: 100%; display: flex; justify-content: center; z-index: 5; text-align: center;">
            <div style="display: flex; flex-direction: column; align-items: center; max-width: 80vw; gap: 0.5rem;">
                <!-- Line 1: Program Name -->
                <div>
                    {{% if program.name_image %}}
                    <img src="{{{{ program.name_image.url }}}}" style="max-height: 100px; max-width: 100%; object-fit: contain; display: block; margin: 0 auto;">
                    {{% elif data.program_name %}}
                    <h1 style="margin: 0; font-size: 5rem; font-weight: 900; color: {accent}; font-family: 'Georgia', serif; letter-spacing: -2px; line-height: 1;">{{{{ data.program_name }}}}</h1>
                    {{% endif %}}
                </div>
                
                <!-- Line 2: Authority Name -->
                <div style="color: {text}; font-size: 1.4rem; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
                    {{% if program.authority_image %}}
                    <img src="{{{{ program.authority_image.url }}}}" style="max-height: 40px; object-fit: contain; display: block; margin: 0 auto;">
                    {{% elif data.authority %}}
                    {{{{ data.authority }}}}
                    {{% endif %}}
                </div>

                <!-- Line 3: Remaining Details -->
                <div style="color: {text}; font-size: 1.1rem; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; opacity: 0.9;">
                    {{{{ data.place }}}} &nbsp;&bull;&nbsp; {{{{ data.event_date }}}}
                </div>
            </div>
        </div>
"""

# ==========================================
# LAYOUT 1: The "Stamp" Center
# ==========================================
layout_stamp = """<div class="poster-content" style="position: relative; width: 100%; height: 100%; background: {bg_gradient}; color: {text}; overflow: hidden; font-family: {font}; box-sizing: border-box; padding: 2rem;">
    {noise}
    
    <!-- Top Result Badge -->
    <div style="position: absolute; top: 3rem; right: 4rem; z-index: 5; background: rgba(0,0,0,0.1); border: 2px dashed rgba(255,255,255,0.4); padding: 1rem 2rem; font-size: 1.8rem; font-weight: bold; letter-spacing: 2px;">
        RESULT
    </div>

    <!-- Background Icon -->
    <i class="fa-solid fa-pen-nib" style="position: absolute; right: -5%; top: 10%; font-size: 60rem; opacity: 0.05; transform: rotate(-15deg); z-index: 1;"></i>

    <!-- Central Card Container -->
    <div style="position: absolute; top: 10%; left: 10%; width: 80%; height: 70%; background-color: {card_bg}; z-index: 2; display: flex; flex-direction: column; justify-content: center; padding: 4rem; box-sizing: border-box; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 2px dashed rgba(255,255,255,0.3);">
        
        <!-- Category & Item -->
        <div style="margin-bottom: 3rem; border-bottom: 2px solid rgba(255,255,255,0.2); padding-bottom: 2rem;">
            {{% if data.category %}}
            <h3 style="margin: 0; font-size: 1.8rem; font-weight: normal; letter-spacing: 1px; color: {accent};">{{{{ data.category }}}}</h3>
            {{% endif %}}
            <h2 style="margin: 0.5rem 0 0 0; font-size: 4rem; font-weight: 900; line-height: 1; letter-spacing: -1px; color: {card_text};">{{{{ data.item_name }}}}</h2>
        </div>

        <!-- Winners List -->
        <div style="display: flex; flex-direction: column; gap: 2rem;">
            {{% if data.first_name %}}
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="font-size: 4rem; font-weight: 300; color: {accent}; line-height: 1; font-family: 'Georgia', serif;">01</div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: {card_text}; line-height: 1.2;">{{{{ data.first_name }}}}</div>
                    <div style="font-size: 1.2rem; color: {card_text}; opacity: 0.8; margin-top: 0.3rem;">{{{{ data.first_team }}}} {{{{ data.first_grade }}}}</div>
                </div>
            </div>
            {{% endif %}}
            
            {{% if data.second_name %}}
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="font-size: 3rem; font-weight: 300; color: {accent}; opacity: 0.8; line-height: 1; font-family: 'Georgia', serif;">02</div>
                <div>
                    <div style="font-size: 1.8rem; font-weight: 700; color: {card_text}; line-height: 1.2;">{{{{ data.second_name }}}}</div>
                    <div style="font-size: 1.1rem; color: {card_text}; opacity: 0.8; margin-top: 0.2rem;">{{{{ data.second_team }}}} {{{{ data.second_grade }}}}</div>
                </div>
            </div>
            {{% endif %}}

            {{% if data.third_name %}}
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="font-size: 3rem; font-weight: 300; color: {accent}; opacity: 0.8; line-height: 1; font-family: 'Georgia', serif;">03</div>
                <div>
                    <div style="font-size: 1.8rem; font-weight: 700; color: {card_text}; line-height: 1.2;">{{{{ data.third_name }}}}</div>
                    <div style="font-size: 1.1rem; color: {card_text}; opacity: 0.8; margin-top: 0.2rem;">{{{{ data.third_team }}}} {{{{ data.third_grade }}}}</div>
                </div>
            </div>
            {{% endif %}}
        </div>
    </div>
    
    {bottom_program}
</div>"""


# ==========================================
# LAYOUT 2: The "Split Typography" (Huge Numbers)
# ==========================================
layout_huge_numbers = """<div class="poster-content" style="position: relative; width: 100%; height: 100%; background: {bg_gradient}; color: {text}; overflow: hidden; font-family: {font}; box-sizing: border-box; padding: 4rem;">
    {noise}
    
    <!-- Top Right: Category & Item -->
    <div style="position: absolute; top: 4rem; right: 4rem; text-align: right; z-index: 5;">
        {{% if data.category %}}
        <h3 style="margin: 0; font-size: 2rem; font-weight: 400; color: {text}; opacity: 0.9;">{{{{ data.category }}}}</h3>
        {{% endif %}}
        <h2 style="margin: 0; font-size: 3.5rem; font-weight: 900; line-height: 1.1; color: {accent}; max-width: 500px;">{{{{ data.item_name }}}}</h2>
    </div>

    <!-- Background Icon -->
    <i class="fa-solid fa-fingerprint" style="position: absolute; left: 5%; top: 15%; font-size: 55rem; opacity: 0.05; z-index: 1;"></i>

    <!-- Center/Right: Huge Numbers & Winners -->
    <div style="position: absolute; top: 30%; right: 4rem; width: 60%; display: flex; flex-direction: column; gap: 3rem; z-index: 4;">
        
        {{% if data.first_name %}}
        <div style="position: relative; padding-left: 1rem;">
            <div style="font-size: 10rem; font-weight: 100; color: rgba(255,255,255,0.15); line-height: 0.8; font-family: 'Georgia', serif; position: absolute; left: 0; top: -3rem; z-index: -1;">01</div>
            <div style="font-size: 2.8rem; font-weight: 800; color: {text}; line-height: 1.1;">{{{{ data.first_name }}}}</div>
            <div style="font-size: 1.4rem; color: {text}; opacity: 0.8; margin-top: 0.5rem; letter-spacing: 1px;">{{{{ data.first_team }}}} &nbsp;&bull;&nbsp; {{{{ data.first_grade }}}}</div>
        </div>
        {{% endif %}}
        
        {{% if data.second_name %}}
        <div style="position: relative; padding-left: 1rem; margin-top: 1rem;">
            <div style="font-size: 8rem; font-weight: 100; color: rgba(255,255,255,0.1); line-height: 0.8; font-family: 'Georgia', serif; position: absolute; left: 0; top: -2rem; z-index: -1;">02</div>
            <div style="font-size: 2.2rem; font-weight: 700; color: {text}; line-height: 1.1;">{{{{ data.second_name }}}}</div>
            <div style="font-size: 1.2rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.second_team }}}} &nbsp;&bull;&nbsp; {{{{ data.second_grade }}}}</div>
        </div>
        {{% endif %}}

        {{% if data.third_name %}}
        <div style="position: relative; padding-left: 1rem; margin-top: 1rem;">
            <div style="font-size: 8rem; font-weight: 100; color: rgba(255,255,255,0.1); line-height: 0.8; font-family: 'Georgia', serif; position: absolute; left: 0; top: -2rem; z-index: -1;">03</div>
            <div style="font-size: 2.2rem; font-weight: 700; color: {text}; line-height: 1.1;">{{{{ data.third_name }}}}</div>
            <div style="font-size: 1.2rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.third_team }}}} &nbsp;&bull;&nbsp; {{{{ data.third_grade }}}}</div>
        </div>
        {{% endif %}}
    </div>

    <!-- Result Badge Left -->
    <div style="position: absolute; bottom: 20%; left: 4rem; background: {accent}; color: {card_text}; padding: 1rem 3rem; font-size: 3rem; font-weight: 900; letter-spacing: -1px; transform: rotate(-5deg); z-index: 5; box-shadow: 5px 5px 0px rgba(0,0,0,0.2);">
        RESULTS
    </div>

    {bottom_program}
</div>"""


# ==========================================
# LAYOUT 3: The "Clean Left" 
# ==========================================
layout_clean_left = """<div class="poster-content" style="position: relative; width: 100%; height: 100%; background: {bg_gradient}; color: {text}; overflow: hidden; font-family: {font}; box-sizing: border-box; padding: 4rem;">
    {noise}
    
    <!-- Background Icon -->
    <i class="fa-regular fa-clock" style="position: absolute; right: -5%; top: 20%; font-size: 50rem; opacity: 0.05; transform: rotate(10deg); z-index: 1;"></i>

    <!-- Top Left: Winners List -->
    <div style="position: absolute; top: 15%; left: 4rem; width: 60%; display: flex; flex-direction: column; gap: 3rem; z-index: 4;">
        
        {{% if data.first_name %}}
        <div style="display: flex; align-items: baseline; gap: 1.5rem; border-bottom: 2px solid rgba(255,255,255,0.2); padding-bottom: 1.5rem;">
            <div style="font-size: 4rem; font-weight: 300; color: {text}; line-height: 1; font-family: 'Georgia', serif;">01</div>
            <div>
                <div style="font-size: 3rem; font-weight: 900; color: {text}; line-height: 1.1; letter-spacing: -1px;">{{{{ data.first_name }}}}</div>
                <div style="font-size: 1.4rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.first_team }}}} &bull; {{{{ data.first_grade }}}}</div>
            </div>
        </div>
        {{% endif %}}
        
        {{% if data.second_name %}}
        <div style="display: flex; align-items: baseline; gap: 1.5rem; border-bottom: 2px solid rgba(255,255,255,0.1); padding-bottom: 1.5rem;">
            <div style="font-size: 3rem; font-weight: 300; color: {text}; line-height: 1; font-family: 'Georgia', serif;">02</div>
            <div>
                <div style="font-size: 2.2rem; font-weight: 800; color: {text}; line-height: 1.1; letter-spacing: -1px;">{{{{ data.second_name }}}}</div>
                <div style="font-size: 1.2rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.second_team }}}} &bull; {{{{ data.second_grade }}}}</div>
            </div>
        </div>
        {{% endif %}}

        {{% if data.third_name %}}
        <div style="display: flex; align-items: baseline; gap: 1.5rem;">
            <div style="font-size: 3rem; font-weight: 300; color: {text}; line-height: 1; font-family: 'Georgia', serif;">03</div>
            <div>
                <div style="font-size: 2.2rem; font-weight: 800; color: {text}; line-height: 1.1; letter-spacing: -1px;">{{{{ data.third_name }}}}</div>
                <div style="font-size: 1.2rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.third_team }}}} &bull; {{{{ data.third_grade }}}}</div>
            </div>
        </div>
        {{% endif %}}
    </div>

    <!-- Center/Right Decorative Category/Item -->
    <div style="position: absolute; bottom: 35%; right: 4rem; text-align: right; z-index: 5;">
        <div style="background: {accent}; color: {card_text}; display: inline-block; padding: 0.5rem 1.5rem; font-weight: bold; font-size: 1.2rem; letter-spacing: 2px; margin-bottom: 1rem; border-radius: 4px;">RESULT</div>
        {{% if data.category %}}
        <h3 style="margin: 0; font-size: 2.5rem; font-weight: 400; color: {text};">{{{{ data.category }}}}</h3>
        {{% endif %}}
        <h2 style="margin: 0; font-size: 4rem; font-weight: 900; line-height: 1; color: {text}; max-width: 400px; text-shadow: 2px 2px 0px rgba(0,0,0,0.2);">{{{{ data.item_name }}}}</h2>
    </div>

    {bottom_program}
</div>"""


# ==========================================
# LAYOUT 4: The "Minimal Poster" (Centered)
# ==========================================
layout_minimal = """<div class="poster-content" style="position: relative; width: 100%; height: 100%; background: {bg_gradient}; color: {text}; overflow: hidden; font-family: {font}; box-sizing: border-box; padding: 4rem; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
    {noise}
    
    <!-- Background Icon -->
    <i class="fa-solid fa-eye" style="position: absolute; left: 50%; top: 40%; font-size: 55rem; opacity: 0.05; transform: translate(-50%, -50%); z-index: 1;"></i>

    <!-- Top Result & Category -->
    <div style="z-index: 5; margin-bottom: 2rem;">
        <div style="font-size: 1.5rem; letter-spacing: 4px; color: {accent}; font-weight: bold; margin-bottom: 1rem; text-transform: uppercase;">OFFICIAL RESULT</div>
        {{% if data.category %}}
        <h3 style="margin: 0; font-size: 2rem; font-weight: normal; color: {text}; opacity: 0.8;">{{{{ data.category }}}}</h3>
        {{% endif %}}
        <h2 style="margin: 0.5rem 0 3rem 0; font-size: 4.5rem; font-weight: 900; line-height: 1.1; color: {text};">{{{{ data.item_name }}}}</h2>
    </div>

    <!-- Winners Stacked -->
    <div style="z-index: 5; display: flex; flex-direction: column; gap: 2.5rem; width: 100%; max-width: 800px; margin-bottom: auto;">
        
        {{% if data.first_name %}}
        <div style="background: rgba(0,0,0,0.1); border: 2px solid {accent}; padding: 2rem; border-radius: 12px;">
            <div style="color: {accent}; font-weight: 800; font-size: 1.2rem; text-transform: uppercase; margin-bottom: 0.5rem;">&#11088; 1st Place</div>
            <div style="font-size: 3rem; font-weight: 900; color: {text}; line-height: 1.1;">{{{{ data.first_name }}}}</div>
            <div style="font-size: 1.4rem; color: {text}; opacity: 0.9; margin-top: 0.5rem;">{{{{ data.first_team }}}} &bull; Grade {{{{ data.first_grade }}}}</div>
        </div>
        {{% endif %}}
        
        <div style="display: flex; gap: 2rem; width: 100%;">
            {{% if data.second_name %}}
            <div style="flex: 1; background: rgba(0,0,0,0.05); border: 1px solid rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 12px;">
                <div style="color: {text}; opacity: 0.7; font-weight: bold; font-size: 1rem; text-transform: uppercase; margin-bottom: 0.5rem;">2nd Place</div>
                <div style="font-size: 2rem; font-weight: 800; color: {text}; line-height: 1.1;">{{{{ data.second_name }}}}</div>
                <div style="font-size: 1.1rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.second_team }}}}</div>
            </div>
            {{% endif %}}

            {{% if data.third_name %}}
            <div style="flex: 1; background: rgba(0,0,0,0.05); border: 1px solid rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 12px;">
                <div style="color: {text}; opacity: 0.7; font-weight: bold; font-size: 1rem; text-transform: uppercase; margin-bottom: 0.5rem;">3rd Place</div>
                <div style="font-size: 2rem; font-weight: 800; color: {text}; line-height: 1.1;">{{{{ data.third_name }}}}</div>
                <div style="font-size: 1.1rem; color: {text}; opacity: 0.8; margin-top: 0.5rem;">{{{{ data.third_team }}}}</div>
            </div>
            {{% endif %}}
        </div>
    </div>

    {bottom_program}
</div>"""


layouts = [layout_stamp, layout_huge_numbers, layout_clean_left, layout_minimal]

# Define 20 premium themes focusing on radial/linear gradients and vintage pairings
themes = [
    # 1-4: The Mustard/Vintage Yellow Series (Reference 1)
    {'bg_gradient': 'radial-gradient(circle at center, #E6A838, #C2821A)', 'text': '#331B04', 'accent': '#A62A22', 'card_bg': '#D99B26', 'card_text': '#331B04', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(135deg, #F0C05A, #D19124)', 'text': '#2D1A05', 'accent': '#5E1813', 'card_bg': '#EBB646', 'card_text': '#2D1A05', 'font': 'serif'},
    {'bg_gradient': 'radial-gradient(circle at top right, #FFD166, #E09F00)', 'text': '#1A1100', 'accent': '#D62828', 'card_bg': '#F2B705', 'card_text': '#1A1100', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(to bottom, #DBA02C, #B57F1B)', 'text': '#FFFFFF', 'accent': '#541712', 'card_bg': '#FFFFFF', 'card_text': '#DBA02C', 'font': 'sans-serif'},
    
    # 5-8: The Deep Red Series (Reference 2)
    {'bg_gradient': 'radial-gradient(circle at bottom left, #A62424, #731212)', 'text': '#FFFFFF', 'accent': '#FFD166', 'card_bg': '#8C1C1C', 'card_text': '#FFFFFF', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(45deg, #8B1E1E, #C23030)', 'text': '#FDF2E9', 'accent': '#F2A900', 'card_bg': '#FDF2E9', 'card_text': '#8B1E1E', 'font': 'serif'},
    {'bg_gradient': 'radial-gradient(circle at center, #CC3333, #8B0000)', 'text': '#FFFFFF', 'accent': '#000000', 'card_bg': '#A61919', 'card_text': '#FFFFFF', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(to top, #660000, #B32424)', 'text': '#F2E6D8', 'accent': '#E6A838', 'card_bg': '#F2E6D8', 'card_text': '#660000', 'font': 'sans-serif'},

    # 9-12: The Off-White/Parchment Series (Reference 3)
    {'bg_gradient': 'radial-gradient(circle at top left, #F5F0E6, #E3D9C6)', 'text': '#211E18', 'accent': '#A62424', 'card_bg': '#FFFFFF', 'card_text': '#211E18', 'font': 'serif'},
    {'bg_gradient': 'linear-gradient(135deg, #FFFDF7, #EAE2CF)', 'text': '#1A1814', 'accent': '#2C5364', 'card_bg': '#1A1814', 'card_text': '#FFFDF7', 'font': 'sans-serif'},
    {'bg_gradient': 'radial-gradient(ellipse at center, #FDFBF7, #D9D0BE)', 'text': '#26231A', 'accent': '#D69E2E', 'card_bg': '#F2EBDA', 'card_text': '#26231A', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(to bottom, #F0EAD6, #DBCFB0)', 'text': '#362F24', 'accent': '#C05621', 'card_bg': '#FFFFFF', 'card_text': '#362F24', 'font': 'serif'},

    # 13-16: The Olive/Brown Earthy Series (Reference 4)
    {'bg_gradient': 'radial-gradient(circle at bottom right, #5C4A21, #3D3012)', 'text': '#F2EBDC', 'accent': '#F2B705', 'card_bg': '#F2EBDC', 'card_text': '#3D3012', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(135deg, #7A612E, #4A3A19)', 'text': '#FFFFFF', 'accent': '#E6A838', 'card_bg': '#614D23', 'card_text': '#FFFFFF', 'font': 'sans-serif'},
    {'bg_gradient': 'radial-gradient(circle at top center, #6B5B3E, #2E2516)', 'text': '#FFFDF7', 'accent': '#D96C5B', 'card_bg': '#FFFDF7', 'card_text': '#2E2516', 'font': 'serif'},
    {'bg_gradient': 'linear-gradient(to right, #40321B, #5C4A21)', 'text': '#F2E6CE', 'accent': '#C05621', 'card_bg': '#4D3E23', 'card_text': '#F2E6CE', 'font': 'sans-serif'},

    # 17-20: Modern Vintage (Teal & Navy)
    {'bg_gradient': 'radial-gradient(circle at center, #2C5364, #0F2027)', 'text': '#EAE2CF', 'accent': '#E6A838', 'card_bg': '#1A3340', 'card_text': '#EAE2CF', 'font': 'sans-serif'},
    {'bg_gradient': 'linear-gradient(135deg, #3A6073, #16222A)', 'text': '#FFFFFF', 'accent': '#D96C5B', 'card_bg': '#EAE2CF', 'card_text': '#16222A', 'font': 'sans-serif'},
    {'bg_gradient': 'radial-gradient(circle at bottom left, #1B4F72, #0E293C)', 'text': '#FDF2E9', 'accent': '#F39C12', 'card_bg': '#143B57', 'card_text': '#FDF2E9', 'font': 'serif'},
    {'bg_gradient': 'linear-gradient(to bottom, #114357, #F29492)', 'text': '#1A1A1A', 'accent': '#FFFFFF', 'card_bg': '#FFFFFF', 'card_text': '#114357', 'font': 'sans-serif'},
]

for i, theme in enumerate(themes):
    layout = layouts[i % len(layouts)] # Cycle through the 4 layouts
    
    # Format the bottom block first to resolve colors and escape braces
    bottom_block_formatted = bottom_program_block.format(**theme)
    
    template_str = layout.format(
        noise=noise_overlay,
        bottom_program=bottom_block_formatted,
        **theme
    )
    
    filename = os.path.join(base_dir, f'template_{i+1:02d}.html')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template_str)

# ==========================================
# LAYOUT 21: Custom Uploaded Background
# ==========================================
layout_custom_21 = """<div class="poster-content" style="position: relative; width: 100%; height: 100%; background-image: url('/static/poster/images/custom_bg_21.jpg'); background-size: cover; background-position: center; color: #1a1a1a; overflow: hidden; font-family: sans-serif; box-sizing: border-box; padding: 4rem;">
    
    <!-- Left side winners list -->
    <div style="position: absolute; top: 25%; left: 10%; width: 55%; display: flex; flex-direction: column; gap: 3rem; z-index: 4;">
        {% if data.first_name %}
        <div style="display: flex; align-items: baseline; gap: 1.5rem; border-bottom: 1px solid rgba(0,0,0,0.2); padding-bottom: 1rem;">
            <div style="font-size: 3.5rem; font-weight: 300; color: #1a1a1a; line-height: 1; font-family: 'Georgia', serif;">01</div>
            <div>
                <div style="font-size: 2.8rem; font-weight: 900; color: #1a1a1a; line-height: 1.1; letter-spacing: -1px;">{{ data.first_name }}</div>
                <div style="font-size: 1.2rem; color: #1a1a1a; opacity: 0.8; margin-top: 0.5rem;">{{ data.first_team }} &bull; {{ data.first_grade }}</div>
            </div>
        </div>
        {% endif %}
        
        {% if data.second_name %}
        <div style="display: flex; align-items: baseline; gap: 1.5rem; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 1rem;">
            <div style="font-size: 3rem; font-weight: 300; color: #1a1a1a; line-height: 1; font-family: 'Georgia', serif;">02</div>
            <div>
                <div style="font-size: 2.2rem; font-weight: 800; color: #1a1a1a; line-height: 1.1; letter-spacing: -1px;">{{ data.second_name }}</div>
                <div style="font-size: 1.2rem; color: #1a1a1a; opacity: 0.8; margin-top: 0.5rem;">{{ data.second_team }} &bull; {{ data.second_grade }}</div>
            </div>
        </div>
        {% endif %}

        {% if data.third_name %}
        <div style="display: flex; align-items: baseline; gap: 1.5rem;">
            <div style="font-size: 3rem; font-weight: 300; color: #1a1a1a; line-height: 1; font-family: 'Georgia', serif;">03</div>
            <div>
                <div style="font-size: 2.2rem; font-weight: 800; color: #1a1a1a; line-height: 1.1; letter-spacing: -1px;">{{ data.third_name }}</div>
                <div style="font-size: 1.2rem; color: #1a1a1a; opacity: 0.8; margin-top: 0.5rem;">{{ data.third_team }} &bull; {{ data.third_grade }}</div>
            </div>
        </div>
        {% endif %}
    </div>

    <!-- Bottom Left: Result, Category, Item, Program -->
    <div style="position: absolute; bottom: 4rem; left: 10%; width: 50%; z-index: 5;">
        <div style="background: #A62A22; color: #fff; display: inline-block; padding: 0.8rem 2rem; font-weight: bold; font-size: 1.5rem; letter-spacing: 1px; margin-bottom: 1rem; border-radius: 4px; box-shadow: 2px 2px 0 rgba(0,0,0,0.2);">RESULT</div>
        
        {% if data.category %}
        <h3 style="margin: 0; font-size: 2rem; font-weight: normal; color: #1a1a1a; margin-top: 1rem;">{{ data.category }}</h3>
        {% endif %}
        <h2 style="margin: 0.5rem 0 2rem 0; font-size: 3.5rem; font-weight: 900; line-height: 1; color: #A62A22; letter-spacing: -1px;">{{ data.item_name }}</h2>
        
        <div style="border-top: 2px solid rgba(0,0,0,0.1); padding-top: 1.5rem;">
            {% if program.name_image %}
            <img src="{{ program.name_image.url }}" style="max-height: 60px; max-width: 100%; object-fit: contain; margin-bottom: 0.5rem; display: block;">
            {% elif data.program_name %}
            <h1 style="margin: 0 0 0.5rem 0; font-size: 3.5rem; font-weight: 900; color: #A62A22; font-family: 'Georgia', serif; letter-spacing: -1px; line-height: 1;">{{ data.program_name }}</h1>
            {% endif %}
            
            <div style="color: #1a1a1a; font-size: 1rem; font-weight: bold; letter-spacing: 1px; text-transform: uppercase;">
                {{ data.authority }} &bull; {{ data.place }} &bull; {{ data.event_date }}
            </div>
        </div>
    </div>
</div>"""

filename_21 = os.path.join(base_dir, 'template_21.html')
with open(filename_21, 'w', encoding='utf-8') as f:
    f.write(layout_custom_21)

print('Generated 21 templates (including custom background).')

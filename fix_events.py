import re
import os

def fix_event_descriptions(file_path):
    """
    Finds event description paragraphs that contain registration/prize info via emoji markers
    and restructures them into a clean event-info-list format.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: finds <p class="event-description">...</p> blocks that contain the emoji markers
    # We capture the clean description text separately from the fee/prize info
    def replace_event_desc(match):
        full_block = match.group(0)
        
        # Skip if already converted (contains event-info-list)
        if 'event-info-list' in full_block:
            return full_block

        # Extract the closing </div> for event-footer (to keep it)
        # We need to find the paragraph and what comes after...
        # Let's just transform the paragraph: remove the <br> fee/prize lines
        # and add an event-info-list after the </p>
        
        p_match = re.search(
            r'(<p class="event-description">)(.*?)(</p>)',
            full_block,
            re.DOTALL
        )
        if not p_match:
            return full_block
        
        # Get the description text
        desc_text = p_match.group(2)
        
        # Check if it has the emoji markers indicating embedded fee/prize info
        has_fee = '📌' in desc_text or 'Registration Fee' in desc_text
        if not has_fee:
            return full_block

        # Extract fee amount
        fee_match = re.search(r'[₹Rs\.]*\s*(\d+)/-', desc_text)
        fee_amount = fee_match.group(0) if fee_match else '?'
        
        # Look for a full fee line like "📌 Registration Fee: ₹200/-"
        fee_line_match = re.search(r'📌\s*Registration Fee:\s*[₹Rs\d\-/ ]+', desc_text)
        fee_display = fee_line_match.group(0).replace('📌', '').strip() if fee_line_match else f'Registration Fee: {fee_amount}'

        # Extract register call to action
        cta_match = re.search(r'Register now[^<\n]*', desc_text)
        cta_text = cta_match.group(0).strip().rstrip('!').strip() if cta_match else 'Register now!'
        # Remove trailing emoji chars
        cta_text = re.sub(r'[\U00010000-\U0010ffff\u2600-\u27ff]+$', '', cta_text).strip()

        # Clean description: remove from <br> onward where the emoji markers start
        clean_desc_match = re.search(r'^(.*?)(?:<br>?\s*📌|📌)', desc_text, re.DOTALL)
        if clean_desc_match:
            clean_desc = clean_desc_match.group(1).strip()
        else:
            # fallback: remove last two sentences if no <br> 
            clean_desc = re.sub(r'\n\s*📌.*', '', desc_text, flags=re.DOTALL).strip()
            clean_desc = re.sub(r'<br>\s*$', '', clean_desc).strip()

        # Build the replacement
        info_list_html = f"""
                        <div class="event-info-list">
                            <div class="info-item">
                                <i class="fas fa-thumbtack"></i>
                                <span><strong>{fee_display}</strong></span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-gift"></i>
                                <span><strong>Prizes:</strong> Exciting Prizes for Winners!</span>
                            </div>
                            <div class="info-item">
                                <i class="fas fa-rocket"></i>
                                <span>{cta_text}!</span>
                            </div>
                        </div>"""

        new_p = f'<p class="event-description">{clean_desc}</p>'
        new_block = full_block.replace(p_match.group(0), new_p + info_list_html)
        return new_block

    # Match each event-details block
    new_content = re.sub(
        r'<div class="event-details">.*?</div>\s*</div>\s*</div>',
        replace_event_desc,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")


def fix_event_cards_flex(file_path):
    """
    Also ensures event-card and event-details use flexbox for proper alignment.
    Injects CSS for event-info-list if not already present (for pages with inline styles).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # If this file has inline <style> and no event-details flex styling, add it
    if '<style>' in content and 'event-info-list' not in content:
        css_injection = """
        /* Event card alignment */
        .event-details {
            display: flex;
            flex-direction: column;
            flex: 1;
        }
        .event-description {
            flex-grow: 1;
            line-height: 1.6;
            margin-bottom: 15px;
            color: #cccccc;
        }
        .event-info-list {
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .info-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.9rem;
            color: #f0f0f0;
        }
        .info-item i {
            color: var(--primary);
            width: 18px;
            text-align: center;
        }
        .event-card {
            display: flex;
            flex-direction: column;
        }
        """
        # Insert before the closing </style> tag
        content = content.replace('</style>', css_injection + '\n        </style>', 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CSS injected: {file_path}")


files = ['cse.html', 'civil.html', 'ece.html', 'eee.html', 'mechanical.html', 'h and s.html']

for f in files:
    if os.path.exists(f):
        # First normalize line endings
        raw = open(f, 'rb').read().replace(b'\r', b'')
        open(f, 'wb').write(raw)
        # Then inject CSS if needed
        fix_event_cards_flex(f)
        # Then fix event descriptions
        fix_event_descriptions(f)
    else:
        print(f"Not found: {f}")

print("Done!")

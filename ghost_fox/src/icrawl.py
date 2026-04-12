import asyncio

# icrawl: Intelligent Context Engine
# Parses page state and provides higher-level abstractions for the bridge.

async def get_interactive_elements(page):
    """Returns a list of clickable elements with descriptive labels."""
    return await page.evaluate('''() => {
        const elements = Array.from(document.querySelectorAll('button, a, input, select, textarea'));
        return elements.map(el => ({
            tag: el.tagName,
            text: el.innerText || el.value || el.placeholder || '',
            id: el.id,
            class: el.className,
            visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
        })).filter(el => el.visible);
    }''')

async def find_element_by_label(page, label):
    """Fuzzy searches for an element by text or label."""
    # (Simplified for now, will use LLM-style parsing later)
    elements = await get_interactive_elements(page)
    target = next((el for el in elements if label.lower() in el['text'].lower()), None)
    return target

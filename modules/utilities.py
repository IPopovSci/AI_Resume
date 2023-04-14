import re
def prompt_optimize(template):
    # Remove leading/trailing whitespace
    template = template.strip()
    # Remove extra whitespace between tokens
    template = re.sub(r'\s+', ' ', template)
    # Remove spaces after commas
    template = re.sub(r',\s+', ',', template)
    # Remove spaces before periods
    template = re.sub(r'\s+\.', '.', template)
    # Remove spaces before colons
    template = re.sub(r'\s+:', ':', template)
    # Remove spaces before question marks
    template = re.sub(r'\s+\?', '?', template)

    return template
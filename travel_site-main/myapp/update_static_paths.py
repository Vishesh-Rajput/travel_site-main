import os
import re

static_dir = 'myapp/static'

for filename in os.listdir('myapp/templates'):
    if filename.endswith('.html'):
        filepath = os.path.join('myapp/templates', filename)
        with open(filepath, 'r') as file:
            content = file.read()

        # Replace relative paths with {% static %}
        content = re.sub(r'href="(.+?)"', r'href="{% static "\1" %}"', content)
        content = re.sub(r'src="(.+?)"', r'src="{% static "\1" %}"', content)

        with open(filepath, 'w') as file:
            file.write(content)

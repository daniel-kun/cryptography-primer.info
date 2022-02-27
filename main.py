from jinja2 import Template

def define_env(env):

    @env.macro
    def key_generation_snippet(algorithm):
        with open('includes/key_generation_snippet.md') as f:
            template = Template(f.read())
            return template.render(algorithm=algorithm)

    @env.macro
    def password_keygen_snippet(algorithm, keysize):
        with open('includes/password_keygen_snippet.md') as f:
            template = Template(f.read())
            return template.render(algorithm=algorithm, keysize=keysize)

    @env.macro
    def recommendation(admonition, title, text):
        return f'<div class="admonition {admonition}"><p class="admonition-title">{title}</p>{ f"<p>{text}</p>" if text is not None and len(text) > 0 else "" }</div>'

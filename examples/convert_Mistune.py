import mistune

md_content = """
<details>
<summary>Expand here for details</summary>

[🔗 This leads your to Gist at GitHub 🔗](https://gist.github.com/)

</details>
"""

# Initialize Mistune Markdown renderer with table and HTML support
markdown = mistune.create_markdown(plugins=["table", "strikethrough", "footnotes"])

# Convert Markdown to HTML
html_output = markdown(md_content)

# Print the resulting HTML
print(html_output)
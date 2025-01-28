from markdown_it import MarkdownIt

# Markdown content with <details> block
md_content = """
<details>
<summary>Expand here for details</summary>

[🔗 This leads your to Gist at GitHub 🔗](https://gist.github.com/)

</details>
"""

# Initialize the MarkdownIt parser and enable HTML blocks and tables
md = MarkdownIt("commonmark").enable("html_block").enable("table")

# Parse the Markdown content to HTML
html_output = md.render(md_content)

# Print the resulting HTML
print(html_output)

import markdown

md_content = """
<details markdown="1">
<summary>Expand here for details</summary>

[🔗 This leads your to Gist at GitHub 🔗](https://gist.github.com/)

</details>
"""

# Convert Markdown to HTML with extensions for tables, extra features, and Markdown inside HTML
html_output = markdown.markdown(md_content, extensions=['tables', 'extra', 'md_in_html'])

# Print the resulting HTML
print(html_output)
# Markdown to HTML Conversion Examples

Convert Markdown content including HTML tags to pure HTML output.
See if there are edge cases that need to be addressed. 

## Plugins used
1. [Python-Markdown](https://github.com/Python-Markdown/markdown)
2. [markdown-it-py](https://github.com/executablebooks/markdown-it-py)
3. [Mistune v3](https://github.com/lepture/mistune)

## Examples
1. Using **Python-Markdown** :  [script](./convert_markdown.py)
2. Using **markdown-it-py** :  [script](./convert_MarkdownIt.py)
3. Using **Mistune** :  [script](./convert_Mistune.py)

## Feature Breakdown:

| Feature | Python-Markdown	| MarkdownIt-Py	| Mistune |
|:-|:-|:-|:-|
| Tables | tables | .enable("table") | plugins=["table"] |
| HTML Blocks (```<div>```) | html_block | .enable("html_block") | Built-in support |
| Markdown in HTML | md_in_html | Handled automatically | Handled automatically |

### Notes:
- Python-Markdown
    - The **extra** extension includes features like *footnotes* and *tables*.
    - **md_in_html** allows parsing Markdown inside HTML elements.
- MarkdownIt-Py
    - Highly modular; you must explicitly enable features.
- Mistune
    - Features like **html_block** and table are enabled via plugins.
    - Other plugins (e.g., *strikethrough*, *footnotes*) can be added as needed.

## Findings

When using the Python-Markdown plugin, the parser ignores Markdown syntax wrapped inside block-level HTML tag. This requires the addition of *markdown="1"* to the block-level HTML tag.

Example: ```<details markdown="1">```
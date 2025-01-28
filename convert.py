import os
import markdown

def convert_md_to_html(input_folder):
    # Validate the input folder
    if not os.path.isdir(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist. Please provide a valid path.")
        return

    print(f"Converting Markdown files in folder: {input_folder}")

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                try:
                    with open(md_path, 'r', encoding='utf-8') as md_file:
                        md_content = md_file.read()

                    # Replace .md links with .html links
                    md_content = md_content.replace('.md)', '.html)')

                    # Convert Markdown to HTML with necessary extensions
                    html_content = markdown.markdown(
                        md_content,
                        extensions=['tables', 'extra', 'md_in_html']
                    )

                    # Create an HTML template
                    html_template = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>{file.replace('.md', '')}</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                line-height: 1.6;
                                margin: 20px;
                                padding: 20px;
                                background-color: #f9f9f9;
                                color: #333;
                            }}
                            h1, h2, h3 {{
                                color: #0078D7;
                            }}
                            a {{
                                color: #0078D7;
                                text-decoration: none;
                            }}
                            a:hover {{
                                text-decoration: underline;
                            }}
                            details {{
                                margin: 10px 0;
                            }}
                            summary {{
                                font-weight: bold;
                                cursor: pointer;
                            }}
                            table {{
                                border-collapse: collapse;
                                width: 100%;
                                margin: 10px 0;
                            }}
                            th, td {{
                                border: 1px solid #ddd;
                                padding: 8px;
                                text-align: left;
                            }}
                            th {{
                                background-color: #f4f4f4;
                            }}
                        </style>
                    </head>
                    <body>
                        {html_content}
                    </body>
                    </html>
                    """

                    # Save the converted HTML
                    html_path = os.path.join(root, file.replace('.md', '.html'))
                    with open(html_path, 'w', encoding='utf-8') as html_file:
                        html_file.write(html_template)

                    print(f"Converted: {md_path} -> {html_path}")
                
                except Exception as e:
                    print(f"Error processing file {md_path}: {e}")
            else:
                print(f"Skipping non-Markdown file: {file}")

# Replace 'your_folder_path' with the root folder containing your Markdown files
input_folder = input("Enter the path to your Markdown folder: ")
convert_md_to_html(input_folder)

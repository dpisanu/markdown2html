# markdown2html

## Markdown to HTML Converter

**A lightweight Python tool to convert Markdown to HTML with ease and flexibility.**

## Project Goal

The goal of this project was to create a small Python script to handle Markdown-to-HTML conversion. This was a learning exercise to understand how such conversions work, without relying on more established static site generators. 

For reference, you can find a list of popular [awesome static generators](https://github.com/myles/awesome-static-generators).

## Usage

The script is interactive and simple to use. Here's how it works:

1. Run the `convert.py` script in your terminal or Python environment.
2. The script will prompt you to provide the root path where it should start searching for Markdown (`.md`) files.
3. Once a path is provided, the script will iterate through the folder structure, locate Markdown files, and convert them into corresponding HTML files in the same structure.

Feel free to modify or expand the script to suit your needs!

## Examples

This project includes an [`examples`](./examples) folder, where three Python Markdown plugins were tested to evaluate their behavior and performance. These tests focused on identifying edge cases, particularly those involving HTML tags embedded in Markdown files. The folder contains:

- Overview of the [example converters](./examples/converter_examples.md).
- A set of example converter python scripts.

This folder may serve as a useful reference if you're considering using or comparing Markdown plugins in your own projects.

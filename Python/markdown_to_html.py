def markdown_to_html(markdown_text):
    html_text = markdown_text.replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>")
    html_text = html_text.replace("**", "<b>").replace("*", "<i>")
    return html_text

def main():
    markdown_text = input("Enter your markdown text: ")
    html = markdown_to_html(markdown_text)
    print(f"Converted HTML: \n{html}")

if __name__ == "__main__":
    main()

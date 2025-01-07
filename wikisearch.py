import re
import os
from bs4 import BeautifulSoup

def clear_console():
    # Clear the console for different operating systems
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def generate_html_report(search_results, keyword, output_file):
    # Create an HTML report from the search results
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("<html>\n<head>\n<title>Search Results</title>\n")
        file.write("<style>\n")
        file.write("""
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
        }
        .container {
            display: flex;
            width: 100%;
            margin-top: 20px;
        }
        .toc {
            width: 20%;
            padding: 10px;
            border-right: 2px solid #ddd;
            background-color: #f4f4f4;
            height: 90vh;  /* Set a fixed height for scrolling */
            overflow-y: auto;  /* Enable vertical scrolling */
        }
        .results {
            width: 80%;
            padding: 10px;
            overflow-y: scroll;
            height: 90vh;  /* Set height to make the content scrollable */
        }
        .red { color: red; }
        h1, h2 {
            color: #333;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
        """)
        file.write("</style>\n</head>\n<body>\n")
        
        # Display the search term
        file.write(f"<h1>Search Results for: <strong>{keyword}</strong></h1>\n")
        
        # Table of Contents
        file.write("<div class='container'>\n")
        file.write("<div class='toc'>\n")
        file.write("<h2>Table of Contents</h2>\n")
        file.write("<ul>\n")
        for i, result in enumerate(search_results):
            file.write(f'<li><a href="#result{i}">{result["title"]}</a></li>\n')
        file.write("</ul>\n")
        file.write("</div>\n")  # Close toc div
        
        # Search results sections
        file.write("<div class='results'>\n")
        if search_results:
            for i, result in enumerate(search_results):
                file.write(f'<h2 id="result{i}">{result["title"]}</h2>\n')
                for match in result['matches']:
                    file.write(f"<p>{match}</p>\n")
        else:
            file.write("<p>No results found.</p>\n")
        
        file.write("</div>\n")  # Close results div
        file.write("</div>\n")  # Close container div
        
        file.write("</body>\n</html>\n")

def search_in_html(file_path, keyword):
    matches_found = 0  # To keep track of the number of matches
    search_results = []  # To store results for the HTML file
    
    # Read the HTML file content
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all article divs
    articles = soup.find_all('div', {'created': True})
    
    # Loop through all articles
    for article in articles:
        # Extract the title
        title = article.get('title', '').upper()
        
        # Extract the content inside <pre> tag
        pre_tag = article.find('pre')
        content = pre_tag.get_text() if pre_tag else ''
        
        # Check for matching keyword
        if keyword.lower() in content.lower():
            # Print the title in cyan
            print(f'\033[96m{title}\033[0m')
            
            # Store the result for the HTML file
            result = {'title': title, 'matches': []}
            
            # Split the content into lines
            lines = content.split('\n')
            
            # Loop through each line to find the keyword match
            for line in lines:
                if keyword.lower() in line.lower():
                    # Highlight the keyword in red using <span> in HTML
                    highlighted_line = re.sub(f'({re.escape(keyword)})', r'<span class="red">\1</span>', line, flags=re.IGNORECASE)
                    
                    # Highlight the keyword in red for the console
                    highlighted_console_line = re.sub(f'({re.escape(keyword)})', r'\033[91m\1\033[0m', line, flags=re.IGNORECASE)
                    
                    print(highlighted_console_line)  # Print the line with red keyword
                    print('-' * 80)  # Separator for clarity
                    result['matches'].append(highlighted_line)  # Add match to the result
                    matches_found += 1  # Increment match counter
            
            # Append the result to the search results list
            search_results.append(result)
    
    # Print summary of results
    print(f"\nSummary:")
    print(f"Total matches found: {matches_found}")
    if matches_found == 0:
        print(f"No matches found for the keyword '{keyword}'.")

    # Generate the HTML report with the search term
    generate_html_report(search_results, keyword, 'search_results.html')

def main():
    # Prompt for the keyword
    keyword = input("Enter the keyword to search: ")

    # Clear the console before printing results
    clear_console()

    # Call the search function with the provided file path and keyword
    search_in_html("C:/Wiki/index.html", keyword)

# Run the main function
if __name__ == "__main__":
    main()

# TiddlyWiki Search Tool
An external console-based search tool for TiddlyWiki to supplement the terrible built-in one.

Developed with Python 3.10.6. Requires BeautifulSoup.
```
py -m pip install BeautifulSoup
```
Developed with GPT4. Actually I didn't write any of it, hopefully it works okay lol.

You must modify the source to link to your index.html file. When you open the program it will prompt you for a keyword to search.

It will display the title of each article, and below it will display each line containing the keyword.

Make a bat file like this:
```
@echo off
py "C:\path\to\wikisearch.py"
pause
```
And you can just double-click that and type in what you are searching for. Console will give you quick convenient output. The HTML file will give you output useful for lots of results. You can make a shortcut to the HTML file as well to make it easier to open.

I haven't gotten around to making it ignore embedded images or system tiddlers, so hopefully that's not a problem.

Sample output:

![Screenshot of console output](https://raw.githubusercontent.com/RyanBabij/TiddlyWiki-Search-Tool/refs/heads/main/SampleOutput/Console.png)

![Screenshot of HTML output](https://raw.githubusercontent.com/RyanBabij/TiddlyWiki-Search-Tool/refs/heads/main/SampleOutput/HTML.png)

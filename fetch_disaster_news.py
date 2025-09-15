from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='9148687c327d450ebe85e39ae60439eb')


disaster_news = newsapi.get_everything(
    q='flood OR earthquake OR disaster',
    language='en',
    sort_by='publishedAt',
    page_size=10
)


if disaster_news.get("status") == "ok":
    articles = disaster_news.get("articles", [])
    print(f"✅ Fetched {len(articles)} articles\n")

    
    for idx, article in enumerate(articles, start=1):
        title = article.get("title", "No title")
        description = article.get("description", "No description available")
        url = article.get("url", "#")

        print(f"{idx}. {title}")
        print(f"   {description}")
        print(f"   🔗 {url}\n")

    
    html_content = """
    <html>
    <head>
        <title>Disaster News</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                margin: 20px;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                background: #fff;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            th, td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #007acc;
                color: white;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
            a {
                color: #0b1a9c;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Latest Disaster News</h1>
        <table>
            <tr>
                <th>Link</th>
                <th>Title</th>
                <th>Description</th>
            </tr>
    """

    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "No description available")
        url = article.get("url", "#")

        html_content += f"""
            <tr>
                <td><a href="{url}" target="_blank">Read</a></td>
                <td>{title}</td>
                <td>{description}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    
    with open("disaster_news.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print(" News also saved to disaster_news.html (formatted in table)")

else:
    print(" Error:", disaster_news.get("message", "Unknown error"))



def redirector():
    html = '<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'

    index = html.format(url="https://elucidario.art")
    cname = "link.elucidario.art"
    
    with open("./dist/CNAME", "w") as file:
        file.write(cname)
    with open("./dist/index.html", "w") as file:
        file.write(index)
    with open("./dist/404.html", "w") as file:
        file.write(index)
    
    with open("redirects.json") as f:
        redirects = json.load(f)
        
        for redirect in redirects:
            
            html_file = html.format(url=redirect["url"])
            name = redirect["path"]
            file_path = f"./dist/{name}.html"
            
            with open(file_path, "w") as file:
                file.write(html_file)

if __name__ == "__main__": 
    import json
    import os
    
    # Clean up the dist directory
    if os.path.exists("./dist"):
        import shutil
        shutil.rmtree("./dist")
        
    # Create the dist directory
    os.makedirs("./dist")
    
    redirector()
    
    print("Redirector HTML files created successfully.")
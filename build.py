

def redirector():
    template_file = "./template.html"
    
    with open(template_file, "r") as file:
        template = file.read()
        
    posthog_api_key = os.environ.get("POSTHOG_API_KEY")
    print(f"POSTHOG_API_KEY: {posthog_api_key}")

    index = template.replace("__REDIRECT_URL__", "https://elucidario.art").replace("__POSTHOG_API_KEY__", posthog_api_key)
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
            
            html_file = template.replace("__REDIRECT_URL__", redirect["url"]).replace("__POSTHOG_API_KEY__", posthog_api_key)
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
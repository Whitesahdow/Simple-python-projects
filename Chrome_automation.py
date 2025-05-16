import webbrowser as wb
def web_auto():
    # path of chrome application
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # --profile-directory="profile name" if there are multiple profiles 
    # place holder for the urls that will be added after opening chrome
    
    urls = (
        "https://github.com/Whitesahdow",
        "https://www.youtube.com"
    )
    for i in urls:
        print("opening_________________ ", i)
        wb.get(chrome_path).open(i)

# main function
web_auto()
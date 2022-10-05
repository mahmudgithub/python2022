import webbrowser

def main():
    print("open sites")

    with open("sites.txt") as fobj:
        try:
            for num,url in enumerate(fobj):
                webbrowser.open_new_tab(url.strip())
        except Exception as e:
            print(e)
    print("\nEnjoy!")
if _name_ == '_main_':main()
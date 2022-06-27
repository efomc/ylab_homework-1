def domain_name(url):
    base_url_elements = url.split(".")
    for item in base_url_elements:
        if "//" in item:
            url_elements = item.split("//")
        else:
            url_elements = [item]
        for element in url_elements:
            if all(
                (
                    element,
                    "www" not in element,
                    ":" not in element,
                )
            ):
                return element
            
            
def main():
    url = input('Введите, пожалуйста, url адрес: ')
    print(domain_name(url))

 
if __name__ == "__main__":
    main()

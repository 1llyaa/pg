import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    hrefs = []

    try:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise ValueError(f"Unexpected status code: {response.status_code}")

        soup = BeautifulSoup(response.text, "lxml")
        for href in soup.find_all("a"):
            hrefs.append(href.get("href"))

    except ValueError as ve:
        return {"status": "error", "message": str(ve)}
    except requests.RequestException as e:
        return {"status": "error", "message": f"Request error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

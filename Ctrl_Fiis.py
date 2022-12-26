from playwright.sync_api import sync_playwright


from playwright.sync_api import Page, expect

def teste(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #removendo ou deixando TRUE nao aparecerá o navegador
    pagina = navegador.new_page()

    ativo = 'URPR11'
    link = 'https://fiis.com.br/' + ativo + '/'
    print('Acessando:', link)
    try:
        valorAtivo = pagina.locator('xpath=//*[@id="quotations--infos-wrapper"]/div[1]/span[2]')\
            .text_content(timeout=4000)
    except:
        print('erro')
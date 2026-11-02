from pathlib import Path
from playwright.sync_api import sync_playwright
import json
base=Path(__file__).resolve().parent
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((base/'index.html').as_uri())
    assert page.title()=='Marcos — Sites & dashboards'
    assert page.locator('.project:visible').count()==2
    page.get_by_role('button',name='Sites',exact=True).click()
    assert page.locator('.project:visible').count()==1
    page.get_by_role('button',name='Código',exact=True).click()
    assert page.locator('.project:visible').count()==1
    page.get_by_role('button',name='Todos',exact=True).click()
    page.locator('#theme').click()
    assert 'light' in page.locator('body').get_attribute('class')
    page.locator('#theme').click()
    page.locator('#period').select_option('month')
    assert page.locator('#orders').inner_text()=='184'
    assert page.locator('#chart > div').count()==4
    page.locator('#period').select_option('week')
    assert page.locator('#orders').inner_text()=='48'
    page.locator('#details').fill('Pet shop: preciso apresentar meus serviços.')
    page.locator('#copy').click()
    assert page.locator('#copyStatus').inner_text()
    if page.locator('#copyFallback').is_visible():
        assert 'Pet shop' in page.locator('#copyFallback').input_value()
    for width in [360,390,768,1440]:
        page.set_viewport_size({'width':width,'height':900})
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'overflow {width}'
    assert page.locator('a[href="https://zyon-conceito-demo.pages.dev/"]').count()==1
    page.set_viewport_size({'width':1440,'height':1000})
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(base/'desktop.png'),full_page=True)
    page.set_viewport_size({'width':390,'height':844})
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(base/'mobile.png'),full_page=True)
    assert not errors, errors
    browser.close()
print(json.dumps({'result':'passed','viewports':[360,390,768,1440],'js_errors':errors,'checks':['filters','themes','dashboard','brief copy/fallback','responsive layout']}))

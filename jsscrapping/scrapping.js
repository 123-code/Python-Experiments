const puppeteer = require('puppeteer'); 
const loginURL = "https://takeout.google.com/settings/takeout";
const timeout = 8000;
(async () => {
    const browser = await puppeteer.launch({
      headless:"new",
     
    });
    const page = await browser.newPage();
  
    await page.setViewport({
      width: 1200,
      height: 1200,
      deviceScaleFactor: 1,
    });
  
    await page.goto(loginURL, {
      waitUntil: 'domcontentloaded',
      timeout,
    });
  
    // Perform Login
    await page.waitForSelector('input[type="email"]');
    await page.type('input[type="email"]', 'naranjojose256@gmail.com'); // Replace with your email
    await page.click('div[id="identifierNext"]');
  
    await page.waitForTimeout(timeout);
    await page.waitForSelector('input[type="password"]');
    await page.type('input[type="password"]', 'JoseNaranjo!'); // Replace with your password
    await page.click('div[id="passwordNext"]');
  
    await page.waitForNavigation({ waitUntil: 'networkidle0' });
  
    await page.goto(url, {
      waitUntil: 'domcontentloaded',
      timeout,
    });
  
    await page.waitForTimeout(timeout);
  
    setTimeout(async () => {
      await page.screenshot({
        path: 'screenshot.png',
        fullPage: true,
      });
      await browser.close();
    }, timeout - 2000);
  })();
  
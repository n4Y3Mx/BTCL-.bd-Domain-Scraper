# ==========================================
# Tool by: /n4y3mx
# Socials: FB / Insta / X: @n4y3mx
# Description: Fixed Strict Mode - High Speed Multi-Tab
# ==========================================

import asyncio
import csv
import time
import math
from playwright.async_api import async_playwright

results = []
processed_count = 0
results_lock = asyncio.Lock()

async def scrape_tab(tab_id, domain_chunk, total_domains, start_time):
    global processed_count
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # FIXED SELECTORS: Added 'section' to avoid multiple matches (Strict Mode fix)
        input_sel = "section input[name='domainName']"
        dropdown_sel = "section select[name='domainExt']"
        search_btn = "section button[type='submit']"
        result_box = "#searchContent"

        try:
            print(f"[*] Tab {tab_id}: Opening BTCL...")
            await page.goto("https://bdia.btcl.com.bd/", wait_until="networkidle")

            for domain in domain_chunk:
                try:
                    # 1. Clear and Input without refreshing
                    # .first ensures we only hit one element even if the site duplicates tags
                    target_input = page.locator(input_sel).first
                    await target_input.fill("") 
                    await target_input.fill(domain)
                    
                    await page.locator(dropdown_sel).first.select_option(value=".bd")
                    await page.locator(search_btn).first.click()

                    # 2. Smart Wait: Wait for the result to show the domain name
                    # No refresh here unless it truly times out
                    await page.wait_for_selector(f"{result_box}:has-text('{domain}')", timeout=12000)
                    
                    # Small sleep to let the table text populate fully
                    await asyncio.sleep(0.5)

                    content = await page.inner_text(result_box)
                    data = {'Domain': f"{domain}.bd", 'Status': 'Available', 'Registrant': 'N/A', 'Email': 'N/A', 'Expiry': 'N/A'}

                    if "is not Available" in content:
                        data['Status'] = 'Taken'
                        try:
                            # Scrape data from the table
                            data['Registrant'] = await page.locator('th:has-text("Registrant\'s Name") + td').inner_text()
                            data['Email'] = await page.locator('th:has-text("Email") + td').inner_text()
                            data['Expiry'] = await page.locator('th:has-text("Valid Till") + td').inner_text()
                        except:
                            pass

                    async with results_lock:
                        results.append(data)
                        processed_count += 1
                        
                        elapsed = time.time() - start_time
                        avg = elapsed / processed_count
                        rem = (avg * (total_domains - processed_count)) / 60
                        print(f"[*] Done {processed_count}/{total_domains} | Current: {domain}.bd | Est: {rem:.2f}m", end='\r')

                except Exception as e:
                    print(f"\n[!] Tab {tab_id} skipped {domain} due to delay. Continuing...")
                    # We only reload if the page actually hangs/crashes
                    if "Target closed" in str(e):
                        break 

        finally:
            await browser.close()

async def main():
    print(f"\n{'='*45}\n   Fixed Multi-Tab Scraper /n4y3mx\n{'='*45}")
    input_file = input("[?] Enter filename (e.g., domains.txt): ").strip()
    
    try:
        with open(input_file, 'r') as f:
            all_domains = [line.strip() for line in f if line.strip()]
    except:
        print("[-] File not found!")
        return

    total = len(all_domains)
    num_tabs = int(input(f"[?] Total: {total}. How many tabs? "))
    
    chunks = [all_domains[i::num_tabs] for i in range(num_tabs)]
    start_time = time.time()

    tasks = [scrape_tab(i+1, chunks[i], total, start_time) for i in range(num_tabs) if chunks[i]]
    await asyncio.gather(*tasks)

    # Save Results
    output = 'results_n4y3mx.csv'
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Domain', 'Status', 'Registrant', 'Email', 'Expiry'])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n\n{'='*45}\nDONE! Results in {output}\n{'='*45}")

if __name__ == "__main__":
    asyncio.run(main())

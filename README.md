# 🚀 BTCL .bd Domain Scraper & Wordlist Generator
**Developed by:** [/n4y3mx](https://github.com/n4y3mx)  
**Socials:** [Facebook](https://fb.com/n4y3mx) | [Instagram](https://instagram.com/n4y3mx) | [X (Twitter)](https://x.com/n4y3mx)

---

##  Description (English)
The **BTCL .bd Domain Scraper** is a high-performance, asynchronous automation tool designed to check the availability of `.bd` domains directly from the official **Bangladesh Telecommunications Company Limited (BTCL)** portal. It includes a specialized **Wordlist Generator** for bulk domain exploration.
### ✨ Key Features
* **Multi-Tab Concurrency:** Run multiple browser instances (tabs) simultaneously to maximize speed.
* **Wise Synchronization:** Custom logic ensures the script waits for the specific domain's result to render before scraping, preventing data mismatch.
* **No-Reload Logic:** Uses DOM injection to swap search queries without refreshing the page, saving 300% more time and data.
* **WHOIS Data Extraction:** Automatically pulls **Registrant Name**, **Admin Email**, and **Expiry Date** for registered domains.

---

এটি একটি হাই-স্পিড ডোমেইন স্ক্র্যাপার এবং ওয়ার্ডলিস্ট জেনারেটর। এর মাধ্যমে আপনি কয়েক হাজার ডোমেইন একসাথে চেক করতে পারবেন।

### 🛠 প্রধান বৈশিষ্ট্যসমূহ:
* **মাল্টি-ট্যাব সাপোর্ট:** আপনার পিসির সক্ষমতা অনুযায়ী একসাথে একাধিক ট্যাবে কাজ করার সুবিধা।
* **স্মার্ট সিঙ্ক্রোনাইজেশন:** ডাটা যাতে ভুল না আসে সেজন্য প্রতিটি রেজাল্ট কনফার্ম হয়ে তবেই সেভ করে।
* **নো-রিলোড লজিক:** বারবার পেজ রিলোড না করেই দ্রুত সার্চ সম্পন্ন করে, যা আপনার ইন্টারনেট ও সময় সাশ্রয় করে।
* **WHOIS ডাটা:** ইতিমধ্যে কেনা ডোমেইনের মালিকের তথ্য ও মেয়াদ শেষ হওয়ার তারিখ বের করে আনে।

---

## ⚙️ Installation
Follow these steps to set up the environment:
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/n4y3mx/BTCL-Scraper.git](https://github.com/n4y3mx/BTCL-Scraper.git)
   cd BTCL-Scraper   ```
   
**Install dependencies:**
```bash
pip install playwright
playwright install chromium  ```

 How to Use / ব্যবহারের নিয়ম
 Step One: Generate Wordlist (লিস্ট তৈরি করা)
To create a custom list (e.g., all 3-character combinations), use the following command: নির্দিষ্ট ক্যারেক্টার দিয়ে ডোমেইন লিস্ট বানাতে চাইলে:

```Bash
python wordlist_generator.py -c qwertyuiopasdfghjklzxcvbnm -min 3 -max 3 -o N
-c: Character set (অক্ষরগুলো)

-min / -max: Length (শব্দের দৈর্ঘ্য)

-o: Output prefix (ফাইলের নাম)

 Step Two: Run Scraper (ডোমেইন চেক করা)
Start checking the availability of your list: ডোমেইন এভেইলিবিলিটি চেক শুরু করতে:

```Bash
python scraper.py
Enter the filename you generated in step one (e.g., N.txt).

Enter the number of parallel tabs (Recommended: 3-5 for stability).

Results will be saved automatically to results_n4y3mx.csv.

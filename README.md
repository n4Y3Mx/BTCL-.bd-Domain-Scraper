#  BTCL .bd Domain Scraper & Wordlist Generator
**Developed by:** [n4y3mx](https://github.com/n4y3mx)  
**Socials:** [Facebook](https://fb.com/n4y3mx) | [Instagram](https://instagram.com/n4y3mx) | [X (Twitter)](https://x.com/n4y3mx)

---

## Description (English)
The **BTCL .bd Domain Scraper** is a high-performance, asynchronous automation tool designed to check the availability of `.bd` domains directly from the official Bangladesh Telecommunications Company Limited (BTCL) search page. It can also generate wordlists for bulk checking and extract WHOIS data for registered domains.

###  Key Features
* **Multi-Tab Concurrency:** Run multiple browser instances (tabs) simultaneously to maximize throughput.
* **Smart Synchronization:** Custom logic ensures the script waits for the specific domain's result to render before scraping, preventing data mismatch.
* **No-Reload Logic:** Uses DOM injection to swap search queries without refreshing the page, greatly saving time and bandwidth.
* **WHOIS Data Extraction:** Automatically pulls Registrant Name, Admin Email, and Expiry Date for registered domains when available.
* **CSV Output:** Results are saved to a CSV file for easy analysis.

---

## বর্ণনা (বাংলা)
এটি একটি হাই-স্পিড ডোমেইন স্ক্র্যাপার এবং ওয়ার্ডলিস্ট জেনারেটর। এটি `.bd` ডোমেইনগুলোর অ্যাভেইলিবিলিটি চেক করতে BTCL-এর অফিসিয়াল সার্চ পেজ ব্যবহার করে এবং রেজিস্টার্ড ডোমেইনের WHOIS তথ্যও সংগ্রহ করতে পারে।

### 🛠 প্রধান বৈশিষ্ট্যসমূহ
* **মাল্টি-ট্যাব সাপোর্ট:** একাধিক ট্যাব দিয়ে দ্রুত চেক করতে পারবেন।
* **স্মার্ট সিঙ্ক্রোনাইজেশন:** প্রতিটি রেজাল্টের রেন্ডার হওয়া পর্যন্ত অপেক্ষা করে সঠিক ডেটা সংগ্রহ করে।
* **নো-রিলোড লজিক:** পেজ বারবার রিলোড না করে DOM ইনজেকশন দিয়ে দ্রুত সার্চ সম্পন্ন করে।
* **WHOIS ডাটা এক্সট্রাকশন:** রেজিস্টার্ড ডোমেইনের মালিকের নাম, ইমেইল, মেয়াদ শেষ হওয়ার তারিখ ইত্যাদি সংগ্রহ করা হয়।
* **CSV আউটপুট:** ফলাফল একটি CSV ফাইলে সংরক্ষণ করা হয়।

---

##  Requirements
* Python 3.8+
* pip
* playwright

(Optional) It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/n4Y3Mx/BTCL-.bd-Domain-Scraper.git
cd BTCL-.bd-Domain-Scraper
```

2. Install dependencies:
```bash
pip install playwright
playwright install chromium
```

(If you have a requirements.txt in the project, you can also run `pip install -r requirements.txt`.)

---

## How to Use / ব্যবহারের নিয়ম

### Step One: Generate Wordlist (লিস্ট তৈরি করা)
Generate a custom wordlist. Example: create all 3-character combinations from a given character set.

Usage:
```bash
python wordlist_generator.py -c qwertyuiopasdfghjklzxcvbnm -min 3 -max 3 -o N
```

Parameters:
* `-c` : Character set (অক্ষরগুলো), e.g. `abcdefghijklmnopqrstuvwxyz`
* `-min` / `-max` : Minimum and maximum length of words to generate
* `-o` : Output file prefix (the script will create a file like `N.txt`)

Example:
```bash
python wordlist_generator.py -c abc -min 2 -max 3 -o sample
# creates sample.txt containing all combinations of 'a','b','c' with length 2 and 3
```

---

### Step Two: Run Scraper (ডোমেইন চেক করা)
Start checking the availability of domains from the generated wordlist.

Run:
```bash
python scraper.py
```

The script will prompt you for:
1. The filename you generated in step one (e.g., `N.txt`).
2. The number of parallel tabs to use (Recommended: 3–5 for most machines).
3. Any additional options as prompted by the script.

Results will be saved automatically to `results_n4y3mx.csv` (or another CSV filename if the script allows customizing it).

---

## Output
* Available domains and WHOIS information (when present) will be written to a CSV file for later review.
* Check the CSV to see domain status, registrant info, and expiry dates.

---

## Notes & Recommendations
* Respect the target site's terms of service. Use reasonable concurrency to avoid overloading BTCL's servers.
* Consider adding delays or using lower concurrency if you notice throttling or blocking.
* Use the tool responsibly and only for permitted legitimate purposes.

---

## Support
If you find a bug or have suggestions, please open an issue in this repository: [Issues](https://github.com/n4Y3Mx/BTCL-.bd-Domain-Scraper/issues)

---

## License
Specify your license here (e.g., MIT). If you don't have one yet, add a LICENSE file to the repository.

---

Thank you and happy scraping! / ধন্যবাদ এবং শুভ স্ক্র্যাপিং!
```

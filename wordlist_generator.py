# python name.py  -c qwertyuiopasdfghjklzxcvbnm -min 3 -max 3 -o N
#a tool by /n4y3mx
import itertools
import argparse
import os
print("Demo cmd: python name.py  -c qwertyuiopasdfghjklzxcvbnm -min 3 -max 3 -o N \n")

def generate_wordlist(charset, min_len, max_len, output_prefix, lines_per_file):
    count = 0
    file_idx = 1
    current_file = f"{output_prefix}_{file_idx}.txt"
    f = open(current_file, 'w')

    print(f"[*] Starting generation: {min_len} to {max_len} chars...")
    
    try:
        for length in range(min_len, max_len + 1):
            for combination in itertools.product(charset, repeat=length):
                word = ''.join(combination)
                f.write(word + '\n')
                count += 1
                
                # Check if we need to split into a new file
                if lines_per_file and count >= lines_per_file:
                    f.close()
                    print(f"[+] Saved {current_file}")
                    file_idx += 1
                    count = 0
                    current_file = f"{output_prefix}_{file_idx}.txt"
                    f = open(current_file, 'w')
        
        f.close()
        if count > 0:
            print(f"[+] Saved {current_file}")
            
    except KeyboardInterrupt:
        f.close()
        print("\n[!] Stopped by user.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Wordlist Generator")
    parser.add_argument("-c", "--charset", required=True, help="Characters to use (e.g. abc123)")
    parser.add_argument("-min", type=int, required=True, help="Minimum length")
    parser.add_argument("-max", type=int, required=True, help="Maximum length")
    parser.add_argument("-o", "--output", default="wordlist", help="Prefix for output files")
    parser.add_argument("-s", "--split", type=int, default=0, help="Number of lines per file (0 for no split)")
    
    args = parser.parse_args()
    generate_wordlist(args.charset, args.min, args.max, args.output, args.split)

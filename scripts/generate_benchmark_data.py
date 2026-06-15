import csv
import random
from datetime import datetime, timedelta

def generate_transactions(num_rows=1034):
    categories = [
        {"name": "Food & Dining", "descriptions": ["HIGHLANDS COFFEE", "KFC", "PHUC LONG", "SHOPEEFOOD", "GRABFOOD", "STARBUCKS", "COM TAM", "NHA HANG", "Lotteria"]},
        {"name": "Shopping", "descriptions": ["SHOPEE VN", "TIKI", "LAZADA", "VINMART", "CIRCLE K", "GS25", "FAMILY MART", "ZARA", "H&M"]},
        {"name": "Transport", "descriptions": ["GRABBIKE", "GRABCAR", "BEE", "XANH SM", "PETROLIMEX", "COMECO", "VEXERE", "VETC"]},
        {"name": "Utilities", "descriptions": ["THANH TOAN TIEN DIEN", "TIEN NUOC WACO", "VNPT INTERNET", "VIETTEL", "FPT TELECOM", "MOBIFONE"]},
        {"name": "Transfer", "descriptions": ["CHUYEN TIEN CHO", "MBBANK TRANSFER", "NAP TIEN MOMO", "ZALOPAY", "RUT TIEN ATM", "CHUYEN KHOAN"]},
        {"name": "Entertainment", "descriptions": ["CGV CINEMAS", "GALAXY CINEMA", "NETFLIX", "SPOTIFY", "STEAM", "TIKTOK"]},
        {"name": "Health", "descriptions": ["PHARMACITY", "LONG CHAU", "BENH VIEN", "NHA KHOA"]},
        {"name": "Salary", "descriptions": ["TRA LUONG THANG", "THUONG QUY", "SALARY", "CTY THANH TOAN L\u01AF\u01A0NG"]}
    ]
    
    start_date = datetime(2026, 1, 1)
    transactions = []
    
    for i in range(num_rows):
        cat = random.choice(categories)
        desc = random.choice(cat["descriptions"])
        if cat["name"] == "Salary":
            amount = random.randint(10000000, 30000000)
        else:
            amount = -random.randint(20000, 2000000)
            
        # 10% chance to add some noise to description
        if random.random() < 0.1:
            desc += f" {random.randint(1000, 9999)}"
            
        date = start_date + timedelta(days=random.randint(0, 180), hours=random.randint(7, 22), minutes=random.randint(0, 59))
        
        transactions.append({
            "Date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "Description": desc,
            "Amount": amount,
            "Ground_Truth_Category": cat["name"]
        })
        
    return transactions

def main():
    import os
    os.makedirs('sample_data', exist_ok=True)
    filename = 'sample_data/benchmark_1000_tx.csv'
    
    data = generate_transactions(1034)
    # Sort by date
    data.sort(key=lambda x: x["Date"])
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "Description", "Amount", "Ground_Truth_Category"])
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Generated {len(data)} transactions at {filename}")

if __name__ == '__main__':
    main()

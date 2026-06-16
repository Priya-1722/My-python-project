import random

# Simulating market data with clean, split text rows
scraped_market_data = [
    {
        "user": "Alex", "item": "Wireless Earbuds", "stars": 5, 
        "text": "Absolutely incredible sound quality, love the bass!"
    },
    {
        "user": "Sam", "item": "Wireless Earbuds", "stars": 2, 
        "text": "Battery dies in one hour. Terrible product quality."
    },
    {
        "user": "Chris", "item": "Smart Watch", "stars": 4, 
        "text": "Great screen, but the charging cable is short."
    },
    {
        "user": "Taylor", "item": "Wireless Earbuds", "stars": 1, 
        "text": "Broken on arrival! Extremely disappointed."
    },
    {
        "user": "Jordan", "item": "Smart Watch", "stars": 5, 
        "text": "Perfect tracker. Best purchase of the year!"
    }
]

print("🚀 RUNNING BACKEND ANALYTICS ENGINE 🚀\n")

total_reviews = len(scraped_market_data)
complaints_count = 0
praise_count = 0

# Processing the raw database queue
for review in scraped_market_data:
    print(f"Processing ID: {random.randint(1000, 9999)} | Item: {review['item']}")
    print(f"Raw Text: '{review['text']}'")
    
    # Core Analytics Logic: Tagging data by business priority
    if review['stars'] <= 2:
        status = "❌ CRITICAL COMPLAINT"
        complaints_count += 1
    else:
        status = "✅ POSITIVE FEEDBACK"
        praise_count += 1
        
    print(f"Automated Classification: {status}")
    print("-" * 50)

# Calculate a Customer Satisfaction Index (CSI) percentage
satisfaction_rate = (praise_count / total_reviews) * 100

print("\n📊 ENTERPRISE ANALYTICS SUMMARY GENERATED 📊")
print(f"Total Records Processed: {total_reviews}")
print(f"Flagged Critical Complaints: {complaints_count}")
print(f"Approved Praise Logs: {praise_count}")
print(f"Final Product Health Score: {satisfaction_rate:.1f}%")

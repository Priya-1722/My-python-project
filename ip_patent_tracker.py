print("📜 INTELLECTUAL PROPERTY & PATENT TRACKER 📜\n")

# Database of currently registered intellectual property
ip_database = {
    "PAT-101": {"title": "Automated Data Filtering Engine", "type": "Patent", "status": "Approved"},
    "TM-202": {"title": "SecureKey", "type": "Trademark", "status": "Pending"},
    "PAT-303": {"title": "Neural Network Optimizer", "type": "Patent", "status": "Under Review"}
}

def scan_trademark_conflict(new_name):
    """Scans database to ensure a new name doesn't conflict with existing IP"""
    print(f"Scanning registry for conflict with: '{new_name}'...")
    for ip_id, details in ip_database.items():
        if new_name.lower() in details["title"].lower():
            return f"❌ CONFLICT DETECTED: Matches {ip_id} ('{details['title']}')"
    return "✅ REGISTRY CLEAN: Name is available for registration."

def check_international_compliance(ip_type, country_count):
    """Checks if the filing meets basic international treaty rules based on country distribution"""
    if ip_type == "Patent" and country_count >= 3:
        return "🌐 Fast-Track Status: Eligible for International Patent Streams."
    return "📍 Status: Standard Regional Filing Only."

# --- SIMULATING THE REGLATORY TECH APP ---

# 1. Display Current IP Portfolio Status
print("--- Current Registered IP Portfolio ---")
for ip_id, data in ip_database.items():
    print(f"[{ip_id}] {data['title']} ({data['type']}) - Status: {data['status']}")

print("\n--- Running System Security & Clearance Checks ---")

# 2. Test the Conflict Scanner (Simulating an infringement check)
check_1 = scan_trademark_conflict("SecureKey Tech")
print(check_1)

check_2 = scan_trademark_conflict("Eco Power Grid")
print(check_2)

# 3. Test Global Filing Compliance Logic
print("\n--- International Treaty Compliance Validation ---")
compliance_check = check_international_compliance("Patent", country_count=4)
print(compliance_check)

print("\n🔒 SYSTEM LOGS SECURED: REGULATORY EVALUATION COMPLETE 🔒")

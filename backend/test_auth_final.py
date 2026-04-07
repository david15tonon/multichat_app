"""
Complete Authentication Test
Verify that users can signup, login, and are stored in the database
"""
import httpx
import json
import sqlite3
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/api"
DB_PATH = "./multichat.db"

async def test_auth_complete():
    print("=" * 60)
    print("🧪 COMPLETE AUTHENTICATION TEST")
    print("=" * 60)
    
    async with httpx.AsyncClient() as client:
        # 1. Create a unique email based on timestamp
        timestamp = int(datetime.now().timestamp())
        email = f"user_{timestamp}@example.com"
        
        print(f"\n1️⃣ Signup with email: {email}")
        signup_data = {
            "email": email,
            "full_name": "Test User",
            "password": "SecurePass123!",
            "preferred_language": "FR",
            "preferred_tone": "CASUAL"
        }
        
        response = await client.post(f"{BASE_URL}/auth/signup", json=signup_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"   ❌ Error: {response.text}")
            return
        
        signup_response = response.json()
        token = signup_response.get("access_token")
        print(f"   ✅ Signup successful")
        print(f"   Token: {token[:40]}...")
        
        # 2. Login with those credentials
        print(f"\n2️⃣ Login with email: {email}")
        login_data = {
            "email": email,
            "password": "SecurePass123!"
        }
        
        response = await client.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"   ❌ Error: {response.json()}")
            return
        
        login_response = response.json()
        login_token = login_response.get("access_token")
        print(f"   ✅ Login successful")
        print(f"   Token: {login_token[:40]}...")
        
        # 3. Get current user
        print(f"\n3️⃣ Get current user info")
        response = await client.get(
            f"{BASE_URL}/auth/me",
            headers={"Authorization": f"Bearer {login_token}"}
        )
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            user_info = response.json()
            print(f"   ✅ User info retrieved:")
            print(f"      ID: {user_info.get('id')}")
            print(f"      Email: {user_info.get('email')}")
            print(f"      Name: {user_info.get('full_name')}")
            print(f"      Language: {user_info.get('preferred_language')}")
        else:
            print(f"   ❌ Error: {response.json()}")
    
    # 4. Verify in database
    print(f"\n4️⃣ Verify in database")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, email, full_name, preferred_language, is_active FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            print(f"   ✅ User found in database:")
            print(f"      ID: {result[0]}")
            print(f"      Email: {result[1]}")
            print(f"      Name: {result[2]}")
            print(f"      Language: {result[3]}")
            print(f"      Active: {result[4]}")
        else:
            print(f"   ❌ User NOT found in database")
    except Exception as e:
        print(f"   ❌ Database error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Authentication test complete!")
    print("=" * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_auth_complete())

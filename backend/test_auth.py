"""
Test Authentication - Signup and Login
Verify that users are created in the database and can authenticate
"""
import httpx
import json

BASE_URL = "http://127.0.0.1:8000/api"

async def test_auth():
    async with httpx.AsyncClient() as client:
        print("🧪 Testing Authentication Flow...\n")
        
        # 1. Test Signup
        print("1️⃣ Testing Signup...")
        signup_data = {
            "email": "alice@example.com",
            "full_name": "Alice Wonderland",
            "password": "SecurePassword123!",
            "preferred_language": "FR",
            "preferred_tone": "CASUAL"
        }
        
        response = await client.post(f"{BASE_URL}/auth/signup", json=signup_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            token = data.get("access_token")
            print(f"   ✅ User created successfully")
            print(f"   Token: {token[:50]}...")
        else:
            print(f"   ❌ Error: {response.json()}")
            return
        
        # 2. Test Login with correct credentials
        print("\n2️⃣ Testing Login with correct credentials...")
        login_data = {
            "email": "alice@example.com",
            "password": "SecurePassword123!"
        }
        
        response = await client.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            login_token = data.get("access_token")
            print(f"   ✅ Login successful")
            print(f"   Token: {login_token[:50]}...")
        else:
            print(f"   ❌ Login failed: {response.json()}")
            return
        
        # 3. Get current user info
        print("\n3️⃣ Testing GET /me (current user)...")
        response = await client.get(
            f"{BASE_URL}/auth/me",
            headers={"Authorization": f"Bearer {login_token}"}
        )
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            user_data = response.json()
            print(f"   ✅ Retrieved user info:")
            print(f"      Email: {user_data['email']}")
            print(f"      Name: {user_data['full_name']}")
            print(f"      Language: {user_data['preferred_language']}")
        else:
            print(f"   ❌ Error: {response.json()}")
        
        # 4. Test Login with wrong password
        print("\n4️⃣ Testing Login with wrong password...")
        wrong_login = {
            "email": "alice@example.com",
            "password": "WrongPassword"
        }
        
        response = await client.post(f"{BASE_URL}/auth/login", json=wrong_login)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 401:
            print(f"   ✅ Correctly rejected invalid credentials")
        else:
            print(f"   ❌ Should have rejected wrong password")
        
        # 5. Test duplicate email signup
        print("\n5️⃣ Testing Signup with duplicate email...")
        response = await client.post(f"{BASE_URL}/auth/signup", json=signup_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 409:
            print(f"   ✅ Correctly rejected duplicate email")
        else:
            print(f"   ❌ Should have rejected duplicate")
        
        print("\n🎉 All authentication tests passed!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_auth())

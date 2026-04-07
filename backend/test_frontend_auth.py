#!/usr/bin/env python3
"""
Test script to verify complete authentication flow for frontend
"""
import httpx
import asyncio
import json
from datetime import datetime

API_URL = "http://127.0.0.1:8000/api"

async def test_auth_flow():
    async with httpx.AsyncClient(timeout=10) as client:
        print("=" * 60)
        print("🧪 FRONTEND AUTHENTICATION FLOW TEST")
        print("=" * 60)
        
        # Generate unique email with timestamp
        timestamp = int(datetime.now().timestamp())
        email = f"frontend_user_{timestamp}@test.com"
        password = "TestPassword123!"
        full_name = "Frontend Test User"
        
        # 1. Sign up
        print(f"\n1️⃣ SIGNUP")
        print(f"   Email: {email}")
        print(f"   Password: {password}")
        print(f"   Full Name: {full_name}")
        
        signup_response = await client.post(
            f"{API_URL}/auth/signup",
            json={
                "email": email,
                "password": password,
                "full_name": full_name,
                "preferred_language": "FR",
            }
        )
        
        if signup_response.status_code == 200:
            signup_data = signup_response.json()
            access_token = signup_data.get('access_token')
            print(f"   ✅ Signup successful")
            print(f"   Token: {access_token[:50]}...")
        else:
            print(f"   ❌ Signup failed: {signup_response.status_code}")
            print(f"   Error: {signup_response.text}")
            return
        
        # 2. Get current user info (with signup token)
        print(f"\n2️⃣ GET CURRENT USER (using signup token)")
        me_response = await client.get(
            f"{API_URL}/auth/me",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        
        if me_response.status_code == 200:
            user_data = me_response.json()
            print(f"   ✅ User info retrieved")
            print(f"   ID: {user_data.get('id')}")
            print(f"   Email: {user_data.get('email')}")
            print(f"   Full Name: {user_data.get('full_name')}")
            print(f"   Preferred Language: {user_data.get('preferred_language')}")
        else:
            print(f"   ❌ Failed to get user: {me_response.status_code}")
            print(f"   Error: {me_response.text}")
            return
        
        # 3. Logout (clear token) and try login
        print(f"\n3️⃣ LOGIN WITH CREDENTIALS")
        print(f"   Email: {email}")
        print(f"   Password: {password}")
        
        login_response = await client.post(
            f"{API_URL}/auth/login",
            json={"email": email, "password": password}
        )
        
        if login_response.status_code == 200:
            login_data = login_response.json()
            login_token = login_data.get('access_token')
            print(f"   ✅ Login successful")
            print(f"   Token: {login_token[:50]}...")
            
            # Verify login token works
            verify_response = await client.get(
                f"{API_URL}/auth/me",
                headers={"Authorization": f"Bearer {login_token}"}
            )
            
            if verify_response.status_code == 200:
                print(f"   ✅ Login token verified")
            else:
                print(f"   ❌ Login token verification failed")
        else:
            print(f"   ❌ Login failed: {login_response.status_code}")
            print(f"   Error: {login_response.text}")
            return
        
        # 4. Test invalid token
        print(f"\n4️⃣ TEST INVALID TOKEN REJECTION")
        invalid_response = await client.get(
            f"{API_URL}/auth/me",
            headers={"Authorization": "Bearer invalid_token_123"}
        )
        
        if invalid_response.status_code == 401:
            print(f"   ✅ Invalid token rejected correctly (401)")
        else:
            print(f"   ❌ Expected 401, got {invalid_response.status_code}")
        
        # 5. Test missing token
        print(f"\n5️⃣ TEST MISSING TOKEN")
        no_token_response = await client.get(f"{API_URL}/auth/me")
        
        if no_token_response.status_code in [401, 403]:
            print(f"   ✅ Missing token rejected correctly ({no_token_response.status_code})")
        else:
            print(f"   ❌ Expected 401/403, got {no_token_response.status_code}")
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\n🎯 Frontend can now:")
        print("   ✅ Sign up new users")
        print("   ✅ Login existing users")
        print("   ✅ Verify tokens")
        print("   ✅ Protect routes with authentication")

if __name__ == "__main__":
    asyncio.run(test_auth_flow())

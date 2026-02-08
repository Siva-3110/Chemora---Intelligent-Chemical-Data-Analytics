"""
Test script to verify desktop app authentication works with web app accounts
"""
import requests
import base64

API_BASE = "http://localhost:8000/api"

def test_auth(username, password):
    """Test authentication with given credentials"""
    print(f"\n{'='*60}")
    print(f"Testing authentication for: {username}")
    print(f"{'='*60}")
    
    # Create Basic Auth header (same as desktop app)
    auth_string = base64.b64encode(f"{username}:{password}".encode()).decode()
    auth_header = {"Authorization": f"Basic {auth_string}"}
    
    try:
        # Test datasets endpoint (same as desktop app)
        response = requests.get(f"{API_BASE}/datasets/", headers=auth_header, timeout=5)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            datasets = response.json()
            print(f"✅ Authentication SUCCESSFUL!")
            print(f"   Found {len(datasets)} datasets")
            return True
        elif response.status_code == 401:
            print(f"❌ Authentication FAILED - Invalid credentials")
            return False
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection Error - Backend not running at {API_BASE}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n🧪 Desktop App Authentication Test")
    print("="*60)
    print("This script tests if desktop app can authenticate with")
    print("accounts created in the web app")
    print("="*60)
    
    # Test admin account
    test_auth("admin", "admin")
    
    # Test with a custom account (replace with your web app account)
    print("\n\nTo test your web app account:")
    print("1. Create an account in the web app")
    print("2. Update the credentials below and run this script")
    print("\nExample:")
    print('test_auth("your_username", "your_password")')
    
    input("\n\nPress Enter to exit...")

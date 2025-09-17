import requests
import os
from urllib.parse import urlparse
from pathlib import Path

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    print("The Wisdom of Ubuntu: 'I am because we are'\n")
    
    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Please try again.")
        return
    
    # Validate URL format
    if not url.startswith(('http://', 'https://')):
        print("❌ Invalid URL format. Please include http:// or https://")
        return
    
    try:
        # Create directory for fetched images
        os.makedirs("Fetched_Images", exist_ok=True)
        print("✓ Fetched_Images directory ready")
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        path = parsed_url.path
        filename = os.path.basename(path)
        
        if not filename:
            # If no filename in URL, generate one
            filename = f"ubuntu_image_{int(os.times()[4])}.jpg"
        
        # Add extension if missing
        if '.' not in filename:
            filename += '.jpg'
        
        # Fetch the image
        print(f"🔄 Connecting to {parsed_url.netloc}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Check if content is an image
        content_type = response.headers.get('content-type', '')
        if 'image' not in content_type:
            print("❌ The URL does not point to an image file")
            return
        
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {str(e)}")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
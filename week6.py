import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher - week6.py:7")
    print("A tool for mindfully collecting images from the web\n - week6.py:8")

    # Get multiple URLs from user (comma-separated)
    urls = input("Enter one or more image URLs (comma-separated): ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Track downloaded files to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        url = url.strip()  # clean spaces
        if not url:
            continue

        try:
            # Fetch the image with headers
            headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()

            # --- Security precautions ---
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} (not an image, got {content_type}) - week6.py:33")
                continue

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            # Compute hash to detect duplicates
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"✗ Skipping duplicate: {filename} - week6.py:45")
                continue
            downloaded_hashes.add(file_hash)

            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename} - week6.py:54")
            print(f"✓ Image saved to {filepath} - week6.py:55")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e} - week6.py:58")
        except Exception as e:
            print(f"✗ An error occurred: {e} - week6.py:60")

    print("\nConnection strengthened. Community enriched. 🌱 - week6.py:62")

if __name__ == "__main__":
    main()

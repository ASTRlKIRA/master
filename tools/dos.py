import threading
import requests
import time

# Function to send a request
def send_request(url, thread_id):
    try:
        response = requests.get(url)
        print(f"Thread {thread_id}: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Thread {thread_id}: Error {e}")

# Main function to create and manage threads
def main():
    url = "https://example.com"  # Replace with the target URL
    num_threads = 99999  # Number of threads

    # List to hold threads
    threads = []

    print("Starting threads...")
    start_time = time.time()

    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"All threads completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()

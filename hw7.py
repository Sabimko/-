import schedule
import requests
import time
import argparse
import logging


logging.basicConfig(filename='http_requests.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def perform_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Successful request to {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to {url} failed: {e}")

def main(url, initial_delay, interval):
    
    time.sleep(initial_delay)
    
    
    schedule.every(interval).seconds.do(perform_request, url=url)

    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            logging.error(f"Error while running scheduled job: {e}")
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated HTTP request scheduler")
    parser.add_argument("url", type=str, help="URL to send requests to")
    parser.add_argument("initial_delay", type=int, help="Initial delay before the first request (in seconds)")
    parser.add_argument("interval", type=int, help="Interval between requests (in seconds)")
    
    args = parser.parse_args()
    
    try:
        main(args.url, args.initial_delay, args.interval)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped manually.")
    except Exception as e:
        logging.error(f"Scheduler stopped due to an error: {e}")

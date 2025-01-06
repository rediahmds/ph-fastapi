import time
from src.scripts.mock_ph import MockPh
import requests


class MockPhRequest(MockPh):
    def __init__(self):
        super().__init__()
        self.url = "http://localhost:8000/ph"
        self.delay_seconds = 1

    def mock_post(self):
        ph = self.generate_random_ph()
        result = self.determine_safety(ph)

        payload = {"ph": ph, "result": result}

        print(f"[INFO] Sending POST request to {self.url}...")
        try:
            response = requests.post(url=self.url, json=payload)
            print(f"[SUCCESS] Server response: {response}")
        except requests.HTTPError as h:
            print(f"[ERROR] Failed HTTPError: {h}")
        except requests.JSONDecodeError as j:
            print(f"[ERROR] Failed JSONDecode: {j}")
        except requests.RequestException as r:
            print(f"[ERROR] Failed unknown: {r}")

    def send_with_delay(self):
        while True:
            self.mock_post()
            time.sleep(self.delay_seconds)

    def begin_mock(self):
        self.send_with_delay()

from pypresence import Presence
import time

start = int(time.time())
client_id = "1098592713106006047"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image = "3296160",
        large_text = "이것은 책이여",
        state = "현대사회와정신건강 (BDU)",
        start = start
    )
    time.sleep(60)
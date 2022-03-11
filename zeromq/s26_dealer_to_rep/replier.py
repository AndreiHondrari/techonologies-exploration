import random
import itertools as itls

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Replier [{UID}] started")

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)

    counter = itls.count(start=1)

    try:
        sock.connect("tcp://127.0.0.1:7777")

        print(f"[{UID}] Start listening for requests")
        while True:
            # request
            request = sock.recv_string()
            print("RECV", request)

            # reply
            reply_value = next(counter)
            reply = f"{UID}_{reply_value}"
            print(f"REP {reply}")
            sock.send_string(reply)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        sock.close(1)

    print("Closing context ...")
    ctx.term()

    print(f"Replier [{UID}] terminated")


if __name__ == '__main__':
    main()

import time
import zmq


if __name__ == '__main__':
    print("Starting receiver ...")

    print("Advertise socket ...")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:5555")

    print("Register polling")
    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    print("Start receiving ....")
    try:
        while True:
            polled = dict(poller.poll())

            msg_parts = []

            while True:
                frame = sock.recv(flags=zmq.DONTWAIT, copy=False)
                msg_parts.append(frame.bytes)
                if not frame.more:
                    print("Multipart read finished", flush=True)
                    break

            msg = tuple(
                map(
                    lambda s: s.decode(),
                    msg_parts
                )
            )

            when = time.strftime("%H:%M:%S")
            print(f"[{when}] Received", msg, flush=True)

    except KeyboardInterrupt:
        print("\nReceiver terminated")

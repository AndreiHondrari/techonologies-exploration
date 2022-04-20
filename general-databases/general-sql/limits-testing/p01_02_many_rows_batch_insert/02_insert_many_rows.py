import time
import random

import psycopg2 as pg
from psycopg2.extras import execute_values


def main() -> None:
    print("Start values generation")

    # setup
    conn = pg.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        database="somedb"
    )
    curr = conn.cursor()

    # main
    start = time.time()

    try:
        print("Generating values list ...")
        values = []

        for i in range(10_000_000):
            val = random.randint(100, 1_000)
            values.append((i, val,))

        print("Executing in batch ... (probably 120 seconds)")
        execute_values(
            curr,
            "INSERT INTO test_table_1 VALUES %s",
            values
        )

        print("Committing ...")
        conn.commit()

        stop = time.time()
        elapsed = stop - start

    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    # cleanup
    curr.close()
    conn.close()
    print(f"Values generation DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()

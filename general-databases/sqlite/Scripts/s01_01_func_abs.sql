DROP TABLE IF EXISTS t1;

CREATE TABLE IF NOT EXISTS t1 (
	x
);

INSERT INTO t1 VALUES (123), (-123), (0), (555), (-555);

SELECT x, abs(x) AS abs_x FROM t1;

DROP TABLE IF EXISTS t1;
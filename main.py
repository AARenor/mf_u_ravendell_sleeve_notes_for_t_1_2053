from pathlib import Path
import os
import sys

TEXT = (
    "After Rain\n"
    "Three frogs play sax, bass and drums in the back of a closed florist's. "
    "The bassist stops a note with one webbed finger. "
    "In the buckets, the cut stems tremble."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()

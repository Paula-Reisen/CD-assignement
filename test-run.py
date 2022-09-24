import sys
import main


def test_main(capsys):
    # Test on a short snippet first
    sys.stdin = io.StringIO("abcdef")
    sys.argv = ["main.py", "f"]

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "abcde"
    assert captured.err == "1"

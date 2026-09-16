from public_core.__main__ import main


def test_demo_reaches_verification(capsys) -> None:
    main()
    output = capsys.readouterr().out

    assert "intake: demo-1" in output
    assert "approved: approval evidence recorded" in output
    assert "verified: verification evidence recorded" in output

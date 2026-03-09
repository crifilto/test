from src.main import main

def test_main(capsys):
    """Prueba básica para la función main"""
    main()
    captured = capsys.readouterr()
    assert "Hello from template Python app" in captured.out

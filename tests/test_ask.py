from types import SimpleNamespace

from app import ask as ask_module


def test_ask_prints_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        text="回答",
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=7),
    )
    client = SimpleNamespace(models=SimpleNamespace(generate_content=lambda **_: response))
    monkeypatch.setattr(ask_module.genai, "Client", lambda **_: client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")

    assert ask_module.ask("質問") == "回答"
    assert capsys.readouterr().out == "[入力トークン] 12\n[出力トークン] 7\n"


def test_ask_handles_missing_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(text="回答", usage_metadata=None)
    client = SimpleNamespace(models=SimpleNamespace(generate_content=lambda **_: response))
    monkeypatch.setattr(ask_module.genai, "Client", lambda **_: client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")

    assert ask_module.ask("質問") == "回答"
    assert capsys.readouterr().out == "[入力トークン] 不明\n[出力トークン] 不明\n"

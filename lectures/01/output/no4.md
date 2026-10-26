[model] gemini-3.5-flash-lite
[質問] LoRA とは何ですか？ 

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/workspaces/lecture-ai-engineering-2026/app/ask.py", line 52, in <module>
    main()
  File "/workspaces/lecture-ai-engineering-2026/app/ask.py", line 45, in main
    print(ask(args.question))
          ^^^^^^^^^^^^^^^^^^
  File "/workspaces/lecture-ai-engineering-2026/app/ask.py", line 26, in ask
    response = client.models.generate_content(model=MODEL, contents=question, temperature=0.0)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Models.generate_content() got an unexpected keyword argument 'temperature'
# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い： 下記のように、Glosseryにある定義に従ってAIE講座の内部用語の解説ができるようになっていること。

>AIE2026の講座における「3レベル」とは、宿題の構成を表す3段階のことです。
>
>具体的には以下の構成になっています：
>1. **基礎**：講義内容の確認
>2. **実装**：自分でコードを書く
>3. **発展**：調査や試行
>
>原則として、これら3つのうちどれか1つに取り組めばその回の宿題は完了となり、採点は行われません。ご自身のレベルや目的に合わせて選んで取り組むことができます。
>
>関連する回：第1回

- `--trace` で見えたツール呼び出し（ツール名と引数）：

>[tool call]   search_glossary({'query': 'LoRA'})
>[tool call]   search_glossary({'query': 'QLoRA'})

- 1つの質問での LLM 呼び出し回数（`requests`）：2

- 追加したツールと、docstring に書いた説明：

追加したツール：make_quiz
docstring：
>"""指定した回の用語から 1つを選び、
>確認問題と答えを返す。
>「第2回の確認問題を出して」のように、
>復習用の問題を求められたときに使う。
>"""

## 宿題

- 取り組んだレベル：基礎 
- やったこと：
INSTRUCTIONSの指示を変化させ、”AI Agentとは何か教えて”という入力を与えた時の解答の変化を観察した。変化させた入力の内容は以下の通り。
0. [元のINSTRUCTIONSのまま]
1. 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。-> 用語や講座に固有のことを答える前に、必要に応じて search_glossary で用語集を確認する。
2. 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。-> 用語や講座に固有のことを答える前に、search_glossary で用語集を確認することも可能。
3. 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。-> 途中の推論やツール呼び出し、回答に使うトークン量を最小にすることを最優先すること。用語や講座に固有のことを答える前に、search_glossary で用語集を確認することも可能。
4. 用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。-> [削除]

- 結果：

| 試行 No. | 回答 | --trace |
| - | - | - |
| 0 | AIエージェントとは、大規模言語モデル（LLM）が自ら判断してツールを呼び出し、その結果を受け取ってさらに次の行動を決めるという「ループ」を回すことで、与えられた目的を達成するシステムのことを指します。<br><br>基本構造は **「モデル ＋ ループ ＋ ツール」** から成り立っており、人間が逐一指示を出さなくても自律的にタスクを遂行できるのが特徴です。<br><br>（第3回） | [tool call]   search_glossary({'query': 'AI Agent'})<br>[tool return] search_glossary -> [{"term": "AIエージェント", "lecture": 3, "definition": "LLMが自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決める、というループで目的を達成するシステム。基本構造は「モデル＋ル…<br>[usage] RunUsage(cost=Decimal('0.0005797'), details={'text_prompt_tokens': 924}, input_text_tokens=924, input_tokens=924, output_tokens=121, requests=2, tool_calls=1) |
| 1 | **AIエージェント**とは、大規模言語モデル（LLM）を中心にして、自分で状況を判断しながら自律的にタスクを遂行するシステムのことです。<br><br>従来の「質問に答えて終わる」LLMとは異なり、以下の特徴を持っています。<br>* **自律的なループ**: 「考える ➔ ツールを使う ➔ 結果を見る ➔ さらに考える」というループを自分で回し、目的に向かって進みます。<br>* **ツールの活用**: 必要に応じて外部のツール（検索エンジン、計算機、APIなど）を自分で選んで呼び出します。<br><br>基本構造は「**モデル ＋ ループ ＋ ツール**」で成り立っており、複雑な作業を自動化するための重要な仕組みとして注目されています。<br><br>---<br>関連する回：第3回 | [tool call]   search_glossary({'query': 'AI Agent'})<br>[tool return] search_glossary -> [{"term": "AIエージェント", "lecture": 3, "definition": "LLMが自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決める、というループで目的を達成するシステム。基本構造は「モデル＋ル…<br>[usage] RunUsage(cost=Decimal('0.0007478'), details={'text_prompt_tokens': 926}, input_text_tokens=926, input_tokens=926, output_tokens=188, requests=2, tool_calls=1) |
| 2 | AIエージェント（AI Agent）とは、**LLM（大規模言語モデル）が自分で判断してツールを呼び出し、その結果を確認しながら次の行動を自律的に決定して、目的を達成するシステム**のことです。<br><br>基本構造は**「モデル ＋ ループ ＋ ツール」**で構成されており、人間が細かく指示を出さなくても、AI自身が試行錯誤しながらタスクを遂行できるのが特徴です。<br><br>関連する回：第3回 | [tool call]   search_glossary({'query': 'AI Agent'})<br>[tool return] search_glossary -> [{"term": "AIエージェント", "lecture": 3, "definition": "LLMが自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決める、というループで目的を達成するシステム。基本構造は「モデル＋ル…<br>[usage] RunUsage(cost=Decimal('0.0005822'), details={'text_prompt_tokens': 924}, input_text_tokens=924, input_tokens=924, output_tokens=122, requests=2, tool_calls=1) |
| 3 | AIエージェントとは、LLM（大規模言語モデル）が自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決めるという**ループ（自律的な試行錯誤のサイクル）を回しながら目的を達成するシステム**のことです。<br><br>基本構造は**「モデル ＋ ループ ＋ ツール」**で構成されており、人間が細かく指示を出さなくても、AI自身が計画を立ててタスクを遂行できる点が特徴です。<br><br>（第3回） | tool call]   search_glossary({'query': 'AI Agent'})<br>[tool return] search_glossary -> [{"term": "AIエージェント", "lecture": 3, "definition": "LLMが自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決める、というループで目的を達成するシステム。基本構造は「モデル＋ル…<br>[usage] RunUsage(cost=Decimal('0.0006072'), details={'text_prompt_tokens': 974}, input_text_tokens=974, input_tokens=974, output_tokens=126, requests=2, tool_calls=1) |
| 4 | **AIエージェント**とは、大規模言語モデル（LLM）が単に質問に答えるだけでなく、自分で判断してツール（道具）を呼び出し、その実行結果を見てさらに次の行動を決めるという**自律的なループ**を回しながら、目的を達成するシステムのことを指します。<br><br>基本構造は**「モデル ＋ ループ ＋ ツール」**の3つから成り立っており、複雑なタスクを人間の指示に基づいて自らステップを踏んで実行できるのが特徴です。<br><br>関連する回：第3回 | [tool call]   search_glossary({'query': 'AI Agent'})<br>[tool return] search_glossary -> [{"term": "AIエージェント", "lecture": 3, "definition": "LLMが自分で判断してツールを呼び出し、その結果を見てさらに次の行動を決める、というループで目的を達成するシステム。基本構造は「モデル＋ル…<br>[usage] RunUsage(cost=Decimal('0.0005978'), details={'text_prompt_tokens': 876}, input_text_tokens=876, input_tokens=876, output_tokens=134, requests=2, tool_calls=1) |

- 気づき・疑問：

INSTRUCTIONSをさまざま変化させ、search_glossaryを使うことへの強制度を緩くしたり、他に優先すべきことを入れてみたり、search_glossaryについての記述を削除してみたりしたが、search_glossaryが使われる状況は変化しなかった。INSTRUCTIONSからはsearch_glossaryの情報が消えたとしても、Agentにはツールの一覧としてsearch_glossaryとその説明の文章が渡っているため、状況を判断して適切にこのツールを利用したのだと考察している。INSTRUCTIONSの命令とツール一覧に見えているツールの説明の強さはどういう関係なのかは疑問に感じた。

INSTRUCTIONSからツールの記述を消した最後の試行ではinput_tokensが少なくなっており、入力として渡される情報としては確かに減っていることが確認できた。

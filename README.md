# eye-catche-maker

ブログでよく見かけるアイキャッチ画像を自動生成するスクリプトです。

- 元画像

    <img width="50%" src="target.jpg" />
- 生成後画像

    <img width="50%" src="output.jpg" />

## 使い方
### 前提
- pythonが使える
- gitが使える
- 検証環境：WSL2(Ubuntu)

### 前準備
- まずはローカルに持ってきて`pip install`します

```bash
git clone https://github.com/u943425f/eye-catch-maker.git
cd eye-catch-maker
python -m venv .venv
.venv/script/bin/activate
pip install -r requirements.txt
```
- ttfファイルを収集してきます
    - https://fontfree.me/ とかから収集できます
    - 冒頭の画像の例では、以下のようにしています
        - http://jikasei.me/font/rounded-mgenplus/ からzipファイルをダウンロード
        - 展開後、.envファイルにて`rounded-mgenplus-1c-black.ttf`を指定
- 編集したい画像を収集してきます
    - 冒頭の画像は https://o-dan.net/ja/ から収集してきました
- `.env-sample`ファイルをコピーして、`.env`という名前のファイルを作ります
- .envファイルのパラメータを自分好みに編集します

### スクリプト実行
```bash
python main.py
```

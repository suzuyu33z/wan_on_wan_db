# 投票アプリ

StreamlitとSupabaseを使用した リアルタイム投票アプリです。「〇〇の人！」のような質問を作成し、みんなでYES/NO投票を楽しめます。

## 機能

- 投票作成: 新しい質問を作成
- 投票参加: スマホからYES/NOで投票
- 結果表示: リアルタイムで結果確認

## セットアップ

### 1. 必要なパッケージをインストール

```bash
pip install -r requirements.txt
```

### 2. Supabaseの設定

1. [Supabase](https://supabase.com)でプロジェクトを作成
2. SQLエディタで`database_setup.sql`の内容を実行
3. `.env.example`を`.env`にコピーして環境変数を設定:

```bash
cp .env.example .env
```

`.env`ファイルに以下を設定:
```
SUPABASE_URL=あなたのSupabaseプロジェクトURL
SUPABASE_KEY=あなたのSupabase匿名キー
```

### 3. アプリの起動

```bash
streamlit run main.py
```

## 使い方

1. **投票作成タブ**: 「カラオケが好きな人！」などの質問を入力して投票を開始
2. **投票参加タブ**: 各参加者がスマホでYES/NOをタップ
3. **結果確認タブ**: 「結果を表示」ボタンを押すとYESの人数がドーンと表示！

## データベース構造

- `polls`: 投票の質問と状態を管理
- `votes`: 各投票の結果を記録

リアルタイムで複数人が同時投票可能です！
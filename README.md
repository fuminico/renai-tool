# 恋愛偏差値診断

このプロジェクトは、ユーザーがいくつかの質問に答えることで、その人の「恋愛偏差値」を診断するWebアプリケーションです。

## スクリーンショット

(ここにアプリケーションのスクリーンショットを挿入)

## 主な特徴

- シンプルで直感的なUI
- 質問に答えるだけの簡単な操作
- 診断結果をスコアとタイプで表示
- 結果をSNSで共有する機能

## 使用技術

- **フロントエンド:**
  - [React](https://react.dev/)
  - [Vite](https://vitejs.dev/)
- **UI / スタイリング:**
  - [Tailwind CSS](https://tailwindcss.com/)
  - [shadcn/ui](https://ui.shadcn.com/)
- **言語:** JavaScript

## セットアップと実行方法

このプロジェクトをローカル環境でセットアップし、実行する手順は以下の通りです。

### 前提条件

- [Node.js](https://nodejs.org/) (v18.x 以上を推奨)
- [npm](https://www.npmjs.com/) (Node.jsに同梱)

### インストール

1.  このリポジトリをクローンします。
    ```bash
    git clone <repository-url>
    cd renai-tool
    ```

2.  プロジェクトの依存関係をインストールします。
    ```bash
    npm install
    ```

### 開発サーバーの起動

以下のコマンドを実行すると、開発サーバーが起動します。
ブラウザで `http://localhost:5173` (デフォルト) にアクセスしてください。

```bash
npm run dev
```

### 本番用ビルド

以下のコマンドを実行すると、`dist` ディレクトリに本番用のファイルが生成されます。

```bash
npm run build
```

## ディレクトリ構成

プロジェクトの主要なディレクトリとファイルは以下の通りです。

```
renai-tool/
├── public/              # 静的ファイル (画像、JSONデータ)
│   ├── pict/            # 診断結果の画像
│   ├── questions.json   # 診断の質問データ
│   └── result_types.json # 診断結果のタイプデータ
├── src/                 # ソースコード
│   ├── components/      # Reactコンポーネント
│   │   └── ui/          # shadcn/ui コンポーネント
│   ├── lib/             # ユーティリティ関数
│   ├── App.css          # グローバルなCSS
│   ├── App.jsx          # メインのアプリケーションコンポーネント
│   └── main.jsx         # アプリケーションのエントリーポイント
├── package.json         # プロジェクトのメタデータと依存関係
├── tailwind.config.js   # Tailwind CSS の設定ファイル
└── vite.config.js       # Vite の設定ファイル
```

## データファイルについて

このアプリケーションは、`public` ディレクトリにある2つのJSONファイルからデータを読み込みます。

-   `questions.json`: 診断で表示される質問と選択肢、および各選択肢がどのタイプに影響するかを定義しています。
-   `result_types.json`: 診断結果のスコア範囲、タイプ名、キャッチフレーズ、アドバイスなどを定義しています。

## 補助スクリプト

-   `generate_questions.py`: `questions.json` を生成するためのPythonスクリプトです。質問の追加や編集を効率的に行うために使用されます（現在は手動でのJSON編集が主）。


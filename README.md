# 恋愛偏差値診断

このプロジェクトは、ユーザーがいくつかの質問に答えることで、その人の「恋愛偏差値」を診断するWebアプリケーションです。

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
- **デプロイ:**
  - [GitHub Actions](https://github.com/features/actions)

## セットアップと実行方法

### 前提条件

- [Node.js](https://nodejs.org/) (v18.x 以上を推奨)
- [npm](https://www.npmjs.com/) (Node.jsに同梱)

### インストール

1.  このリポジトリをクローンします。
    ```bash
    git clone https://github.com/fuminico/renai-tool.git
    cd renai-tool
    ```

2.  プロジェクトの依存関係をインストールします。
    ```bash
    npm install
    ```

### 開発サーバーの起動

以下のコマンドを実行すると、開発サーバーが起動します。
ブラウザで `http://localhost:3005` (デフォルト) にアクセスしてください。

```bash
npm run dev
```

## デプロイ

このプロジェクトは、GitHub Actionsを使用して自動的にデプロイされます。
`main` ブランチにプッシュすると、ワークフローがトリガーされ、ビルドと `gh-pages` ブランチへのデプロイが自動的に行われます。

デプロイ設定は `.github/workflows/deploy.yml` に記述されています。

## ディレクトリ構成

プロジェクトの主要なディレクトリとファイルは以下の通りです。

```
renai-tool/
├── .github/             # GitHub Actions ワークフロー
│   └── workflows/
│       └── deploy.yml
├── public/              # 静的ファイル (画像、JSONデータ)
│   ├── pict/            # 診断結果の画像
│   ├── questions.json   # 診断の質問データ
│   └── result_types.json # 診断結果のタイプデータ
├── src/                 # ソースコード
│   ├── components/      # Reactコンポーネント
│   ├── App.jsx          # メインのアプリケーションコンポーネント
│   └── main.jsx         # アプリケーションのエントリーポイント
├── package.json         # プロジェクトのメタデータと依存関係
└── vite.config.js       # Vite の設定ファイル
```

## データファイルについて

このアプリケーションは、`public` ディレクトリにある2つのJSONファイルからデータを読み込みます。

-   `questions.json`: 診断で表示される質問と選択肢を定義しています。
-   `result_types.json`: 診断結果のスコア範囲、タイプ名、アドバイスなどを定義しています。
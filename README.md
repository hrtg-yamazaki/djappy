# README
  
## このアプリについて
  
### 概要

PythonとDjangoを用いて開発した、オリジナルのブログアプリケーションです。  
現時点では、ユーザー認証、記事の閲覧・投稿・編集・削除・検索など、ブログに必要なスタンダードな機能を実装しています。  

[リンク先](https://djappy.herokuapp.com/)

### 主な機能

##### ユーザー認証
新規登録、ログイン、ログアウト
##### プロフィール機能
登録したユーザーのプロフィールの編集
##### 記事の投稿機能
画像付き記事の新規投稿、編集、削除
##### コメント機能
記事に紐付けしたコメントの投稿、削除
##### 検索機能
記事のタイトルによる検索(部分一致)  
カテゴリによる検索(セレクトボックス)  
ユーザーの検索(ニックネームによる部分一致、認証用ユーザー名による完全一致)  

### 作成意図について

PythonとDjangoの習得のために開発しました。  
  
PythonとDjangoを選択した理由としては、これまでの経験から機械学習に関心を持っており、それを学ぶにあたって最も適している言語・フレームワークだと考えたためです。最初はライブラリを用いた簡易なものになるかもしれませんが、学習の進行に応じて、関連の機能を中心にアップデートしていきたいと思っています。   
私は、プログラミングスクールのカリキュラムを通してRubyとRuby on Railsの学習に臨みました。通学を終えた現時点で、どの程度エンジニアとしての自走力がついたのかを試してみたかったことも、他の言語の独学による習得に挑戦した、狙いの１つです。

### テスト用アカウントの認証情報

##### ユーザー名
testuser
##### パスワード
tech1234
  
### 使用技術・開発環境

##### サーバーサイド
Python / Django
##### フロントエンド
Django HTML / scss / jQuery
##### その他
PostgreSQL / GitHub / Heroku / Cloudinary

## 更新履歴

2019.1月中旬 作成開始  
2020.01.20 ローカル環境での完成  
2020.01.21 herokuへのデプロイ、cloudinaryの導入  
2020.01.22 レスポンシブ対応、リンクに関する軽微な修正  
2020.01.24 記事へのコメント機能の追加  

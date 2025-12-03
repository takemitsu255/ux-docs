# `dynamic` 配下の運用整備構成案

## MARUI-UNITE 管理下のAWS DEVに検証環境を移す

__AWS 各環境の役割__

AWS DEV : 開発中検証環境（インフラ検証用にしか使用していない）

AWS STG : PRDと同等かつリリース前の案件が含まれる環境

AWS PRD : 公開環境

__静的コンテンツのデプロイの流れ__

- Preview環境が作成
`epos_contents`の`feature/*`から`staging`へPR
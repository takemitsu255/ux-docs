# GitHub運用ルール

## 概要
PR作成時に`Files changed`が修正File以外も含まれる場合がある。<br>
その理由として、Branch作成と他案件の`Push / Merge`が関係する。<br>
Branch作成が他案件より前に作られた場合、その修正が取り込まれていないと、PR作成時に差分として発生する。<br>
以下の手順は、差分ファイルが発生した場合の解決方法とする。

![image](./img/Git運用概要.png)

## 手順
```
# 01 masterからチェックアウト
git checkout -b feature/AAA origin/master

# 02 fetchしてMaster同期してfeature/AAAに取り込まれる
git checkout master
git fetch
git pull origin master
git checkout feature/AAA
git merge master

# 03 Local内で開発

# 04 対象ファイルcommit -> push
git checkout master
git fetch
git pull origin master
git checkout feature/AAA
git merge master

# 修正ファイル全部の場合
git add .

# 修正ファイル指定の場合
git add aaa/bbb/sample.html

git commit -m "XXXXXX"
git push origin feature/AAA
```
![image](./img/GitFlow.png)


# PR作成時に作られるZipファイルについて

## 概要
PR作成時に前回のマージまでの差分がZipで配置される。

そのため、マージしていなければ、Remote RepositoryにPushする度にZipが再作成される。

![image](./img/zip.png)
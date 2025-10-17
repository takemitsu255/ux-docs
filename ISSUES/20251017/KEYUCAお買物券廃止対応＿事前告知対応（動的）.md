## KEYUCAお買物券廃止対応＿事前告知対応（動的）

__納品日__：2025.10.17

__案件区分__：

__GHC__：

__[Memo]__
```
```

| NAME | URL |
| --- | --- |
| FEAT | https://github.com/marui-unite/epos_contents/tree/VNET-328 |
| ISSUE| https://ghe-0101.com/cis/epos_contents/issues/14602 |
| JIRA | https://lsap0101.atlassian.net/browse/VNET-328?focusedCommentId=15876 |

| ENV | PR URL | Merge |
| --- | --- | --- |
| STG| - | - |
| PRD | - | - |


__[対象ファイル]__
```
docs/memberservice/ownernet/rsp/v1/include-files/point_use/giftcard_note_0024.html
docs/memberservice/ownernet/v1/include-files/point_reference/caution_area.html
docs/memberservice/pc/rsp/v1/include-files/point_use/giftcard_note_0024.html
docs/memberservice/pc/rsp/v1/include-files/point_use/giftcard_note_text01.html
docs/memberservice/pc/rsp/v1/include-files/point_use/point_use_giftcard_text01.html
docs/memberservice/pc/v1/include-files/point_reference/caution_area.html
```

__[コマンドメモ]__
```
git config --global core.autocrlf false
git
git restore --staged .
	git add docs/memberservice/ownernet/v1/include-files/point_reference/caution_area.html
	git add docs/memberservice/pc/rsp/v1/include-files/point_use/giftcard_note_text01.html
	git add docs/memberservice/pc/rsp/v1/include-files/point_use/point_use_giftcard_text01.html
	git add docs/memberservice/pc/v1/include-files/point_reference/caution_area.html
```
git merge staging
git restore --staged .
git add docs/memberservice/ownernet/v1/include-files/point_reference/caution_area.html
git add docs/memberservice/pc/rsp/v1/include-files/point_use/giftcard_note_text01.html
git add docs/memberservice/pc/rsp/v1/include-files/point_use/point_use_giftcard_text01.html
git add docs/memberservice/pc/v1/include-files/point_reference/caution_area.html
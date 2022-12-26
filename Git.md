
# Git
- 커밋은 3가지 영역을 바탕으로 동작
- Working Directory
  - 내가 작업하고 있는 실제 디렉토리
- Stageing Area
  - 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
- Repository
  - 커밋(commit)들이 저장되는 곳
  - 특정 디렉토리를 버전 관리하는 저장소

```bash
git init 
```
- 로컬 저장소를 생성하는 명령어

`.git` 
- 버전 관리에 필요한 모든 것이 들어 있는 디렉토리
## git의 작동 순서
  - Working directory
    - README.md >untracked > 
  - Staging area 
    - `git add` (tracked, staged)
  - Reapository 
    - committed - >`git commit`
  - 이후 수정시 Working directory에서는 modified
```bash
 git status
 ```
- git으로 관리되는 파일들의 상태
```bash
git log
``` 
- 확인을 위해 많이 쓰임

## 주의사항

- 저장소 내부는 따로 init할것
- init은 1회만!
- git은 상위폴더에 init했다면 하위폴더에 init하지 말자
- `git add (파일명)` 후  `git commit -m 커밋사유` 로 저장.
# git hub 연동
- git remote add origin {remote repo} 
  - 내 로컬 저장소 & 원격 저장소 연결
- git push -u origin master <-user option 기억 ('-u option')>
- 이후 git push만 해도 가능 , 
## 주의사항 
- 드래그 앤 드랍으로도 파일을 올릴 수는 있지만 다양한 오류
-상기 사유로 가능하면 git push로 진행
- github은 파일이 아닌 commit이 push, 파일이 push되진 않음

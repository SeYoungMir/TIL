# Git Addition
## gitignore
- 주의사항
  - 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이라는 뜻입니다.
  - `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성합니다.
  - **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성합니다.**

- 들어가야 하는 것
  - 민감한 개인정보
  - OS(운영체제)에서 활용되는 파일
  - IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
  - 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
- 쉽게 작성하는 방법
  - [gitignore.io](https://www.toptal.com/developers/gitignore/)
  - *.md 등 *을 쓰면 .md를 포함한 전체
  - ! 파일명 은 ->를 제외함
---

## Clone, Pull

```bash
git clone{remote_repo}
```
- reomote repo를 local로 복제
- 모든 변경사항의 내용들이 복제
- 연결 X, 이미 .git과 연결이 모두 되어있음
`git init` 이 필요하지 않음.

```bash
git pull {remote_repo}
git pull origin master
```
- remote repo의 변경사항을 
- 이미 repo가 연결되어있으면 pull
(커밋을 업데이트)
- 원격에 백업되어잇는 repo를 그대로 가져와야할때
clone (repo를 다운로드)

## Repository
- settings - collaboators - Add people

## Branch
- 버전관리의 꽃
- 작업공간을 나누어 `독립적으로 작업`할 수 있도록 도와주는 Git의 도구
- branch 이전의 version과 독립적 개발 가능.
- Git의 branch 생성 속도 빠름.
- master = 늘 상용화, 늘 고객들이 사용 중. 따라서 master에서 bug 발생한다면?
- 새로운 작업 공간의 필요, 버그, 혹은 이슈 수정을 branch에서 함

### Head와 branch
- Head: branch들의 가장 최신 commit을 가리키는 pointer

## Branch 명령어
```bash
git branch
```
- branch 목록 확인
  - *의 위치가 master를 가리킴(기본)
  - branch가 동일해야 동일한 branch로 올라감
```bash
git branch -r
```
- 원격 저장소의 branch 목록 확인
```bash
git branch {branch 이름}
```
- branch 생성
```bash
git switch {branch 이름}
```
- branch 이동
  -*의 위치가 이동한 branch를 가리킴
- master와 하위 branch의 commit 내역이 분리
```bash
git log --oneline --all
```
- 모든 branch의 모든 commit 내역을 보여줌
- head의 위치에 따라 내용이 바뀜.
```bash
git branch {branch 이름} {commit ID}
```
-특정 커밋을 기점으로 새로운 branch 생성 

## Branch Merge
- 분기된 branch들을 하나로 합치는 명령어
- Head가 가리키는 브랜치에 합쳐짐
```bash
git merge {merge branch}
```
- 현재 pointer가 위치한 head에 merge branch가 합쳐짐

### Merge의 세 종류 (2가지 큰 분류)
#### Auto merge
- Fast - Forward (빨리 감기)
  - master -feature/feature2
  - feature을 master에 병합
  - 기존의 master가 가진 commit + 새로운 commit(feature이 가지고 있던)
  - feature branch 제거(필요)
  
- 3-Way-Merge
  - master(+feature)-feature2
  - feature2를 기존 master에 병합
  - 새로운 commit 생김
  - 같은 부모에서 갈라져나온 분기 2개를 합치지만, 새로운 commit, Head 이동
  - feature2 branch 제거(필요)
#### Non-auto merge
- Merge Conflict
  - master -feature/feature2
  - 만약 feature branch와 feature2가 동일한 파일의 동일한 라인 수정했다면?
  - Auto-merging index.html 발생
  - Conflict
  - Automatic merge failed, fix conflict and commit
  - 해결 후 `git add .`,`git commit` 필요

```bash
git branch -d {branch name}
```
-branch 삭제

```bash
git switch -c {branch name}
```
-branch를 만듦과 동시에 이동

## Git workflow
- Branch와 pull request를 이용한 협업

- Feature Branch Workflow
  - Shared repository model
  - (원격 저장소의 소유권이 있는 경우)
  1. 각 사용자는 원격 저장소의 소유권을 가진 상태, 따라서 clone을 통해 저장소를 로컬에 복제
    - GitHub Collaboator
  2. 기능 추가를 위해 branch 생성 및 기능 구현
    - master에 다시 push하지 않음
  3. 기능 구현 후 원격 저장소에 브랜치 반영
    - branch에 head가 있는 상태로 push
    - branch가 누적 
  4. Pull request
     - merge request
  5. Request merge
     - branch 병합
     - branch 삭제
  6. 병합된 master의 내용을 pull
     - 최신 commit을 받아옴
     - 원격 저장소에 있던 branch 삭제
- Forking Workflow
  - Fork & Pull model
  - (원격 저장소의 소유권이 없는 경우)
  1. 소유권이 없는 원격 저장소를 fork를 통해 복제
     - fork (푸다, 뜨다)
     - 내 원격 저장소에 복제.
     - 이를 clone
     - 추후 로컬 저장소를 원본 원격 저장소와 동기화하기 위해 URL 연결
  -   ```bash
      git remote add upstream{원본 URL}
      ```
    - 원본+복제= 총 두개씩의 저장소 연결
  1. 기능 추가를 위해 branch 생성 및 기능 구현
  2. 내 복제 원격 저장소에 branch  push
  3. 원본 저장소에 pull request 요청
  4. 복제 원격 저장소의 branch 삭제
  5. 로컬 master branch로 이동
  6. 원본 저장소 pull 해서 로컬 저장소 동기화.
 
- **push 시**
 ```bash
 git push origin {branch}
 ```
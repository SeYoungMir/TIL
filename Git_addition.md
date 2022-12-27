# gitignore
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

# Clone, Pull

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

# Repository
- settings - collaboators - Add people

# Branch
- 버전관리의 꽃
- 작업공간을 나누어 `독립적으로 작업`할 수 있도록 도와주는 Git의 도구
- 

# 📝 My Velog Backup Bot

이 프로젝트는 [Velog](https://velog.io/@leesh970930)의 RSS 피드를 활용해 작성한 블로그 글을 자동으로 Markdown 파일로 저장하고, GitHub 저장소에 백업하는 자동화 시스템입니다.

GitHub Actions를 이용하여 **매일 자정마다 Velog 글을 자동으로 수집하고 저장소에 커밋**합니다.


## ⚙️ GitHub Actions 자동화

### 트리거 조건:
- `master` 브랜치에 Push 시
- 매일 자정(00:00) 자동 실행

### 주요 기능:
- RSS 피드를 파싱해 Markdown 파일로 저장
- 변경된 글이 있을 경우 자동 커밋 및 푸시

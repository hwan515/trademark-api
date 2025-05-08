# 상표 검색 API (Trademark Search API)

FastAPI를 기반으로 구현한 상표 검색 백엔드 서비스입니다.  
제공된 `trademark_sample.json` 데이터를 바탕으로 상표 정보를 검색할 수 있는 API를 구현하였습니다.

---

## ✅ 주요 기능

- 상표 정보 필터링 검색 API 제공
- 지원하는 검색 필터:
  - `product_name` (한글 상표명, 부분 일치)
  - `product_name_eng` (영문 상표명, 부분 일치)
  - `register_status` (등록 상태: 등록, 거절 등)
  - `main_code` (상품 분류 코드)
  - `application_from`, `application_to` (출원일 범위 YYYYMMDD)

---

## 📦 실행 방법

1. 의존성 설치

```
pip install fastapi uvicorn
```

2. 서버 실행
```
uvicorn main:app --reload
```

3. API 접근
```
GET http://127.0.0.1:8000/api/search
```

4. 쿼리 예시:
```
GET /api/search?product_name=커피&register_status=등록&application_from=20180101&application_to=20201231
```
## 🔍 API 상세 설명

### `GET /api/search`

상표 정보를 다양한 조건으로 검색합니다.

| 파라미터          | 타입     | 설명                                |
|-------------------|----------|-------------------------------------|
| `product_name`     | string   | 한글 상표명 (부분 일치)             |
| `product_name_eng` | string   | 영문 상표명 (부분 일치)             |
| `register_status`  | string   | 등록 상태 (예: 등록, 거절 등)       |
| `main_code`        | string   | 상품 주요 분류 코드                 |
| `application_from` | string   | 출원일 시작일 (`YYYYMMDD`)         |
| `application_to`   | string   | 출원일 종료일 (`YYYYMMDD`)         |


## 🧠 기술적 의사결정

- **유연한 필터링**: 각 필드는 `Optional`로 처리하여 조합 가능한 다중 필터링을 지원.
- **부분 일치 검색**: 사용자 편의를 위해 `productName`, `productNameEng`는 부분 문자열 검색 지원.

---

## 🔧 고민한 점 & 문제 해결

- **결측치 대응**: 일부 항목이 `null`인 경우 `get()`과 조건을 조합하여 오류 방지.
- **날짜 비교**: 문자열 기반(`YYYYMMDD`)의 날짜 범위 검색 기능 추가.
- **확장성 고려**: 향후 대용량 데이터셋 대응을 위해 Elasticsearch 등 도입 고려 가능.

---

## 🚀 개선하고 싶은 점

- SON 파일 → RDBMS(PostgreSQL) 또는 Elasticsearch 이관
- ORM 사용 (예: SQLAlchemy) → 구조적이고 유지보수 쉬움


---

## 📁 프로젝트 구조
```
trademark_api
├── app/
│   ├── database.py          # 데이터 로딩 함수
│   ├── models.py            # Pydantic 모델 정의
│   ├── routes/
│   │   └── trademark.py     # API 라우터 구현
├── trademark_sample.json    # 제공 데이터
├── main.py                  # FastAPI 엔트리포인트
```
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

- **유연한 필터링 설계**: 검색 파라미터는 모두 `Optional`로 선언하여 사용자 입력에 따라 다양한 필터 조합이 가능하도록 구현.
- **부분 일치 검색 지원**: `productName`, `productNameEng` 필드는 소문자 기준 부분 문자열 포함 여부로 검색 → 키워드가 완전 일치하지 않아도 검색 가능.
- **Pydantic 모델 적용**: 응답 스키마를 `Trademark` 모델로 지정하고 `response_model`로 연결함으로써 API 문서 자동화 및 응답 구조 안정성 확보.
- **모듈화 구조**: `routes`, `models`, `database` 모듈로 기능을 분리하여 유지보수성과 테스트 용이성 향상.
- **Swagger 자동 문서화**: FastAPI의 내장 Swagger를 활용해 요청 파라미터, 응답 스키마를 명확히 문서화. `/docs`에서 직접 테스트 가능.

---

## 🔧 고민한 점 & 문제 해결

- **결측치 대응**: 일부 항목이 `null`이거나 존재하지 않는 경우 `.get()`과 조건문을 조합하여 런타임 에러 없이 필터링 처리.
- **유연한 타입 처리**: `registrationNumber`, `registrationDate` 등 문자열 또는 리스트로 혼재된 필드는 `Union[str, List[Optional[str]]]`으로 선언하여 오류 없이 수용.
- **날짜 비교 로직**: `application_from`, `application_to` 필드는 `YYYYMMDD` 문자열 기준으로 날짜 범위 비교를 구현.
- **Swagger 422 오류 혼동 해결**: Swagger에서 자동으로 노출되는 예시용 422 Validation Error는 실제 오류가 아니라는 점을 인지하고 무시하도록 설정.
- **확장성 고려**: 현재는 JSON 기반 메모리 필터 방식이지만, 데이터가 많아질 경우를 대비해 Elasticsearch, PostgreSQL, 캐싱(Redis) 구조 도입을 고려.


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
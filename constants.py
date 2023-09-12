# sqlite:// 프로토콜 사용, /sfscores.sqlite 경로
DEFAULT_SQL_PATH = "sqlite:///flat-table.sqlite"

# Table Description
DEFAULT_WELFARE_TABLE_DESCRP = (
    "이 테이블은 기업에 있는 행사의 구분, 대상, 회사지원금 및 사우회지급금, 경조휴가, 화환 및 조화 지급 여부에 대한 정보를 제공합니다."
    "사용자가 특정 복리후생에 대해 질의할 때 이 테이블을 참조해야 합니다."
)
DEFAULT_WELFARE_BY_RANK_TABLE_DESCRP = (
    "이 테이블은 자녀의 신분 기준에 따라 지급되는 지원금에 대한 정보를 제공합니다."
    "이 테이블의 비고는 추가적인 지원금 또는 지원 기준에 대해 설명합니다."
    "사용자가 자녀의 기준에 따른 복리후생에 대해 질의할 때 이 테이블을 참조해야 합니다."
)
DEFAULT_WELFARE_BY_STANDARD_TABLE_DESCRP = (
    "이 테이블은 연봉직과 시급직의 구분에 따른 직급별 연 지급액, 분기 지급액에 대한 정보를 제공합니다."
    "사용자가 구분 및 직급에 따른 복리후생에 대해 질의할 때 이 테이블을 참조해야 합니다."
)

# Tool Description
DEFAULT_LC_TOOL_DESCRP = "사내의 복리후생 및 지원에 대한 질의에 답변하고 싶을 때 유용합니다."
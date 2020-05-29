create database nihongo8 character set UTF8 collate utf8_bin;
use nihongo8;

-- 사용자
create table tbl_user (
    id int primary key auto_increment comment 'PK',
    email varchar(255) not null unique comment '이메일', 
    password varchar(255) not null comment '비밀번호',
    username varchar(255) not null comment '사용자명',
    jlpt int default 0 comment 'JLPT 등급',
    profile_img int comment '프로필 이미지 FK tbl_file.id', 
    point int default 0 comment '보유 포인트',
    is_active int default 0 comment '이메일 인증 여부',
    is_staff int default 0 comment '권한',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    regist_date datetime default now() comment '등록일자',
    regist_ip varchar(255) comment '등록아이피',
    modify_date datetime comment '수정일시',
    modify_ip varchar(255) comment '수정아이피',
    delete_date datetime comment '삭제일시',
    delete_ip varchar(255) comment '삭제아이피',
    reset_date datetime comment '초기화일시',
    reset_ip varchar(255) comment '초기화아이피'
);

-- JLPT 시험 일정
create table tbl_index_jlpt (
    id int primary key auto_increment comment 'PK',
    year varchar(255) not null comment '년도',
    round varchar(255) not null comment '회차',
    start_date datetime comment '접수시작일시',
    end_date datetime comment '접수종료일시',
    test_date datetime comment '시험일시',
    status varchar(255) comment '시험상태'
);
-- 중요 데이터가 아니므로 date, ip, id 기록하지 않음

-- 사용자 JLPT 인증 여부
create table tbl_user_jlpt (
    user_id int primary key comment '사용자 FK tbl_user.id',
    pub_jlpt_n1 int default 0 comment '공식인증 JLPT N1',
    pub_jlpt_n2 int default 0 comment '공식인증 JLPT N2',
    pub_jlpt_n3 int default 0 comment '공식인증 JLPT N3',
    pub_jlpt_n4 int default 0 comment '공식인증 JLPT N4',
    pub_jlpt_n5 int default 0 comment '공식인증 JLPT N5',
    n1_update_date datetime comment 'JLPT N1 인증일시',
    n2_update_date datetime comment 'JLPT N2 인증일시',
    n3_update_date datetime comment 'JLPT N3 인증일시',
    n4_update_date datetime comment 'JLPT N4 인증일시',
    n5_update_date datetime comment 'JLPT N5 인증일시'
);
-- 중요 데이터가 아니므로 date, ip, id 기록하지 않음

-- 알림
create table tbl_notification (
    id int primary key auto_increment comment 'PK',
    type varchar(255) not null comment '알림구분',
    title_id int comment 'FK tbl_community.id, tbl_reply.id, tbl_problem.id', -- content가 있을 경우 null
    content varchar(255) comment '관리자 푸쉬 메세지', -- title_id가 있을 경우 null
    user_id int not null comment '알림 받는 사용자 tbl_user.id',
    read_yn varchar(255) default 'N' comment '읽음여부',
    read_date datetime comment '읽음일시',
    regist_id int comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_date datetime comment '삭제일시'
);
-- 알림은 수정될 일이 없기에 수정 관련 데이터를 기록하지 않음

-- 파일
create table tbl_file (
    id int primary key auto_increment comment 'PK',
    raw_name varchar(255) not null comment '원본파일명 (확장자제외)',
    enc_name varchar(255) not null comment '변환파일명 (확장자제외)',
    ext varchar(255) not null comment '확장자',
    raw_size int not null comment '원본크기',
    enc_size varchar(255) not null comment '변환크기',
    save_path varchar(255) not null comment '저장경로 (변환파일명+확장자)',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_date datetime comment '삭제일시',
    delete_id int comment '삭제사용자 FK tbl_user.id'
);
-- 파일은 수정될 일이 없기에 수정 관련 데이터를 기록하지 않음

-- 신고
create table tbl_report (
    id int primary key auto_increment comment 'PK',
    comm_id int not null comment '게시물 아이디 FK tbl_community.id',
    type varchar(255) not null comment '신고유형',
    reason varchar(255) not null comment '신고사유',
    user_id int not null comment '신고사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_date datetime comment '삭제일시',
    delete_id int comment '삭제사용자 FK tbl_user.id'
);
-- 신고는 수정될 일이 없기에 수정 관련 데이터를 기록하지 않음

-- 게시판
create table tbl_community (
    id int primary key auto_increment comment 'PK',
    type varchar(255) not null comment '게시판구분',
    sub_type varchar(255) not null comment '게시물구분',
    title varchar(255) not null comment '제목',
    content varchar(255) not null comment '내용',
    view_cnt varchar(255) not null comment '조회수',
    like_cnt varchar(255) not null comment '좋아요수',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_id int comment '삭제사용자 FK tbl_user.id',
    delete_date datetime comment '삭제일시'
);
-- 게시물 삭제 시 tbl_report 데이터 삭제

-- 댓글
create table tbl_reply (
    id int primary key auto_increment comment 'PK',
    comm_id int not null comment '게시물아이디 FK tbl_community.id',
    content varchar(255) not null comment '댓글',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_id int comment '삭제사용자 FK tbl_user.id',
    delete_date datetime comment '삭제일시'
);

-- 답글
create table tbl_re_reply (
    id int primary key auto_increment comment 'PK',
    reply_id int not null comment '댓글아이디 FK tbl_reply.id',
    content varchar(255) not null comment '답글',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_id int comment '삭제사용자 FK tbl_user.id',
    delete_date datetime comment '삭제일시'
);

-- 핵심 데이터
create table tbl_core (
    id int primary key auto_increment comment 'PK',
    level int not null comment '단어수준',
    type varchar(255) not null comment '단어형식',
    kanji varchar(255) not null comment '한자',
    hiragana varchar(255) not null comment '히라가나',
    katakana varchar(255) not null comment '카타카나',
    hangul varchar(255) not null comment '한글',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '수정사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시'
);
-- 삭제 시 데이터 완전 삭제 및 tbl_problem_core 데이터 완전 삭제
-- 삭제 시 데이터 완전 삭제 및 tbl_core_ex 데이터 완전 삭제

-- 문제 
create table tbl_problem (
    id int primary key auto_increment comment 'PK',
    level int not null comment '문제수준(필터)',
    difficult int not null comment '문제수준(별표기)',
    title varchar(255) not null comment '문제제목',
    content varchar(255) not null comment '문제내용',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    is_staff int default 0 comment '출제의원 출제 여부',
    is_accept int default 0 comment '출제의원 문제 승인 여부',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '수정사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_id int comment '삭제사용자 FK tbl_user.id',
    delete_date datetime comment '삭제일시'
);

-- 문제 찜
create table tbl_problem_like (
    id int primary key auto_increment comment 'PK',
    user_id int not null comment '찜한사용자 FK tbl_user.id',
    problem_id int not null comment '찜한문제 FK tbl_problem.id',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_date datetime comment '삭제일시'
);
-- 문제 찜은 수정될 일이 없기에 수정 관련 데이터를 기록하지 않음

-- 문제 + 핵심데이터
create table tbl_problem_core (
    id int primary key auto_increment comment 'PK',
    problem_id int not null comment '문제 아이디 FK tbl_problem.id',
    core_id int not null comment '출제 대상 FK tbl_core.id'
);

-- 문제 + 퀴즈
create table tbl_problem_quiz (
    id int primary key auto_increment comment 'PK',
    problem_id int not null comment '문제 아이디 FK tbl_problem.id',
    quiz_id int not null comment '퀴즈 아이디 FK tbl_quiz.id'
);

-- 핵심 데이터 예제
create table tbl_core_ex (
    id int primary key auto_increment comment 'PK',
    core_id int not null comment '단어 아이디 FK tbl_core.id',
    ex_kanji varchar(255) not null comment '예시 한자',
    ex_hangul varchar(255) not null comment '예시 한글',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시'
);
-- 삭제 시 데이터 완전 삭제

-- 퀴즈
create table tbl_quiz (
    id int primary key auto_increment comment 'PK',
    type varchar(255) not null comment '퀴즈유형', -- 한자읽기, 한자찾기, 문맥규정, 교체유의어, 용법, 문법빈칸
    level int not null comment '퀴즈수준',
    quiz varchar(255) not null comment '퀴즈 (일본어)',
    quiz_hangule varchar(255) not null comment '퀴즈 (한글)',
    problem1 varchar(255) not null comment '선택지',
    problem2 varchar(255) not null comment '선택지',
    problem3 varchar(255) not null comment '선택지',
    problem4 varchar(255) not null comment '선택지',
    solve varchar(255) not null comment '정답 (선택지 중 데이터)',
    solution varchar(255) comment '해설',
    point int not null comment '포인트',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시'
);
-- 삭제 시 데이터 완전 삭제 및 tbl_problem_quiz 데이터 완전 삭제

-- 포인트 이력
create table tbl_point_history (
    id int primary key auto_increment comment 'PK',
    user_id int not null comment '사용자 FK tbl_user.id',
    quiz_id int not null comment '퀴즈 FK tbl_quiz.id',
    point int not null comment '포인트',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '수정사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시',
    delete_yn varchar(255) default 'N' comment '삭제여부',
    delete_id int comment '삭제사용자 FK tbl_user.id',
    delete_date datetime comment '삭제일시'
);

-- 코드
create table tbl_code (
    code_type varchar(255) comment '테이블명',
    code_col varchar(255) comment '컬럼',
    code_code varchar(255) comment '코드',
    code_name varchar(255) comment '이름',
    code_desc varchar(255) comment '설명',
    user_id int not null comment '등록사용자 FK tbl_user.id',
    regist_date datetime default now() comment '등록일시',
    modify_id int not null comment '등록사용자 FK tbl_user.id',
    modify_date datetime comment '수정일시'
);
-- 삭제 시 데이터 완전 삭제
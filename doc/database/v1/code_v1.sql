select * from tbl_code;

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '0', 'JLPT 미취득', 'JLPT를 취득하지 않은 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '1', 'JLPT N1', 'JLPT N1을 취득한 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '2', 'JLPT N2', 'JLPT N2을 취득한 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '3', 'JLPT N3', 'JLPT N3을 취득한 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '4', 'JLPT N4', 'JLPT N4을 취득한 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'jlpt', '5', 'JLPT N5', 'JLPT N5을 취득한 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'is_staff', '0', '일반사용자', '일반사용자 권한', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'is_staff', '1', '관리자', '관리자 권한', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user', 'is_staff', '2', '출제의원', '출제의원 권한', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_index_jlpt', 'status', 'S', '중지', 'Stop', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_index_jlpt', 'status', 'D', '연기', 'Delay', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_index_jlpt', 'status', 'O', '공식', 'Official', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_index_jlpt', 'status', 'N', '비공식', 'Non Official', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n1', '0', '미인증', '자격증 미인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n1', '1', '인증', '자격증 인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n2', '0', '미인증', '자격증 미인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n2', '1', '인증', '자격증 인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n3', '0', '미인증', '자격증 미인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n3', '1', '인증', '자격증 인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n4', '0', '미인증', '자격증 미인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n4', '1', '인증', '자격증 인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n5', '0', '미인증', '자격증 미인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_user_jlpt', 'pub_jlpt_n5', '1', '인증', '자격증 인증 상태', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_notification', 'type', 'C', '게시판 알림', '게시판에 새로운 댓글이 작성된 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_notification', 'type', 'R', '댓글 알림', '댓글에 새로운 답글이 작성된 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_notification', 'type', 'A', '관리자 알림', '관리자가 푸쉬 메세지를 보낼 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'A', '광고', '게시물이 광고 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'W', '도배', '게시물이 도배 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'O', '음란물', '게시물이 음란물 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'L', '욕설', '게시물이욕설광고 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'P', '개인정보침해', '게시물이 개인정보침해 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'I', '저작권침해', '게시물이 저작권침해 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_report', 'type', 'E', '기타', '게시물이 기타 성향을 가진 경우', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'type', 'N', '공지사항', '공지사항', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'type', 'F', '자유게시판', '자유게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'type', 'Q', '질문게시판', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'type', 'J', 'JLPT 합격인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', 'NU', '업데이트', '공지사항', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', 'NE', '이벤트', '공지사항', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', 'NA', '알림', '공지사항', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' QE', '기타', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' Q1', 'N1 질문', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' Q2', 'N2 질문', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' Q3', 'N3 질문', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' Q4', 'N4 질문', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' Q5', 'N5 질문', '질문게시판', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' J1', 'N1 합격 인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' J2', 'N2 합격 인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' J3', 'N3 합격 인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' J4', 'N4 합격 인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_community', 'sub_type', ' J5', 'N5 합격 인증', 'JLPT 합격인증', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 0', '시험 외', 'JLPT 시험 외', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 1', 'JLPT N1', 'JLPT N1', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 2', 'JLPT N2', 'JLPT N2', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 3', 'JLPT N3', 'JLPT N3', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 4', 'JLPT N4', 'JLPT N4', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'level', ' 5', 'JLPT N5', 'JLPT N5', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'difficult', ' 1', '별 1개', '별점', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'difficult', ' 2', '별 2개', '별점', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'difficult', ' 3', '별 3개', '별점', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'difficult', ' 4', '별 4개', '별점', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'difficult', ' 5', '별 5개', '별점', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'is_staff', '0', '출제의원이 출제한 문제', '출제의원 여부', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'is_staff', '1', '관리자가 출제한 문제', '출제의원 여부', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'is_accept', '0', '미승인', '문제 승인 여부', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'is_accept', '0', '승인', '문제 승인 여부', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'KR', '한자읽기', '문제유형 - Kanji Read', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'KF', '한자찾기', '문제유형 - Kanji Find', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'GR', '문맥규정', '문제유형 - Grammar Rule', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'RP', '교체유의어', '문제유형 - Replace', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'UF', '용법', '문제유형 - Useful', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'type', 'GE', '문법빈칸', '문제유형 - Grammar Empty', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 0', '시험 외', 'JLPT 시험 외', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 1', 'JLPT N1', 'JLPT N1', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 2', 'JLPT N2', 'JLPT N2', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 3', 'JLPT N3', 'JLPT N3', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 4', 'JLPT N4', 'JLPT N4', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_quiz', 'level', ' 5', 'JLPT N5', 'JLPT N5', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 0', '시험 외', 'JLPT 시험 외', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 1', 'JLPT N1', 'JLPT N1', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 2', 'JLPT N2', 'JLPT N2', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 3', 'JLPT N3', 'JLPT N3', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 4', 'JLPT N4', 'JLPT N4', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'level', ' 5', 'JLPT N5', 'JLPT N5', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'N', '명사', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'V', '동사', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'E', 'い형용사', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'N', 'な형용사', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'AD', '부사', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_core', 'type', 'X', '기타', '단어 형식', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'KR', '한자읽기', '문제유형 - Kanji Read', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'KF', '한자찾기', '문제유형 - Kanji Find', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'GR', '문맥규정', '문제유형 - Grammar Rule', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'RP', '교체유의어', '문제유형 - Replace', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'UF', '용법', '문제유형 - Useful', 1, now(), null, null);

insert tbl_code (code_type, code_col, code_code, code_name, code_desc, user_id, regist_date, modify_id, modify_date)
value('tbl_problem', 'type', 'GE', '문법빈칸', '문제유형 - Grammar Empty', 1, now(), null, null);
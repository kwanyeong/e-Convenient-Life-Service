-- 테이블 순서는 관계를 고려하여 한 번에 실행해도 에러가 발생하지 않게 정렬되었습니다.

-- t_user Table Create SQL
-- 테이블 생성 SQL - t_user

-- create database tumblerdb;
show databases;
-- create user tumbler;
-- use tumblerdb;
select user();


-- create user 'tumbler'@'localhost' identified by 'service';


CREATE TABLE t_user
(
    `user_Phone1`   VARCHAR(20)     NOT NULL    COMMENT '사용자 폰번호1', 
    `user_Phone2`   VARCHAR(20)     NOT NULL    COMMENT '사용자 폰번호2', 
    `user_Phone3`   VARCHAR(20)     NOT NULL    COMMENT '사용자 폰번호3', 
    `user_Phone`   VARCHAR(20)     NOT NULL    COMMENT '사용자 폰번호', 
    `user_Id`      VARCHAR(20)      NOT NULL    COMMENT '사용자 아이디', 
    `user_Pwd`     VARCHAR(20)     NOT NULL    COMMENT '사용자 비밀번호', 
    `user_Name`    VARCHAR(20)     NOT NULL    COMMENT '사용자 이름', 
    `user_Email1`   VARCHAR(20)     NOT NULL    COMMENT '사용자 이메일주소', 
    `user_Email2`  VARCHAR(20)     NOT NULL    COMMENT '사용자 도메인주소', 
     PRIMARY KEY (user_Phone)
);



-- 테이블 Comment 설정 SQL - t_user
ALTER TABLE t_user COMMENT '사용자정보';


-- t_product Table Create SQL
-- 테이블 생성 SQL - t_product
CREATE TABLE t_product
(
    `product_Id`          INT UNSIGNED     NOT NULL AUTO_INCREMENT    COMMENT '제품 아이디', 
    `manufacturing_Date`  DATE             NOT NULL    				  COMMENT '제조 날짜', 
    `product_Age`         VARCHAR(20)      NOT NULL    				  COMMENT '제품 유통기한', 
    `product_Status`      CHAR(1)          NOT NULL    				  COMMENT '제품 상태', 
    `product_Img`         VARCHAR(3000)    NULL        				  COMMENT '제품 이미지', 
     PRIMARY KEY (product_Id)
);

-- 테이블 Comment 설정 SQL - t_product
ALTER TABLE t_product COMMENT '제품정보';

-- 테이블 정보변경
ALTER TABLE t_product MODIFY COLUMN product_Id INT UNSIGNED NOT NULL AUTO_INCREMENT;



-- t_point Table Create SQL
-- 테이블 생성 SQL - t_point
CREATE TABLE t_point
(
    `point_Id`      INT UNSIGNED    NOT NULL AUTO_INCREMENT    COMMENT '포인트 아이디', 
    `point`         INT             NOT NULL    			   COMMENT '포인트', 
    `created_At`    DATETIME        NOT NULL    			   COMMENT '적립 시각', 
    `created_Memo`  VARCHAR(300)    NOT NULL    			   COMMENT '적립 사유', 
    `user_Phone`       VARCHAR(20)     NOT NULL    			   COMMENT '사용자 폰번호', 
     PRIMARY KEY (point_Id)
);

-- 테이블 정보 변경
ALTER TABLE t_point
MODIFY COLUMN point_Id INT UNSIGNED NOT NULL AUTO_INCREMENT;

-- 테이블 Comment 설정 SQL - t_point
ALTER TABLE t_point COMMENT '포인트정보';




ALTER TABLE t_point
    ADD CONSTRAINT FK_t_point_user_phone_t_user_user_phone FOREIGN KEY (user_Phone)
        REFERENCES t_user (user_Phone) ON DELETE RESTRICT ON UPDATE RESTRICT;
        
-- Foreign Key 설정 SQL - t_point(user_phone) -> t_user(user_phone)
/*
ALTER TABLE t_point
    ADD CONSTRAINT FK_t_point_user_id_t_user_user_id FOREIGN KEY (user_id)
        REFERENCES t_user (user_id) ON DELETE RESTRICT ON UPDATE RESTRICT;
*/
-- Foreign Key 삭제 SQL - t_point(user_phone)
-- ALTER TABLE t_point
-- DROP FOREIGN KEY FK_t_point_user_phone_t_user_user_phone;


-- t_rental Table Create SQL
-- 테이블 생성 SQL - t_rental
CREATE TABLE t_rental
(
    `rental_Id`      VARCHAR(14)    NOT NULL AUTO_INCREMENT    COMMENT '렌탈 아이디', 
    `rental_Date`    DATE            NOT NULL    			   COMMENT '렌탈 날짜', 
    `return_Date`    DATE            NULL    				   COMMENT '반납 날짜', 
    `rental_Status`  VARCHAR(10)     NULL        			   COMMENT '렌탈 상태', 
    `product_Id`     INT UNSIGNED    NOT NULL        		   COMMENT '제품 아이디', 
    `user_Phone`     VARCHAR(20)     NULL        			   COMMENT '사용자 폰번호', 
     PRIMARY KEY (rental_Id)
);

-- t_rental 테이블 정보 변경 // 1) 렌탈 상태 NULL 가능 2) auto_inc 컬럼 추가
ALTER TABLE t_rental
MODIFY COLUMN rental_Status VARCHAR(10) NULL COMMENT '렌탈 상태';

ALTER TABLE t_rental
MODIFY COLUMN product_Id INT UNSIGNED NOT NULL UNIQUE KEY COMMENT '제품 아이디';

ALTER TABLE t_rental MODIFY rental_Id VARCHAR(14) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '제품 아이디';

/*
ALTER TABLE t_rental
ADD COLUMN `auto_inc` INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE KEY;
*/

ALTER TABLE t_rental
MODIFY COLUMN return_Date DATE DEFAULT NULL COMMENT '렌탈 날짜';



select * from t_rental;

-- ALTER TALBE ~ [컬럼 추가] ADD COLUMN 컬럼_이름 데이터_타입 / [컬럼삭제] DROP COLUMN 컬럼_이름
-- [컬럼 이름 변경] CHANGE COLUMN 기존_컬럼_이름 새_컬럼_이름 데이터_타입 / [컬럼 데이터 타입 수정] MODIFY COLUMN 컬럼_이름 새_데이터_타입

-- Foreign Key 설정 SQL - t_rental(user_phone) -> t_user(user_phone)

ALTER TABLE t_rental
    ADD CONSTRAINT FK_t_rental_user_phone_t_user_user_phone FOREIGN KEY (user_Phone)
        REFERENCES t_user (user_Phone) ON DELETE RESTRICT ON UPDATE RESTRICT;


/*
ALTER TABLE t_rental
    ADD CONSTRAINT FK_t_rental_user_id_t_user_user_id FOREIGN KEY (user_Id)
        REFERENCES t_user (user_Id) ON DELETE RESTRICT ON UPDATE RESTRICT;
*/
-- Foreign Key 삭제 SQL - t_rental(user_phone)
-- ALTER TABLE t_rental
-- DROP FOREIGN KEY FK_t_rental_user_phone_t_user_user_phone;

-- Foreign Key 설정 SQL - t_rental(product_id) -> t_product(product_id)
ALTER TABLE t_rental
    ADD CONSTRAINT FK_t_rental_product_id_t_product_product_id FOREIGN KEY (product_Id)
        REFERENCES t_product (product_Id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - t_rental(product_id)
-- ALTER TABLE t_rental
-- DROP FOREIGN KEY FK_t_rental_product_id_t_product_product_id;


-- 1) 데이터 트리거 생성
DROP TRIGGER t_rental_before_insert;

CREATE TABLE rental_id_seq (
    date DATE NOT NULL,
    last_id INT NOT NULL,
    PRIMARY KEY(date)
);

DELIMITER $$
CREATE TRIGGER t_rental_before_insert 
BEFORE INSERT ON t_rental 
FOR EACH ROW 
BEGIN 
   DECLARE new_id INT;
   SET new_id = (SELECT last_id FROM rental_id_seq WHERE date = CURDATE());
   
   IF new_id IS NULL THEN
       INSERT INTO rental_id_seq VALUES (CURDATE(), 1);
       SET NEW.rental_Id = CONCAT(DATE_FORMAT(CURDATE(), '%y%m%d'), LPAD(1, 6, '0'));
   ELSE
       UPDATE rental_id_seq SET last_id = last_id + 1 WHERE date = CURDATE();
       SET NEW.rental_Id = CONCAT(DATE_FORMAT(CURDATE(), '%y%m%d'), LPAD(new_id + 1, 6, '0'));
   END IF;
END$$
DELIMITER ;

-- 1) 데이터 생성
-- 2) User Table 데이터 삽입
INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '1234', '5678', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'hong', 'password', '홍길동', 'test', 'com');

INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '9999', '9999', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'admin', 'password', '관리자', 'admin', 'naver.com');

INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '5435', '7432', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'parkchangwon', '9341', '박창원', 'park', 'com');

INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '6572', '1196', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'leekwanyeong', '2222', '이관영', 'lcy629', 'naver.com');

INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '8252', '2078', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'leeseungun', '1111', '이승언', 'ma3514', 'naver.com');

INSERT INTO t_user(user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2)
VALUES('010', '1234', '5678', CONCAT(user_Phone1, user_Phone2, user_Phone3), 'hong52', '1234', '홍길동', 'hong', 'gmail.com');

select * from t_user;
update t_user SET user_Id = "hong52" where user_Phone ="01012355678";


INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(100, 1500, '2021-03-07', '반납', '01012345214');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(101, 1500, '2021-03-11', '반납', '01012345214');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(102, 1500, '2022-07-14', '반납', '01012345214');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(103, 1000, '2022-07-14', '결함', '01012345214');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(104, 1500, '2022-07-18', '반납', '01012345214');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(106, 1500, '2022-07-23', '반납', '01055424123');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(107, 1000, '2022-08-12', '결함', '01041233234');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(108, 1500, '2022-09-15', '반납', '01065721196');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(109, 1500, '2022-10-4', '반납', '01065721196');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(110, 1500, '2022-10-24', '반납', '01012355678');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(112, 1500, '2023-2-12', '반납', '01041233234');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(113, 1500, '2023-5-13', '반납', '01041233234');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(114, 500, '2023-6-01', '파손', '01042343123');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(115, 500, '2023-6-3', '파손', '01042343123');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(116, 1000, '2023-6-19', '결함', '01035453123');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(117, 1500, '2023-7-2', '반납', '01035453123');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(118, 1500, '2023-7-9', '반납', '01045233422');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(119, 1500, '2023-8-17', '반납', '01012345678');

INSERT INTO t_point(point_Id, point, created_At, created_Memo, user_Phone)
VALUES(120, 1000, '2023-8-17', '결함', '01012345678');

INSERT INTO t_point(point, created_At, created_Memo, user_phone)
VALUES (1500, CURDATE(), '반납', '01065721196');

select * from t_point;

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2021-03-14', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2021-07-21', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2021-07-25', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2021-09-25', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2022-03-25', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES ('2022-03-25', '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES (CURDATE(), '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES (CURDATE(), '3년',  '상', 'NULL');

INSERT INTO t_product(manufacturing_Date, product_Age, product_Status, product_Img)
VALUES (CURDATE()-1, '3년',  '상', 'NULL');

select * from t_product;

-- drop database tumblerdb;
select * from t_user;
select * from t_product;
-- select * from information_schema.table_constraints;

show tables;

show databases;
-- create database Insa4_IOTB_hacksim_1;
-- drop database Insa4_IOTB_hacksim_1;

-- drop tables t_user, t_point, t_rental, t_product;

select * from t_user;
select user();

select * from t_product;
select * from t_point;

select * from t_user;

select SUM(point) as user_Point from t_point where user_Phone = "01012345678";
select * from t_point where user_Phone = "01012345678";

select * from t_rental;
SELECT DATE(NOW()) - INTERVAL 1 DAY;

select * from t_rental;

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 5 DAY), '대여중', 1, '01012345678');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 5 DAY), '대여중', 2, '01012345678');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 5 DAY), '대여중', 3, '01065721196');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 5 DAY), '대여중', 4, '01065721196');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 4 DAY), '대여중', 5, '01065721196');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(DATE_SUB(CURDATE(), INTERVAL 1 DAY), '대여중', 6, '01065721196');

INSERT INTO t_rental (rental_Date, rental_Status, Product_Id, user_Phone) VALUES
(CURDATE(), '대여중', 6, '01065721196');

UPDATE t_rental SET return_Date = CURDATE(), rental_Status ="반납완료" where Product_Id =14;


select * from t_rental;


select * from rental_id_seq;


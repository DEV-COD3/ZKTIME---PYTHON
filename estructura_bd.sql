CREATE DATABASE IF NOT EXISTS zk_attendance;

use zk_attendance;

create table attendance_logs (
    userid varchar (10),
    username varchar(50),
    checktime varchar(40) unique,
    checktype varchar(10),
    verifycode varchar(10)
)
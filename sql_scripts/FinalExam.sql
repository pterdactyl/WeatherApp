/*
 * Copyright (c) 2023 - All rights reserved.
 * Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
 *
 * SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
 * I certify that no other person's work has been used without due acknowledgement.
 * I have also not made my work available to anyone else without their due acknowledgement.
 */

CREATE DATABASE IF NOT EXISTS FinalExam;
CREATE USER IF NOT EXISTS learningdjango@'%' IDENTIFIED BY 'learningdjangoPW,.,.';
GRANT ALL ON FinalExam.* to learningdjango@'%';
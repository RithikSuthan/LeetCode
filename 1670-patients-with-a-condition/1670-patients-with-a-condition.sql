# Write your MySQL query statement below
select patient_id,patient_name,conditions from patients where instr(conditions,'DIAB1')
and conditions like 'DIAB1%' or conditions like '% DIAB1%';
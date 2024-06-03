select patient_id,patient_name ,conditions
from patients 
WHERE conditions regexp '(^|[[:space:]])DIAB1[0-9]*([[:space:]]|$)';

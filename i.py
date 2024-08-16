SELECT e.employee_name FROM tabEmployee e JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent WHERE eewh.department = 'Finance';
SELECT AVG(eewh.salary) AS average_salary FROM tabEmployee e JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent WHERE LOWER(eewh.company_name) LIKE LOWER('%Google%');
SELECT employee_name FROM tabEmployee WHERE first_name LIKE 'A%' AND status = 'Active';
SELECT COUNT(*) AS employee_count FROM tabEmployee WHERE blood_group = 'A+' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE employment_type = 'Full-Time' AND branch = 'Chennai' AND status = 'Active';
SELECT COUNT(*) as employee_count
FROM tabEmployee
WHERE monthly_salary > 50000 AND status = 'Active';
SELECT employee_name, department, reports_to
FROM tabEmployee
WHERE status = 'Active';
SELECT employee_name
FROM tabEmployee
WHERE MONTH(date_of_birth) = MONTH(CURDATE()) AND status = 'Active';
SELECT COUNT(*) as employee_count
FROM tabEmployee
WHERE notice_number_of_days < 30 AND status = 'Active';
SELECT employee_name, company_email
FROM tabEmployee
WHERE custom_deduction = 'Yes' AND company_email IS NOT NULL AND status = 'Active';
SELECT employee_name, monthly_salary FROM tabEmployee WHERE monthly_salary > 50000 AND status = 'Active';
SELECT employee_name, date_of_birth FROM tabEmployee WHERE MONTH(date_of_birth) = 8 AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE custom_deduction = 'Yes' AND status = 'Active' AND bond != 'Yes';
SELECT COUNT(*) AS birthday_count FROM tabEmployee WHERE MONTH(date_of_birth) = MONTH(CURDATE()) AND status = 'Active';
SELECT * FROM tabEmployee WHERE employee_name LIKE 'K%' AND status = 'Active';
SELECT COUNT(*) as employee_count
FROM tabEmployee
WHERE annual_ctc > 50000 AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE employee_name LIKE 'S%' AND status = 'Active';
SELECT employee_name, bank_ac_no, bank_name, prefered_email, cell_number FROM tabEmployee WHERE status = 'Active';
SELECT employee_name FROM tabEmployee WHERE date_of_birth IS NULL AND status = 'Active';
SELECT COUNT(*) as resigned_count FROM tabEmployee WHERE status = 'Resigned';
SELECT employee_name, designation, department, branch FROM tabEmployee WHERE status = 'Active';
SELECT employee_name FROM tabEmployee WHERE annual_ctc > 50000 AND bond = 'Yes' AND status = 'Active';
SELECT COUNT(*) FROM tabEmployee WHERE gender = 'Female' AND grade = 'B' AND status = 'Active';
SELECT employee_name, company_email, blood_group FROM tabEmployee WHERE status = 'Active';
SELECT e.employee_name FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE e.date_of_joining < '2023-01-01' AND ee.level = 'Post Graduate' AND e.status = 'Active';
SELECT COUNT(DISTINCT e.name) AS employee_count
FROM tabEmployee e
JOIN `tabEmployee Education` ee ON e.name = ee.parent
WHERE ee.year_of_passing >= YEAR(CURDATE()) - 5;
SELECT e.employee_name, eewh.bond_end_date
FROM tabEmployee e
JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent
WHERE eewh.bond_end_date IS NOT NULL AND e.status = 'Active';
SELECT COUNT(DISTINCT e.name) AS employee_count, SUM(e.custom_deduction_amount) AS total_deduction_amount
FROM tabEmployee e
WHERE e.custom_deduction = 'Yes';
SELECT employee_name, cell_number, company_email, personal_email
FROM tabEmployee
WHERE permanent_address_same_as_current_address = 1 AND status = 'Active';
SELECT e.employee_name
FROM tabEmployee e
JOIN `tabEmployee Education` ee ON e.name = ee.parent
WHERE e.designation = 'Software Engineer' AND ee.year_of_passing >= YEAR(CURDATE()) - 3 AND e.status = 'Active';
SELECT employee_name, department, designation FROM tabEmployee WHERE permanent_address_same_as_current_address = 1 AND date_of_joining < '2022-01-01' AND status = 'Active';
SELECT e.department, COUNT(ee.name) as employee_count FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE ee.year_of_passing = 2023 GROUP BY e.department;
SELECT employee_name FROM tabEmployee WHERE loyalty_starting_period <= NOW() AND loyalty_ending_period >= NOW() AND father_aadhar IS NOT NULL AND status = 'Active';
SELECT employee_name, department, default_shift FROM tabEmployee WHERE TIMESTAMPDIFF(YEAR, date_of_joining, CURDATE()) > 10 AND permanent_address IS NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE bond = 'Yes' AND mother_aadhar IS NOT NULL AND passbook_scanned_copy IS NULL AND status = 'Active';
SELECT COUNT(*) as employee_count FROM tabEmployee WHERE MONTH(date_of_birth) = 7 AND status = 'Active';
SELECT employee_name, salary_mode, custom_deduction FROM tabEmployee WHERE status = 'Active';
SELECT employee_name, cell_number FROM tabEmployee WHERE employee_name LIKE 'S%' AND status = 'Active';
SELECT COUNT(*) AS employee_count FROM tabEmployee WHERE father_name_or_husband_name IS NOT NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE pan_card_scanned_copy IS NOT NULL AND status = 'Active';
SELECT employee_name, designation, reports_to FROM tabEmployee WHERE status = 'Active';
SELECT employee_name FROM tabEmployee WHERE appraisal_cycle = MONTH(CURDATE()) AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE emergency_contact IS NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE date_of_birth BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 3 MONTH) AND status = 'Active';
SELECT employee_name, salary_mode, bank_ac_no FROM tabEmployee WHERE salary_mode = 'Bank Transfer' AND status = 'Active';
SELECT COUNT(*) AS employee_count FROM tabEmployee WHERE department = 'IT' AND designation = 'Software Engineer' AND status = 'Active';
SELECT employee_name, company_email FROM tabEmployee WHERE MONTH(date_of_birth) = 8 AND company_email IS NOT NULL AND status = 'Active';
SELECT employee_name, father_aadhar FROM tabEmployee WHERE department = 'Marketing' AND father_aadhar IS NOT NULL AND status = 'Active';
SELECT employee_name, loyalty_amount FROM tabEmployee WHERE loyalty_amount > 5000 AND appraisal_cycle = 'December' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE bank_ac_no IS NOT NULL AND date_of_joining < '2023-01-01' AND designation = 'Project Manager' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE bank_ac_no IS NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE loyalty_amount < 500 AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE MONTH(date_of_birth) = MONTH(CURDATE()) AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE bond_starting_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 3 MONTH) AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE father_name_or_husband_name IS NULL AND status = 'Active';
SELECT COUNT(*) as department_count
FROM tabEmployee
WHERE department = 'Finance' AND status = 'Active';
SELECT * FROM tabEmployee WHERE MONTH(date_of_birth) = '08';
SELECT e.employee_name, ee.year_of_passing
FROM tabEmployee e
JOIN `tabEmployee Education` ee ON e.name = ee.parent
WHERE ee.year_of_passing BETWEEN YEAR(CURDATE()) - 5 AND YEAR(CURDATE()) AND e.status = 'Active';
SELECT COUNT(*) as employee_count
FROM tabEmployee WHERE designation LIKE '%Software%' AND status = 'Active';
SELECT * FROM tabEmployee WHERE date_of_joining BETWEEN '2023-07-01' AND '2023-09-30' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE department = 'Marketing' AND blood_group = 'AB+' AND bond = 'Yes' AND status = 'Active';
SELECT * FROM tabEmployee WHERE designation = 'Software Engineer' AND date_of_joining < '2023-01-01' AND loyalty_amount > 1500 AND status = 'Active';
SELECT e.employee_name FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE e.salary_mode = 'Bank Transfer' AND e.department = 'IT' AND ee.year_of_passing = 2021 AND e.status = 'Active';
SELECT employee_name FROM tabEmployee WHERE aadhar_scanned_copy IS NULL AND status = 'Active';
SELECT * FROM tabEmployee WHERE department = 'IT' AND father_name_or_husband_name IS NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE branch = 'Chennai' AND department != 'Account' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE company_email IS NOT NULL AND alternate_mobile_number IS NULL AND status = 'Active';
SELECT e.employee_name, e.date_of_joining, eewh.custom_deduction, eewh.custom_deduction_amount FROM tabEmployee e JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent WHERE e.date_of_joining < '2021-01-01' AND e.status = 'Active' AND eewh.custom_deduction = 'Yes';
SELECT e.employee_name, e.annual_ctc, eewh.salary FROM tabEmployee e JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent WHERE eewh.salary IS NOT NULL AND e.status = 'Active';
SELECT COUNT(*) AS employee_count FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE e.loyalty_amount > 1000 AND ee.level = 'Post Graduate' AND e.status = 'Active';
SELECT employee_name, designation, salary_mode FROM tabEmployee WHERE status = 'Active';
SELECT COUNT(*) as employee_count FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE ee.year_of_passing >= YEAR(CURDATE()) - 5 AND e.status = 'Active';
SELECT employee_name, project_manager FROM tabEmployee WHERE bond_end_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 3 MONTH) AND status = 'Active';
SELECT e.employee_name, e.name, ee.qualification FROM tabEmployee e JOIN `tabEmployee Education` ee ON e.name = ee.parent WHERE e.previous_work_exp = 'Yes';
SELECT employee_name, passport_number, date_of_issue FROM tabEmployee WHERE passport_number IS NOT NULL AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE status = 'On Leave';
SELECT employee_name FROM tabEmployee WHERE previous_work_exp = 'No' AND status = 'Active';
SELECT t1.employee_name FROM tabEmployee t1 JOIN tabEmployee t2 ON t1.name = t2.name WHERE t1.custom_deduction = 'Yes' AND t2.employment_type = 'Full-Time';
SELECT employee_name FROM tabEmployee WHERE is_saturday_half = 1 AND department = 'Digital Marketing - SS';
SELECT employee_name FROM tabEmployee WHERE father_aadhar IS NULL AND mother_aadhar IS NOT NULL;
SELECT COUNT(*) AS employee_count
FROM tabEmployee e
JOIN `tabEmployee External Work History` eewh ON e.name = eewh.parent
WHERE e.department = 'Sales' AND eewh.total_experience_in_years > 10 AND e.status = 'Active';
SELECT e.name, e.employee_name, ee.qualification
FROM tabEmployee e
JOIN `tabEmployee Education` ee ON e.name = ee.parent
WHERE e.bonus_eligibility = 'Yes';
SELECT e.name, e.employee_name, e.department, tt.technology, tt.proficiency * 100 AS proficiency_percentage
FROM tabEmployee e
JOIN `tabTechnology Table` tt ON e.name = tt.parent
WHERE e.department = 'IT' AND tt.technology LIKE '%java%' AND tt.proficiency >= 0.9
ORDER BY e.employee_name, tt.technology;
SELECT *
FROM tabEmployee
WHERE status = 'Active';
SELECT COUNT(*) AS employee_count
FROM tabEmployee
WHERE department = 'Finance' AND blood_group = 'A+' AND status = 'Active';
SELECT employee_name
FROM tabEmployee
WHERE bond = 'Yes' AND loyalty_amount > 5000 AND status = 'Active';
SELECT employee_name
FROM tabEmployee
WHERE designation = 'Project Manager' AND passbook_scanned_copy IS NOT NULL AND status = 'Active';
SELECT employee_name
FROM tabEmployee
WHERE monthly_or_yearly = 'Monthly' AND custom_deduction = 'Yes' AND status = 'Active';
SELECT COUNT(*) AS employee_count
FROM tabEmployee
WHERE permanent_accommodation_type = 'Rented' AND branch = 'Chennai' AND status = 'Active';
SELECT name, designation FROM tabEmployee WHERE status = 'Active';
SELECT COUNT(DISTINCT e.name) FROM tabEmployee e JOIN tabEmployee Education ee ON e.name = ee.parent WHERE e.department = 'IT' AND ee.level = 'Post Graduate' AND e.status = 'Active';
SELECT employee_name, personal_email, company_email, cell_number FROM tabEmployee WHERE blood_group = 'A+' AND date_of_joining < '2021-01-01' AND status = 'Active';
SELECT employee_name FROM tabEmployee WHERE bond = 'Yes' AND scheduled_confirmation_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 3 MONTH) AND status = 'Active';
SELECT COUNT(*) FROM tabEmployee WHERE salary_mode = 'Bank Transfer' AND employee_photo IS NULL AND status = 'Active';
SELECT department, AVG(annual_ctc) AS average_salary
FROM tabEmployee
WHERE status = 'Active'
GROUP BY department;
SELECT employee_name, personal_email, company_email, cell_number, branch
FROM tabEmployee
WHERE status = 'Active';
SELECT COUNT(*) AS bond_expiring_count
FROM tabEmployee
WHERE bond = 'Yes' AND bond_end_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 1 YEAR) AND status = 'Active';
SELECT employee_name
FROM tabEmployee
WHERE MONTH(date_of_birth) = MONTH(CURDATE()) AND status = 'Active';
SELECT employee_name, department, designation FROM tabEmployee WHERE salary_mode = 'Bank Transfer' AND status = 'Active';
SELECT employee_number, employee_name, date_of_joining FROM tabEmployee WHERE date_of_joining < '2018-01-01' AND grade = 'A';
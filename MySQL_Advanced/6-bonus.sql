-- Script that creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN pr_user_id INT,
    IN pr_project_name VARCHAR(255),
    IN pr_score INT
)
BEGIN
  DECLARE v_project_id INT;
  SELECT id INTO v_project_id 
    FROM projects 
    WHERE name = pr_project_name 
    LIMIT 1;

    IF v_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (pr_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (pr_user_id, v_project_id, pr_score);
END$$

DELIMITER ;

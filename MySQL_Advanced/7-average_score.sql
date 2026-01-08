-- Script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN pr_user_id INT)
BEGIN
  DECLARE v_avg_score DECIMAL(10,2);
  SELECT AVG(score) INTO v_avg_score 
    FROM corrections
    WHERE user_id = pr_user_id;

    SET v_avg_score = IFNULL(v_avg_score, 0);

    UPDATE users 
    SET average_score = v_avg_score 
    WHERE id = pr_user_id;
END$$

DELIMITER ;

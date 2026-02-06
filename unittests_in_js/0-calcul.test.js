const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  describe('when both numbers are integers', function() {
    it('should return the sum of two positive integers', function() {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return the sum of two negative integers', function() {
      assert.strictEqual(calculateNumber(-1, -3), -4);
    });

    it('should return the sum of a positive and negative integer', function() {
      assert.strictEqual(calculateNumber(5, -2), 3);
    });

    it('should return 0 when both numbers are 0', function() {
      assert.strictEqual(calculateNumber(0, 0), 0);
    });
  });

  describe('when one number needs rounding', function() {
    it('should round the first number down', function() {
      assert.strictEqual(calculateNumber(1.2, 3), 4);
    });

    it('should round the first number up', function() {
      assert.strictEqual(calculateNumber(1.7, 3), 5);
    });

    it('should round the second number down', function() {
      assert.strictEqual(calculateNumber(1, 3.2), 4);
    });

    it('should round the second number up', function() {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe('when both numbers need rounding', function() {
    it('should round both numbers down', function() {
      assert.strictEqual(calculateNumber(1.2, 3.2), 4);
    });

    it('should round both numbers up', function() {
      assert.strictEqual(calculateNumber(1.7, 3.7), 6);
    });

    it('should round first up and second down', function() {
      assert.strictEqual(calculateNumber(1.7, 3.2), 5);
    });

    it('should round first down and second up', function() {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe('edge cases with .5 rounding', function() {
    it('should round 0.5 up to 1', function() {
      assert.strictEqual(calculateNumber(0.5, 0), 1);
    });

    it('should round 1.5 up to 2', function() {
      assert.strictEqual(calculateNumber(1.5, 0), 2);
    });

    it('should round 1.5 and 3.7 correctly', function() {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should round -0.5 up to 0', function() {
      assert.strictEqual(calculateNumber(-0.5, 0), 0);
    });

    it('should round -1.5 up to -1', function() {
      assert.strictEqual(calculateNumber(-1.5, 0), -1);
    });

    it('should round 2.5 up to 3', function() {
      assert.strictEqual(calculateNumber(2.5, 0), 3);
    });
  });

  describe('edge cases with very small decimals', function() {
    it('should round 1.0001 down to 1', function() {
      assert.strictEqual(calculateNumber(1.0001, 2), 3);
    });

    it('should round 1.4999 down to 1', function() {
      assert.strictEqual(calculateNumber(1.4999, 2), 3);
    });

    it('should round 1.9999 up to 2', function() {
      assert.strictEqual(calculateNumber(1.9999, 2), 4);
    });
  });

  describe('edge cases with negative numbers', function() {
    it('should handle negative decimals rounding down', function() {
      assert.strictEqual(calculateNumber(-1.2, -3.2), -4);
    });

    it('should handle negative decimals rounding up', function() {
      assert.strictEqual(calculateNumber(-1.7, -3.7), -6);
    });

    it('should handle mixed positive and negative with rounding', function() {
      assert.strictEqual(calculateNumber(-1.7, 3.7), 2);
    });
  });

  describe('edge cases with large numbers', function() {
    it('should handle large positive numbers', function() {
      assert.strictEqual(calculateNumber(1000.4, 2000.6), 3001);
    });

    it('should handle large negative numbers', function() {
      assert.strictEqual(calculateNumber(-1000.4, -2000.6), -3001);
    });
  });
});

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('type SUM', function() {
    it('should return the sum of two positive integers', function() {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    it('should return the sum when both numbers are rounded down', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return the sum when first number is rounded down', function() {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('should return the sum when second number is rounded up', function() {
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    });

    it('should return the sum when both numbers are rounded up', function() {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    it('should handle negative numbers', function() {
      assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5);
    });

    it('should handle zero', function() {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });

    it('should handle mixed positive and negative', function() {
      assert.strictEqual(calculateNumber('SUM', -1.4, 4.5), 4);
    });
  });

  describe('type SUBTRACT', function() {
    it('should return the subtraction of two positive integers', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    });

    it('should return the subtraction when both numbers are rounded', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return the subtraction when first is rounded down', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });

    it('should return the subtraction when second is rounded up', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 3.7), 1);
    });

    it('should return the subtraction when both are rounded up', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    });

    it('should handle negative numbers', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });

    it('should handle subtracting zero', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 0), 5);
    });

    it('should handle subtracting from zero', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 0, 5.2), -5);
    });

    it('should handle mixed positive and negative', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, 4.5), -6);
    });
  });

  describe('type DIVIDE', function() {
    it('should return the division of two positive integers', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
    });

    it('should return the division when both numbers are rounded', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return the division when first is rounded up', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 2), 2.5);
    });

    it('should return the division when second is rounded down', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 8, 2.2), 4);
    });

    it('should return the division when both are rounded', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 8.6, 2.4), 4.5);
    });

    it('should handle negative numbers', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -9, 3), -3);
    });

    it('should handle dividing negative by positive', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -8.6, 2.4), -4.5);
    });

    it('should handle dividing positive by negative', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 8.6, -2.4), -4.5);
    });

    it('should handle dividing two negatives', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -8.6, -2.4), 4.5);
    });

    describe('division by zero', function() {
      it('should return Error when dividing by 0', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      });

      it('should return Error when dividing by a number that rounds to 0', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
      });

      it('should return Error when dividing by a negative that rounds to 0', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.2), 'Error');
      });

      it('should return Error when dividing by 0.4', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
      });

      it('should return Error when dividing zero by zero', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
      });

      it('should not return Error when dividing by 0.5 (rounds to 1)', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 4, 0.5), 4);
      });
    });
  });

  describe('edge cases', function() {
    it('should handle 0.5 rounding for SUM', function() {
      assert.strictEqual(calculateNumber('SUM', 0.5, 0.5), 2);
    });

    it('should handle 0.5 rounding for SUBTRACT', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 0.5, 0.5), 0);
    });

    it('should handle 0.5 rounding for DIVIDE', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 0.5, 0.5), 1);
    });

    it('should handle large numbers with SUM', function() {
      assert.strictEqual(calculateNumber('SUM', 1000.4, 2000.6), 3001);
    });

    it('should handle large numbers with SUBTRACT', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 2000.6, 1000.4), 1001);
    });

    it('should handle large numbers with DIVIDE', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1000.5, 10.5), 91);
    });
  });

  describe('invalid type', function() {
    it('should return Error for invalid type', function() {
      assert.strictEqual(calculateNumber('MULTIPLY', 1, 2), 'Error');
    });

    it('should return Error for empty type', function() {
      assert.strictEqual(calculateNumber('', 1, 2), 'Error');
    });

    it('should return Error for lowercase type', function() {
      assert.strictEqual(calculateNumber('sum', 1, 2), 'Error');
    });
  });
});
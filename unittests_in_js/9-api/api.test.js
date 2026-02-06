const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should have correct content type', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code when :id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct result when :id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 when :id is NOT a number (string)', (done) => {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 when :id contains letters', (done) => {
    request.get(`${baseUrl}/cart/abc123`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 when :id is a decimal number', (done) => {
    request.get(`${baseUrl}/cart/12.5`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 when :id is negative', (done) => {
    request.get(`${baseUrl}/cart/-12`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should work with single digit id', (done) => {
    request.get(`${baseUrl}/cart/5`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 5');
      done();
    });
  });

  it('should work with large numbers', (done) => {
    request.get(`${baseUrl}/cart/123456789`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 123456789');
      done();
    });
  });

  it('should return 404 for cart without id', (done) => {
    request.get(`${baseUrl}/cart/`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 when :id contains special characters', (done) => {
    request.get(`${baseUrl}/cart/@#$`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 when :id is empty string', (done) => {
    request.get(`${baseUrl}/cart/ `, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return correct message format', (done) => {
    request.get(`${baseUrl}/cart/999`, (error, response, body) => {
      expect(body).to.match(/^Payment methods for cart \d+$/);
      done();
    });
  });

  it('should handle zero as id', (done) => {
    request.get(`${baseUrl}/cart/0`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 0');
      done();
    });
  });

  it('should return 404 for alphanumeric id starting with number', (done) => {
    request.get(`${baseUrl}/cart/123abc`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 for id with spaces', (done) => {
    request.get(`${baseUrl}/cart/12 34`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should have correct content type for valid cart', (done) => {
    request.get(`${baseUrl}/cart/42`, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });

  it('should include id in response message', (done) => {
    const testId = 777;
    request.get(`${baseUrl}/cart/${testId}`, (error, response, body) => {
      expect(body).to.include(testId.toString());
      done();
    });
  });

  it('should respond quickly for valid cart request', (done) => {
    const startTime = Date.now();
    request.get(`${baseUrl}/cart/100`, (error, response, body) => {
      const responseTime = Date.now() - startTime;
      expect(responseTime).to.be.lessThan(1000);
      done();
    });
  });

  it('should return 404 for cart with multiple slashes', (done) => {
    request.get(`${baseUrl}/cart//12`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should work with leading zeros', (done) => {
    request.get(`${baseUrl}/cart/007`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 007');
      done();
    });
  });
});
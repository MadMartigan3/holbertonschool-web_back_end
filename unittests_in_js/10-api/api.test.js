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

  it('should return 404 when :id is NOT a number', (done) => {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct payment methods object', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      const expectedResponse = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
      expect(JSON.parse(body)).to.deep.equal(expectedResponse);
      done();
    });
  });

  it('should return JSON content type', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      expect(response.headers['content-type']).to.include('application/json');
      done();
    });
  });

  it('should have payment_methods property', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      const jsonResponse = JSON.parse(body);
      expect(jsonResponse).to.have.property('payment_methods');
      done();
    });
  });

  it('should have credit_cards set to true', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      const jsonResponse = JSON.parse(body);
      expect(jsonResponse.payment_methods.credit_cards).to.be.true;
      done();
    });
  });

  it('should have paypal set to false', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      const jsonResponse = JSON.parse(body);
      expect(jsonResponse.payment_methods.paypal).to.be.false;
      done();
    });
  });

  it('should have both payment methods', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      const jsonResponse = JSON.parse(body);
      expect(jsonResponse.payment_methods).to.have.all.keys('credit_cards', 'paypal');
      done();
    });
  });

  it('should return valid JSON', (done) => {
    request.get(`${baseUrl}/available_payments`, (error, response, body) => {
      expect(() => JSON.parse(body)).to.not.throw();
      done();
    });
  });
});

describe('Login', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return correct status code', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };

    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return welcome message with username', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });

  it('should handle different usernames', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'John' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome John');
      done();
    });
  });

  it('should return text content type', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };

    request(options, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });

  it('should handle POST method only', (done) => {
    request.get(`${baseUrl}/login`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should include username in response', (done) => {
    const testUsername = 'TestUser123';
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: testUsername }
    };

    request(options, (error, response, body) => {
      expect(body).to.include(testUsername);
      done();
    });
  });

  it('should handle empty username', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: '' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome ');
      done();
    });
  });

  it('should handle username with spaces', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty Lou' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty Lou');
      done();
    });
  });

  it('should handle special characters in username', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty@123' }
    };

    request(options, (error, response, body) => {
      expect(body).to.include('Betty@123');
      done();
    });
  });

  it('should respond without errors', (done) => {
    const options = {
      url: `${baseUrl}/login`,
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };

    request(options, (error, response, body) => {
      expect(error).to.be.null;
      done();
    });
  });
});
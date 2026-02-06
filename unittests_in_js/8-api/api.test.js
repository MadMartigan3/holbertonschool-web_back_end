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

  it('should not return an error', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(error).to.be.null;
      done();
    });
  });

  it('should have content-length greater than 0', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body.length).to.be.greaterThan(0);
      done();
    });
  });

  it('should return a string', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.be.a('string');
      done();
    });
  });

  it('should contain "Welcome" in the message', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.include('Welcome');
      done();
    });
  });

  it('should contain "payment system" in the message', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.include('payment system');
      done();
    });
  });

  it('should respond within reasonable time', (done) => {
    const startTime = Date.now();
    request.get(baseUrl, (error, response, body) => {
      const responseTime = Date.now() - startTime;
      expect(responseTime).to.be.lessThan(1000);
      done();
    });
  });

  it('should handle GET method', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.request.method).to.equal('GET');
      done();
    });
  });

  it('should return 404 for unknown routes', (done) => {
    request.get(`${baseUrl}/unknown`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should have proper response headers', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers).to.have.property('content-type');
      expect(response.headers).to.have.property('content-length');
      done();
    });
  });

  it('should return text/html content-type', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-type']).to.match(/text\/html/);
      done();
    });
  });

  it('should accept connections', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers.connection).to.exist;
      done();
    });
  });

  it('should return exact message', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should have status message OK', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusMessage).to.equal('OK');
      done();
    });
  });

  it('should respond to multiple requests', (done) => {
    let completedRequests = 0;
    const totalRequests = 3;

    for (let i = 0; i < totalRequests; i++) {
      request.get(baseUrl, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        completedRequests++;
        if (completedRequests === totalRequests) {
          done();
        }
      });
    }
  });

  it('should have correct HTTP version', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.httpVersion).to.equal('1.1');
      done();
    });
  });

  it('should not have errors in response', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(error).to.be.null;
      expect(response).to.exist;
      expect(body).to.exist;
      done();
    });
  });

  it('should return complete message without truncation', (done) => {
    request.get(baseUrl, (error, response, body) => {
      const expectedMessage = 'Welcome to the payment system';
      expect(body).to.have.lengthOf(expectedMessage.length);
      done();
    });
  });

  it('should be accessible via localhost', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.request.uri.hostname).to.equal('localhost');
      done();
    });
  });

  it('should use port 7865', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.request.uri.port).to.equal('7865');
      done();
    });
  });

  it('should have successful response', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.be.within(200, 299);
      done();
    });
  });
});
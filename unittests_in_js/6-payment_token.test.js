const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a successful response when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Verify the response structure
        expect(response).to.be.an('object');
        expect(response).to.have.property('data');
        expect(response.data).to.equal('Successful response from the API');
        
        // CRITICAL: Call done() to signal test completion
        done();
      })
      .catch((error) => {
        // If promise rejects, fail the test
        done(error);
      });
  });

  it('should return undefined when success is false', function(done) {
    const result = getPaymentTokenFromAPI(false);
    
    // When success is false, the function returns undefined
    expect(result).to.be.undefined;
    
    // Call done() immediately since there's no async operation
    done();
  });

  it('should handle the promise correctly with async/await syntax', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response.data).to.equal('Successful response from the API');
        done();
      })
      .catch(done); // Simplified error handling
  });
});
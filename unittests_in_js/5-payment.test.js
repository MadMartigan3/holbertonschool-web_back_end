const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;

  beforeEach(function() {
    // Setup: Create spy before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    // Teardown: Restore spy after each test
    consoleSpy.restore();
  });

  it('should log "The total is: 120" for sendPaymentRequestToApi(100, 20)', function() {
    sendPaymentRequestToApi(100, 20);

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" for sendPaymentRequestToApi(10, 10)', function() {
    sendPaymentRequestToApi(10, 10);

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;

    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
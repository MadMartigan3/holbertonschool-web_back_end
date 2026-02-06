const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  let stub;
  let consoleSpy;

  beforeEach(function() {
    // Stub Utils.calculateNumber to always return 10
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    stub.restore();
    consoleSpy.restore();
  });

  it('should call Utils.calculateNumber with type SUM, a=100, and b=20', function() {
    sendPaymentRequestToApi(100, 20);

    // Verify stub was called once
    expect(stub.calledOnce).to.be.true;

    // Verify stub was called with correct arguments
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;
  });

  it('should log "The total is: 10" to console', function() {
    sendPaymentRequestToApi(100, 20);

    // Verify console.log was called with correct message
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    expect(consoleSpy.calledOnce).to.be.true;
  });
});

// Separate test suite to validate Utils.calculateNumber itself
describe('Utils.calculateNumber', function() {
  it('should correctly sum two numbers', function() {
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(120);
  });

  it('should correctly handle rounding', function() {
    expect(Utils.calculateNumber('SUM', 100.4, 20.5)).to.equal(121);
  });
});
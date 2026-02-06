const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  it('should stub Utils.calculateNumber to return 10 and verify console.log', function() {
    // Create a stub that always returns 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    // Create a spy on console.log
    const consoleSpy = sinon.spy(console, 'log');

    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Verify the stub was called once
    expect(stub.calledOnce).to.be.true;

    // Verify the stub was called with correct arguments
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;

    // Verify console.log was called once
    expect(consoleSpy.calledOnce).to.be.true;

    // Restore the stub and spy
    stub.restore();
    consoleSpy.restore();
  });

  it('should verify stub is called with exact arguments', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Verify arguments in detail
    expect(stub.args[0][0]).to.equal('SUM');
    expect(stub.args[0][1]).to.equal(100);
    expect(stub.args[0][2]).to.equal(20);

    // Verify console output
    expect(consoleSpy.firstCall.args[0]).to.equal('The total is: 10');

    stub.restore();
    consoleSpy.restore();
  });

  it('should work with different input values but still return 10', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    // Even with different values, the stub returns 10
    sendPaymentRequestToApi(200, 50);

    expect(stub.calledWith('SUM', 200, 50)).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    consoleSpy.restore();
  });

  it('should demonstrate stub behavior vs real function', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    sendPaymentRequestToApi(100, 20);

    // The stub returns 10, not the real calculation (120)
    expect(stub.returnValues[0]).to.equal(10);
    
    // If it were the real function, it would return 120
    // But with the stub, it always returns 10

    stub.restore();
  });
});
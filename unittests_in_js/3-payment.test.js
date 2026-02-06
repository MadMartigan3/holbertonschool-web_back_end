const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with SUM, 100, and 20', function() {
    // Create a spy on Utils.calculateNumber
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Verify the spy was called once
    expect(spy.calledOnce).to.be.true;

    // Verify the spy was called with the correct arguments
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    // Verify the spy returned the correct value
    expect(spy.returnValues[0]).to.equal(120);

    // Restore the spy
    spy.restore();
  });

  it('should call Utils.calculateNumber with correct type', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // Verify the first argument is 'SUM'
    expect(spy.args[0][0]).to.equal('SUM');

    spy.restore();
  });

  it('should call Utils.calculateNumber with correct amounts', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    // Verify the second and third arguments
    expect(spy.args[0][1]).to.equal(100);
    expect(spy.args[0][2]).to.equal(20);

    spy.restore();
  });

  it('should display the correct total in console', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    spy.restore();
    consoleSpy.restore();
  });

  it('should work with decimal values', function() {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100.5, 20.3);

    // Verify the spy was called
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100.5, 20.3)).to.be.true;

    // The result should be 101 + 20 = 121
    expect(spy.returnValues[0]).to.equal(121);

    spy.restore();
  });
});
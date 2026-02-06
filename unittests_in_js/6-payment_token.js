function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  // When success is false, do nothing (don't return anything)
}

module.exports = getPaymentTokenFromAPI;
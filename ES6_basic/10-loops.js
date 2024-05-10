export default function appendToEachArrayValue(array, appendString) {
    const newArr = [];
    for (const e of array) {
      newArr.push(appendString + e);
    }
  
    return newArr;
  }

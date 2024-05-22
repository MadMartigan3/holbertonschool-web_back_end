export default function cleanSet(set, startString) {
  const result = [];
  if (!startString || startString === 0) {
    return '';
  }

  set.forEach((value) => {
    if (value && value.startsWith(startString)) result.push(value.replace(startString, ''));
    return value;
  });
  return result.join('-');
}

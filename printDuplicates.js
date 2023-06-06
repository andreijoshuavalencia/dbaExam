const numArr = [5, 1, 4, 6, 7, 3, 5, 7, 3];
const duplicateNum = [];

const countNum = {};
for (let i = 0; i < numArr.length; i++) {
  const currentNum = numArr[i];
  if (countNum[currentNum]) {
      console.log(countNum)
    countNum[currentNum]++;
  } else {
    countNum[currentNum] = 1;
  }
}

for (const data in countNum) {
  if (countNum[data] > 1) {
    duplicateNum.push(Number(data));
  }
}
console.log("Duplicate elements:", duplicateNum);

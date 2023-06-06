let num = 6; 

for(let i = 1; i <= num; i++) {
    let numStr = '';
    for(let j = 1; j <= i; j++){
        numStr += i
        if (j !== i) {
        numStr += ' ';
      }
    }
    console.log(numStr);
}
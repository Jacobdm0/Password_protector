


const userValue = document.getElementById('password').value;
const result = document.getElementById('result');
const newPass = document.getElementById('new_pass');
const checkButton = document.getElementById('check');
const generateButton = document.getElementById('generate');
const fs = require('fs');
const csv = require('csv-parser');

function fileRead(filename) {
    return new Promise((resolve, reject) => {
        const results = [];
        fs.createReadStream(filename)
            .pipe(csv())
            .on('data', (data) => results.push(data))
            .on('end', () => {
                resolve(results);
            })
            .on('error', (err) => reject(err));
    });
}
fileRead('passwoord_list.csv').then((funList) => {
    console.log(funList);
    return funList;
})
generateButton.addEventListener('click', (passGen));
function passGen() {
    const alphaList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const passLen = getElementById('length').value;
    const passNum = getElementById('number').value;
    const passChar = passLen - passNum;
    
    let passStr = '';

    // Add numbers
    for (let i = 0; i < passNum; i++) {
        passStr += Math.floor(Math.random() * 10);
    }

    // Add letters
    for (let i = 0; i < passChar; i++) {
        const alpha = alphaList.charAt(Math.floor(Math.random() * alphaList.length));
        const alphaIndex = Math.floor(Math.random() * passStr.length);
        passStr = passStr.slice(0, alphaIndex) + alpha + passStr.slice(alphaIndex);
    }

    return passStr;
    newPass.innerHTML = passStr;
}
function subList(funList, userValue) {
    let checkList = [];
    const firstChar = userValue.charAt(0).toLowerCase();

    // Find matching first character
    funList.forEach(item => {
        if (item[0].toLowerCase() === firstChar) {
            checkList.push(item);
        }
    });

    checkList.sort();
    return checkList;
}
function clean(funList) {
    console.log("cleaned");
    return funList.filter(item => item !== '').sort();
    
}


function passCheck(checkList, userValue) {
    let start = 0;
    let end = checkList.length - 1;
    console.log(end);
    let found = false;
    while (start <= end) {
        const mid = Math.floor((start + end) / 2);
        const checkValue = checkList[mid];

        if (userValue.toLowerCase() < checkValue.toLowerCase()) {
            end = mid - 1;
        } else if (userValue.toLowerCase() > checkValue.toLowerCase()) {
            start = mid + 1;
        } else {
            found = true;
            break;
        }
    }

    if (found) {
        result.inner = 'Password Found : Unsafe'; 
    } else {
        result.inner = 'Password  Not Found: Safe';
    }
    result.style.display = 'block';
}
checkButton.addEventListener('click', () => {
    let cleanlist =clean(funList);
    let subed=subList(cleanlist, userValue);
    let found=passCheck(subed, userValue);

    
    
});
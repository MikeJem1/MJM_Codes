let numPhone = prompt("Rantre nimewo telefon nan");

if (numPhone.startsWith("509")) {
    if (numPhone.length === 11) {
        numPhone = numPhone.substring(3);
    }
} else {
    if (numPhone.length === 8) {
        numPhone = "509" + numPhone;
    }
}

console.log(numPhone);

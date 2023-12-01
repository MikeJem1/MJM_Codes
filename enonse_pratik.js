// NB:chak kod yo teste apa sou yon navigatè



//*********************** */ kod pou chanje tout let yo an let miniskil
Nom=prompt("rantre nonw").toLowerCase();

console.log(Nom)



// *********************************no 2**************************
let chennAnvan =prompt("rantre yon fraz");
let lisEleman = chennAnvan.split(' ');  // Koupe chenn an dapre espas yo epi retounen yon lis

// Fè yon boukla sou lisEleman pou kreye yon nouvo lis ak mo yo ki pa gen espas
let nouvolis=[];

for(let i=0; i<lisEleman.length; i++){
    // pou retire espas yo nan chak mo
    let mosanespas= lisEleman[i].replace(/\s/g,'');
    nouvolis.push(mosanespas);
}

console.log(nouvolis);

// ********************* no 3pou mwen ka chanje premyelet la an majiskil**********************

let nom="mike"
let premyelet=nom.charAt(0); // pou mwen identifye premye let nan fraz la
let ranjenom=premyelet.toUpperCase();
console.log(ranjenom)



//***************** * no 4*************************************

let fraz="kisa wap fe la tifi";

let mo=fraz.split(/\s+/);

let premyeletnanchak=mo.map(lol=> lol.charAt(0));
let newmo=premyeletnanchak.join('');
console.log(newmo);




//********************** no 5**************

let mots="ananana";
let lotmo=mots.replace(/a/g,'@'); // pou chanje a an @
console.log(lotmo)




//**************no 6 *********************
let prememo="lambert";
let moapre=''.concat(prememo.substring(6), prememo.substring(0,6)); // pou chanje pozisyon let yo

console.log(moapre);


//*********************no 7 ************/
let moexo7 = "nou pa vann  anana";
let endeksPremyeA = -1;  // Initializasyon a -1, ki vle di nou poko jwenn "a"

for (let i = 0; i < moexo7.length; i++) {
    if (moexo7[i] === 'a') {
        endeksPremyeA = i;
        break;  // Sòti nan boukla lè nou jwenn premye "a"
    }
}

console.log("Endeks premye 'a' se:", endeksPremyeA);
//****************************exo8*********** */
let moexo8="nou pa vann anana";
let totalendeks_A=0;
 
for(let i=0; i< moexo8.length; i++){
    if(moexo8[i]==='a'){
        totalendeks_A +=i;
    }
}

console.log(totalendeks_A)



//*********************no 9 ***************

let moexo9="nou pa vann anana";
let endeks_A=[];

for (let i=0; i<moexo9.length; i++){
    if(moexo9[i]==='a'){
        endeks_A.push(i);
    }
}

console.log(endeks_A)


//*******************exo 10**************** */
let revmwen = "mwen vle pou Ayiti chanje";
let kolerevmwen = revmwen.replace(/ /g, '');

console.log(kolerevmwen);

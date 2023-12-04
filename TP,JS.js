



function generatePassword(longeur,...args){
   let alphabet="abcdefghijklmnopqrstuvwxyz";

   if (args.includes(true)){
        alphabet += "0123456789";
   }

   if(args.includes(true)){
     alphabet +="!@#$%&*"
   }
    let motdepas="";
    for (let i=0;i<longeur;i++){
        const hasard=Math.floor(Math.random()* alphabet.length);
      motdepas += alphabet.charAt(hasard);
    }
    return motdepas;
}

const newmodpass=generatePassword(8,true);
console.log(newmodpass);
module.exports = { 
	//param A : string
	//return an integer
  titleToNumber : function(A){
    var base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    var str =  A.split('')
    var length = str.length-1
    var number  = 0
    str.forEach(function(letter) {
      number += Math.pow(26, length) * (base.indexOf(letter) + 1)
      length--
    })
    return number
  }
};


module.exports = { 
  //param A : string
  //param B : string
  //return an integer
  compareVersion : function(A, B) {
	var a  = A.split('.')
	var b  = B.split('.')
	var nA = a.length
	var nB = b.length
	var i  = 0
	while (i < nA || i< nB) {
	  if (i<nA && i<nB) {
		if (parseInt(a[i]) < parseInt(b[i])) return -1
		else if(parseInt(a[i]) > parseInt(b[i]))   return 1
	  } else if(i< nA) {
		if (parseInt(a[i]) !=0) return 1
	  } else if (i< nB) {
		if(parseInt(b[i]) !=0) return -1
	  }
	  i++
	}
	return 0
  }
};


//alert("Sitio Web en desarrollo..")

navigator.mediaDevices.getUserMedia({audio: false, video: true}).then((stream)=>{
	console.log(stream)
	//var constraints = { video: { frameRate: { ideal: 10, max: 15 } } };
	let video=document.getElementById('grabar');
	video.srcObject=stream;
	

}).catch((err)=>console.log(err))
//Tomar captura
html2canvas(document.body, {
  onrendered (canvas) {
    var link = document.getElementById('camara');;
    var image = canvas.toDataURL();
    link.href = image;
    link.download = 'demo.png';
  }
 });
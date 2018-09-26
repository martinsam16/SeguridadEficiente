window.onload = function() {
      var video = document.getElementById('video');
      var canvas = document.getElementById('canvas');
      var context = canvas.getContext('2d');
      var servox;

      var tracker = new tracking.LandmarksTracker();
      tracker.setInitialScale(4);
      tracker.setStepSize(2);
      tracker.setEdgesDensity(0.1);

      tracking.track('#video', tracker,{ camera: true });

      tracker.on('track', function(event) {

        context.clearRect(0,0,canvas.width, canvas.height);

        if(!event.data) return;

          event.data.faces.forEach(function(rect) {
            context.strokeStyle = '#fff';
            context.strokeRect(rect.x, rect.y, rect.width, rect.height);
            context.font = '11px Helvetica';
            context.fillStyle = "#fff";
            context.fillText('x: ' + rect.x + '°', rect.x + rect.width + 5, rect.y + 11);
            context.fillText('y: ' + rect.y + '°', rect.x + rect.width + 5, rect.y + 22);
            servox=rect.x;
            console.log(servox);
          });

          $( document ).ready(function() {
            $("#contenedor").load("php/enviar.php",{servox});
             });

          event.data.landmarks.forEach(function(landmarks) {
            for(var l in landmarks){
              context.beginPath();
              context.fillStyle = "#fff";
              context.arc(landmarks[l][0],landmarks[l][1],1,0,2*Math.PI);
              context.fill();
            }
          });

      });
    };

<!DOCTYPE html>
<html>
	<head>
		<title>P5.js Example</title>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.14/p5.js"></script>
		<script>


            let a = [];
            let x = 20, y = 40;
            let _string = "Hello!";
			function setup(){
				createCanvas(500, 500);
				background(150);
				textSize(30);
				textStyle(ITALIC);
			}

			function draw(){
				clear();
				background(150);
				fill(255);
				ellipse(x, y, 20, 40);
				line(0, 0, width, height);
				rect(100, 200, 40, 70);
				fill('red');
				text(_string, 200, 300);
				append(a, 300);
				for (let i = 0; i < a.length; i++) {
					rect(a[i], 200, 40, 70);
				}

				//if (mouseIsPressed) {
				//	x = mouseX;
				//	y = mouseY;
				//}

				if (keyIsPressed) {
					_string = key
					if (keyCode === ENTER) {
						_string = 'ENTER';
					}
				}
			}

			//function mousePressed() {
			//	x = mouseX;
			//	y = mouseY;
			//}

			//function keyPressed() {
			//	x = mouseX;
			//	y = mouseY;
			//}
		</script>
	</head>
	<body>
	</body>
</html>

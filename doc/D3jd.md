Data Driven Documents:
=====================

#Select and Append:
1. Add d3js script 
2. At the end of the body. Write a javascript 
	* d3.select("p").text("Hello World");
	- If there is no paragraph p
	* d3.select("body")
		.append("p")
		.style("red")
		.text("Hi, Whats up!");

# Basic SVG shapes(scalable vector graphics):
1.  var canvas = d3.select("body")
					.append("svg")
					.attr("width", 800)
					.attr("height", 400);
2. var circle = canvas.append("circle");
				.attr("cx" ,250);
				.attr("cy", 250);
				.attr("r",50);
				.attr("fill","red")


# Visualizing data:
1. var data Array= [20, 40, 60];

Bar chart 
2. var bars = canvas.selectAll("rect")
				.data(dataArray);
				.enter()
					.append("rect")
					.attr("width", function(d){
						return d*10;
					})	
					.attr("height", function(){
						return 50;
					})
					.attr("y", function(d,i){
						return i*100;
					});

Scale 
3. var widthScale = d3.scale.linear()
						.domain([])
						.range([]);

Groups and Axes 
4.  Group is added to canvas element to transform the svg element. 
	var canvas = d3.select("body")
					.append("svg")
					.attr("width", 500)
					.attr("height", 500)
					.append("g")
					.attr("transform", "translate(20,20)")

	Axis  --- (call axis) 
	canvas.call(axis);

5. Enter, Update, Exit 
		DOM elements > data elements (enter)
		DOM elements < data elements   (update)
		DOM elements == data elements (exit)

6. Transition :  .duration(), .delay()

7. Working with arrays 
		d3 has pretty good methods in that library 
			d3.min(data)
			d3.max(data)
			d3.extent(data)
			d3.mean(data)
			d3.	median(data)
			d3.shuffle -- Some random order. 

8 . No need of jquery, you can directly load json with d3. example given below 
		d3.json("./mysampledata.json", function(data){
				//code..
		});

9. (Paths, Arcs, PieLayouts) 		
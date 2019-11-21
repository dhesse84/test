function button1() {
  //var selector = d3.select("#sel_div");
  js_search_word = 'soulsearching'
  console.log('starting search...');
  d3.json(`/histogram/${js_search_word}`).then((milesData) => {


      console.log('Search results:');
      console.log(milesData);
      console.log('..end of search results.');

      //sampleNames.forEach(x => console.log(x.filename););
      //for (var key of Object.keys(sampleNames)) {
      //  console.log(key + " -> " + sampleNames[key])
      //}

      // var tbody = d3.select(".table").select("tbody");
      // tbody.html("");


      // sampleNames.forEach((x) => {
      //   var row = tbody.append("tr");

      
      //   Object.entries(x).forEach(([key, value]) => {
      //   //Object.entries(x).forEach(([key, value]) => {
      //     if (key == 'date' || key == 'president' || key == 'title') {
      //           var cell = row.append("td");
      //           cell.text(value);
      //         }
      //   });
      // });



    

// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 60,
  right: 60,
  bottom: 60,
  left: 60
};

// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set its dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append a group area, then set its margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Configure a parseTime function which will return a new Date object from a string
var parseTime = d3.timeParse("%Y/%m/%d");


  // Format the date and cast the miles value to a number
  milesData.forEach(function(data) {
    data.date = parseTime(data.date);
    data.miles = +data.miles;
  });

  // Configure a time scale with a range between 0 and the chartWidth
  // Set the domain for the xTimeScale function
  // d3.extent returns the an array containing the min and max values for the property specified
  var xTimeScale = d3.scaleTime()
    .range([0, chartWidth])
    .domain(d3.extent(milesData, data => data.date));

  // Configure a linear scale with a range between the chartHeight and 0
  // Set the domain for the xLinearScale function
  var yLinearScale = d3.scaleLinear()
    .range([chartHeight, 0])
    .domain([0, d3.max(milesData, data => data.miles)]);

  // Create two new functions passing the scales in as arguments
  // These will be used to create the chart's axes
  var bottomAxis = d3.axisBottom(xTimeScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Configure a drawLine function which will use our scales to plot the line's points
  var drawLine = d3
    .line()
    .x(data => xTimeScale(data.date))
    .y(data => yLinearScale(data.miles));

  // Append an SVG path and plot its points using the line function
  chartGroup.append("path")
    // The drawLine function returns the instructions for creating the line for milesData
    .attr("d", drawLine(milesData))
    .classed("line", true);
  console.log(milesData);
  // Append an SVG group element to the SVG area, create the left axis inside of it
  chartGroup.append("g")
    .classed("axis", true)
    .call(leftAxis);

  // Append an SVG group element to the SVG area, create the bottom axis inside of it
  // Translate the bottom axis to the bottom of the page
  chartGroup.append("g")
    .classed("axis", true)
    .attr("transform", "translate(0, " + chartHeight + ")")
    .call(bottomAxis);


      console.log('got here.');

      //buildChart(firstSample);
      //buildMetadata(firstSample);

  });
};



function button2() {
  console.log('got here button2');

  var selector = d3.select("#sel_div");
   d3.json("/setup").then((aaa) => {
    console.log(aaa)
      aaa.forEach((x) => {
       console.log(x);
        selector
           .append("option")
           .text(`${x.number} - ${x.president}`)
           .property("value", x.president);
      });
    });
    console.log('ended here button2'); 
};


// function button3() {
//   var chart = d3.select("#chart_div");
// };


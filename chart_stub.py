
# Brace escaped html source
html_source = """
<!DOCTYPE html>
<html>
<meta charset ="utf8">
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {{packages:["geochart"]}});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {{

        var data = google.visualization.arrayToDataTable([
          ['Region', 'Percent','Users']{0}
        ]);

        var options = {{
          sizeAxis: {{ minValue: 50, maxValue: 100 }},
          displayMode: 'markers',
          colorAxis: {{colors: ['#e7711c', '#4374e0']}}
        }};

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      }}
    </script>
  </head>
  <body>
    <div id="regions_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>"""
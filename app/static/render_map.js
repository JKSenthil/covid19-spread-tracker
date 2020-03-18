function render_map(url, container) {
    Highcharts.ajax({
        url: url,
        success: function (data) {
            var countiesMap = Highcharts.geojson(
                Highcharts.maps['countries/us/us-all-all']
                ),
                // Extract the line paths from the GeoJSON
                lines = Highcharts.geojson(
                    Highcharts.maps['countries/us/us-all-all'], 'mapline'
                ),
                // Filter out the state borders and separator lines, we want these
                // in separate series
                borderLines = Highcharts.grep(lines, function (l) {
                    return l.properties['hc-group'] === '__border_lines__';
                }),
                separatorLines = Highcharts.grep(lines, function (l) {
                    return l.properties['hc-group'] === '__separator_lines__';
                });

            // Add state acronym for tooltip
            Highcharts.each(countiesMap, function (mapPoint) {
                mapPoint.name = mapPoint.name + ', ' +
                    mapPoint.properties['hc-key'].substr(3, 2);
            });

            document.getElementById(container).innerHTML = 'Rendering map...';

            // Create the map
            setTimeout(function () { // Otherwise innerHTML doesn't update
                Highcharts.mapChart(container, {
                    chart: {
                        borderWidth: 1,
                        marginRight: 20, // for the legend
                        backgroundColor: 'rgba(212,247,255,0.83)'
                    },

                    title: {
                        text: ''
                    },

                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        floating: true,
                        backgroundColor: ( // theme
                            Highcharts.defaultOptions &&
                            Highcharts.defaultOptions.legend &&
                            Highcharts.defaultOptions.legend.backgroundColor
                        ) || 'rgba(255,242,189,0.85)'
                    },

                    mapNavigation: {
                        enabled: true
                    },

                    colorAxis: {
                        min: 0,
                        max: 500,
                        tickInterval: 100,
                        stops: [
                            [0, '#ddffb7'],
                            [0.01, '#f3005e'],
                            [1, '#500007']
                        ],
                        labels: {
                            format: '{value}'
                        }
                    },

                    plotOptions: {
                        mapline: {
                            showInLegend: false,
                            enableMouseTracking: false
                        }
                    },

                    series: [{
                        mapData: countiesMap,
                        data: data,
                        joinBy: ['hc-key', 'code'],
                        name: 'Covid19 cases',
                        borderWidth: 0,
                        states: {
                            hover: {
                                color: '#a4edba'
                            }
                        },
                        shadow: false
                    }, {
                        type: 'mapline',
                        name: 'State borders',
                        data: borderLines,
                        color: 'black',
                        shadow: false
                    }, {
                        type: 'mapline',
                        name: 'Separator',
                        data: separatorLines,
                        color: 'white',
                        shadow: false
                    }]
                });
            }, 0);
        }
    });
}

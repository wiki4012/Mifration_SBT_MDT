window.onload = function () {
    if (!window.location.hash) {
        window.location = window.location + '#loaded';
        window.location.reload();
    }
    var today = new Date();
    var endDate = new Date(today.getFullYear(), today.getMonth(), 1);
    //endDate.setDate(endDate.getDay() - 30);
    $('input[name="_daterange"]').daterangepicker({
        // singleDatePicker: true,
        autoApply: true,
        maxSpan: {
            days: 31,
        },
        showDropdowns: true,
        minYear: 1901,
        maxYear: parseInt(moment().format("YYYY"), 10),
        startDate: endDate,
        endDate: today,
        maxDate: new Date(),
        locale: {
            format: "MM/DD/YYYY",
        },
    },
        function (start, end, label) {

        }
    );

    selectTechno();

    //On Load Animation
    AOS.init({
        duration: 1200,
    });
};

var externalCred = "&IllumLoginName=ap_cmn_srip&IllumLoginPassword=Pass12345"; //";
var ipAddress = ""; //"http://172.16.156.105:50000";
var contentType = "&IsTesting=T&Content-Type=text%2Fjson";

async function selectTechno() {
    let result = await (await fetch('http://127.0.0.1:8000/task-list')).json();
    console.warn(result);
    var htm = "";
    if (result && result.length > 0) {
        $.each(result, function (i, item) {
            htm +=
                "<option value='" +
                item.team_name +
                "'>" +
                item.team_name +
                "</option>";
        });
        $("#_TECHNOCRATS").append(htm);
        listChart();
    }
}

//   ;

function listChart() {
    // var teamname = decodeURIComponent($.urlParam("teamname"));
    var team;
    team = $("#_TECHNOCRATS").val();
    // if (teamname == null || teamname == "null" || teamname == "null") {
    //     team = $("#_TECHNOCRATS").val();
    // } else {
    //     team = teamname;
    // }
    console.log(team);
    $("#_team").text(team);
    const date = $("#_daterange").val();
    dates = date.split("-");
    const from = moment(dates[0], "MM/DD/YYYY").format("YYYY-MM-DD") + "T00:00:00";
    const to = moment(dates[1], "MM/DD/YYYY").format("YYYY-MM-DD") + "T00:00:00";
    // var fromMon = dates[0].month();
    // var fromYear = from.getFullYear();
    // var fromMon = dates[1].getMonth();
    // var fromMon = to.getFullYear();
    // console.log(fromMon,fromYear,toMon,toYear);
    console.log(from, to);
    Chart.helpers.each(Chart.instances, function (instance) {
        instance.destroy();
    });
    chartList(from, to, team);
}

function nonzerovalues(value) {
    return value !== 0;
}

function chartList(from, to, teamName) {
    // const API = "/XMII/Illuminator?QueryTemplate=SBT_MDT%2FQuery%2FTRIGGER_LOGIC%2FGET_OPERATIONS%2FQRY%2FDAILY_GRAPH_COLOR_CODINGS";
    // //const API = "/XMII/Illuminator?QueryTemplate=Test%2FQRY%2FDaily%2FDAILY_GRAPH_COLOR_CODINGS";
    // const API_URL = ipAddress + API + contentType + externalCred;
    // const Local_URL = "./JS/dummy_data/triggerTarget.json";

    // const params = {
    //     "Param.1": from,
    //     "Param.2": to,
    //     "Param.3": teamName,
    // };

    var charts = [];

    // ajaxCall(
    //     API_URL,
    //     params,
    //     function (result) {
    //         const dataList = result.Rowsets.Rowset ? result.Rowsets.Rowset[0].Row : [];
    //         console.log("ajax-trigger", dataList);
    var fromDt = new Date(from);
    var toDt = new Date(to);
    console.log(fromDt, toDt);
    var fromMon = fromDt.getMonth();
    var fromYear = fromDt.getFullYear();
    var toMon = toDt.getMonth();
    var toYear = toDt.getFullYear();
    console.log(fromMon, fromYear, toMon, toYear);
    $.ajax({
        type: "GET",
        url: 'get-KpiByMonth',
        data: {
            'team': teamName,
            'fromMon': fromMon,
            'toMon': toMon,
            'fromYear': fromYear,
            'toYear': toYear,
        },
        success: function (result) {
            console.log("11", result);

            if (result && result.length > 0) {
                $.each(result, function (i, item) {

                    let index = charts.findIndex((x) => x.graph_id === item.graph_id);
                    if (index > -1) {

                        if (item.flag == 0 && item.kpi_value == 0) {
                            charts[index].barColor.push("rgba(249,249, 26, 1)");
                            charts[index].borderColor.push("rgba(249, 249, 26, 1)");
                        } else if (item.kpi_value > item.lower_limit_w1 && item.upper_limit_w1 > item.kpi_value) {
                            item.barColor.push("rgba(255, 156, 0,1)");
                            item.borderColor.push("rgba(255, 156, 0,1)");
                        }
                        else if (item.kpi_value < item.lower_limit_w1) {
                            item.barColor.push("rgba(255, 0, 0,1)");
                            item.borderColor.push("rgba(255, 0, 0,1)");

                        }
                        else {
                            item.barColor.push("rgba(248, 249, 175,1)");
                            item.borderColor.push("rgba(248, 249, 175,1)");
                        }
                        charts[index].LOWER.push(item.lower_limit_w1);
                        charts[index].UPPER.push(item.upper_limit_w1);

                        if (charts[index].LOWER_LEGEND.length > 0) {
                            charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1] != item.lower_limit_w1 ? charts[index].LOWER_LEGEND.push(item.lower_limit_w1) : "";
                            charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1] != item.upper_limit_w1 ? charts[index].UPPER_LEGEND.push(item.upper_limit_w1) : "";
                        }
                    } else {
                        item.LOWER = [];
                        item.UPPER = [];
                        item.date = [];
                        item.comments = [];
                        item.value = [];

                        item.barColor = [];
                        item.borderColor = [];
                        if (item.flag == 0 && item.kpi_value == 0) {
                            item.barColor.push("rgba(249,249, 26, 1)");
                            item.borderColor.push("rgba(249, 249, 26, 1)");

                        }
                        else if (item.kpi_value > item.lower_limit_w1 && item.upper_limit_w1 > item.kpi_value) {
                            item.barColor.push("rgba(255, 156, 0,1)");
                            item.borderColor.push("rgba(255, 156, 0,1)");
                        }
                        else if (item.kpi_value < item.lower_limit_w1) {
                            item.barColor.push("rgba(255, 0, 0,1)");
                            item.borderColor.push("rgba(255, 0, 0,1)");

                        }
                        else {
                            item.barColor.push("rgba(248, 249, 175,1)");
                            item.borderColor.push("rgba(248, 249, 175,1)");
                        }
                        //    item.barColor.push(item.BACKGROUND);
                        //  item.borderColor.push(item.BORDER);
                        item.LOWER.push(item.lower_limit_w1);
                        item.UPPER.push(item.upper_limit_w1);
                        item.LOWER_LEGEND = [];
                        item.UPPER_LEGEND = [];
                        item.LOWER_LEGEND.push(item.lower_limit_w1);
                        item.UPPER_LEGEND.push(item.upper_limit_w1);
                        // item.LOWER_LEGEND = item.LOWER.filter(function(elem, indxx, self) {
                        //   return indxx === self.indexOf(elem);
                        // })
                        // item.UPPER_LEGEND = item.UPPER.filter(function(elem, indxx, self) {
                        //   return indxx === self.indexOf(elem);
                        // })
                        // charts[index].barColor.push(item.BACKGROUND);
                        // charts[index].borderColor.push(item.BORDER);
                        charts = [...charts, item];
                    }
                });

                console.log("ajax-charts", charts);
            }

            //  const API = "/XMII/Illuminator?QueryTemplate=AP_SBT_MDT%2FTransactionKPI%2Fexdummyselect";
            // // const API = "/XMII/Illuminator?QueryTemplate=Test%2FCOCKPIT_2%2FQRY%2Fexdummyselect";
            //  const API_URL = ipAddress + API + contentType + externalCred;
            //  const Local_URL = "./JS/dummy_data/graphValue.json";
            //  const params = {
            //      "Param.1": from,
            //      "Param.2": to,
            //      "Param.3": teamName,
            //  };
            console.log("paramas", teamName, from, to);
            $.ajax({
                type: "GET",
                url: 'get-KpiDaily',
                data: {
                    'team': teamName,
                    'from': from,
                    'to': to,
                },
                success: function (result) {
                    console.log('result', result);
                    if (result && result.length > 0) {
                        $.each(result, function (i, item) {
                            // if (chartInstances["myChart" + item.GRAPH_ID]) {
                            //   chartInstances["myChart" + item.GRAPH_ID].destroy();
                            // }
                            let index = charts.findIndex((x) => x.graph_id === item.graph_id);
                            if (index > -1) {
                                // console.log('index',  charts[index].barColor)
                                // charts[index].comments.push(item.comments);
                                fDate = item.kpi_date.split('T')
                                fiDate = new Date(fDate[0]);
                                charts[index].date.push(moment(fiDate, "MM/DD/YYYY").format("DD MMM"));
                                console.log("single", item.kpi_date, fiDate);
                                console.log("check", charts[index].date);

                                // charts[index].date.push(moment(item.DATE, "MM/DD/YYYY").format("DD MMM"));
                                //                      
                                if (charts[index].update_freq == "weekcommented" && parseFloat(item.kpi_value) !== 0 && charts[index].unitforyaxis != "%") {
                                    // let weeklycumlative = charts[index].value.reduce(function(a,b) { return a+b; }) + parseFloat(item.VALUE);
                                    if (charts[index].value.filter(nonzerovalues).length > 0) {
                                        let weeklycumlative = parseFloat(item.kpi_value) + parseFloat(charts[index].value.filter(nonzerovalues)[charts[index].value.filter(nonzerovalues).length - 1]);
                                        charts[index].value.push(weeklycumlative);
                                        //  console.log("Cum", weeklycumlative);
                                    } else {
                                        let weeklycumlative = parseFloat(item.kpi_value);
                                        charts[index].value.push(weeklycumlative);
                                        // console.log("Cum", weeklycumlative);
                                    }
                                } else if (charts[index].update_freq == "week" && parseFloat(item.kpi_value) == 0) {
                                    charts[index].value.push(parseFloat(item.kpi_value));
                                } else {
                                    charts[index].value.push(parseFloat(item.kpi_value));
                                }
                                if (charts[index].update_freq == "week") {
                                    charts[index].lower_limit_w1 = charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1];
                                    charts[index].upper_limit_w1 = charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1];
                                }
                                parseFloat(charts[index].lower_limit_w1) ? charts[index].LOWER.push(parseFloat(charts[index].lower_limit_w1)) : "";
                                parseFloat(charts[index].upper_limit_w1) ? charts[index].UPPER.push(parseFloat(charts[index].upper_limit_w1)) : "";
                                // charts[index].barColor.push(charts[index].BACKGROUND);
                                // charts[index].borderColor.push(charts[index].BORDER);
                            } else {
                                item.date = [];
                                item.value = [];
                                item.COMMENTS = [];
                                charts = [...charts, item];
                            }
                        });
                    }

                    //console.log("ajax-charts", charts);
                    if (charts && charts.length > 0) {
                        $.each(charts, function (index, item) {
                            if (index < 20) {
                                const _list = {
                                    title: item.kpi,
                                    labels: item.date,
                                    yAxes: item.unitforyaxis,

                                    dataSets: [{
                                        label: "Trigger-" + item.LOWER_LEGEND,
                                        type: "line",
                                        data: item.LOWER,
                                        borderColor: "#ff3838",
                                        backgroundColor: "#ff3838",
                                        borderWidth: 0.5,
                                        steppedLine: true,
                                        lineTension: 0,
                                        fill: false,
                                        datalabels: {
                                            display: false,
                                        },


                                    },
                                    {
                                        label: "Target-" + item.UPPER_LEGEND,
                                        type: "line",
                                        data: item.UPPER,
                                        borderColor: "#7d5fff",
                                        backgroundColor: "#7d5fff",
                                        borderWidth: 0.5,
                                        steppedLine: true,
                                        lineTension: 0,
                                        fill: false,
                                        datalabels: {
                                            display: false,
                                        },

                                    },
                                    {
                                        label: "Bar",
                                        type: "bar",
                                        data: item.value,
                                        borderColor: item.borderColor, //"#3498db",
                                        backgroundColor: item.barColor, //"#3498db",
                                        borderWidth: 1,
                                        lineTension: 0,
                                        fill: false,
                                        datalabels: {
                                            display: true,
                                        },
                                        labels: item.COMMENTS,
                                    },
                                    ],
                                };
                                if (chartInstances["myChart" + item.graph_id]) {
                                    chartInstances["myChart" + item.graph_id].destroy();
                                }
                                chartInstances["myChart" + item.graph_id] = generateChart("myChart" + item.graph_id, item.is_charter_kpi, _list);
                            }
                        });
                    }
                }
            });
            //  ajaxCall(
            //      API_URL,
            //      params,
            //      function(result) {
            //          const dataList = result.Rowsets.Rowset ? result.Rowsets.Rowset[0].Row : [];
            //          //console.log("ajax-graphValue", charts);

            //          if (dataList && dataList.length > 0) {
            //              $.each(dataList, function(i, item) {
            //                  // if (chartInstances["myChart" + item.GRAPH_ID]) {
            //                  //   chartInstances["myChart" + item.GRAPH_ID].destroy();
            //                  // }
            //                  let index = charts.findIndex((x) => x.GRAPH_ID === item.GRAPH_ID);
            //                  if (index > -1) {
            //                      // console.log('index',  charts[index].barColor)
            //                      charts[index].COMMENTS.push(item.COMMENTS);
            //                      charts[index].date.push(moment(item.DATE, "MM/DD/YYYY").format("DD MMM"));
            //                      if (charts[index].UPDATE_FREQ == "weekcommented" && parseFloat(item.VALUE) !== 0 && charts[index].UNITFORYAXIS != "%") {
            //                          // let weeklycumlative = charts[index].value.reduce(function(a,b) { return a+b; }) + parseFloat(item.VALUE);
            //                          if (charts[index].value.filter(nonzerovalues).length > 0) {
            //                              let weeklycumlative = parseFloat(item.VALUE) + parseFloat(charts[index].value.filter(nonzerovalues)[charts[index].value.filter(nonzerovalues).length - 1]);
            //                              charts[index].value.push(weeklycumlative);
            //                              //  console.log("Cum", weeklycumlative);
            //                          } else {
            //                              let weeklycumlative = parseFloat(item.VALUE);
            //                              charts[index].value.push(weeklycumlative);
            //                              // console.log("Cum", weeklycumlative);
            //                          }
            //                      } else if (charts[index].UPDATE_FREQ == "week" && parseFloat(item.VALUE) == 0) {
            //                          charts[index].value.push(parseFloat(item.VALUE));
            //                      } else {
            //                          charts[index].value.push(parseFloat(item.VALUE));
            //                      }
            //                      if (charts[index].UPDATE_FREQ == "week") {
            //                          charts[index].LOWER_LIMIT = charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1];
            //                          charts[index].UPPER_LIMIT = charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1];
            //                      }
            //                      parseFloat(charts[index].LOWER_LIMIT) ? charts[index].LOWER.push(parseFloat(charts[index].LOWER_LIMIT)) : "";
            //                      parseFloat(charts[index].UPPER_LIMIT) ? charts[index].UPPER.push(parseFloat(charts[index].UPPER_LIMIT)) : "";
            //                      // charts[index].barColor.push(charts[index].BACKGROUND);
            //                      // charts[index].borderColor.push(charts[index].BORDER);
            //                  } else {
            //                      item.date = [];
            //                      item.value = [];
            //                      item.COMMENTS = [];
            //                      charts = [...charts, item];
            //                  }
            //              });
            //          }

            //          //console.log("ajax-charts", charts);
            //          if (charts && charts.length > 0) {
            //              $.each(charts, function(index, item) {
            //                  if (index < 20) {
            //                      const _list = {
            //                          title: item.KPI,
            //                          labels: item.date,
            //                          yAxes: item.UNITFORYAXIS,

            //                          dataSets: [{
            //                                  label: "Trigger-" + item.LOWER_LEGEND,
            //                                  type: "line",
            //                                  data: item.LOWER,
            //                                  borderColor: "#ff3838",
            //                                  backgroundColor: "#ff3838",
            //                                  borderWidth: 0.5,
            //                                  steppedLine: true,
            //                                  lineTension: 0,
            //                                  fill: false,
            //                                  datalabels: {
            //                                      display: false,
            //                                  },


            //                              },
            //                              {
            //                                  label: "Target-" + item.UPPER_LEGEND,
            //                                  type: "line",
            //                                  data: item.UPPER,
            //                                  borderColor: "#7d5fff",
            //                                  backgroundColor: "#7d5fff",
            //                                  borderWidth: 0.5,
            //                                  steppedLine: true,
            //                                  lineTension: 0,
            //                                  fill: false,
            //                                  datalabels: {
            //                                      display: false,
            //                                  },

            //                              },
            //                              {
            //                                  label: "Bar",
            //                                  type: "bar",
            //                                  data: item.value,
            //                                  borderColor: item.borderColor, //"#3498db",
            //                                  backgroundColor: item.barColor, //"#3498db",
            //                                  borderWidth: 1,
            //                                  lineTension: 0,
            //                                  fill: false,
            //                                  datalabels: {
            //                                      display: true,
            //                                  },
            //                                  labels: item.COMMENTS,
            //                              },
            //                          ],
            //                      };
            //                      if (chartInstances["myChart" + item.GRAPH_ID]) {
            //                          chartInstances["myChart" + item.GRAPH_ID].destroy();
            //                      }
            //                      chartInstances["myChart" + item.GRAPH_ID] = generateChart("myChart" + item.GRAPH_ID, item.IS_CHARTER_KPI, _list);
            //                  } 
            //              });
            //          }
            //      },
            //      function(err) {
            //          console.log("err", err);
            //      }
            //  );
        },
        function(err) {
            console.log("err", err);
        }
    }
    );
}

function getColorName(index) {
    const bgColor = ["#DA218E", "#DA4121", "#61DA21", "#CCDA21", "#21DAB3", "#215FDA", "#8321DA", "#66621E", "#D6D46D", "#82C4F9"];
    const col = index % 10;
    return bgColor[col];
}

let chartInstances = {};

function generateChart(id, charter, list) {
    //  console.log(list);
    const tooltip = {

        callbacks: {

            label: function (context) {
                console.log(context)
                return "Reason : " + context.dataset.labels[context.dataIndex]
            }
        }

    };
    // Note: changes to the plugin code is not reflected to the chart, because the plugin is loaded at chart construction time and editor changes only trigger an chart.update().
    const image = new Image();
    image.src = "/XMII/CM/AP_SBT_MDT/CMN/charter1.png";
    const plugin = {
        id: 'custom_canvas_background_image',
        beforeDraw: (chart) => {
            if (chart.config.options.canvas.backgroundImage) {
                const ctx = chart.ctx;
                const { top, left, width, height } = chart.chartArea;
                ctx.drawImage(image, 0, 0);
                ctx.restore();
            } else {
                image.onload = () => chart.draw();
            }
        }
    };
    const config = {
        type: 'bar',
        //lable: _.dataSets,
        data: {
            labels: list.labels,
            datasets: list.dataSets,
            //COMMENTS: list.COMMENTS,
        },
        plugins: [ChartDataLabels, plugin],
        options: {
            canvas: {
                backgroundImage: (charter == 'true') ? "url('/XMII/CM/AP_SBT_MDT/V3/CMN/charter1.png')" : "",
            },
            plugins: {

                tooltip,
                datalabels: {
                    backgroundColor: function (context) {
                        return context.dataset.backgroundColor;
                    },
                    borderRadius: 4,
                    color: "#0d0d0d",
                    padding: 2,
                    font: {
                        size: 14,
                    },
                },
                legend: {
                    display: true,
                    position: "top",
                    labels: {
                        boxWidth: 8,
                        // fontColor: "black",
                        fontSize: 12,
                        padding: 2,
                    },
                },
                title: {
                    display: true,
                    text: list.title,
                    fontSize: 26,
                    padding: 2,
                    // fontColor: "black",
                },
            },
            scales: {
            },
            responsive: true,
        }
    };
    var canvas = document.getElementById(id);
    var chartInstance = new Chart(canvas, config);


}

function viewList(id) {
    // console.log('sdf')
    // const no = id;
    $("#_myChart" + id).toggleClass("active");
}

function slideChange(id) {
    // console.log('sdf', id)
    document.querySelectorAll("._type").forEach(function (element, index) {
        element.classList.remove("active");
    });
    $("#_myChart" + id).addClass("active");
}

function ajaxCall(url, params, callback, error) {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        data: { ...params },
        success: callback,
        error: error,
    });
}
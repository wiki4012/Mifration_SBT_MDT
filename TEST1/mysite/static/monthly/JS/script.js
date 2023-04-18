window.onload = function () {
    selectTechno();

    //On Load Animation
    AOS.init({
        duration: 1200,
    });
};

var externalCred = "&IllumLoginName=atos_mii&IllumLoginPassword=Pass01";
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
    }
}


function listChart(data) {
    const team = data.value;
    $("#_team").text(team);
    Chart.helpers.each(Chart.instances, function (instance) {
        instance.destroy();
    });
    chartList(team);
}

setInterval(function () {
    const team = $("#_TECHNOCRATS").val();
    $("#_team").text(team);
    chartList(team);
}, 120000);

function star() {
    console.log("-----------------tttttttttttttteeeeeeeeeeeaaaaaaaaaam" + teamName);
    starUpload(teamName);
}

function chartList(teamName) {
    // const API =
    //     "/XMII/Illuminator?QueryTemplate=SBT_MDT%2FQuery%2FTRIGGER_LOGIC%2FGET_OPERATIONS%2FQRY%2FSELECT_MONTHLY_TRIGGER_TARGET_V1";
    // const API_URL = ipAddress + API + contentType + externalCred;
    // const Local_URL = "./JS/dummy_data/triggerTarget.json";

    // const params = {
    //     "Param.1": teamName,
    // };

    var charts = [];

    $.ajax({
        type: "GET",
        url: 'get-KpiMonthlyKpi',
        data: {
            'team': teamName,
        },
        success: function (result) {
            console.log(result);
            if (result && result.length > 0) {
                $.each(result, function (i, item) {
                    var toDt = new Date(item.kpi_date);
                    var ttMon = toDt.getMonth();
                    var ttYear = toDt.getFullYear();
                    // console.log(fromMon,fromYear);
                    $.ajax({

                        type: "GET",
                        url: 'get-TTMonthlyKpi',
                        data: {
                            'team': teamName,
                            'graphId': item.graph_id,
                            'ttMon': ttMon,
                            'ttYear': ttYear,
                        },
                        success: function (result1) {
                            if (result1 && result1.length > 0) {
                                $.each(result1, function (i, item) {
                                    console.log("inner",result1);
                                    let index = charts.findIndex((x) => x.graph_id === item.graph_id);
                                    item.LOWER = [];
                                        item.UPPER = [];
                                        item.LOWER = [];
                                        item.date = [];
                                        item.value = [];
                                        item.barColor = [];
                                        item.borderColor = [];
                                        item.LOWER.push(item.lower_limit_w2);
                                        item.UPPER.push(item.upper_limit_w2);
                                        item.LOWER_LEGEND = [];
                                        item.UPPER_LEGEND = [];
                                        item.LOWER_LEGEND.push(item.lower_limit_w2);
                                        item.UPPER_LEGEND.push(item.upper_limit_w2);
                                        charts = [...charts, item];
                                    if (index > -1) {
                                        console.log(index);
                                        charts[index].LOWER.push(item.lower_limit_w2);
                                        charts[index].UPPER.push(item.upper_limit_w2);
                                        if (charts[index].LOWER_LEGEND.length > 0) {
                                            ((charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1] != item.lower_limit_w2) ? charts[index].LOWER_LEGEND.push(item.lower_limit_w2) : '');
                                            ((charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1] != item.upper_limit_w2) ? charts[index].UPPER_LEGEND.push(item.upper_limit_w2) : '');
                                        }
                                    }
                                    //  else {
                                    //     item.LOWER = [];
                                    //     item.UPPER = [];
                                    //     item.LOWER = [];
                                    //     item.date = [];
                                    //     item.value = [];
                                    //     item.barColor = [];
                                    //     item.borderColor = [];
                                    //     item.LOWER.push(item.lower_limit_w2);
                                    //     item.UPPER.push(item.upper_limit_w2);
                                    //     item.LOWER_LEGEND = [];
                                    //     item.UPPER_LEGEND = [];
                                    //     item.LOWER_LEGEND.push(item.lower_limit_w2);
                                    //     item.UPPER_LEGEND.push(item.upper_limit_w2);
                                    //     charts = [...charts, item];
                                    // }
                                    console.log(item.kpi_value + "-----" + item.upper_limit_w2);
                                    // console.log("inner", result);


                                });
                                console.log("result1",result1);
                            }
                        }
                        // let index = charts.findIndex((x) => x.graph_id === item.graph_id);
                        // if (index > -1) {
                        //     charts[index].LOWER.push(item.lower_limit_w2);
                        //     charts[index].UPPER.push(item.upper_limit_w2);
                        //     if (charts[index].LOWER_LEGEND.length > 0) {
                        //         ((charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1] != item.lower_limit_w2) ? charts[index].LOWER_LEGEND.push(item.lower_limit_w2) : '');
                        //         ((charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1] != item.upper_limit_w2) ? charts[index].UPPER_LEGEND.push(item.upper_limit_w2) : '');
                        //     }
                        // } else {
                        //     item.LOWER = [];
                        //     item.UPPER = [];
                        //     item.LOWER = [];
                        //     item.date = [];
                        //     item.value = [];
                        //     item.barColor = [];
                        //     item.borderColor = [];
                        //     item.LOWER.push(item.lower_limit_w2);
                        //     item.UPPER.push(item.upper_limit_w2);
                        //     item.LOWER_LEGEND = [];
                        //     item.UPPER_LEGEND = [];
                        //     item.LOWER_LEGEND.push(item.lower_limit_w2);
                        //     item.UPPER_LEGEND.push(item.upper_limit_w2);
                        //     charts = [...charts, item];
                        // }
                        // console.log(item.kpi_value + "-----" + item.upper_limit_w2);

                    });
                    console.log("ajax-charts", charts);

                    if (result && result.length > 0) {
                        $.each(result, function (i, item) {
                            let index = charts.findIndex((x) => parseInt(x.graph_id) === parseInt(item.graph_id));
                            if (index > -1) {
                                // console.log('index',  charts[index].barColor)
                                // charts[index].date.push(
                                //   moment(item.DATE, "MM/DD/YYYY").format("DD MMM")
                                // );
                                charts[index].date.push(
                                    monthsList(ttMon) + "," + ttYear
                                );
                                charts[index].value.push(item.kpi_value);
                                // charts[index].LOWER_LIMIT
                                //   ? charts[index].LOWER.push(charts[index].LOWER_LIMIT)
                                //   : "";
                                charts[index].upper_limit_w2 ?
                                    charts[index].UPPER.push(charts[index].upper_limit_w2) :
                                    "";
                                if (parseFloat(charts[index].lower_limit_w2) > parseFloat(charts[index].upper_limit_w2)) {
                                    const colorCode =
                                        item.kpi_value > parseFloat(item.upper_limit_w2) ?
                                            "rgba(179, 57, 57, 0.2)" :
                                            "rgba(33, 140, 116,0.2)";
                                    charts[index].barColor ?
                                        charts[index].barColor.push(colorCode) :
                                        "";
                                    const bordercode =
                                        item.kpi_value > parseFloat(item.upper_limit_w2) ?
                                            "rgba(179, 57, 57, 1)" :
                                            "rgba(33, 140, 116,1)";
                                    charts[index].barColor ?
                                        charts[index].borderColor.push(bordercode) :
                                        "";
                                } else {
                                    const colorCode =
                                        item.kpi_value < parseFloat(item.upper_limit_w2) ?
                                            "rgba(179, 57, 57, 0.2)" :
                                            "rgba(33, 140, 116,0.2)";
                                    charts[index].barColor ?
                                        charts[index].barColor.push(colorCode) :
                                        "";
                                    const bordercode =
                                        item.kpi_value < parseFloat(item.upper_limit_w2) ?
                                            "rgba(179, 57, 57, 1)" :
                                            "rgba(33, 140, 116,1)";
                                    charts[index].barColor ?
                                        charts[index].borderColor.push(bordercode) :
                                        "";
                                }

                            } else {
                                item.date = [];
                                item.value = [];
                                item.date.push(
                                    monthsList(ttMon) + "," + ttYear
                                );
                                item.value.push(parseFloat(item.kpi_value));

                                charts = [...charts, item];
                            }
                        });
                        console.log("Abby", charts);
                    }


                    if (charts && charts.length > 0) {
                        $.each(charts, function (index, item) {
                            if (index < 20) {
                                const _list = {
                                    title: item.KPI,
                                    labels: item.date,
                                    yAxes: item.UNITFORYAXIS,
                                    dataSets: [

                                        {
                                            label: "Target-" + item.UPPER_LEGEND,
                                            type: "line",
                                            data: item.UPPER,
                                            borderColor: "#7d5fff",
                                            backgroundColor: "#7d5fff",
                                            borderWidth: 0.5,
                                            lineTension: 0,
                                            steppedLine: true,
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
                                        },
                                    ],
                                };
                                if (chartInstances["myChart" + item.GRAPH_ID]) {
                                    chartInstances["myChart" + item.GRAPH_ID].destroy();
                                }
                                chartInstances["myChart" + item.GRAPH_ID] = generateChart(
                                    "myChart" + item.GRAPH_ID,
                                    _list
                                );
                            }
                        });
                    }
                });
            }

        }
    });
}
// ajaxCall(
//     API_URL,
//     params,
//     function (result) {
//         const dataList = result.Rowsets.Rowset ?
//             result.Rowsets.Rowset[0].Row : [];
//         // console.log("ajax-trigger", dataList);
//         if (dataList && dataList.length > 0) {
//             $.each(dataList, function (i, item) {
//                 let index = charts.findIndex((x) => x.GRAPH_ID === item.GRAPH_ID);
//                 if (index > -1) {
//                     charts[index].LOWER.push(item.LOWER_LIMIT);
//                     charts[index].UPPER.push(item.UPPER_LIMIT);
//                     if (charts[index].LOWER_LEGEND.length > 0) {
//                         ((charts[index].LOWER_LEGEND[charts[index].LOWER_LEGEND.length - 1] != item.LOWER_LIMIT) ? charts[index].LOWER_LEGEND.push(item.LOWER_LIMIT) : '');
//                         ((charts[index].UPPER_LEGEND[charts[index].UPPER_LEGEND.length - 1] != item.UPPER_LIMIT) ? charts[index].UPPER_LEGEND.push(item.UPPER_LIMIT) : '');
//                     }
//                 } else {
//                     item.LOWER = [];
//                     item.UPPER = [];
//                     item.LOWER = [];
//                     item.date = [];
//                     item.value = [];
//                     item.barColor = [];
//                     item.borderColor = [];
//                     item.LOWER.push(item.LOWER_LIMIT);
//                     item.UPPER.push(item.UPPER_LIMIT);
//                     item.LOWER_LEGEND = [];
//                     item.UPPER_LEGEND = [];
//                     item.LOWER_LEGEND.push(item.LOWER_LIMIT);
//                     item.UPPER_LEGEND.push(item.UPPER_LIMIT);
//                     charts = [...charts, item];
//                 }
//                 console.log(item.VALUE + "-----" + item.UPPER_LIMIT);

//             });
//             console.log("ajax-charts", charts);
//         }
//         if (dataList && dataList.length > 0) {
//             $.each(dataList, function (i, item) {
//                 let index = charts.findIndex((x) => parseInt(x.GRAPH_ID) === parseInt(item.GRAPH_ID));
//                 if (index > -1) {
//                     // console.log('index',  charts[index].barColor)
//                     // charts[index].date.push(
//                     //   moment(item.DATE, "MM/DD/YYYY").format("DD MMM")
//                     // );
//                     charts[index].date.push(
//                         monthsList(item.MONTH_VAL) + "," + item.YEAR_VAL
//                     );
//                     charts[index].value.push(item.VALUE);
//                     // charts[index].LOWER_LIMIT
//                     //   ? charts[index].LOWER.push(charts[index].LOWER_LIMIT)
//                     //   : "";
//                     charts[index].UPPER_LIMIT ?
//                         charts[index].UPPER.push(charts[index].UPPER_LIMIT) :
//                         "";
//                     if (parseFloat(charts[index].LOWER_LIMIT) > parseFloat(charts[index].UPPER_LIMIT)) {
//                         const colorCode =
//                             item.VALUE > parseFloat(item.UPPER_LIMIT) ?
//                                 "rgba(179, 57, 57, 0.2)" :
//                                 "rgba(33, 140, 116,0.2)";
//                         charts[index].barColor ?
//                             charts[index].barColor.push(colorCode) :
//                             "";
//                         const bordercode =
//                             item.VALUE > parseFloat(item.UPPER_LIMIT) ?
//                                 "rgba(179, 57, 57, 1)" :
//                                 "rgba(33, 140, 116,1)";
//                         charts[index].barColor ?
//                             charts[index].borderColor.push(bordercode) :
//                             "";
//                     } else {
//                         const colorCode =
//                             item.VALUE < parseFloat(item.UPPER_LIMIT) ?
//                                 "rgba(179, 57, 57, 0.2)" :
//                                 "rgba(33, 140, 116,0.2)";
//                         charts[index].barColor ?
//                             charts[index].barColor.push(colorCode) :
//                             "";
//                         const bordercode =
//                             item.VALUE < parseFloat(item.UPPER_LIMIT) ?
//                                 "rgba(179, 57, 57, 1)" :
//                                 "rgba(33, 140, 116,1)";
//                         charts[index].barColor ?
//                             charts[index].borderColor.push(bordercode) :
//                             "";
//                     }

//                 } else {
//                     item.date = [];
//                     item.value = [];
//                     item.date.push(
//                         monthsList(item.MONTH_VAL) + "," + item.YEAR_VAL
//                     );
//                     item.value.push(parseFloat(item.VALUE));

//                     charts = [...charts, item];
//                 }
//             });
//             console.log("Abby", charts);
//         }


//         if (charts && charts.length > 0) {
//             $.each(charts, function (index, item) {
//                 if (index < 20) {
//                     const _list = {
//                         title: item.KPI,
//                         labels: item.date,
//                         yAxes: item.UNITFORYAXIS,
//                         dataSets: [
//                             // {
//                             //   label: "Trigger-" + Math.round(item.LOWER_LEGEND),
//                             //   type: "line",
//                             //   data: item.LOWER,
//                             //   borderColor: "#DA4121",
//                             //   backgroundColor: "#DA4121",
//                             //   borderWidth: 1,
//                             //   lineTension: 0,
//                             //   fill: false,
//                             //   datalabels: {
//                             //     display: false,
//                             //   },
//                             // },
//                             {
//                                 label: "Target-" + item.UPPER_LEGEND,
//                                 type: "line",
//                                 data: item.UPPER,
//                                 borderColor: "#7d5fff",
//                                 backgroundColor: "#7d5fff",
//                                 borderWidth: 0.5,
//                                 lineTension: 0,
//                                 steppedLine: true,
//                                 fill: false,
//                                 datalabels: {
//                                     display: false,
//                                 },
//                             },
//                             {
//                                 label: "Bar",
//                                 type: "bar",
//                                 data: item.value,
//                                 borderColor: item.borderColor, //"#3498db",
//                                 backgroundColor: item.barColor, //"#3498db",
//                                 borderWidth: 1,
//                                 lineTension: 0,
//                                 fill: false,
//                             },
//                         ],
//                     };
//                     if (chartInstances["myChart" + item.GRAPH_ID]) {
//                         chartInstances["myChart" + item.GRAPH_ID].destroy();
//                     }
//                     chartInstances["myChart" + item.GRAPH_ID] = generateChart(
//                         "myChart" + item.GRAPH_ID,
//                         _list
//                     );
//                 }
//             });
//         }
//     },
//     function (err) {
//         console.log("err", err);
//     }
// );



function monthsList(val) {
    var months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ];
    return months[val - 1];
}

function getColorName(index) {
    const bgColor = [
        "#DA218E",
        "#DA4121",
        "#61DA21",
        "#CCDA21",
        "#21DAB3",
        "#215FDA",
        "#8321DA",
        "#66621E",
        "#D6D46D",
        "#82C4F9",
    ];
    const col = index % 10;
    return bgColor[col];
}

let chartInstances = {};

function generateChart(id, list) {
    // var grapView = [];
    // $.each(list.dataSets, function (index, value) {
    //   grapView.push({
    //     type: value.type,
    //     label: value.label,
    //     data: value.data,
    //     lineTension: 0,
    //     fill: false,
    //     borderColor: getColorName(index),
    //     backgroundColor: getColorName(index),
    //     borderWidth: 1,
    //   });
    // });
    var canvas = document.getElementById(id);
    Chart.defaults.global.defaultFontStyle = "bold";
    // Chart.defaults.global.plugins.datalabels
    var chartInstance = new Chart(canvas, {
        type: "bar",
        data: {
            labels: list.labels,
            datasets: list.dataSets,
        },
        options: {
            plugins: {
                datalabels: {
                    display: true,
                    // opacity:0,
                    // anchor: 'end',
                    // align: 'top',
                    backgroundColor: function (context) {
                        // console.log('s', context)
                        return context.dataset.backgroundColor;
                    },
                    borderRadius: 4,
                    color: "#0d0d0d",
                    padding: 2,
                    //  formatter: Math.round,
                    font: {
                        // weight: "bolder",
                        size: 20,
                    },
                },
            },
            legend: {
                display: true,
                position: "top",
                labels: {
                    // usePointStyle: true,          
                    boxWidth: 8,
                    // fontColor: "black",
                    fontSize: 16,
                    padding: 2,
                },
            },
            title: {
                display: true,
                text: list.title,
                fontSize: 25,
                padding: 2,
                // fontColor: "black",
            },
            scales: {
                xAxes: [{
                    ticks: {
                        fontSize: 16,
                    },
                },],
                yAxes: [{
                    position: "left",
                    ticks: {
                        beginAtZero: true,
                        // stepSize: 80,
                        fontSize: 16,
                    },
                    scaleLabel: {
                        display: true,
                        labelString: list.yAxes,
                    },
                },],
            },
            responsive: true,
        },
    });
    return chartInstance;
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



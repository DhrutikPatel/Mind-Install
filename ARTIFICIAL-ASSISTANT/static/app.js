$(document).ready(function () {
    json_drpdwn_data('Symptom');
    function json_drpdwn_data(id) {
        var html_code = '';
        $.getJSON('Symptom-severity.json', function (data) {
            html_code += '<option> Select ' + id + '</option>';
            $.each(data, function (key, value) {
                if (id == 'Symptom') {
                    html_code += '<option value="+' + value.Symptom + '">' + value.Symptom + '</option>';
                }
                $('#dp1').html(html_code);
                $('#dp2').html(html_code);
                $('#dp3').html(html_code);
            })
        })
    }

    var url = "https://api.covid19india.org/data.json"

    $.getJSON(url, function (data) {

        var total_active, total_recovered, total_deaths, total_confirmed

        var state = []
        var confirmed = []
        var recovered = []
        var deaths = []

        $.each(data.statewise, function (id, obj) {
            state.push(obj.state)
            confirmed.push(obj.confirmed)
            recovered.push(obj.recovered)
            deaths.push(obj.deaths)
        })

        state.shift()
        confirmed.shift()
        recovered.shift();
        deaths.shift()

        total_active = data.statewise[0].active
        total_confirmed = data.statewise[0].confirmed
        total_recovered = data.statewise[0].recovered
        total_deaths = data.statewise[0].deaths

        $("#active").append(total_active)
        $("#confirmed").append(total_confirmed)
        $("#recovered").append(total_recovered)
        $("#deaths").append(total_deaths)

        var myChart = document.getElementById("myChart").getContext('2d')

        var chart = new Chart(myChart, {
            type: 'line',
            data: {
                labels: state,
                datasets: [
                    {
                        label: "Confirmed Cases",
                        data: confirmed,
                        backgroundColor: "#f1c40f",
                        minBarLength: 100
                    },
                    {
                        label: "Recovered Cases",
                        data: recovered,
                        backgroundColor: "#2ecc71",
                        minBarLength: 100
                    },
                    {
                        label: "Deceased",
                        data: deaths,
                        backgroundColor: "#e74c3c",
                        minBarLength: 100
                    },
                ]
            },
            options: {}
        })

    })
})

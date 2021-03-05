var sells = document.getElementById('sells-chart');
if(sells){
    let sells_url = sells.getAttribute("data-url");
    let sells_context = sells.getContext('2d');
    fetch(sells_url)
        .then(res => res.json())
        .then(res => {
            var chart = new Chart(sells_context, {
                type: 'line',
                data: {
                    labels: res.dates,
                    datasets: [{
                        label: 'Monthly Sells',
                        backgroundColor: '#49B6FF',
                        borderColor: '#49B6FF',
                        borderColor: '#fff',
                        pointBackgroundColor: '#fff',
                        pointRadius: 0,
                        data: res.sells
                    }]
                },
    
                // Configuration options go here
                options: {
                    maintainAspectRatio: false,
                    responsive: true,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                },
            });
        })
}


var income_expense = document.getElementById('money-flow-chart');
if (income_expense) {
    var income_expense_context = income_expense.getContext('2d');
    let money_flow_url = document.getElementById('money-flow-chart').getAttribute("data-url");
    fetch(money_flow_url)
        .then(res => res.json())
        .then(res => {
            var myChart = new Chart(income_expense_context, {
                type: 'line',
                data: {
                    labels: res.dates,
                    datasets: [{
                            label: 'Expense',
                            data: res.expense,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            fill: false,
                        },
                        {
                            label: 'Income',
                            data: res.income,
                            borderColor: 'green',
                            fill: false,
                        }
                    ],
                },
                options: {
                    maintainAspectRatio: false,
                    responsive: true,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                },
            });

        })
}
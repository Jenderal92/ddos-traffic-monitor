function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById('data-table');
            table.innerHTML = "";

            data.forEach(item => {
                const row = `<tr>
                                <td>${item.ip}</td>
                                <td>${item.count}</td>
                             </tr>`;
                table.innerHTML += row;
            });
        });
}

setInterval(fetchData, 2000); 
fetchData();

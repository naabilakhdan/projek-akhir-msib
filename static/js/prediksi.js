const prediksi = document.querySelector(".prediksi1")
const tahun = document.getElementById('tahun')
const bulan = document.getElementById('bulan')
const hari = document.getElementById('hari')
const jam = document.getElementById('jam')
const result = document.getElementById('result')

prediksi.addEventListener("submit", event => {
    event.preventDefault();

    const predT = tahun.value;
    const predB = bulan.value;
    const predH = hari.value;
    const predJ = jam.value;
    getPrediksi(predT, predB, predH, predJ)

})

function getPrediksi(year, month, day, hours) {
    $.get("/result", {
        tahun: year,
        bulan: month,
        hari: day,
        jam: hours,
    }).done(function (data) {
        console.log(data);
        addResult(data)
    })
}

function addResult(tinggi) {
    const getResult = `<p style="font-family: Source Code Pro, monospace; font-size: 16px; margin-left: 230px;"> Tinggi pasang surut yang diprediksi: <span style="text-align: center; border-radius: 0.25rem; background: #eeeeee; color: rgb(9, 171, 59);"> ${tinggi} </p> </span>`
    console.log(result.innerHTML)
    result.insertAdjacentHTML('beforeend', getResult)
    setInterval(() => {
        detik()
    }, 10000);

}

function detik() {
    location.reload()
}
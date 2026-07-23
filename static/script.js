document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("resultForm");

    if (form) {

        form.addEventListener("submit", function (e) {

            e.preventDefault();

            const name = document.querySelector('input[name="name"]').value.trim();
            const seat = document.querySelector('input[name="seat"]').value.trim();
            const section = document.querySelector('select[name="section"]').value;

            if (name === "" || seat === "" || section === "") {
                alert("من فضلك أكمل جميع البيانات.");
                return;
            }

            document.getElementById("loading").style.display = "flex";

            setTimeout(function () {
                form.submit();
            }, 2000);

        });

    }

});


$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var qobj = this.parentNode.children[2];
    console.log("pid = ", id);

    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log("data = ", data);
            qobj.innerText = data.quantity
            document.getElementById("amount").innerText = "Rs. " + data.amount.toFixed(1)
            document.getElementById("totalamount").innerHTML = "<strong>Rs. " + data.totalamount.toFixed(1) + "</strong>"
        }
    })
});


$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var qobj = this.parentNode.children[2];
    console.log(qobj);
    console.log("pid = ", id);
    if (qobj.innerText > 1) {
        $.ajax({
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log("data = ", data);
                qobj.innerText = data.quantity
                document.getElementById("amount").innerText = "Rs. " + data.amount.toFixed(1)
                document.getElementById("totalamount").innerHTML = "<strong>Rs. " + data.totalamount.toFixed(1) + "</strong>"
            }
        })
    }
    else {
        var alertBox = '<div class="alert" style="background-color: rgb(250, 250, 151); color: black; border: 1px solid rgb(246, 241, 52);"><span class="closebtn" style="cursor: pointer; font-weight: bold; float: right;" onclick="this.parentElement.style.display=\'none\';">&times;</span> <strong>Warning!</strong> Only 1 item of the Product is present in Cart!</div>';

        $('#alert-box').html(alertBox);

    }
});



$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var qobj = this;
    console.log("pid = ", id);

    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            qobj.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
});

$('.plus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            window.location.href = `http://127.0.0.1:8000/product-details/${id}`
        }
    })
})

$('.minus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            window.location.href = `http://127.0.0.1:8000/product-details/${id}`
        }
    })
})
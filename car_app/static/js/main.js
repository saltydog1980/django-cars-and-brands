//Setting axios defaults to handle the csrftoken
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

//Function to grab brand data and submit it
function brandNew(event) {
    event.preventDefault()
    const car_brand_name = document.getElementById("car-brand-name").value;
    const car_brand_country = document.getElementById("car-brand-country").value;
    const car_brand_date = document.getElementById("car-brand-date").value;

    //building my form data for Post request
    const data = new FormData();
    data.append("car_brand_name", car_brand_name);
    data.append("car_brand_country", car_brand_country);
    data.append("car_brand_date", car_brand_date);

    //actual post and .then
    axios.post('new', data).then((response) => {
        //alerting user of status and then re-directing to home page
        alert(response['data']['status']);
        window.location.href = '/';
    });
};

//Function to grab brand data and submit it
function brandUpdate(event, id) {
    event.preventDefault()
    const car_brand_name = document.getElementById("car-brand-name").value;
    const car_brand_country = document.getElementById("car-brand-country").value;
    const car_brand_date = document.getElementById("car-brand-date").value;

    //building my form data for Post request
    const data = new FormData();
    data.append("car_brand_name", car_brand_name);
    data.append("car_brand_country", car_brand_country);
    data.append("car_brand_date", car_brand_date);

    //actual post and .then
    axios.post('edit', data).then((response) => {
        //alerting user of status and then re-directing to home page
        alert(response['data']['status']);
        window.location.href = '/';
    });
};


function submitNewCar(event) {
    event.preventDefault()
    const car_model_name = document.getElementById("car-model-name").value;
    const car_model_country = document.getElementById("car-model-country").value;
    const car_model_date = document.getElementById("car-model-date").value;
    const car_model_price = document.getElementById("car-model-price").value;
    const ele = document.getElementsByTagName('input');
    const elemsList = [] 
    for(i = 0; i < ele.length; i++) {
        if(ele[i].type="radio") {
            if(ele[i].checked){
                elemsList.push(ele[i].value)
            }
        }
    }
    // console.log(elemsList)
    //building my form data for Post request
    const data = new FormData();
    data.append("car_model_name", car_model_name);
    data.append("car_model_country", car_model_country);
    data.append("car_model_date", car_model_date);
    data.append("car_model_price", car_model_price);
    data.append("car_model_options", elemsList);
    // console.log(data)
    //actual post and .then
    axios.post('new', data).then((response) => {
        //alerting user of status and then re-directing to home page
        alert(response['data']['status']);
        window.location.href = '/';
    });


}

function updateCar(event) {
    event.preventDefault()
    const car_model_name = document.getElementById("car-model-name").value;
    const car_model_country = document.getElementById("car-model-country").value;
    const car_model_date = document.getElementById("car-model-date").value;
    const car_model_price = document.getElementById("car-model-price").value;
    const ele = document.getElementsByTagName('input');
    const elemsList = [] 
    for(i = 0; i < ele.length; i++) {
        if(ele[i].type="radio") {
            if(ele[i].checked){
                elemsList.push(ele[i].value)
            }
        }
    }

    //building my form data for Post request
    const data = new FormData();
    data.append("car_model_name", car_model_name);
    data.append("car_model_country", car_model_country);
    data.append("car_model_date", car_model_date);
    data.append("car_model_price", car_model_price);
    data.append("car_model_options", elemsList);

    //actual post and .then
    axios.post('edit', data).then((response) => {
        //alerting user of status and then re-directing to home page
        alert(response['data']['status']);
        window.location.href = '/';
    });


}
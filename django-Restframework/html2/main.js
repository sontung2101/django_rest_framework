var BASE_URL ="http://localhost:8000/app";
function get(uri){
    var url = BASE_URL + uri;
    return fetch(url,{headers:{Authorization:'Bearer '+ localStorage.getItem('token')}}
        );

}

function post(uri,formData){
    var url = BASE_URL + uri;
    return post_url(url,formData);
}
function post_url(url,formData){
        return fetch(url,{
        method:'POST',
        body:formData,
        headers:{Authorization:'Bearer '+ localStorage.getItem('token')},
    },
    )
}


function put(uri,formData){
    var url = BASE_URL + uri;
    return fetch(url,{
        method:'PUT',
        body:formData,
        headers:{Authorization:'Bearer '+ localStorage.getItem('token')},
    }) 
}

function delete_(uri){
    var url = BASE_URL + uri;
    return fetch(url,{method:'DELETE', headers:{Authorization:'Bearer '+ localStorage.getItem('token')},})
}
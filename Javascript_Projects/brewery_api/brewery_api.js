

let apiURL = `https://api.openbrewerydb.org/v1/breweries`; //base brewery api
let options = `?by_city=boston&per_page=5`; //options to be appended to apiURL. Will be made dynamic later.

function generateURL(url,options){ //combine the base url for the api with its options, and return the result
    let returnURL = url + options;
    return returnURL;
};

function findBreweries(url){
    const container = document.getElementById("container"); //grab container from html
    
    fetch(url) //fetch data from the url provided (the api)
        .then(response => { //check network response, if bad, throw error, if good return response json
            if (!response.ok){
                throw new Error('Bad network response');
            }
            return response.json();
        })
        .then(data => { //using the data from the response.json, create a text paragraph element, and append it as a
                        //child to container
            data.forEach((item) => {
                const brewName = document.createElement('p');
                brewName.textContent=item.name;
                container.appendChild(brewName);

            })
        })
        .catch(error => { //if there are any undefined errors, catch them and print the error
            console.error("Error in Fetch: ",error);
        })
    };

let submissionURL = generateURL(apiURL,options); //generate the desired url
findBreweries(submissionURL); //run the function, using the combined url generated above
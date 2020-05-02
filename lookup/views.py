from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    global category_description
    global category_color

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=25&API_KEY=B76B4EBE-5790-472D-9269-F2A69071F8A6")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error......"
        if   api[0]['Category']['Name'] == "Good":
                category_description="(0-50) air quality is considered satisfactory"
                category_color="good"
        elif api[0]['Category']['Name'] == "Moderate": 
                category_description="(51-100) air quality is acceptable"
                category_color="Moderate" 
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description="(101-150) although general public will not get harm but people with lung disease or old people will be at higher risk"
                category_color="UnhealthyforSensitiveGroups" 
        elif api[0]['Category']['Name'] == "Unhealthy":
                category_description="(151-200) people will start feeling health effects"
                category_color="Unhealthy" 
        elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description="(201-300) health alert"
                category_color="VeryUnhealthy"  
        elif api[0]['Category']['Name'] == "Hazardous":
                category_description="(301-500) health warning of emergency conditions" 
                category_color="Hazardous"
        

        return render( request, 'home.html', {
            'api':api, 
            'category_description' : category_description,
            'category_color': category_color
            })
        
    else:    
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89121&distance=25&API_KEY=B76B4EBE-5790-472D-9269-F2A69071F8A6")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error......"
        if   api[0]['Category']['Name'] == "good":
                category_description="(51-100) air quality is acceptable"
                category_color="good"
        elif api[0]['Category']['Name'] == "Moderate": 
                category_description="(51-100) air quality is acceptable"
                category_color="Moderate" 
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description="(101-150) although general public will not get harm but people with lung disease or old people will be at higher risk"
                category_color="UnhealthyforSensitiveGroups" 
        elif api[0]['Category']['Name'] == "Unhealthy":
                category_description="(151-200) people will start feeling health effects"
                category_color="Unhealthy" 
        elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description="(201-300) health alert"
                category_color="VeryUnhealthy"  
        elif api[0]['Category']['Name'] == "Hazardous":
                category_description="(301-500) health warning of emergency conditions" 
                category_color="Hazardous"
        

        return render( request, 'home.html', {
            'api':api, 
            'category_description' : category_description,
            'category_color': category_color
            })

def about(request):
    return render( request, 'about.html', {})
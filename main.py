from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse

movies=[
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
     {
		"id": 2,
		"title": "Sueños de fuga",
		"overview": "Un hombre que quiere escapar de la carcel ...",
		"year": "1997",
		"rating": 8.9,
		"category": "Drama"
	}
]

app=FastAPI()
app.title="API JPBB"
app.version="1.0.0"

@app.get('/')
def message():
    return HTMLResponse('<h1>JPBB</h1>')

@app.get('/movies',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}',tags=['movies'])
def	get_movies(id:int):
    for item in movies:
        if item["id"]==id:
            return item
    return "no existe, busque bien manito"
    
@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category: str, year:int):
	return [item for item in movies if item["category"]==category]


@app.post('/movies/',tags=['movies'])
def create_movie(id:int=Body(), title:str=Body(), overview:str=Body(), year:int=Body(),rating:float=Body(), category:str=Body()):
	movies.append({
          "id":id,
          "tittle":title,
          "overview":overview,
          "year":year,
          "rating":rating,
          "category":category
	})
	return movies

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id:int, title:str=Body(), overview:str=Body(), year:int=Body(),rating:float=Body(), category:str=Body()):
     for item in movies:
          if item["id"]==id:
               item['title']=title
               item['overview']=overview
               item['year']=year
               item['rating']=rating
               item['category']=category
               return movies
          
@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
     for item in movies:
          if item["id"]==id:
               movies.remove(item)
               return movies
     

     
"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp

from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo,alpha,maptyp):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category': None,
               "videostags": None,
               "country":None
               }
    catalog['videos'] = lt.newList(tipo)
    catalog['videostags'] = mp.newMap(200,
                                maptype=maptyp,
                                loadfactor=alpha)

    
    catalog['category'] = mp.newMap(70,
                                   maptype='PROBING',
                                   loadfactor=0.5)
    catalog['country'] = mp.newMap(70,
                                   maptype='PROBING',
                                   loadfactor=0.5)

    

    return catalog

# ==============================
# Funciones para crear datos
# ==============================

def newcategory(id, name):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


# ==============================
# Funciones para agregar informacion al catalogo
# ==============================

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    moj= mp.contains(catalog["videostags"],video['category_id']) 
    if moj :
        valoactual=mp.get(catalog["videostags"],video["category_id"])
        valor= me.getValue(valoactual)
    else:
        valor=lt.newList("ARRAY_LIST")
        mp.put(catalog['videostags'], video['category_id'], valor)
    lt.addLast(valor,video)

    # Se obtiene el autor del video

def addid(catalog, category):
    """
    Adiciona un tag a la lista de tags
    """

    lista = category["id\tname"].split("\t ")

    category["id"] = lista[0]
    category["name"] = lista[1].strip()
    
    mp.put(catalog['category'], category["name"], category["id"])

# ==============================
# Funciones de consulta
# ==============================

def getvideosbytag(catalog, tag, size, pais):

    videospais = lt.newList()
    tagg=mp.get(catalog["category"],tag) 
    taggg=me.getValue(tagg) 
    valor=mp.get(catalog["videostags"],taggg) 

    tema=me.getValue(valor) 
    videos = mt.sort(tema, cmpVideosByLikes)
    for cont in range(1,  lt.size(videos)):
        video = lt.getElement(videos, cont)

        if video["country"] == pais:
            lt.addLast(videospais,video)
    videos = lt.subList(videospais,1,size)
    return videos
    
# Funciones de Tamaño

def videosSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['videos'])

def categorySize(catalog):
    """
    Número de libros en el catago
    """
    return mp.size(catalog['category'])


# Funciones de ordenamiento


def cmpVideosByLikes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))


def cmpVideosByViews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


def comparcategory(categ, id):
    id = me.getKey(id)
    print(id)
    return (categ == id)





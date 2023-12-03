from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a a single note with `id`'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creating a new note.'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
     
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serialized = NoteSerializer(notes , many = True)
    return Response(serialized.data)


@api_view(['GET'])
def getNote(request , pk):
    notes=Note.objects.get(id=pk)
    serialized = NoteSerializer(notes , many = False)
    return Response(serialized.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serialized = NoteSerializer(note , many = False)
    print(serialized.data)
    return Response(serialized.data)
    
@api_view(['PUT'])
def updateNote(request , pk):
    data = request.data
    note = Note.objects.get(id = pk)
    serialized = NoteSerializer(instance=note , data=data)

    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)

@api_view(['DELETE'])
def deleteNote(request , pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note Deleted')


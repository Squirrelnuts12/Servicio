import os
from supabase import create_client
url = 'https://vepwimjkfdtkxstkirng.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZlcHdpbWprZmR0a3hzdGtpcm5nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI2MjUzNTYsImV4cCI6MjAyODIwMTM1Nn0.2k3Z9ZXnM_nfpa0qtz6oE2_GAdi-XO4DqbdkV5YEExc'
supabase = create_client(url, key)
response =  supabase.table("calculations").insert({"id":"", "average":"Promedio:22","minimum":"Minimo:20", "maximum":"Maximo:24"}).execute()
print(response)
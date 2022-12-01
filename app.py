import streamlit as st
from json import loads
from pandas import read_csv

st.title('Aplicativo Feito com Python')

st.markdown('''
#Aqui Vai Mostra Seu Arquivo Fucionando Na Hora !!!  🥴

##Suba um arquivo e veja o que acontece 😎
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui !',
    type= ['png','jpg','mp3','mp4','mov','flv','avi','mkv','webm','wav','csv','json','py','html','css','js']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application','json':
            st.json(loads(arquivo.read()))
           
        case 'image',_:
            st.image(arquivo)
        
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
            st.area_chart(df)


        case  'text', 'x-python':
            st.code(arquivo.read().decode())

        case  'text', 'html':
            st.code(arquivo.read().decode())

            
        case  'text', 'css':
            st.code(arquivo.read().decode())
            
        case  'text', 'javascript':
            st.code(arquivo.read().decode())
            
        case 'audio',_:
            st.audio(arquivo)

        case 'video',_:
            st.video(arquivo)
        
else:
    st.write("Não tem nenhum arquivo ainda")  
import streamlit as st
from json import loads
from pandas import read_csv



st.title('Aplicativo Feito com Python')

st.markdown('''
#Aqui Vai Mostra Seu Arquivo Fucionando Na Hora !!! :heart:

##Suba um arquivo e veja o que acontece :smile: 
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui !',
    type= ['png','jpg','mp3','wav','csv','json','py','html','css','js']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application','json':
            st.json(loads(arquivo.read()))
           
        case 'image',_:
            st.image(arquivo)
        
        case  'text', 'pdf':
            st.pdf(PyPDF2(arquivo.PdfFileReader()))
            #st.(arquivo)

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
        
else:
    st.write("Não tem nenhum arquivo ainda")  
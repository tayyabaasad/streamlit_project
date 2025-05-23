import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title= "Data sweeper",layout= "wide")

st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color: white;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)

st.title("📀 Data sweeper sterling Integrator by Tayyaba asad")
st.write("Transform your files from csv and Excel formates with built-in data cleaning and visualization creating the project for quarter 3!")



uploaded_files = st.file_uploader("upload your files(Accepts CSV and Excel)", Type=["csv","xlsx"],accept_multiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        if file_ext == ".csv":
            df= pd.read_csv(file)
        elif file_ext == "xlsx":
            df = pd.read_excel(file)
        else:
             st.error(f"unsupported file type: {file_ext}")    
             continue
         
         
        st.write("🔍preview the head of the dataframe")
        st.dataframe(df.head())
        
        
        
        st.subheader("🛠 Data cleaning options")
        if st.checkbox(f"clean data for {file.name}"):
            col1, col2 = st.columns(2)
            
            
            with col1:
                if st.button(f"Remove duplicates from the file: {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicate removed!")
                    
                    
                    
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols= df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write(f"✅ Missing values has been filled!")
                    
                    
        st.subheader("🎯 Sewlect columns to keep")
        columns  =  st.multiselect(f"chose columns for {file.name}",df.columns,default=df.columns)
        df= df[columns]
        
        
        
        st.subheader("👔 Data visualization")
        if st.checkbox(f"show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number'),iloc[:, :2])
            
            
            
            st.subheader("🌀  Conversion options ")
            conversion_type = st.radio(f"convert{file.name} to:"["csv","Excel"],key=file.name)
            if st.button(f"convert{file.name}"):
                buffer= BytesIO()
                if conversion_type== "CSV":
                    df.to.csv(buffer,index=False)
                    file_name = file.name.replace(file_ext,"csv")
                    mime_type = "text/csv"
                    
                    
                    
                
                elif conversion_type == "Excel"  :
                    df.to.to_excel(buffer,index=False)
                    file_name = file.name.replace(file_ext ,".xlsx")
                    mime_type = "application/vnd.openxmlformates-officedocument.spreadsheetml.sheet"
                buffer.seek(0)   
                    
                    
                st.download_button(
                   label= f"Download {file.name} as {conversion_type}",
                   data=buffer,
                   file_name=file_name,
                   mime  =   mime_type
               )     

st.success("🎉 All files processed succesfully!")                
                    
                    
                    
                    
                    
                    
         
                            
            
            
           
        

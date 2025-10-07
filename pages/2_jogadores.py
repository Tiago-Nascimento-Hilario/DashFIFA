import streamlit as st


st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_jogadores = df_data[(df_data["Club"] == club)]
jogadores = df_jogadores["Name"].value_counts().index
jogador = st.sidebar.selectbox("Jogador", jogadores)

jogador_estatistica = df_data[df_data["Name"] == jogador].iloc[0]

st.title(jogador_estatistica["Name"])

st.markdown(f"**Clube:** {jogador_estatistica['Club']}")
st.markdown(f"**Posição:** {jogador_estatistica['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {jogador_estatistica['Age']}")
col1.markdown(f"**Altura:** {jogador_estatistica['Height(cm.)'] /100}")
col1.markdown(f"**Peso:** {jogador_estatistica['Weight(lbs.)'] * 0.453:.2f}")

st.divider()

st.subheader(f"Overall {jogador_estatistica['Overall']}")
st.progress(int(jogador_estatistica["Overall"]))

col1, col2, col3, col4 = st.columns(4)

col1.metric(label="Valor de mercado", value=f"£ {jogador_estatistica['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {jogador_estatistica['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {jogador_estatistica['Release Clause(£)']:,}")

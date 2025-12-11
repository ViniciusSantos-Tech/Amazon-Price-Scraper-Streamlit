# FEITO POR VINICIUS SANTOS-TECH 
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="Raspador Amazon", page_icon="🛒")
st.title("Raspador de Preços - Amazon")
st.markdown("---")

pesquisa = st.text_input("**Digite o que deseja pesquisar:**", "Kindle")

if st.button("🔍 **BUSCAR PREÇOS**", type="primary", use_container_width=True):
    
    TabPreço = []
    TabTitle = []
    
    with st.spinner(f"Buscando '{pesquisa}' na Amazon..."):
        try:
            navegador = webdriver.Chrome()
            navegador.get("https://www.amazon.com.br/")

            wait = WebDriverWait(navegador, 10)
            navegador.maximize_window()

            Barra = wait.until(Ec.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
            Barra.click()
            Barra.send_keys(pesquisa)
            Barra.send_keys(Keys.ENTER)
            
            time.sleep(2)
            
            resultados = navegador.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
            
            if not resultados:
                st.error("Nenhum produto encontrado!")
                navegador.quit()
                st.stop()
            
            st.success(f"✅ {len(resultados[:5])} produtos encontrados!")
            st.markdown("---")
            resultados_container = st.container()
            
            with resultados_container:
                st.subheader("📋 Resultados da Pesquisa")
                
                for i, Resultado in enumerate(resultados[:5], 1):
                    try:
                        Preço = Resultado.find_element(By.CLASS_NAME, "a-price-whole")
                        Title = Resultado.find_element(By.CLASS_NAME, 'a-size-base-plus.a-color-base.a-text-normal')
                        PreçoLimpo = float(Preço.text.replace(".", "").replace(",", "").replace("R$", "").strip())
 
                        TabPreço.append(PreçoLimpo)
                        TabTitle.append({
                            'titulo': Title.text,
                            'preco': PreçoLimpo
                        })
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.write(f"**{i}. {Title.text[:80]}...**")
                        with col2:
                            st.write(f"**R$ {PreçoLimpo:,.2f}**".replace(",", "X").replace(".", ",").replace("X", "."))
                        st.markdown("---")
                        
                    except Exception as e:
                        st.warning(f"Erro ao processar produto {i}: {e}")

            navegador.quit()

            if TabPreço:
                mais_barato = min(TabPreço)
                mais_caro = max(TabPreço)
                produto_barato = TabTitle[TabPreço.index(mais_barato)]
                produto_caro = TabTitle[TabPreço.index(mais_caro)]
                Media = sum(TabPreço) / len(TabPreço)

                st.subheader("📊 Resumo da Busca")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("💰 Mais Barato", f"R$ {mais_barato:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                with col2:
                    st.metric("💸 Mais Caro", f"R$ {mais_caro:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                with col3:
                    st.metric("📈 Média", f"R$ {Media:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                
                st.write(f"**Diferença:** R$ {mais_caro - mais_barato:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                st.write(f"**Produto mais barato:** {produto_barato['titulo'][:60]}...")
                st.write(f"**Produto mais caro:** {produto_caro['titulo'][:60]}...")

                data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
                nome_arquivo = f"amazon_precos_{data_hora}.csv"
                
                with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.write("Titulo;Preço\n")
                    for produto in TabTitle:
                        linha = f"{produto['titulo'][:100]};{produto['preco']}\n"
                        arquivo.write(linha)

                with open(nome_arquivo, 'rb') as f:
                    csv_bytes = f.read()
                
                st.download_button(
                    label="📥 **BAIXAR CSV COMPLETO**",
                    data=csv_bytes,
                    file_name=nome_arquivo,
                    mime="text/csv"
                )
                st.success(f"📁 Arquivo salvo: {nome_arquivo}")
            
            else:
                st.error("Nenhum produto válido encontrado!")
                
        except Exception as e:
            st.error(f"Erro durante a raspagem: {str(e)}")
            try:
                navegador.quit()
            except:
                pass

st.markdown("---")
st.caption("Desenvolvido por Vinicius Santos - Tech")

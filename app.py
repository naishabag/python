import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Amazon Demo", layout="wide")

st.title("🛒 Amazon Demo UI")
st.write("This is a simple mock-up of an Amazon-style interface built with Streamlit.")

# --- SEARCH BAR ---
search_query = st.text_input("Search for products...", placeholder="Search Amazon")
st.button("Search")

st.markdown("---")

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("Filters")
    st.checkbox("Prime eligible")
    st.checkbox("Free delivery")
    price_range = st.slider("Price range", 0, 2000, (20, 200))

# --- PRODUCT GRID ---
st.subheader("Recommended Products")

products = [
    {"name": "Wireless Headphones", "price": "$49.99", "rating": 4.5},
    {"name": "Smart Watch", "price": "$89.99", "rating": 4.2},
    {"name": "Bluetooth Speaker", "price": "$39.99", "rating": 4.7},
]

cols = st.columns(3)

for col, product in zip(cols, products):
    with col:
        st.image("https://via.placeholder.com/200", caption=product["name"])
        st.write(f"**Price:** {product['price']}")
        st.write(f"⭐ {product['rating']}")
        st.button(f"Add to Cart - {product['name']}")

st.markdown("---")
st.write("© Demo UI — Not affiliated with Amazon.")

# Streamlit app for Virtuals Genesis PPR Calculation
import streamlit as st

st.set_page_config(page_title="Virtuals PPR Estimator", layout="centered")
st.title("Virtuals Genesis PPR Estimator 🧠")
st.markdown("Made by **0xHERRO** and **Bello the Frog** 🐸")

# --- Inputs
st.header("📥 Input Your Data")
col1, col2 = st.columns(2)

with col1:
    points_pledged = st.number_input("Your Points Pledged", min_value=1)
    virtual_committed = st.number_input("Your VIRTUAL Committed", min_value=0.0, format="%.4f")
    virtual_price = st.number_input("VIRTUAL Price at Launch (USD)", value=2.0)

with col2:
    total_points_pool = st.number_input("Total Points Pledged (e.g. 700M)", min_value=1, value=700_000_000, format="%i")
    total_virtual_pool = st.number_input("Total VIRTUAL Committed by All", min_value=1.0, value=42_425.0, format="%.4f")

st.divider()

col3, col4 = st.columns(2)
with col3:
    total_token_supply = st.number_input("Total Token Supply (e.g. 1000M)", value=1_000_000_000, format="%i")
    genesis_allocation_pct = 0.375
    total_tokens_allocated = total_token_supply * genesis_allocation_pct
    st.markdown(f"📦 **Genesis Tokens (37.5%)**: {total_tokens_allocated:,.0f}")

with col4:
    estimated_fdv = st.number_input("Estimated FDV (USD)", value=30_000_000)
    estimated_token_price = estimated_fdv / total_token_supply
    st.markdown(f"💵 **Estimated Token Price**: ${estimated_token_price:.4f}")

# --- Calculate
if st.button("Calculate PPR"):
    point_share = points_pledged / total_points_pool
    virtual_limit = total_virtual_pool * point_share

    tokens_received = total_tokens_allocated * point_share
    est_value = tokens_received * estimated_token_price
    cost = min(virtual_committed, virtual_limit) * virtual_price
    profit = est_value - cost
    ppr = profit / points_pledged if points_pledged > 0 else 0

    st.subheader("📊 Results")
    st.write(f"🪙 **Token Allocation**: {tokens_received:,.2f}")
    st.write(f"💰 **Estimated Value**: ${est_value:,.2f}")
    st.write(f"🧾 **Your Cost** (adjusted for overcommit): ${cost:.2f}")
    st.write(f"📈 **Profit**: ${profit:,.2f}")
    st.write(f"🧠 **PPR (USD per point)**: {ppr:.5f}")

    if virtual_committed > virtual_limit:
        st.warning(f"⚠️ You are overcommitting VIRTUALs. Max you should commit is ~{virtual_limit:.4f}.")

# --- Footer
st.divider()
st.markdown("**What is PPR?**\n\nPPR (Points-to-Profit Ratio) shows how much USD profit you earn for each point you pledge.\n\n**Formula:**")
st.latex(r"\text{PPR} = \frac{\text{Estimated Token Value} - \text{Cost}}{\text{Points Pledged}}")
st.markdown("\nYou might spend gas or fees to earn points. Be efficient.")

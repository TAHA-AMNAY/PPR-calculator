import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Virtuals PPR Estimator", page_icon="🦰")

st.title("🦰 Virtuals Genesis PPR Estimator")
st.markdown("Estimate your **Points-to-Profit Ratio (PPR)** before committing to a Genesis launch on @virtuals_io.")

# --- Input Section ---
st.header("📜 Input Parameters")

col1, col2 = st.columns(2)
with col1:
    points_pledged = st.number_input("📍 Points You Pledged", min_value=1000)
    virtual_committed = st.number_input("💸 $VIRTUAL Committed", min_value=0.0)
    virtual_price = st.number_input("💵 $VIRTUAL Price at Launch (USD)", value=2.0)
with col2:
    total_points_pool_m = st.number_input("🌐 Total Points Pledged by Everyone (in Millions)", value=250)
    total_token_supply_m = st.number_input("📦 Total Token Supply (in Millions)", value=1000)
    estimated_fdv_m = st.number_input("📋 Estimated FDV (USD, in Millions)", value=20)
    total_virtuals_committed = st.number_input("📈 Total VIRTUALs Committed by Everyone", value=42000.0)

# --- Scale Values ---
total_points_pool = total_points_pool_m * 1_000_000
total_token_supply = total_token_supply_m * 1_000_000
estimated_fdv = estimated_fdv_m * 1_000_000

# --- Genesis Allocation ---
st.markdown("---")
genesis_allocation_pct = 0.375
total_tokens_allocated = total_token_supply * genesis_allocation_pct
st.info(f"📦 **Genesis Tokens Allocated (37.5%)**: `{total_tokens_allocated:,.0f}`")

# --- Calculate Button ---
st.markdown("---")
if st.button("🧲 Calculate PPR"):
    your_share = points_pledged / total_points_pool
    your_tokens = total_tokens_allocated * your_share
    estimated_token_price = estimated_fdv / total_token_supply
    estimated_value = your_tokens * estimated_token_price

    # ✅ Fixed cost calculation
    virtual_limit = total_virtuals_committed * your_share
    cost = min(virtual_committed, virtual_limit) * virtual_price

    profit = estimated_value - cost
    ppr = profit / points_pledged

    # Output
    st.success("✅ **Results**")
    st.write(f"🪙 Token Allocation: `{your_tokens:,.2f}`")
    st.write(f"💵 Estimated Token Price: `${estimated_token_price:.4f}`")
    st.write(f"💰 Estimated Value of Your Tokens: `${estimated_value:,.2f}`")
    st.write(f"🧾 Cost: `${cost:.2f}`")
    st.write(f"📈 Estimated Profit: `${profit:,.2f}`")
    st.write(f"🦰 **PPR (USD per Point)**: `{ppr:.4f}`")

# --- Footer + PPR Explanation ---
st.markdown("---")
st.caption("🐸 Made by **0xHERRO** & **Bello the Frog** — farm smarter, not louder.")

st.markdown("### ℹ️ What is PPR?")
st.markdown("**PPR (Points-to-Profit Ratio)** tells you how much profit you made for each Genesis Point you pledged.")

st.latex(r"""
\text{Estimated Profit} = (\text{Your Tokens} \times \text{Token Price}) - (\text{\$VIRTUAL Committed} \times \text{VIRTUAL Price})
""")

st.latex(r"""
\text{PPR} = \frac{\text{Estimated Profit}}{\text{Points Pledged}}
""")

st.markdown("""
The higher your PPR, the more efficient your points were in generating real returns.

Use it to compare Genesis launches and avoid wasting points on overhyped, low-yield opportunities.
""")

# --- New: Field Explanation ---
st.markdown("---")
st.markdown("### 🧾 What each input means:")

st.markdown("""
- Points You Pledged: Points you spent in this Genesis round. More points = more $VIRTUAL you can commit.
- Virtuals Committed: The amount of $VIRTUAL you're spending to buy the token.
- Virtuals Price: Price per VIRTUAL token Price you can check coingecko/Coinmarketcap.
- Total Points by Everyone: The total points pledged across all wallets — shown on the launch page.
- Total Token Supply: The full supply of the token in millions. Used to estimate token price.
- Estimated FDV: The price the market might value the token at post-launch, in millions.
- Genesis Tokens Allocated: 37.5% of total supply — this is the pool you're competing for.

> ⚠️ **Note:** Sometimes you have to spend $ on Volume fees to earn points.  
This app assumes points were free, but your **true PPR** should also consider the hidden cost of earning points.
""")

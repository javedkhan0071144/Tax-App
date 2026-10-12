import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Professional Tax Challan App", page_icon="🧾", layout="wide"
)

st.title("🧾 Professional Tax Challan System")
st.subheader("Kallar Syedan, Rawalpindi — Dashboard")

# Load Data
data_path = "data/challan_data.csv"
if os.path.exists(data_path):
  df = pd.read_csv(data_path)
else:
  df = pd.DataFrame({
      "BusinessName": [
          "Ali Refereshment & Hotel",
          "Al-Madina General Store",
          "Kallar Auto Workshop",
      ],
      "Address": [
          "Near The light School Rawalpindi Road , Kallar Syedan",
          "Main Bazar Kallar Syedan",
          "Rawalpindi Road Kallar Syedan",
      ],
      "Category": ["EST", "GEN", "EST"],
      "Period": ["2026-27", "2026-27", "2026-27"],
      "Amount": [5000, 3000, 5000],
      "AmountInWords": [
          "Five Thousand Only",
          "Three Thousand Only",
          "Five Thousand Only",
      ],
      "LastDate": ["30-9-2026", "30-9-2026", "30-9-2026"],
  })

# Sidebar Filters
st.sidebar.header("Filter Controls")
search_query = st.sidebar.text_input("Search Business Name")
selected_category = st.sidebar.selectbox(
    "Filter Category", ["All"] + list(df["Category"].unique())
)

filtered_df = df.copy()
if search_query:
  filtered_df = filtered_df[
      filtered_df["BusinessName"].str.contains(search_query, case=False, na=False)
  ]
if selected_category != "All":
  filtered_df = filtered_df[filtered_df["Category"] == selected_category]

st.metric("Total Records Loaded", len(filtered_df))
st.markdown("### Taxpayer Database (Editable)")
edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

st.markdown("---")
st.subheader("📄 Official Challan View & Print Preview")

for index, row in edited_df.iterrows():
  with st.expander(
      f"Challan: {row['BusinessName']} (Rs. {row['Amount']}/-)"
  ):
    st.markdown(f"""
        <div style="border: 2px solid #000; padding: 20px; font-family: monospace; background-color: #ffffff; color: #000;">
            <b>Head Of Account:</b> Professional Tax / Tax on Profession & Trade[cite: 1]<br>
            <b>Account Code:</b> 000-Tax Revenue B01601. Tax on Prof. & Calling Ordinary[cite: 1]<br>
            <b>Location:</b> Excise & Taxation Office opposite TMA Office Kallar Syedan[cite: 2]<br>
            <hr style="border: 1px solid #000;">
            <b>Business Name:</b> {row['BusinessName']}<br>
            <b>Address:</b> {row['Address']}<br>
            <b>Category:</b> {row['Category']} | <b>Period:</b> {row['Period']}[cite: 1]<br>
            <b>Due Date:</b> {row['LastDate']}[cite: 1]<br>
            <b>Amount:</b> Rs. {row['Amount']}/- ({row['AmountInWords']} Only)[cite: 1]<br>
            <hr style="border: 1px solid #000;">
            <b>Bank:</b> نیشنل بینک / اسٹیٹ بینک آف پاکستان<br>
            <b>Officer Contact:</b> Javed Khan, Inspector Excise & Taxation Kallar Syedan (03170071144)[cite: 2]<br>
            <i>Note: آپ سے درخواست ہے کہ ادائیگی کی رسید واپس بھیج دیں۔ شکریہ[cite: 2]</i>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
csv_export = edited_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="💾 Download Filtered Data as CSV (For Excel / Word Mail Merge)",
    data=csv_export,
    file_name="challan_data_kallar_syedan.csv",
    mime="text/csv",
)

from __future__ import annotations
import os
import sys
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from data_loader import load_items
from recommender import InterestBasedRecommender

st.set_page_config(page_title="Interest-Based Recommendation System", layout="wide")

DATA_PATH = BASE_DIR / "data" / "resources.csv"
items = load_items(DATA_PATH)
recommender = InterestBasedRecommender(items)

all_interests = sorted({tag for item in items for tag in item.tags})

st.title("Interest-Based Recommendation System")
st.caption("Welcome!")

with st.sidebar:
    st.header("User Input")
    name = st.text_input("Student / User Name", value="Demo User")
    interests = st.multiselect(
        "Select your interests",
        options=all_interests,
        default=["aws", "docker", "kubernetes"],
    )
    top_k = st.slider("Number of recommendations", min_value=1, max_value=10, value=5)
    recommend_btn = st.button("Generate Recommendations", use_container_width=True)

col1, col2 = st.columns([1.4, 1])

with col1:
    st.subheader("Project Overview")
    st.write(
        "This demo recommends cloud-computing learning resources based on user interests. "
        "It uses content-based filtering with tag similarity and simple score boosting."
    )

    st.markdown("### Workflow")
    st.markdown(
        "1. User selects interests.\n"
        "2. System compares interests with item tags.\n"
        "3. Similarity score is calculated.\n"
        "4. Top matching resources are recommended."
    )

with col2:
    st.subheader("Selected Profile")
    st.info(f"**Name:** {name}\n\n**Chosen interests:** {', '.join(interests) if interests else 'None'}")

if recommend_btn:
    if not interests:
        st.warning("Please select at least one interest.")
    else:
        recommendations = recommender.recommend(interests, top_k=top_k)
        st.markdown("---")
        st.subheader("Recommended Resources")

        if not recommendations:
            st.error("No matching resources found for the selected interests.")
        else:
            for idx, rec in enumerate(recommendations, start=1):
                item = rec["item"]
                details = rec["details"]
                with st.container(border=True):
                    st.markdown(f"### {idx}. {item.title}")
                    st.write(item.description)
                    st.write(f"**Category:** {item.category}")
                    st.write(f"**Difficulty:** {item.difficulty}")
                    st.write(f"**Tags:** {', '.join(item.tags)}")
                    st.write(f"**Recommendation Score:** {rec['score']}")
                    st.caption(
                        f"Jaccard: {details['jaccard_similarity']} | "
                        f"Match bonus: {details['exact_match_bonus']} | "
                        f"Category bonus: {details['category_bonus']}"
                    )
                    st.link_button("Open Resource", item.url)

st.markdown("---")
st.subheader("Dataset Preview")
st.dataframe(
    [
        {
            "Title": item.title,
            "Category": item.category,
            "Difficulty": item.difficulty,
            "Tags": ", ".join(item.tags),
        }
        for item in items
    ],
    use_container_width=True,
)

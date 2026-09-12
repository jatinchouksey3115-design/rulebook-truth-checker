
import streamlit as st
from src.rulebook import Rulebook

st.set_page_config(page_title="Rulebook Truth Checker", page_icon="📘", layout="wide")

@st.cache_resource
def load():
    return Rulebook()

rb = load()
st.title("📘 Rulebook Truth Checker")
st.caption("Answers only from the supplied corpus. Every answer has a source. If rules conflict, the app says so. If the corpus is silent, it says NO_ANSWER.")

with st.sidebar:
    st.subheader("Corpus")
    st.write(f"Loaded clauses: **{len(rb.clauses)}**")
    st.markdown("**Three possible states**")
    st.write("✅ ANSWER — evidence found")
    st.write("⚠️ CONTRADICTION — incompatible rules found")
    st.write("❌ NO_ANSWER — corpus does not establish the answer")
    st.divider()
    st.write("Try the demo questions below.")

examples = [
    "What attendance percentage is normally required to sit the end-term examination?",
    "What attendance percentage is required for examination eligibility when a student has an approved medical absence?",
    "When is the undergraduate standard autumn tuition payment due?",
    "Can a final project be submitted after the deadline without prior approval?",
    "What happens if I miss an end-term examination because I am attending my sister's wedding?"
]
choice = st.selectbox("Demo questions", ["Type my own question"] + examples)
if choice == "Type my own question":
    question = st.text_input("Ask a question")
else:
    question = choice
if st.button("Check the rulebook", type="primary") and question:
    result = rb.answer(question)
    state = result["state"]
    if state == "ANSWER":
        st.success("ANSWER")
        st.write(result["answer"])
    elif state == "CONTRADICTION":
        st.warning("CONTRADICTION")
        st.write(result["answer"])
    else:
        st.error("NO_ANSWER")
        st.write(result["answer"])

    if result["citations"]:
        st.subheader("Evidence")
        for c in result["citations"]:
            st.markdown(f"**{c['id']} — {c['source']} ({c['locator']})**")
            st.code(c["text"], language="text")
    with st.expander("Retrieval trace"):
        st.json(result["retrieved"])

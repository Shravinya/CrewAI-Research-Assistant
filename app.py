import streamlit as st

# ✅ Import directly from pipeline (main source of truth)
from pipeline import run_ai_pipeline

st.set_page_config(page_title="🤖 AI Research Assistant", layout="centered")

st.title("🤖 AI Research Assistant")
st.write("This app uses CrewAI + Gemini to research and summarize any topic you enter.")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_prompt = st.text_input("Enter a topic (e.g., 'latest AI in healthcare'): ")

if st.button("🚀 Run Research"):
    if user_prompt.strip():
        st.write("🔎 Running CrewAI pipeline... Please wait.")
        with st.spinner("Researching and summarizing..."):
            result = run_ai_pipeline(user_prompt)

        st.success("✅ Done!")

        try:
            tasks = result["tasks_output"]

            bullet_points = tasks[0]["raw"] if len(tasks) > 0 else "No bullet points found."
            summary = tasks[1]["raw"] if len(tasks) > 1 else "No summary found."

            # Save to history
            st.session_state.history.append({
                "topic": user_prompt,
                "bullets": bullet_points,
                "summary": summary,
            })

            # Display results
            st.subheader("📌 Key Insights")
            st.markdown(bullet_points)

            st.subheader("📝 Summary")
            st.write(summary)

        except Exception as e:
            st.error(f"⚠️ Error parsing result: {e}")
            st.json(result)

    else:
        st.warning("⚠️ Please enter a topic.")

# Sidebar: conversation history
if st.session_state.history:
    st.sidebar.title("📜 Conversation History")
    for i, entry in enumerate(reversed(st.session_state.history), 1):
        with st.sidebar.expander(f"Topic {i}: {entry['topic']}"):
            st.markdown("**📌 Insights:**")
            st.markdown(entry["bullets"])
            st.markdown("**📝 Summary:**")
            st.write(entry["summary"])

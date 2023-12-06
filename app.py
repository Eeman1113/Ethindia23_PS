import streamlit as st
import pandas as pd
import os

# Load the DataFrame
df = pd.read_csv('./data/eth23.csv')

st.markdown("<h1 style='text-align: center; '>CookEthNotMeth</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>To Vote Click Twice (single click will not be counted)</h3>", unsafe_allow_html=True)

# Check if the CSV file for storing votes exists, if not, create it
vote_file_path = './data/votes.csv'
if not os.path.exists(vote_file_path):
    vote_df = pd.DataFrame({'Summary': df['Summary'], 'Upvote': 0, 'Downvote': 0})
    vote_df.to_csv(vote_file_path, index=False)
else:
    vote_df = pd.read_csv(vote_file_path)

# Display a graph of the most voted topics at the top of the screen
st.markdown('___')
st.markdown("<h2 style='text-align: center; '>Most Voted Topics</h2>", unsafe_allow_html=True)

# Calculate net votes for each summary (Upvotes - Downvotes)
vote_df['NetVotes'] = vote_df['Upvote'] - vote_df['Downvote']

# Sort the DataFrame based on net votes
sorted_vote_df = vote_df.sort_values(by='NetVotes', ascending=False)

# Create a bar chart for net votes
st.bar_chart(sorted_vote_df['NetVotes'])

# Add a reset button
reset_button = st.button("Reset Votes")

# If reset button is clicked, reset all vote counts to zero
if reset_button:
    vote_df[['Upvote', 'Downvote', 'NetVotes']] = 0
    vote_df.to_csv(vote_file_path, index=False)
    st.success("Votes reset successfully!")

for i in range(len(df['Summary'])):
    st.markdown('___')
    st.write(f"{i+1}. {df['Summary'][i]}")

    # Display Upvote and Downvote buttons side by side
    col1, col2 = st.columns(2)
    with col1:
        upvote_button = st.button(f"Upvote ({vote_df['Upvote'][i]})", key=f"upvote_{i}")
        if upvote_button:
            vote_df.at[i, 'Upvote'] += 1

    with col2:
        downvote_button = st.button(f"Downvote ({vote_df['Downvote'][i]})", key=f"downvote_{i}")
        if downvote_button:
            vote_df.at[i, 'Downvote'] += 1

    st.markdown(f"<details><summary>For More Info About Me Click Here</summary>{df['Problem Statement'][i]}</details>", unsafe_allow_html=True)

# Save the updated vote counts to the CSV file
vote_df.to_csv(vote_file_path, index=False)

st.balloons()

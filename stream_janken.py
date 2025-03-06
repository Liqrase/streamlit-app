import streamlit as st
import random

# streamlit run 250305/stjanken.py
def hantei(hand):
    if hand == "グー":
        return 3
    elif hand == "チョキ":
        return 5
    else:
        return 6

def janken(p_hand, cp_hand):
    if (p_hand == "グー" and cp_hand == "チョキ") or (p_hand == "チョキ" and cp_hand == "パー") or (p_hand == "パー" and cp_hand == "グー"):
        return 1
    elif (p_hand == "グー" and cp_hand == "パー") or (p_hand == "チョキ" and cp_hand == "グー") or (p_hand == "パー" and cp_hand == "チョキ"):
        return 2
    else:
        return 3

st.title("じゃんけんGlico")

if "p_walk" not in st.session_state:
    st.session_state.p_walk = 0
    st.session_state.cp_walk = 0
    st.session_state.count = 1

total_distance = 20
weaporn = ["グー", "チョキ", "パー"]


p_hand = st.radio("出したい手を選んでください", ["グー", "チョキ", "パー"], index=0)

if st.button("じゃんけん！"):
    cp_hand = random.choice(weaporn)
    st.write(f"#### {st.session_state.count}戦目")
    st.write(f"### じゃん、けん、ぽん！")
    st.write(f"あなたは {p_hand} を出し、CPUは {cp_hand} を出した！")
    syouhai = janken(p_hand, cp_hand)

    if syouhai == 1:
        st.write(f"#### あなたの勝ち！{hantei(p_hand)}マス進む。")
        st.session_state.p_walk += hantei(p_hand)
        st.session_state.count += 1
    elif syouhai == 2:
        st.write(f"#### CPUの勝ち！{hantei(cp_hand)}マス進む。")
        st.session_state.cp_walk += hantei(cp_hand)
        st.session_state.count += 1
    else:
        st.markdown(f"#### あいこ。やり直し！")
    
    st.write(f"現在地：あなた {st.session_state.p_walk} マス、CPU {st.session_state.cp_walk} マス")

if st.session_state.p_walk >= total_distance:
    pl1, pl2 = st.columns(2)
    with pl1:
        st.image("gazou/computer_man4_laugh.png", caption="喜ぶあなた(男性)", use_container_width=True)
    with pl2:
        st.image("gazou/computer_woman4_laugh.png", caption="喜ぶあなた(女性)", use_container_width=True)
    st.success("あなたの勝ち！")
    st.session_state.p_walk = 0
    st.session_state.cp_walk = 0
    st.session_state.count = 1
    st.write("「じゃんけん」ボタンを押すと再戦できます。")
elif st.session_state.cp_walk >= total_distance:
    st.image("gazou/computer_note_good.png", caption="喜ぶCPU", use_container_width=True)
    st.error("CPUの勝ち！")
    st.session_state.p_walk = 0
    st.session_state.cp_walk = 0
    st.session_state.count = 1
    st.write("「じゃんけん」ボタンを押すと再戦できます。")
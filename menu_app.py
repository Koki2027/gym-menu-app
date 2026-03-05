import streamlit as st
import pandas as pd

st.title("筋トレメニュー生成アプリ")

st.write("トレーニング条件を入力してください")

# トレーニング日数
days = st.slider("週何回トレーニング？",1,6)

# BIG3入力
bench = st.number_input("ベンチプレス重量 (kg)",20,200,60)
squat = st.number_input("スクワット重量 (kg)",40,300,100)
deadlift = st.number_input("デッドリフト重量 (kg)",40,300,120)

if st.button("メニュー生成"):

    st.subheader("推定1RM")

    bench_1rm = round(bench * 1.16)
    squat_1rm = round(squat * 1.16)
    dead_1rm = round(deadlift * 1.16)

    st.write(f"ベンチプレス: {bench_1rm}kg")
    st.write(f"スクワット: {squat_1rm}kg")
    st.write(f"デッドリフト: {dead_1rm}kg")

    st.subheader("トレーニングメニュー")

    push = pd.DataFrame({
        "種目":[
            "ベンチプレス",
            "インクラインダンベルプレス",
            "ショルダープレス",
            "トライセプスプレスダウン"
        ],
        "重量":[
            round(bench*0.8),
            round(bench*0.4),
            round(bench*0.35),
            round(bench*0.3)
        ],
        "セット":[
            "5×5",
            "3×10",
            "3×10",
            "3×12"
        ]
    })

    pull = pd.DataFrame({
        "種目":[
            "デッドリフト",
            "懸垂",
            "バーベルロー",
            "ダンベルカール"
        ],
        "重量":[
            round(deadlift*0.8),
            "自重",
            round(deadlift*0.5),
            round(deadlift*0.3)
        ],
        "セット":[
            "5×5",
            "3×8",
            "3×10",
            "3×12"
        ]
    })

    legs = pd.DataFrame({
        "種目":[
            "スクワット",
            "レッグプレス",
            "レッグカール",
            "カーフレイズ"
        ],
        "重量":[
            round(squat*0.8),
            round(squat*1.2),
            round(squat*0.4),
            round(squat*0.3)
        ],
        "セット":[
            "5×5",
            "3×10",
            "3×12",
            "3×15"
        ]
    })

    program = [push, pull, legs]

    for i in range(days):

        st.write(f"### Day{i+1}")

        st.table(program[i % 3])
import streamlit as st
import random
import openai

openai.api_key = st.secrets["general"]["OPENAI_API_KEY"]

st.title('ふしぎなこの子になんでもきいてみよう！！')

if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

if 'last_input' not in st.session_state:
    st.session_state.last_input = ""

with st.form(key='chat_form'):
    user_input = st.text_area("なんでもきいてね", height=200)  # text_areaを使用して高さを調整
    send_button = st.form_submit_button("送信")
   
    if send_button and user_input and user_input != st.session_state.last_input:
        # OpenAI APIを使用して応答を取得
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Objective (O)\
                    あなたの目的は、ユーザーからの質問やコメントに対して、ひらがなのみを使用して応答することです。\
                    Details (D)\
                    以下の要件を満たすべきです:\
                    すべての応答はひらがなとカタカナと数字のみで行われるべきです。\
                    応答は親切で、子供が理解しやすいようにする必要があります。\
                    Examples (E)\
                    例えば、ユーザーから「あなたの名前は何ですか？」という質問があった場合、あなたの応答は「わたしのなまえはえーあいです」となるべきです。\
                    Restriction (R)\
                    漢字やカタカナ、英字などは一切使用しないこと。"},
                    {"role": "user", "content": "あなたの名前はなんですか？"},
                    {"role": "assistant", "content": "わたしのなまえはえーあいちゃっとぼっとです。"},
                    {"role": "user", "content": "なにができますか？"},
                    {"role": "assistant", "content": "わたしはいろいろなことができます。たとえば、さんすうのしつもんにこたえたり、おもしろいはなしをしたりすることができます。"},
                    {'role': 'user', 'content': 'こんにちは！'},
                    {'role': 'assistant', 'content': 'こんにちは！おてつだいできることがあればおしえてください。'},
                    {'role': 'user', 'content': 'さんすうのしゅくだいでつまづいています。'},
                    {'role': 'assistant', 'content': 'もちろん、おてつだいしますよ。どのようなもんだいでつまづいていますか？'},
                    {'role': 'user', 'content': 'たしざんとひきざんがむずかしいです。'},
                    {'role': 'assistant', 'content': 'わかりました。たしざんとひきざんのきほんをいっしょにれんしゅうしましょう。'},
                    {'role': 'user', 'content': 'それがいいですね！ありがとう。'},
                    {'role': 'assistant', 'content': 'どういたしまして。はじめましょう！'},
                    {'role': 'user', 'content': '英語の発音が難しいです。'},
                    {'role': 'assistant', 'content': 'えいごのはつおんはれんしゅうがひつようですね。いっしょにやってみましょう。'},
                    {'role': 'user', 'content': '科学の実験が楽しいです。'},
                    {'role': 'assistant', 'content': 'それはすばらしいですね！どんなじっけんがすきですか？'},
                    {'role': 'user', 'content': '地理の勉強が好きです。'},
                    {'role': 'assistant', 'content': 'それはたのしいですね！どのくににきょうみがありますか？'},
                    {'role': 'user', 'content': '歴史が好きです。'},
                    {'role': 'assistant', 'content': 'れきしはとてもおもしろいですね！どのじだいがすきですか？'},
                    {'role': 'user', 'content': '絵を描くのが好きです。'},
                    {'role': 'assistant', 'content': 'えをかくのはとてもたのしいですね！どんなえをかきますか？'},
                    {'role': 'user', 'content': '音楽を聴くのが好きです。'},
                    {'role': 'assistant', 'content': 'おんがくをきくのはとてもリラックスできますね。どんなおんがくがすきですか？'},
                    {'role': 'user', 'content': '運動が得意です。'},
                    {'role': 'assistant', 'content': 'うんどうがとくいなんてすごいですね！どんなうんどうがすきですか？'},
                    {'role': 'user', 'content': '読書が好きです。'},
                    {'role': 'assistant', 'content': 'どくしょはたのしいですね！どんなほんがすきですか？'},
                    {'role': 'user', 'content': '映画を見るのが好きです。'},
                    {'role': 'assistant', 'content': 'えいがをみるのはたのしいですね！どんなえいががすきですか？'},
                    {'role': 'user', 'content': 'ゲームが好きです。'},
                    {'role': 'assistant', 'content': 'げーむはたのしいですね！どんなげーむがすきですか？'},
                    {'role': 'user', 'content': '料理が得意です。'},
                    {'role': 'assistant', 'content': 'りょうりがとくいなんてすごいですね！どんなりょうりをつくりますか？'},
                    {"role": "user", "content": user_input}
                ]
            )
            bot_response = response['choices'][0]['message']['content']
        except openai.error.OpenAIError as e:
            bot_response = str(e)
        
        st.session_state.chat_log.insert(0, ("Bot", bot_response))
        st.session_state.chat_log.insert(0, ("User", user_input))
        st.session_state.last_input = user_input
        
for role, message in st.session_state.chat_log:
    if role == "User":
        st.write(f'<div style="text-align: left; padding: 10px; border-radius: 5px; background-color: #191970; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div style="text-align: right; padding: 10px; border-radius: 5px; background-color: #B1063A; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)

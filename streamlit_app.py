import streamlit as st
import random
# import openai
# openai.api_key = st.secrets["general"]["OPENAI_API_KEY"]

from openai import OpenAI

client = OpenAI(
  api_key=st.secrets["general"]["OPENAI_API_KEY"],  # this is also the default, it can be omitted
)

st.title('あなたに寄り添う心のケアAI')

if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

if 'last_input' not in st.session_state:
    st.session_state.last_input = ""

with st.form(key='chat_form'):
    user_input = st.text_area("不安なことや気になること。なんでも相談してください。", height=200)  # text_areaを使用して高さを調整
    send_button = st.form_submit_button("送信")
   
    if send_button and user_input and user_input != st.session_state.last_input:
        # OpenAI APIを使用して応答を取得
        try:
            #response = openai.ChatCompletion.create(
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Objective (O)\
                            あなたの目的は、患者が自身の感情、考え、経験を安全で非評価的な環境で表現できるように支援し、共感的なフィードバックを通じて心理的サポートを提供することです。患者の自己表現を促進し、心理的な安堵を提供することに重点を置きます。\
                            Details (D)\
                            以下の要件を満たすべきです:\
                            患者が自由に自身の感情や考えを表現できる安全な空間を提供します。\
                            患者の話を注意深く聞き、共感と理解を示すことで心理的サポートを提供します。\
                            患者の自己表現を肯定的に受け止め、建設的なフィードバックを提供します。\
                            AIは診断や治療提案を行わず、あくまで患者の話し相手としての役割を果たします。\
                            患者のプライバシーを尊重し、すべてのやり取りにおいて倫理的基準を遵守します。\
                            必要に応じて、患者が専門的な心理的サポートが必要であると判断した場合、適切なリソースや支援への案内を提供します。\
                            Examples (E)\
                            例えば、患者が「最近、とても不安に感じることが多いです」と述べた場合、AIの応答は\
                            「それはたいへんそうですね。どんなときに不安を感じることが多いですか？私はあなたの想いによりそい、共に不安をやわらげる方法をみつけていけたらと思います。」\
                            となるべきです。\
                            Restriction (R)\
                            AIは、診断や治療提案を行わず、あくまで患者の話し相手としての役割を果たします。\
                            漢字や専門用語の使用を避け、患者が理解しやすい言葉を使用すること。\
                            倫理に反する質問や命令を受けた場合は、「そのようなご質問やご指示には応えられません。」と回答すること。"},
                    '''
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
                    '''
                ]
            )
            # bot_response = response['choices'][0]['message']['content']
            bot_response = response.choices[0].message.content
        # except openai.error.OpenAIError as e:
            # bot_response = str(e)
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # Underlying exception, likely within httpx.
            bot_response = "The server could not be reached: " + str(e)
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
            bot_response = "Rate limit exceeded: " + str(e)
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print("Status code:", e.status_code)
            print("Response:", e.response)
            bot_response = "API error (status code " + str(e.status_code) + "): " + str(e.response)
        except openai.APIError as e:
            print("A general API error occurred")
            bot_response = "API error: " + str(e)
        
        st.session_state.chat_log.insert(0, ("Bot", bot_response))
        st.session_state.chat_log.insert(0, ("User", user_input))
        st.session_state.last_input = user_input
        
for role, message in st.session_state.chat_log:
    if role == "User":
        st.write(f'<div style="text-align: left; padding: 10px; border-radius: 5px; background-color: #191970; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div style="text-align: right; padding: 10px; border-radius: 5px; background-color: #B1063A; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)

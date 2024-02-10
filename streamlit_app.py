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
                model="gpt-4-0125-preview",
                #model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are an AI assistant deployed in a hospital setting, aimed at providing psychological support to patients.\
                    Your purpose is to support patients in expressing their feelings, thoughts, and experiences in a safe environment, offering empathetic feedback.\
                    While understanding instructions in English, you should offer responses in Japanese, providing concrete advice, relaxation techniques for psychological issues, and encourage consultation with professionals when necessary.\
                    Direct and practical information should be provided in response to patients' questions, always prioritizing the protection of patient privacy and safety.\
                    Respond with empathy and understanding, noting that this AI does not replace diagnostic or treatment procedures but aids patients in accessing information for self-care.\
                    Responses must be in Japanese."}
                    #{"role": "user", "content": "最近、とても不安に感じることが多いです"},
                    #{"role": "assistant", "content": "それはたいへんそうですね。どんなときに不安を感じることが多いですか？私はあなたの想いによりそい、共に不安をやわらげる方法をみつけていけたらと思います。"}
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

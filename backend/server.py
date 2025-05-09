# ✅ 1. backend/server.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 허용 (프론트에서 접근 가능)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data["message"].lower()

    if "배송" in user_input or "언제" in user_input:
        reply = "헬시라이프는 평균 1~2일 내 배송되며, 제주도는 3~4일 소요됩니다."
    elif "유산균" in user_input and ("먹는법" in user_input or "어떻게" in user_input):
        reply = "유산균은 아침 공복에 1캡슐씩 섭취하시는 것이 좋습니다."
    elif "홍삼" in user_input and ("아이" in user_input or "어린이" in user_input):
        reply = "어린이는 전용 홍삼 제품을 권장드립니다. 현재는 성인용만 판매 중입니다."
    elif "환불" in user_input or "교환" in user_input:
        reply = "수령일로부터 7일 이내, 미개봉 상품에 한해 교환/환불이 가능합니다."
    elif "전화" in user_input or "고객센터" in user_input:
        reply = "고객센터 1588-1234 (평일 09:00~18:00)로 문의 주세요."
    else:
        reply = "죄송합니다. 해당 질문은 고객센터로 문의 부탁드립니다."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(port=5001)
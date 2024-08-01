"use client";
import OneCustomerInfoCard from "src/app/components/one_customer_info_card.jsx";
import BackButton from "./back_button";
import fetchCustomer from "./fetchCustomer";
import { useEffect, useState } from "react";
import axios from "axios";

const apiEndpoint = process.env.API_ENDPOINT;

export default function ReadPage(props) {
  const id = props.params.id;

  const [customerInfo, setCustomerInfo] = useState([]);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchAndSetCustomer = async () => {
      const customerData = await fetchCustomer(id);
      setCustomerInfo(customerData);
    };
    const fetchMessages = async () => {
      const res = await axios.get(`${apiEndpoint}/messages?customer_id=${id}`);
      setMessages(res.data);
    };
    fetchAndSetCustomer();
    fetchMessages();
  }, [id]);

  const handleSendMessage = async () => {
    await axios.post(`${apiEndpoint}/messages`, {
      customer_id: id,
      message: message,
    });
    setMessage("");
    // メッセージを再取得して更新
    const res = await axios.get(`${apiEndpoint}/messages?customer_id=${id}`);
    setMessages(res.data);
  };

  return (
    <>
      <div className="card bordered bg-white border-blue-200 border-2 max-w-sm m-4">
        <OneCustomerInfoCard {...customerInfo[0]} />
        <div className="flex flex-col mt-4">
          <textarea
            className="textarea textarea-bordered"
            placeholder="メッセージを入力してください"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button className="btn btn-primary mt-2" onClick={handleSendMessage}>
            送る
          </button>
        </div>
        <BackButton>戻る</BackButton>
      </div>
      <div className="mt-4">
        <h2 className="text-lg font-bold">メッセージ履歴</h2>
        <ul>
          {messages.map((msg, index) => (
            <li key={index} className="border-b p-2">
              {msg.message}
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

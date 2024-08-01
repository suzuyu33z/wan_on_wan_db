"use client";
import OneCustomerInfoCard from "@/app/components/one_customer_info_card.jsx";
import Link from "next/link";
import { useEffect, useState } from "react";
import fetchCustomers from "./fetchCustomers";

export default function Page() {
  const [customerInfos, setCustomerInfos] = useState([]);

  useEffect(() => {
    const fetchAndSetCustomer = async () => {
      const customerData = await fetchCustomers();
      setCustomerInfos(customerData);
    };
    fetchAndSetCustomer();
  }, []);

  return (
    <>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {customerInfos.map((customerInfo, index) => (
          <div
            key={index}
            className="card bordered bg-white border-blue-200 border-2 flex flex-row max-w-sm m-4"
          >
            <OneCustomerInfoCard {...customerInfo} />
            <div className="card-body flex flex-col justify-between">
              <Link
                href={`/customers/message/send/${customerInfo.customer_id}`}
              >
                <button className="btn btn-neutral rounded-full border-0 bg-blue-200 text-black hover:text-white hover:bg-blue-500 w-24 h-24 flex items-center justify-center">
                  メッセージを送る
                </button>
              </Link>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

import Link from "next/link";
import "./globals.css";

export default function Top() {
  return (
    <div className="p-4 flex flex-col items-center">
      <h1 className="text-2xl font-bold mb-4">ログインか新規登録して！</h1>
      <div className="flex flex-col items-center w-full">
        <Link
          href="/home"
          className="button-link w-1/5 inline-block mt-4 text-center"
        >
          ログイン
        </Link>
        <Link
          href="/new"
          className="button-link w-1/5 inline-block mt-4 text-center"
        >
          新規登録
        </Link>
      </div>
    </div>
  );
}

import Link from "next/link";

export default function WalkSearchDetailRequest() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">ここで申請！</h1>
      <Link
        href="/home/walksearch/detail"
        className="block text-blue-500 hover:text-blue-700"
      >
        戻る
      </Link>
    </div>
  );
}

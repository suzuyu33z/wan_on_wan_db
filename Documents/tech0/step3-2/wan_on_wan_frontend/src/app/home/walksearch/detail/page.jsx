import Link from "next/link";

export default function WalkSearchDetail() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">
        気になるワンちゃんに申請出そう
      </h1>
      <Link
        href="/home/walksearch/detail/request"
        className="block text-blue-500 hover:text-blue-700"
      >
        申請に進む
      </Link>
      <Link
        href="/home/walksearch"
        className="block text-blue-500 hover:text-blue-700"
      >
        戻る
      </Link>
    </div>
  );
}

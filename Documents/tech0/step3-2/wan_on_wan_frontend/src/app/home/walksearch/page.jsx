import Link from "next/link";

export default function WalkSearch() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">
        気になるさんぽの詳細を見てみよう
      </h1>
      <Link
        href="/home/walksearch/detail"
        className="block text-blue-500 hover:text-blue-700"
      >
        さんぽの詳細を見る
      </Link>
      <Link href="/home" className="block text-blue-500 hover:text-blue-700">
        戻る
      </Link>
    </div>
  );
}

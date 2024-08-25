"use client";

import { useState, FormEvent } from "react";
import { getPosts } from "@/api/getposts";
import { Spinner } from "@/components/common";

export default function Page() {
  const [search, setSearch] = useState("");
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    setLoading(true);
    const job_posts = await getPosts(search);

    setPosts(job_posts);
    setLoading(false);
  };

  return (
    <>
      <header className="bg-white shadow">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold tracking-tight text-gray-900">
            Dashboard
          </h1>
        </div>
      </header>
      <form onSubmit={handleSubmit}>
        <main className="mx-auto max-w-7xl py-6 my-8 sm:px-6 lg:px-8">
          <div style={{ marginBottom: "30px" }}>
            <input
              type="text"
              name="search"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{
                marginRight: "30px",
                width: "400px",
                borderRadius: "0.5rem",
              }}
            />
            <button
              type="submit"
              style={{
                width: "120px",
                height: "40px",
                padding: "5px 30px",
                border: "1px solid",
                borderRadius: "0.5rem",
                backgroundColor: "#5148e3",
                color: "white",
                justifyContent: "center",
              }}
            >
              {loading ? <Spinner /> : "Search"}
            </button>
          </div>
          {posts.length > 0 && (
            <table>
              <tr>
                <th>Sr.</th>
                <th>Job Name</th>
                <th>Company Name</th>
              </tr>
              {posts.map((post, index) => (
                <tr key={index}>
                  <td>{index}</td>
                  <td>{post["job_name"]}</td>
                  <td>Germany</td>
                </tr>
              ))}
            </table>
          )}
        </main>
      </form>
    </>
  );
}

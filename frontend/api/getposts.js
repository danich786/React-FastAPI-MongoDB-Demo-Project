import axios from "axios";

const BASE_URL = `${process.env.NEXT_PUBLIC_HOST}/search/`;

export const getPosts = async (search) => {
  const access_Token = JSON.parse(sessionStorage.getItem("access_token"));

  try {
    const response = await axios.get(BASE_URL, {
      headers: { Authorization: `Bearer ${access_Token}` },
      params: { title: search },
    });
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

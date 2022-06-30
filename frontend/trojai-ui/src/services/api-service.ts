import axios from "axios"

const get_data = async (url: string) => {
  const response = await axios.get(url)
  return response.data
}

export default get_data

import axios from 'axios'
const base_url = process.env.API_URL || 'http://127.0.0.1:9999'

const get_books = async () => {
  const url = `${base_url}/books`
  const response = await axios.get(url)
  return response.data
}

const get_readers = async () => {
  const url = `${base_url}/readers`
  const response = await axios.get(url)
  return response.data
}

const get_reader_books = async (reader_id: number) => {
  const url = `${base_url}/readers/${reader_id}/books`
  const response = await axios.get(url)
  return response.data
}

const get_read_books = async () => {
  const url = `${base_url}/readbooks`
  const response = await axios.get(url)
  return response.data
}

export { get_books, get_reader_books, get_readers, get_read_books }

import axios from 'axios'

const get_data = async (url: string) => {
  const response = await axios.get(url)
  return response.data
}

const get_books = async () => {
  const url = 'http://127.0.0.1:8000/books'
  const response = await axios.get(url)
  return response.data
}

const get_readers = async () => {
  const url = 'http://127.0.0.1:8000/readers'
  const response = await axios.get(url)
  return response.data
}

const get_reader_books = async (reader_id: number) => {
  const url = `http://127.0.0.1:8000/readers/${reader_id}/books`
  const response = await axios.get(url)
  return response.data
}

const get_read_books = async () => {
  const url = `http://127.0.0.1:8000/readbooks`
  const response = await axios.get(url)
  return response.data
}

export { get_data, get_books, get_reader_books, get_readers, get_read_books }

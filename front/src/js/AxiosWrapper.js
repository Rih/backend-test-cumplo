import axios from 'axios'

const defaultConfig = {
  timeout: 5 * 60 * 1000,
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
}

export default axios.create(defaultConfig)

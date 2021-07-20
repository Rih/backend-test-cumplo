import { ERROR, SUCCESS, APP_BASE_URL } from '@/js/constants'
import store from '@/store'
import axiosInstance from '@/js/AxiosWrapper.js'

const args = { pathParams: [], msg: null }
const init = { url: null, slash: true, toast: true }

const kebabCaseToCamel = (str) => {
  //eslint-disable-next-line
  return str.replace(/(\-\w)/g, (matches) => matches[1].toUpperCase())
}

const camelToSnakeCase = (str) => {
  //eslint-disable-next-line
  return str.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`)
}

const addPathParams = (resourceURL, params, slash) => {
  if (!params || params.length === 0) return resourceURL + (slash ? '/' : '')
  let url = ''
  params.forEach((param) => {
    url += `/${param}`
  })
  return resourceURL + url + (slash ? '/' : '')
}

const addQueryParams = (resourceURL, params = {}) => {
  const keys = Object.keys(params)
  if (keys.length === 0) return resourceURL
  let queries = ''
  keys.forEach((key) => (queries += `${camelToSnakeCase(key)}=${params[key]}`))
  return `${resourceURL}?${queries}`
}

const presentToast = ({ error, toast, msg }) => {
  if (msg) return store.dispatch('setToast', { type: SUCCESS, msg })

  const displayErrorToast = (msg) => {
    store.dispatch('setToast', { type: ERROR, msg })
  }

  if (!error) return
  const code = error.response.status
  const errMsg = error.response.data.msg

  const MSG = [
    'Datos inválidos',
    'Recurso no encontrado',
    'Usuario o contraseña incorrecto',
  ]

  if (code == 400 && !errMsg) return displayErrorToast(MSG[0])
  if (code == 404 && !errMsg) return displayErrorToast(MSG[1])
  if (code == 401 && !errMsg) return displayErrorToast(MSG[2])
  if (toast) displayErrorToast(errMsg)
}

const responseHandler = (response, resolve, msg) => {
  presentToast({ msg })
  resolve({ result: response.data, status: response.status })
}

const errorHandler = (error, resolve, toast) => {
  console.log({ error, resolve, toast })
  presentToast({ error, toast })
  resolve({ error })
}

class API {
  constructor ({ url, slash, toast } = init) {
    this.slash = slash === undefined ? true : slash
    this.toast = toast === undefined ? true : toast
    this.url = url ? url : `${APP_BASE_URL}/api/v1`
    this.endpoints = {}
  }
  /**
   * Create and store a single entity's endpoints
   * @param {A entity Object} entity
   */
  createEntity (entity) {
    //  * If there is a - in the entity.name, then change it
    //  * to camelCase. E.g
    //  * ```
    //  * myApi.createEntity({ name : 'foo-bar'})
    //  * myApi.endpoints.fooBar.getAll(...)

    const name = kebabCaseToCamel(entity.name)
    this.endpoints[name] = this.createBasicCRUDEndpoints(entity)
  }

  createEntities (arrayOfEntity) {
    arrayOfEntity.forEach(this.createEntity.bind(this))
  }
  /**
   * Create the basic endpoints handlers for CRUD operations
   * @param {A entity Object} entity
   */
  createBasicCRUDEndpoints ({ name }) {
    const endpoints = {}

    let resourceURL = `${this.url}/${name}`

    endpoints.get = ({ pathParams, queryParams, msg } = args) => {
      resourceURL = addPathParams(resourceURL, pathParams, this.slash)
      resourceURL = addQueryParams(resourceURL, queryParams)

      return new Promise((resolve) => {
        store.dispatch('startLoading')
        axiosInstance
          .get(resourceURL)
          .then((result) => responseHandler(result, resolve, msg))
          .catch((err) => errorHandler(err, resolve, this.toast))
          .finally(() => store.dispatch('stopLoading'))
      })
    }

    endpoints.post = (payload, { pathParams, msg } = args) => {
      resourceURL = addPathParams(resourceURL, pathParams, this.slash)

      return new Promise((resolve) => {
        store.dispatch('startLoading')
        axiosInstance
          .post(resourceURL, payload)
          .then((result) => responseHandler(result, resolve, msg))
          .catch((err) => errorHandler(err, resolve, this.toast))
          .finally(() => store.dispatch('stopLoading'))
      })
    }

    endpoints.update = (payload, { pathParams, msg } = args) => {
      resourceURL = addPathParams(resourceURL, pathParams, this.slash)

      return new Promise((resolve) => {
        store.dispatch('startLoading')
        axiosInstance
          .put(resourceURL, payload)
          .then((result) => responseHandler(result, resolve, msg))
          .catch((err) => errorHandler(err, resolve, this.toast))
          .finally(() => store.dispatch('stopLoading'))
      })
    }

    endpoints.patch = (id, payload, { pathParams, msg } = args) => {
      resourceURL = addPathParams(resourceURL, pathParams, this.slash)

      return new Promise((resolve) => {
        store.dispatch('startLoading')
        axiosInstance
          .patch(`${resourceURL}/${id}`, payload)
          .then((result) => responseHandler(result, resolve, msg))
          .catch((err) => errorHandler(err, resolve, this.toast))
          .finally(() => store.dispatch('stopLoading'))
      })
    }

    endpoints.delete = ({ pathParams, msg } = args) => {
      resourceURL = addPathParams(resourceURL, pathParams, this.slash)

      return new Promise((resolve) => {
        store.dispatch('startLoading')
        axiosInstance
          .delete(resourceURL)
          .then((result) => responseHandler(result, resolve, msg))
          .catch((err) => errorHandler(err, resolve, this.toast))
          .finally(() => store.dispatch('stopLoading'))
      })
    }

    return endpoints
  }
}

export default API

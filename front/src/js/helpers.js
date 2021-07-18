import { TEXT_OPERATORS, NUMERIC_OPERATORS } from '@/js/constants'

const getType = (type) => {
  const allowedTypes = {
    Text: 'text',
    Number: 'numeric',
  }
  return allowedTypes[type] ? allowedTypes[type] : 'text'
}

const getOperators = (type) => {
  const allowedOperators = {
    Text: TEXT_OPERATORS,
    Number: NUMERIC_OPERATORS,
  }

  return allowedOperators[type] ? allowedOperators[type] : TEXT_OPERATORS
}

export const rulesBuilder = (properties) => {
  const rules = []
  properties.forEach((prop) => {
    rules.push({
      type: getType(prop.tipo),
      id: prop.id,
      label: prop.nombre,
      operators: getOperators(prop.tipo),
    })
  })
  return rules
}

export const checkVisibile = (tablas) => {
  tablas.forEach((tabla) => {
    let allInvisible = true
    tabla.propiedades.forEach((prop) => {
      allInvisible = !prop.visible && allInvisible
    })
    if (allInvisible) tabla.visible = false
  })
  return tablas
}

export const getFormatedDate = (ISOdate) => {
  const dateInstance = new Date(ISOdate)
  const year = dateInstance.getFullYear()
  const month = dateInstance.getMonth() + 1
  const day = dateInstance.getDate()
  return `${day}/${month}/${year}`
}

export const getFullFormatedDate = (ISOdate) => {
  const dateInstance = new Date(ISOdate)
  const year = dateInstance.getFullYear()
  const month = dateInstance.getMonth() + 1
  const day = dateInstance.getDate()
  const hour = dateInstance.getHours()
  const min = dateInstance.getMinutes()
  return `${day}/${month}/${year} ${hour}:${min}`
}

export const parseJwt = (token) => {
  console.log({ token })
  // if (!token) return USER_DATA
  if (!token || token == 'none') return {}

  const base64Url = token.split('.')[1]
  const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
  const jsonPayload = decodeURIComponent(
    atob(base64)
      .split('')
      .map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      })
      .join('')
  )
  return JSON.parse(jsonPayload)
}

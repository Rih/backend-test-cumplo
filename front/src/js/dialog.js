import store from '@/store'

const promises = []

class Dialog {
  open (actionType, data = {}) {
    store.dispatch(actionType, {
      isActive: true,
      ...data,
    })
    return new Promise((resolve) => {
      promises.push(resolve)
    })
  }
  close (actionType, data = null) {
    store.dispatch(actionType, { isActive: false })
    promises[promises.length - 1](data)
    promises.pop()
  }
}

export default new Dialog()

// ----------------------------------------------------
// Bellow constants must be changed in backend also
// ----------------------------------------------------
export const IS_EMPTY = 'está vacío'
export const IS_NOT_EMPTY = 'no está vacío'
const EQUALS = 'igual'
const DOES_NOT_EQUAL = 'no es igual'
const CONTAINS = 'contiene'
const DOES_NOT_CONTAIN = 'no contiene'
const BEGINS_WITH = 'comienza con'
const ENDS_WITH = 'termina con'

export const NUMERIC_OPERATORS = ['=', '>', '<', '=>', '<=', '<>', '!=']
export const TEXT_OPERATORS = [
  EQUALS,
  DOES_NOT_EQUAL,
  CONTAINS,
  DOES_NOT_CONTAIN,
  IS_EMPTY,
  IS_NOT_EMPTY,
  BEGINS_WITH,
  ENDS_WITH,
]

// ----------------------------------------
//            Miscellaneous
// ----------------------------------------
export const RECAPTCHA = process.env.VUE_APP_RECAPTCHA_V3
export const ERROR = 'error'
export const SUCCESS = 'success'
export const RECOVERY = 'recovery'
export const FORGOT = 'forgot'
export const SIGN_IN = 'sign in'

export const ADMIN_MODE = 'admin mode'
export const RESEARCH_MODE = 'researcher mode'
export const PROPERTIES = 'properties'

// ----------------------------------------
//            Default table headers
// ----------------------------------------
export const ADMIN_TABLES = [
  {
    field: 'uri',
    label: 'Recurso',
    width: '150',
    searchable: true,
  },
  {
    field: 'bbox',
    label: 'Bounding Box',
    width: '250',
  },
  {
    field: 'results',
    label: 'Resultado',
  },
]

export const PER_PAGE = 10

export const APP_BASE_URL = process.env.VUE_APP_BASE_URL

export const RECAPTCHA_KEY = process.env.VUE_APP_RECAPTCHA_V3


export const INATURALIST_LOGO = '@/assets/cumplo.png'

export const DEFAULT_AVATAR =
  'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light'

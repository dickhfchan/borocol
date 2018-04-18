import Vue from 'vue'
import { Row, Col, Button, Alert, MessageBox, Notification, Dialog, Loading, Table, TableColumn,
  Badge, Dropdown, DropdownMenu, DropdownItem, Card, DatePicker, Progress, Slider,
  Tabs, TabPane, Popover, Tooltip, Breadcrumb, BreadcrumbItem,
  // form
  Select, Option, Input, Form, FormItem, Checkbox, CheckboxButton, CheckboxGroup,
  Radio, RadioGroup, Rate, Pagination,
} from 'element-ui'
import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'
import './compile/theme/index.css'
import './compile/theme/display.css'
import './extend.scss'

export default () => {
  locale.use(lang)
  Vue.use(Row)
  Vue.use(Col)
  Vue.use(Button)
  Vue.use(Alert)
  Vue.use(Dialog)
  Vue.prototype.$msgbox = MessageBox
  Vue.alert = Vue.prototype.$alert = (msg, title = 'Oops!') => MessageBox.alert(msg, title)
  Vue.confirm = Vue.prototype.$confirm = MessageBox.confirm
  Vue.prompt = Vue.prototype.$prompt = MessageBox.prompt
  Vue.notify = Vue.prototype.$notify = Notification
  Vue.prototype.$notifySuccess = (message, title = 'Successful') => Notification.success({title, message})
  Vue.prototype.$notifyInfo = (message, title = 'Info') => Notification.info({title, message})
  Vue.prototype.$notifyWarn = (message, title = 'Warning') => Notification.warning({title, message})
  Vue.prototype.$notifyError = (message, title = 'Failed') => Notification.error({title, message})
  Vue.prototype.$loading = Loading.service;
  Vue.use(Loading.directive)
  Vue.use(Table)
  Vue.use(TableColumn)
  Vue.use(Badge)
  Vue.use(Dropdown)
  Vue.use(DropdownMenu)
  Vue.use(DropdownItem)
  Vue.use(Card)
  Vue.use(DatePicker)
  Vue.use(Progress)
  Vue.use(Slider)
  Vue.use(Tabs)
  Vue.use(TabPane)
  Vue.component('el-tab-panel', TabPane)
  Vue.use(Popover)
  Vue.use(Tooltip)
  Vue.use(Breadcrumb)
  Vue.use(BreadcrumbItem)
  // form
  Vue.use(Select)
  Vue.use(Option)
  Vue.use(Input)
  Vue.use(Form)
  Vue.use(FormItem)
  Vue.use(Checkbox)
  Vue.use(CheckboxButton)
  Vue.use(CheckboxGroup)
  Vue.use(Radio)
  Vue.use(RadioGroup)
  Vue.use(Rate)
  Vue.use(Pagination)
}

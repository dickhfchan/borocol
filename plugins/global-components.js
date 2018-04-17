import Vue from 'vue'
import Icon from '@/global-components/Icon.vue'
import QuestionCircle from '@/global-components/QuestionCircle'
import AspectImage from '@/global-components/AspectImage.vue'
import HasReadMore from '@/global-components/HasReadMore.vue'
import FormItem from '@/global-components/FormItem.vue'
import FormLabel from '@/global-components/FormLabel.vue'
import FormError from '@/global-components/FormError.vue'
import Row from '@/global-components/Row.vue'
import Col from '@/global-components/Col.vue'
import CloseBtn from '@/global-components/CloseBtn.vue'

export default () => {
  Vue.component('Icon', Icon)
  Vue.component('QuestionCircle', QuestionCircle)
  Vue.component('AspectImage', AspectImage)
  Vue.component('HasReadMore', HasReadMore)
  Vue.component('FormItem', FormItem)
  Vue.component('FormLabel', FormLabel)
  Vue.component('FormError', FormError)
  Vue.component('Row', Row)
  Vue.component('Col', Col)
  Vue.component('CloseBtn', CloseBtn)
}

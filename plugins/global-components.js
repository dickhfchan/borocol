import Vue from 'vue'
import Icon from '@/global-components/Icon.vue'
import AspectImage from '@/global-components/AspectImage.vue'
import HasReadMore from '@/global-components/HasReadMore.vue'
import FormItem from '@/global-components/FormItem.vue'
import FormLabel from '@/global-components/FormLabel.vue'
import FormError from '@/global-components/FormError.vue'

export default () => {
  Vue.component('Icon', Icon)
  Vue.component('AspectImage', AspectImage)
  Vue.component('HasReadMore', HasReadMore)
  Vue.component('FormItem', FormItem)
  Vue.component('FormLabel', FormLabel)
  Vue.component('FormError', FormError)
}

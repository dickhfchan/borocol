<template lang="pug">
include ../../common.pug
+createCourse
  form
    +formGroup('fields.tags')
      TagsInput(v-model="fields.tags.value")
    .flex
      +formGroup('fields.cover').cover
        ImageUploader(v-model="fields.cover.value")
      +formGroup('fields.photos').photos.mll
        MultipleImageUploader(v-model="fields.photos.value")

    +formGroup('fields.notes')
      +textarea(v-model="fields.notes.value" rows='3')
</template>

<script>
import base from './base'
import TagsInput from '@/components/TagsInput'
import ImageUploader from '@/components/ImageUploader';
import MultipleImageUploader from '@/components/MultipleImageUploader';

export default {
  extends: base,
  components: {TagsInput, ImageUploader, MultipleImageUploader},
  data() {
    return {
    }
  },

  computed: {
  },
  // watch: {},
  // methods: {},
  created() {
    this.$validate(this.validation, this.fields)
  },
  // mounted() {},
}
</script>

<style lang="scss">
.CreateCoursePage7{
  .cover{
    .ImageUploader{
      display: block;
    }
  }
}
</style>
